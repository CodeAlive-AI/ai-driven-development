## A.10 - Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph

> **Type:** Kernel pattern
> **Status:** Stable
> **Normativity:** Normative

### A.10:1 - Problem frame

Use this pattern when a source, carrier, result episteme, credential, dashboard, provenance label, generated explanation, model card, or review note is being relied on for a named claim or bounded action and the source-to-use account is still implicit.

**Primary EntityOfConcern.** The live object is the exact relied-on claim and bounded use. A.10 builds a descriptive evidence-provenance path that represents the independently established sources, carriers, work, result epistemes, provenance relations, currentness, and later-use relations needed to judge that use. The path is not a new world-side relation and its edges establish none of the facts they cite.

**First useful move.** Write: “Claim episteme `E` is being relied on for bounded use `U`; `E` states local result `R`; the cited sources, carriers, and direct relations are `S`; currentness is `T`; the bounded A.10 disposition is `D`.” Add a dated `U.Work` occurrence only when that Work is itself a current claim. If the account says that Work returned, produced, or obtained a value, name the exact A.6.1 application binding, one local A.15.PROD claim, or a direct subject relation under its own pattern; otherwise keep the Work and value as separate facts. Mark any missing rule or relation as a gap.

**What goes wrong if missed.** Carrier presence becomes truth, provenance becomes approval, a result record becomes performed work, MethodDescription becomes a run trace, a graph edge becomes an obtaining relation, and a currentness or assurance decision is inferred from display styling.

**What this buys.** A source-to-use account that can be replayed, contested, refreshed, narrowed, or handed to the pattern that defines or tests an additional claim, while keeping the claim, carrier, performed work, local result, result episteme, provenance, currentness, reliance, assurance, and action distinct.

**Not this pattern when.** A.10 does not establish measurement, formal, causal, diagnostic, conformance, comparison, selection, acceptance, gate, permission, commitment, Work, or decision results. It does not establish representation correspondences. Use the pattern that defines or tests each result, A.15.1 and A.6.1 for performed Work and actual bindings, C.2.1 for the result episteme, G.11 for currentness, C.29 for representation, and B.3 only when an actual named assurance claim is current.

Use A.2.4 first when only the first evidence-use or status-use classification of an episteme is at issue. Enter A.10 when carrier identity, source recovery, provenance, currentness, rival explanations, or bounded reliance must remain replayable.

Here `path` means a path in a descriptive evidence/provenance graph, never a route of action or a universal evidence relation.

### A.10:2 - Problem

Source-backed reasoning fails in recurring ways:

1. the relied-on claim is not named;
2. a carrier or publication face is substituted for the claim it represents;
3. a method description, plan, signature, or stored reference is substituted for actual work and bindings;
4. a local domain result is replaced by a generic evidence or result field;
5. provenance, currentness, reliance, assurance, and authorization are collapsed; or
6. a graph edge is asserted before the direct source, work, production, representation, participation, or use relation is known to obtain.

The practical effect is false authority and unreplayable decisions: a badge looks like permission, a dashboard looks like a gate decision, or a model output looks like an accepted conclusion.

### A.10:3 - Forces

- **Minimality vs consequence.** Orientation needs a small path; material reliance needs the exact fields that change the decision.
- **Carrier identity vs claim content.** The same content can appear in several carriers and editions; a carrier can be authentic while the claim is false or stale.
- **Reusable method vs performed work.** A method describes a repeatable way. Ordinary reading, orientation, or reliance can remain ordinary; a claim about performed `U.Work` requires the dated occurrence and exact bindings.
- **Provenance vs result establishment.** A.10 must make a result traceable without establishing the result itself.
- **Graph convenience vs ontic discipline.** A graph can represent many relations compactly but cannot make them obtain.
- **Contestability vs confidentiality.** Reliance must be challengeable while sensitive carriers may require scoped, redacted, hashed, or access-controlled views.

### A.10:4 - Solution — recover exact objects before drawing the path

#### A.10:4.1 - Start with the relied-on claim

Name the exact C.2.1 episteme whose content is being relied on. Its ClaimGraph states one local result or proposition, subject, interpretation basis, polarity or status when current, and uncertainty or qualification when relevant. The local result must come from the pattern that defines or tests it: C.16 for measurement, C.28 for causal support, A.19 for comparison or selection, G.4 for an acceptance-clause application, A.21 for a gate decision, C.11 for a decision, and the applicable formal, diagnostic, conformance, identity, permission, or commitment pattern. When *role* appears in a technical result, use E.10.ROLE to select the exact local system-role-kind classification, `U.SystemRoleAssignment` occurrence or state, relation among system-role kinds, declaration, participation, interface, or representation claim before citing its governor.

A carrier, citation, provenance entry, or A.10 classification does not constitute the result episteme or the domain result. When their identity or inception is live, use C.2.1 and A.15.PROD respectively.

#### A.10:4.2 - Ground source, carrier, publication, and representation

Recover the selected source episteme and its edition and claim content. When availability, form, or carrier matters, separately recover the `EpistemePublicationRelation` occurrence, publication form, carrier, or face involved, together with any copy, extraction, or transformation between source and use. Use E.17 for publication and C.29 for representation correspondences. The descriptive graph points outward to those independently established objects and relations.

Carrier authenticity, integrity, or provenance may support only its named origin, history, build, or transformation claim. It does not imply truth, safety, approval, release, permission, assurance, or work occurrence.

#### A.10:4.3 - Separate method, work, participants, and local result

`U.MethodDescription` is an episteme about one exact `U.Method`. It may state generic participants, parameters, effects, and operating conditions. It has no actual-participant slots and no intrinsic design-time intention, proof criterion, test criterion, or claim that work occurred.

Source production, measurement, verification, interpretation, transformation, query, review, publication, or later reliance may be described ordinarily. When the current claim says that one of these is a dated `U.Work` occurrence, point to its complete A.15.1/F.6 basis. A short evidence account may omit only an assignment identifier unused by the receiving claim; the covering assignment occurrence and F.6 attribution still obtain and remain recoverable. Affected or evaluated referents, resources, and actual participants enter only through direct subject relations or A.6.1 operation-application bindings. Capability, authority, and responsibility remain separate predicates. A compatible signature, plan, description, log schema, or graph node establishes none of those bindings.

For every cited result, name the pattern that defines or tests it and its C.2.1 result episteme separately. The provenance path may represent exact Work, participants, entities, domain results, result epistemes, and outcomes only after their direct relations are established. Relate Work to a returned or produced value only through an exact A.6.1 application binding, one exact local A.15.PROD claim, or a direct subject predicate under its own pattern; otherwise show the two facts separately and return the reason-specific non-assertability result if that connection is needed.

#### A.10:4.4 - Build a descriptive evidence-provenance path

The minimum A.10 path records only what the bounded use needs:

| Field | Required content |
| --- | --- |
| Relied-on claim | Exact C.2.1 episteme and the local result or proposition it states |
| Bounded use | The ordinary orientation, learning, action, or reliance use being judged, and its premise, reference, decision-use, operation-argument, or other direct use relation. Add an exact later `U.Work` occurrence only when it is independently current. |
| Sources and carriers | Selected source epistemes and editions; publication occurrences, forms, carriers, and faces when material; transformations; and direct provenance/citation relations |
| Work and bindings | Only independently current dated `U.Work`, its complete basis, and the performers, Methods, resources, direct relations, and A.6.1 bindings used by the claim. A claimed Work-to-value link also needs an A.6.1 application binding, one local A.15.PROD claim, or a direct subject predicate defined by its own pattern. |
| Result rule | The pattern that defines or tests each local result, and its distinct result episteme |
| Time/currentness | Source and result windows plus G.11 currentness when currentness affects use |
| Challenge | Principal rival explanation, unsupported attempted use, contest/redress path, and reopen trigger |

Graph nodes retain their admitted kinds. Each edge cites one independently established direct relation; no generic `evidences`, `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, or criterion-participant relation is minted as a fallback. A project may label display edges for navigation, but the label has no ontic force.

#### A.10:4.5 - Classify bounded reliance

The canonical local `RelianceDisposition` member set is exactly: `pass`, `degrade`, `abstain`, `reopen`, `evidence-needed`, `assurance-needed`, and `blocked-current-use`. `pass` supports only the exact bounded use; `degrade` supports only the named narrower or reversible use. `assurance-needed` says that A.10 alone cannot support the attempted use because a direct domain rule or receiving decision requires a separately stated assurance claim. It creates no assurance claim and does not open B.3 until that claim is current. No disposition is claim truth, `CV.Status`, gate decision, selector outcome, approval, permission, release, assurance, or Work authorization.

When an actual named assurance claim is current, use B.3 for that assurance question. A.10 continues to supply the exact source and provenance paths but does not issue the assurance result. Consequential evidence use without such a claim stays with the direct safety, access, status, gate, permission, release, responsibility, or controlled-action pattern.

#### A.10:4.6 - Currentness, actual use, and graph limits

Source availability and source currentness are distinct. Record issue/effective windows, supersession, revocation, source-order rules, and the G.11 currentness result when a use depends on them.

Actual reliance requires one exact premise, reference, decision-use, operation-argument, or other direct relation to the result episteme. When that reliance is also claimed as dated `U.Work`, recover the Work independently. Storage, indexing, citation, graph membership, visibility, or co-location establishes neither reliance nor performed Work.

Part-whole, temporal, production, publication, representation, provenance, participation, and reliance relations must each be established separately. The A.10 graph may cite them together for replay but never substitutes one for another.

#### A.10:4.6a - Authority-reliance use of ordinary A.10 evidence-provenance paths

Use this subsection when an authority-looking carrier is being relied on. The A.10 path represents one named claim, its exact sources and direct relations, and one bounded use; it is not an authority relation. If the Work occurrence, gate decision, speech act, commitment, permission, exact system-role assignment, assignment-state assertion, or other required relation already exists in a project-side source, recover that object by value and let the graph cite it.

A10-lite is enough for source-finding, orientation, learning, and bounded reversible probes:

| Field | Required content |
| --- | --- |
| claim or effect | The claim, effect, or source-backed reliance use the evidence carrier is being asked to evidence for the named work occurrence or reliance use. |
| evidence carrier | The display, badge, credential, attestation, dashboard tile, copied text, generated text, log, trace, source file, report, or other `SymbolCarrier`/publication carrier. |
| producer, issuer, verifier, or source contact | Name the admitted System that issued, attested, copied, generated, verified, displayed, or maintains the source-backed content, and the direct issuer, verification, publication, register, or source-maintenance relation used by this claim. If dated Work is asserted, also recover the assignment occurrence that covers it, that occurrence's declared species, and F.6 attribution. |
| method use or Work occurrence | Name the ordinary source-finding or method use. Add admitted measurement, verification, review, build, attestation, copy, extraction, generation, query, trace, or log `U.Work` only when independently current. If that Work is said to have returned, produced, or first constituted the carrier or result, cite an exact A.6.1 application binding, one local A.15.PROD claim, or a direct subject predicate under its own pattern; otherwise keep the facts separate. |
| time window | Issue time, effective window, decay, supersession, revocation, policy or gate version, and reopen condition. |

Minimum evidence-provenance path for routine reliance:

| Field | Required content |
| --- | --- |
| evidenced claim or effect | Approval, permission, gate passage, local system-role-kind classification, system-role-assignment occurrence or state, relation among system-role kinds, status currentness, work occurrence, evidence relation, assurance input, or other claim named by value or effect being attempted. Route any other technical *role* use through E.10.ROLE. |
| evidence carrier | The visible or recovered carrier, with enough identity to reopen it. |
| issuer, performer, trust root, status register, and source-side predicates | Name every object this path actually uses: the admitted System performing source-side Work; the trust-root or status-register episteme, register, or service; and the issuer, publication, registration, status-source, source-maintenance, trust, acceptance, or currentness predicate by which that object bears on the relied-on claim. For admitted Work, recover the covering assignment occurrence, its declared species, and F.6 attribution. If no current pattern defines or tests the needed predicate, return the A.6.RCD `missing-governor` result. Authority and source-maintenance responsibility remain separate relations. |
| affected entity and relying context | The release, service, model, person, admitted System and any separately obtaining assignment, policy subject, work target, claim, audience, tenant, environment, or other entity for which reliance is attempted. |
| time window and freshness | Issue time, effective window, decay, supersession, revocation, policy or gate version, and reopen condition. |
| relevant Work occurrence or method trace | Any independently current production, verification, query, generation, review, or other `U.Work`, plus the method trace when the method matters. Connect that Work to the carrier or result only through an exact A.6.1 application binding, one local A.15.PROD claim, or a direct subject predicate under its own pattern; otherwise record them separately. |
| evidence relation and rival explanation | Which claim the carrier evidences, how it evidences it, and the principal rival explanation that remains plausible, such as stale display, spoofed badge, copied wording, generated paraphrase, context shift, carrier-only provenance, or local-only transform relation. |

Expanded fields are collected only insofar as they decide the current reliance question. Evidence depth follows consequence severity, reuse, contestability, cross-context movement, and the evidence relation required for the attempted claim. Do not expand a source-finding note into a full evidence dossier, and do not collect every expanded field merely because a carrier is copied, generated, credential-like, provenance-like, or cross-context.

**Adversarial misuse guard.** Do not let carrier authenticity, provenance, copied approval, generated summary, stale screenshot, credential status view, or dashboard export convert into claim truth or currentness. Treat each as a rival explanation to test against the exact issuer, publication, registration, status-source, source-maintenance, trust, acceptance, or currentness predicate actually used; any source-side Work and its attribution; the time window; and the relying context. If the needed predicate has no governor, return that A.6.RCD gap rather than calling it support.

**Data-minimization and privacy boundary.** Preserve the minimum source, provenance, and direct-relation account sufficient for the intended use. Use redacted, hashed, scoped, or access-controlled carrier refs when raw material would expose personal identity, access tokens, cryptographic proof payloads, tenant identifiers, security logs, incident details, internal release metadata, audit trails, privileged reviewer identities, sensitive model provenance, or sensitive data provenance. Redaction creates no source relation; it must preserve enough recoverability for the relying context.

| Expanded field | When it is needed |
| --- | --- |
| method trace or work trace | Provenance, attestation, generated source relation, copied source relation, dashboard source relation, rollback source relation, or work occurrence is being used. |
| evidence-carrier integrity | The carrier may be spoofed, stale, copied, transformed, rendered, redacted, or context-shifted. |
| identity or holder binding | The claim depends on a credential holder, admitted System, separately obtaining assignment holder, acting holon, issuer, performer, delegate, revoker, verifier, or relying party. |
| verifier context, relying-party context, and acceptance rule | The evidence relation is accepted only for a verifier, audience, tenant, environment, release line, policy subject, operational mode, or consumer-side policy or gate rule that accepts the evidence for this use. |
| proof, cryptographic-signature, or status verification result | Credential, provenance, attestation, authenticity, revocation, or currentness relation is claimed. |
| policy version, gate version, and decision source | Permission, gate passage, release, rollback authority, policy authorization, or another bounded use boundary is attempted. |
| source-chain transform notes | Evidence relation passed through extraction, copy, rewrite, representation shift, explanation rendering, summary, export, redaction, or another transform step before reliance. |
| source order and supersession rule | Multiple source candidates disagree or freshness or priority may defeat the visible publication face, publication carrier, rendering, or cue. Include the direct register or status-source-order relation when a register entry is the source for an exact system-role-assignment occurrence, status assertion, permission, commitment, or gate state. |
| minimum disclosure boundary | Raw evidence would expose secrets, personal data, tenant identifiers, privileged logs, tokens, security-sensitive traces, or unnecessary identities. |

Case repairs:

| Case | Evidence repair |
| --- | --- |
| Stale credential badge or status display | Name the exact issuer or trust-root object and its direct issuer or trust relation; name the exact status register, entry, and direct registration or status-source relation when one exists; then show holder or subject binding, verifier and relying-party context, proof or status result, revocation and freshness, effective window, entry version, and carrier integrity. Display presence is not an obtaining system-role-assignment occurrence, status assertion, or permission. |
| Verifiable credential, credential view, or register excerpt | Treat it as an `A.10` carrier. Name the exact issuer or trust-root object and relation; the exact status register, entry, and registration or status-source relation when present; the selected source `U.Episteme` and edition and, when availability matters, its exact `EpistemePublicationRelation`; holder or subject binding; verifier; proof and status results; currentness; relying context; effective and revocation windows; and acceptance rule. Passing those checks may evidence credential currentness for that holder and use. A strong grant, exercise, weak non-prohibition or non-violation finding, or conflict requires `A.2.8.PER`; an actual commitment requires `A.2.8`; an issuing act, exact system-role assignment or status assertion, entry predicate, or gate passage requires `A.2.9`, `A.2.1`, `A.6.B`, or `A.21` respectively. Display presence creates none of them. |
| Copied approval or review summary | Show the original `A.2.9 SpeechActRef` or issuing act when approval or authorization is claimed, or the original reviewed source when only review-content currentness is claimed. Add the copy relation, currentness, scope, and window. Add a separately identified dated `U.Work` only when it is current, and connect it to the copy or result only through an A.6.1 application binding, one local A.15.PROD claim, or a direct subject predicate defined by its own pattern. State separately whether the claim concerns an `A.2.8.PER` grant, finding, exercise, or conflict result; an `A.2.8` duty, recommendation, or prohibition commitment; or another Work relation. Copy evidence is not approval by itself. |
| Provenance, authenticity, or attestation label | Show the bounded origin, history, build, or process claim; selected source `U.Episteme`, the exact `EpistemePublicationRelation` occurrence when availability is material, or evidence carrier; method trace or work trace; source-specific proof; evidence-carrier integrity; verifier or relying policy that accepts it for this claim or effect; and rival explanation. Provenance does not show truth, safety, approval, release, gate passage, permission, or assurance unless another FPF relation named by value carries that additional claim or effect. |
| Dashboard status tile | For gate-passage or release reliance, show dashboard query, the source relation used by the dashboard query or the source-bearing record used by that query, time, window, currentness, source-order relation, freshness policy, rival explanation, and the current `A.21` `GateDecision` or `DecisionLogRef` with gate profile, gate version, release target, and work target; the A.10 evidence-provenance path evidences that source-to-use path. A status display is not gate passage or work occurrence by itself. |
| Rollback command-like cue | Show command record or issuing speech act, authorization relation, actor, affected work target or claim target, scope, window, and whether the cue is only an `A.6.A` action invitation. A command cue is not performed-work evidence. |
| Rollback performed-work result | Show `A.15.1` `U.Work` occurrence, method trace or work trace, logs, outcome evidence, and time window. Performed-work evidence is not approval, assurance, or gate passage by itself. |
| Generated explanation | Use `E.17.EFP` to classify the explanation relation and source-finding use. For reliance, show claim-bound attribution alignment: every operative claim relied on maps to a source passage, carrier, or `relationFunctionClaimRef` or `authoritySourceRef` named by value that evidences that claim in the relying context. When that mapping is complete, A.10 may evidence those operative claims as source-backed evidence; the explanation itself still does not issue, approve, authorize, pass a gate, evidence performed work, or raise assurance. |
| Model card or datasheet used as evidence | Show documented bounded-use statement or external intended-use field, version, window, evaluation condition, limitations, evidence carriers, and whether a `B.3` assurance claim is being made. Documentation does not become readiness or assurance by presence. |
| Extracted source-to-use path to gate or release claim | Name the selected source `U.Episteme` ref and, when availability is material, the exact `EpistemePublicationRelation` occurrence ref; the source-bearing relation or pattern reference that identifies the rule carrying the claim; the first lossy or non-commutative transform step; the FPF relation or pattern that defines or constrains that transform (`A.6.3.CR`, `A.6.3.RT`, `A.6.3.CSC`, `E.17.EFP`, `E.17.ID.CR`, or `E.18` where applicable); the bounded inference relation after the step; the `relationFunctionClaimRef` or `authoritySourceRef` named by value that carries the claim being made; the reopen trigger naming the selected source episteme, publication occurrence when relevant, source-bearing relation, transform record, evidence relation, or pattern passage that must be rechecked; and the gate claim or release claim blocked until those source-to-use and cited-claim relations are recoverable. |
| Conflicting source relations | When display, source publication carrier, decision log, recency signal, freshness signal, copied summary, generated summary, credential status, provenance label, or assurance evidence disagree, name the visible source relation, rival source relation, source-order rule, decision-source relation, freshness policy, and supersession rule. Do not choose by color, visual salience, confidence wording, copied wording, or apparent recency; the work claim or reliance claim is contested until the source-order question is resolved. |
| Sensitive evidence-provenance path | Use redacted, hashed, scoped, or access-controlled carrier refs when raw carriers expose secrets, personal data, security-sensitive traces or data, privileged logs, tenant identifiers, or unnecessary identities. Redaction does not create a source relation; it must preserve enough recoverability for the relying context. |
| Pointer or proof-status evidence-provenance path | Use a hash, proof or status verification result, selected source `U.Episteme`, exact `EpistemePublicationRelation` occurrence when availability matters, source or source-currentness relation, scoped pointer, disclosure receipt, or access-controlled view instead of copying raw sensitive carriers or payloads when that pointer preserves enough recoverability for the relied-on claim or effect. Do not copy raw secrets, tokens, privileged logs, personal identities, or tenant details merely to make the path look fuller. |

If the evidence-provenance path is incomplete, A.10 reports the missing source, carrier, work, rule for the cited result, direct relation, or G.11 currentness fact and narrows or blocks only the attempted use. Possible dispositions include source-finding only, reopen original carrier, request issuer or status verification, refresh the source query, mark stale or contested, narrow the attempted P2W class or reliance claim, proceed only with a reversible local probe under an explicit work plan, or block the unsupported use.

**Missing source-relation repair assignment.** If the relying actor cannot recover or verify the source relation, name the admitted System selected by an independently obtaining project-side repair-responsibility relation and assign only prospective repair Work. The relevant issuer or performer, exact verifier system-role-assignment occurrence when one is current, status-source relation, evidence-producing Work and System, gate-decision source relation, system-role-assignment source relation, status register entry, boundary claim relation, or source-currentness relation remains a separate fact; none is a responsibility relation by form. If the corpus has no direct predicate that selects the repair System for this case, record the exact A.6.RCD missing governor. The A.10 result names the missing source relation or source-bearing record and blocked use rather than making the relying actor reconstruct a relation they cannot issue or verify.

| Viewpoint | Prompt |
| --- | --- |
| Relying actor | Which claim named by value or effect needs an evidence relation, and what is the minimum carrier, source-bearing record or relation, time, and evidence-provenance relation for that claim or effect? |
| Issuer, verifier, or status relation maintainer | Which issuer, holder, verifier, proof result, status result, currentness relation, revocation relation, or acceptance-rule relation must be exposed or repaired? |
| Auditor or technical reviewer | Which carrier, exact issuer, publication, registration, status-source, source-maintenance, trust, acceptance, or currentness predicate, ordinary method trace or admitted Work trace, time window, evidence relation, and rival explanation must be recoverable? |
| Security reviewer or compliance reviewer | Which source-order relation, supersession relation, proof result, status result, revocation relation, and minimum-disclosure boundary decide this reliance question? |
| LLM user or tool user | Which generated or copied operative claims map to source passages or carriers, and which claims remain only source-finding? |
| Model documentation or data documentation | Which intended-use, evaluation-condition, version, window, limitation, and evidence carriers bound the model documentation or data documentation? |

**Repeated missing-source-relation indicator.** If the same visible carrier family repeatedly returns stale, contested, missing-source-relation, or no-currentness A.10 results, record a source-relation repair action: instrument the source relation, expose the carrier field that carries the source-bearing relation, expose decision-log refs, add currentness checks and status checks, preserve claim-bound source relations for generated or copied outputs, require credential views to show status windows and currentness windows, require model documentation and data documentation to expose intended-use and evaluation-condition fields, or require provenance labels and attestation labels to name their bounded claim type. Repetition is an indicator that the source relation or display needs repair; it is not a reason to make each acting user rebuild the evidence-provenance path manually.

Display guidance for evidence and currentness: an evidence or status display should show the claim or effect, evidence carrier, the exact issuer, publication, registration, status-source, source-maintenance, trust, acceptance, or currentness predicate it uses, reference or link named by value, time window, freshness, relying context, and unsupported Work use, reliance use, claim, or effect. A display that can only show source availability should say so; it must not imply approval, permission, gate passage, Work occurrence, or assurance.

Incident-learning fields for evidence and currentness overread: visible carrier or publication face, intended claim or effect, missing evidence-provenance field, evidence carrier named by value, exact source-side predicate actually used, ordinary method trace or admitted Work trace, and needed time relation; rival explanation; current safe disposition; and the smallest upstream repair to instrumentation, selected source `U.Episteme`, exact publication occurrence when availability matters, changed publication form or carrier, issuer, registration, status-source, source-maintenance, trust, acceptance, or currentness relation, claim-bound source relation, credential view, model or data documentation, or provenance or attestation label.

Contestability and redress relation: when an evidence-provenance path or source-currentness relation affects person or team status, access, responsibility, a compliance relation, or a release decision, the A.10 result names the disputed claim, evidence carrier, affected use or harm, available challenge, review, redress, communication, source, publication, register, access, or contact relation, allowed evidence or argument, possible disposition change, outcome route, reopen trigger, and safe interim disposition. Source exposure remains independent of who may later perform review or repair Work. Name a responsibility, allocation, commitment, permission, or authority relation—or its exact missing governor—only when assigning that future Work; its absence does not close the challenge.

**Positive repaired evidence-use statement.** When the source account is complete, write the smallest bounded statement: named relied-on claim; carrier and source; direct provenance, citation, and currentness relations; ordinary bounded use; `RelianceDisposition`; unsupported attempted use; and reopen condition. Add producing or interpreting `U.Work`, its complete A.15.1/F.6 basis, method, actual bindings, and later Work only when those facts are independently current. A claimed Work-to-value link needs an exact A.6.1 application binding, one local A.15.PROD claim, or a direct subject predicate under its own pattern. Add authority or responsibility only when an exact relation is independently required by the use. A short Work statement may omit only an unused assignment identifier, not the underlying attribution; an assignment is never the authority or responsibility result.

What this does not authorize: A.10 does not approve, authorize, pass a gate, release, create permission or commitment, classify a local system-role kind, establish a `U.SystemRoleAssignment` occurrence or state, establish a relation among system-role kinds, record Work, establish a domain result, assert a representation correspondence, or raise assurance. It supplies source recovery, provenance, and bounded reliance for the exact neighboring objects named by value.

#### A.10:4.6b - Local evidence-use classifier and `RelianceDisposition` for source-bearing carrier or display reliance

Use this subsection when a visible carrier, publication face, selected source `U.Episteme` ref, exact `EpistemePublicationRelation` occurrence ref when availability is material, source relation ref, or display is being relied on for a named claim or act. First recover the claim kind, the pattern or source rule that defines or tests the claim, the source/provenance path, and the bounded use. Broad words such as `source`, `metric`, `confidence`, `conformant`, `safe`, `ready`, `certified`, `approval`, or `permission` are recovery prompts, not relation names.

This is a local reliance-use classifier, not a Core evidence-kind ontology. Use only the row that decides the attempted use. The path represents exact direct relations and the `RelianceDisposition` records one bounded A.10 judgment; neither becomes a general evidence or authority relation.
Affordability card: orientation or source-finding remains a cue and stops here; bounded reliance states one evidence use, unsupported attempted use, window, and reopen condition. If a direct domain rule requires assurance, state the exact assurance claim and then use B.3. Plain wording remains ordinary unless it changes one of the named source, evidence, gate, assurance, Work, decision, or control claims.

Cheap stop: if a bounded claim, current carrier, evidence-provenance path, window, bounded evidence use, unsupported attempted use, and reopen trigger are present, and there is no actual assurance claim, gate relation, Work relation, control-bearing relation, or release relation, stay in `A.10`. Do not open B.3, A.21, B.2.5, or a broad evidence pack merely because the carrier or display looks official, quantitative, generated, credentialed, or safety-related.

Common wrong first classification: a visible carrier, selected source `U.Episteme` ref, publication-form or carrier ref, exact `EpistemePublicationRelation` occurrence ref, source relation ref, or display is approval, permission, safety, or readiness. First honest entry: recover the A.10 evidence-provenance path for one bounded claim or use; approval, permission, safety, readiness, gate passage, and work authority must be established separately under the pattern that defines or tests each claim.

Plain disposition palette: `RelianceDisposition=pass` means proceed only inside the bounded evidence use; `degrade` means use only a narrower or reversible version; `abstain` means do not decide yet; `reopen` means a changed or contested evidence relation defeated the previous classification; `evidence-needed` names missing evidence at the decision point; `assurance-needed` says a separately stated assurance claim is required before this attempted use can proceed; `blocked-current-use` blocks the attempt until its evidence-provenance path or source relation changes.

| Source-looking evidence use or attempted use | First A.10 action | Escalation trigger | Forbidden overread |
| --- | --- | --- | --- |
| Ordinary source-backed report, record, citation, observation, model card, datasheet, data card, or publication excerpt | Name the claim, carrier, producer or Method trace when relied on, evidence-provenance path, currentness window, bounded evidence use, unsupported attempted use, and reopen trigger. | Open B.3 only when an actual named assurance claim is current; open A.21 for a relied-on gate decision, A.15 or A.15.1 for Work, or another pattern only when that relation is actually claimed. | Evidence presence as approval, gate passage, assurance, release permission, Work authority, control authority, or safety acceptance. |
| Confidence, calibration, prediction interval, abstention reason, or selective-action cue | Name the act, window, calibration population, exchangeability, shift, applicability, and stop condition for the bounded evidence use. Use `pass` or `degrade` only for that use and state the unsupported attempt. | Open C.27 or G.11 when timing, expiry, refresh, distribution shift, monitoring, or applicability changes the act; open B.3 only for an actual named assurance claim. | Confidence as global permission, trust, readiness, safety, release reliance, or engineering justification. |
| Generated explanation, generated summary, or didactic reconstruction | Keep the rendering in `E.17.EFP` as explanation or source-finding unless each relied-on operative claim has an `A.10` evidence-provenance path or another source relation that carries or exposes the source basis for the operative claim. | Apply `A.10`, `B.3`, `A.21`, `A.15`, or the pattern that defines or tests the operative claim being relied on. | Explanation wording as evidence, assurance, approval, gate passage, work occurrence, or permission. |
| Conformance label, `CV.Status`, benchmark result, score, semantic-fidelity marker, or CV-looking publication near release | Recover the declared relation: measurement or marker relation, `A.20` step-local CV status, `A.21` gate check, `E.19` pattern-quality result, `C.16` characterization, or external-rule source named by value. | Open `A.21` only when an `OperationalGate(profile)` consumes effective gate-check refs and emits a `GateDecision`; open `B.3` only when an assurance claim is being made. | Conformance or score as value, adequacy, release confidence, work occurrence, safety, trust, or gate passage outside the declared relation. |
| Provenance, authenticity, C2PA-like credential, SLSA-like attestation, build record, or status-register display | State the bounded origin, history, build method or production trace, holder, status, verifier rule, relying context, and currentness claim it evidences. | Open the record or relation that carries truth, permission, safety, release, gate passage, work occurrence, or assurance only when that relation is being claimed by value. | Provenance, authenticity, or status-currentness as truth, safety, approval, permission, release, gate passage, or assurance. |
| Contest, redress request, challenge, appeal, or conflicting source relation | Name the contested claim, evidence carrier, source-order or currentness issue, affected use or harm, available challenge or redress relation, allowed evidence, possible disposition change, outcome route, and reopen trigger. Add a review-responsibility relation or missing governor only when the claim assigns future review Work. | Open neighboring system-role, assignment-state, commitment, gate, control, assurance, Work, or representation patterns only when those effects are claimed by value. | Appeal-channel presence, challenge form, or redress workflow presence as truth, compliance proof, social-effect acceptance, completed redress, gate passage, or work authorization. |

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
| `RelianceDisposition=evidence-needed` | The visible carrier, selected source `U.Episteme` ref, exact publication-occurrence ref when availability is material, source relation ref, or display may matter, but the required evidence kind or source-currentness relation is absent. | State the missing evidence kind, the pattern or source rule that defines or tests it, and the decision point so delay does not become indefinite. |
| `RelianceDisposition=assurance-needed` | A direct domain rule or receiving decision requires a separately stated assurance claim before the attempted use may proceed, and the current A.10 basis alone cannot supply it. | State the required assurance claim and its direct domain basis. Apply B.3 only after that claim is current; until then block or narrow the attempted use. |
| `RelianceDisposition=blocked-current-use` | No current evidence-provenance path carries the evidence relation needed for the attempted act, work, claim, gate, release, assurance, review, control-bearing feedback, or P2W use. | State the blocked use and the neighboring pattern or project record required before a new attempt. |

Minimum contest relation with possible redress: a contest relation exists when the affected party can identify the disputed claim or source, affected use or harm, an available challenge, review, redress, communication, source, publication, register, access, or contact relation, evidence or argument allowed in challenge, possible disposition change, outcome route, and reopen trigger. A system-role label, assignment, feedback channel, complaint form, or appeal label without those recoverable values is not enough to change the disposition. Responsibility for future review Work is a separate claim.

Affected-party contestable minimum: even when raw evidence stays restricted, the contesting party must be able to see enough of the claim, source class, disposition, affected use, available challenge or contact route, and allowed challenge evidence to challenge the result. Privacy, security, or privilege can narrow disclosure; they cannot erase the challengeable minimum while still claiming contest or redress.

False-negative reliance guard: a blocked, abstained, or evidence-needed use is not final if challenge evidence, missing affected-party evidence, changed source relation, changed selected source `U.Episteme` edition, changed `EpistemePublicationRelation` occurrence when availability is material, changed publication form, changed evidence carrier, changed representation, or redress can materially change the disposition. If refusal is based on missing evidence, name the missing evidence kind and decision point rather than closing the dispute by vagueness.

Sensitive evidence boundary: use scoped, hashed, redacted, or access-controlled evidence refs when raw carriers would expose personal data, secrets, tokens, privileged logs, tenant identifiers, incident details, security-sensitive traces, or unnecessary identities. A redacted path must still preserve enough recoverability for the relied-on claim, disposition, and contest relation.

Worked source-overread slices:

| Slice | A.10 usable classification | Unsupported lift |
| --- | --- | --- |
| Software supply-chain attestation is cited near a release conversation. | The attestation may evidence bounded origin, build method or production trace, verifier-rule, holder, and currentness claims. | Runtime safety, release approval, gate passage, or assurance unless `B.3`, `A.21`, or another relation that carries the asserted use is established for that use. |
| A verified provenance credential, watermark, or authenticity mark appears on a publication face. | The mark may evidence where the carrier, signature, assertion, or manifest came from under the verifier regime. | Truth of the represented world-state, safety, permission, or adequacy by provenance alone. |
| A confidence interval or calibration result is used for one reversible act. | State the act, context, calibration condition, window, bounded evidence use, unsupported attempted use, and stop condition. | Global readiness, trust, safety, release reliance, or engineering justification. |
| A generated explanation or summary says a result is reliable. | Treat the rendering as source-finding or explanation until the operative claim has an `A.10` evidence-provenance path or another source relation that carries or exposes the source basis for the operative claim. | Evidence, approval, gate passage, work occurrence, or assurance by fluent wording. |
| Contest or redress is claimed after a source relation, selected source `U.Episteme`, exact publication occurrence, publication form, or evidence carrier is challenged. | State the disputed claim, affected use or harm, available challenge or redress relation, allowed challenge evidence, possible disposition change, outcome route, and reopen trigger. Add future-review responsibility only when that stronger claim is current. | Claim truth, compliance proof, completed redress, or social-effect acceptance by appeal-channel presence. |
| A harmed party gives challenge evidence that could change the disposition, but the receiving System answers "evidence insufficient" without naming the missing evidence kind or decision point. | Treat the refusal as `RelianceDisposition=reopen` or invalid `RelianceDisposition=evidence-needed`; name the missing evidence kind, decision point, available challenge route, and possible disposition change. | Closed refusal, completed redress, or `RelianceDisposition=blocked-current-use` by vague insufficiency. |

#### A.10:4.7 - Causal support in evidence-provenance paths

An A.10 path used for a causal claim cites the exact C.28 components it actually carries; it does not compress them into one alternative-valued “support basis” or copy C.28's field list.

```text
causalSupportComponentRefs?: CausalSupportComponentRefs
causalUseSupportResultRef?: CausalUseSupportResultRef
```

`CausalSupportComponentRefs` remains defined only by C.28. A.10's ordinary evidence-provenance path still identifies the exact source, carrier, Work or data, provenance relations, and bounded use required by this pattern. Inside the C.28 contract, cite only the components the causal claim actually relies on. When C.28 admits another specialist component, A.10 can cite it through that contract without defining a second schema.

Examples:

- an observational cohort path cites the observation and measurement Work plus `observationalOrNaturalBehaviorData`; an intervention-effect statement still needs a C.28 identification or design result;
- a randomized estimate path cites assignment and Work evidence, its identification or design result, estimate, uncertainty, and limits;
- a prospective counterfactual-sampling path may cite the realizability result with its decision Method, construction, bound, or obstruction, but claims no performed sampling or data;
- a performed counterfactual-sampling path cites dated sampling Work, attribution, and the resulting sample or data; only that complete path may support `realizedCounterfactualSamplingData`;
- a simulation path cites model output, assumptions, validation, and bounded model use; it does not become realized or interventional evidence by relabeling;
- a target-trial emulation path cites its `TargetTrialMappingResult`, including the observational source, protocol-to-data mappings, gaps, residual-confounding assessment, and sensitivity mappings; reporting completeness alone establishes neither identification nor low bias;
- an off-policy or causal-RL path cites its exact `OffPolicyCausalEvaluationResult` with the question, behaviour and evaluation policies, overlap check, supported and unsupported use, and reopen condition. It also cites optional details about history or horizon, confounding, changed endpoints or transport, the estimator, and uncertainty only when they change what the path supports, where that support came from, whether it is current, its bounded use, or when it reopens;
- a causal-representation path cites its exact `CausalVariableRepresentationRecord` with the question, source representation, selection or abstraction Method, representation assumptions, intervention-validity result, supported and unsupported use, and reopen condition. It also cites optional invariance, fidelity, query-preservation, uncertainty, or shift-limit results only when they change what the path supports, where that support came from, whether it is current, its bounded use, or when it reopens;
- a transport path cites every changed endpoint, assumptions, overlap evidence, formula or comparator, uncertainty or unresolved assumptions, and bounded use carried by its transportability result; and
- an observationally identified estimate cites both the evidence path and separate identification and estimate results.

What changes in practice: the path exposes where every relied-on component came from and may cite the C.28 support-result episteme. A.10 creates none of the C.28 components, the causal verdict, or downstream authority by carrying their refs.

### A.10:5 - Archetypal Grounding

**Runtime acceptance from a measurement result.** C.16 dated measurement work obtains a pressure measurement result with uncertainty under a named model and calibration; a distinct C.2.1 episteme states it. If the claim that this Work first constituted that episteme is current, A.15.PROD recovers one local entity-inception claim. Separate evaluation work applies the declared G.4 pressure clause through A.6.1 bindings and obtains `unknown`; another C.2.1 episteme states that verdict. A.10 records the source publications, calibration and measurement work, result episteme, evaluation work, clause declaration, exact bindings, provenance, currentness, and rival explanation. Later C.11 decision work uses the verdict episteme as a premise and defers. No ledger edge establishes measurement, verdict, decision, or use.

**Meta-analysis.** Source study publications, datasets, analysis code, inclusion work, statistical method, and synthesis work are recovered by their direct relations. The statistical method and result relation establish the pooled estimate and uncertainty; its C.2.1 episteme is the relied-on claim. A.10 records source identity, transformations, coverage, provenance, currentness, and the bounded clinical or policy use, not a generic `validatedBy` relation.

**Credential display.** A credential view can support credential currentness only when it names the exact issuer or trust-root object and relation, holder binding, verifier, exact status source or register relation, revocation, and window. Permission, commitment, an exact system-role-assignment occurrence, status assertion, entry predicate, and gate passage remain with A.2.8.PER, A.2.8, A.2.9, A.2.1, A.6.B, and A.21 as applicable. Display presence creates none of them.

### A.10:6.1 - Bias-Annotation

A.10 corrects carrier-authority bias and graph-authority bias. A polished badge, attestation, dashboard, generated explanation, or provenance mark can make an unsupported claim look settled; a tidy graph can make an ungrounded edge look like an obtaining relation. The repair is to recover the claim, source, carrier, work, local result, pattern or source rule that establishes it, result episteme, direct relations, currentness, bounded use, rival explanation, and disposition. More impressive paperwork is not a substitute.

### A.10:6 - Conformance Checklist

1. **Claim:** the exact relied-on C.2.1 episteme and proposition/local result are named.
2. **Result rule:** every measurement, formal, causal, diagnostic, conformance, comparison, selection, acceptance, gate, permission, commitment, system-role-kind classification, system-role-assignment occurrence or state, relation among system-role kinds, or decision result identifies the pattern that defines or tests it; any other technical *role* use is first routed through E.10.ROLE.
3. **Carrier/source:** the selected source episteme and edition, any material publication occurrence, form, carrier, or face, the copy/transform chain, and direct provenance or citation relations are recoverable.
4. **Work:** whenever production, interpretation, transformation, evaluation, or reliance is asserted as dated `U.Work`, point to its complete A.15.1/F.6 basis. Add direct relations, A.6.1 bindings, and resource-use facts only when the receiving claim uses them. Ordinary source-finding action need not be admitted as `U.Work`.
5. **MethodDescription boundary:** the description contains only generic method claims; it supplies no actual participants, occurrence, use, proof/test event, or result.
6. **Result boundary:** domain result, result episteme, carrier, provenance entry, outcome, and later action remain distinct.
7. **Graph boundary:** every asserted edge names an independently established direct relation; no edge establishes work, participation, production, result, currentness, reliance, or representation by graph membership.
8. **Time/currentness:** edition, window, supersession, revocation, source order, and G.11 result are explicit when they affect use.
9. **Reliance:** bounded use, unsupported attempted use, local `RelianceDisposition`, rival explanation, and reopen trigger are present; B.3 opens only when an actual named assurance claim is current.
10. **Contest/privacy:** the affected party can challenge the claim and disposition, while sensitive carrier access is minimized without erasing recoverability.

### A.10:6.2 - Common Anti-Patterns and How to Avoid Them

- **Carrier as truth.** Recover the claim and direct source relation; authenticity or availability is not truth.
- **MethodDescription as intent or trace.** Recover generic method claims separately from the dated work and actual bindings.
- **Generic result field.** Name the domain result, the pattern that defines or tests it, and the distinct C.2.1 episteme.
- **Edge as fact.** Establish the direct relation first; then let the graph represent or cite it.
- **Provenance as assurance or permission.** Enter B.3, A.2.8.PER, A.21, or the pattern that defines or tests the additional claim only when that claim is live.
- **Citation as actual use.** Ground the later work and exact premise/reference/argument relation.
- **Full dossier by default.** Collect only fields that decide the bounded use, consequence, contestability, and reopen condition.

### A.10:7 - Consequences

**Benefits.** Reliance becomes replayable without turning A.10 into an authority over the results it cites. The same path can expose stale sources, hidden transformations, ungrounded work, incompatible currentness, or an unsupported lift from provenance to action.

**Trade-offs.** Subject-pattern recovery takes more effort than a single evidence edge. The gain is that later users can challenge exactly the claim, work fact, source relation, currentness result, or reliance boundary that failed.

**Failure containment.** Missing source, work, direct binding, rule for a cited result, currentness, or use relation blocks or narrows only the affected reliance use. It does not authorize a universal evidence or result relation.

### A.10:8 - Rationale

Evidence use is a relation-specific claim about why one later use may rely on one episteme. Provenance records make the source history recoverable; they do not create the source facts, local result, truth, work, or use. Keeping the descriptive graph outward-facing keeps each cited result with the rule that establishes it while still making complex source chains inspectable.

### A.10:8.1 - SoTA-Echoing

Source qualification was checked against the publishers' current surfaces on 2026-07-30. It remains qualified through 2027-07-30 unless a latest specification, Recommendation, tagged framework release, status mechanism, or adopted documentation baseline changes earlier. Each source changes only the bounded A.10 locus named below; lineage and popular comparators not listed here are non-governing.

| Exact source and source-use decision | Visible A.10 mutation | Rejected overread | Smallest source-change replay |
| --- | --- | --- | --- |
| [W3C PROV-O, Recommendation 30 April 2013](https://www.w3.org/TR/prov-o/) — **adapt** qualified provenance descriptions and stable source/activity/agent references to A.10's exact FPF objects and direct relations. | §4.4 requires each path edge to cite an independently established relation; checklist items 3 and 7 require source/copy/transform identity and reject graph membership as fact creation. | A PROV-shaped graph, `wasGeneratedBy` label, or qualified relation does not establish FPF work, participation, result, truth, currentness, or later use. | Reopen only §4.4's edge rule, the affected path in one worked case, and checklist items 3 and 7 if PROV-O's qualified-relation contract changes. |
| [W3C Verifiable Credentials Data Model v2.0, Recommendation 15 May 2025](https://www.w3.org/TR/vc-data-model-2.0/) — **adapt** the separation among issuer, represented subject, holder, verifier, validity, status, proof, and relying context. | §4.6b's credential-and-status row, the credential-display case, and checklist items 8–9 require the verifier rule, status source, validity window, currentness, bounded use, and local disposition. | A conforming or cryptographically verifiable credential does not by itself create transitive trust, permission, a `U.SystemRoleAssignment` occurrence, gate passage, assurance, or truth of every represented claim. | Reopen only the credential-and-status classifier row, the credential-display case, and checklist items 8–9 when the VC data model or its adopted status specification changes. |
| [SLSA specification v1.2](https://slsa.dev/spec/v1.2/) together with [in-toto Attestation Framework v1.2, `Statement/v1`](https://github.com/in-toto/attestation/blob/main/spec/README.md) — **adapt** artifact subject, predicate type, producing context, inputs, authenticated envelope, verifier expectation, and versioned attestation separation. | The §4.6b supply-chain row and software-attestation slice require a bounded build/source claim, producing work or system, verifier rule, source inputs, holder, window, and unsupported attempted use; checklist items 3 and 9 retain provenance and reliance separately. | A signed attestation, SLSA level, or verification summary is not runtime safety, release approval, gate passage, assurance, or proof that an uncited work/result relation obtains. | Reopen only that classifier row, the software-attestation slice, and checklist items 3 and 9 when SLSA's adopted provenance/verification contract or in-toto `Statement/v1` semantics change. |
| [C2PA Content Credentials Technical Specification 2.4, April 2026](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html) — **adapt** asset/manifest identity, claim generator, assertions, ingredients/actions, signature validation, trust policy, and specification version for claim-bound content attribution. | §4.6b's provenance/authenticity row, generated-content boundary, credential-display case, and checklist items 3 and 8 require the exact carrier, manifest/assertion, transformation, verifier/trust regime, edition, and currentness window. | A valid manifest, repository receipt, authenticity mark, or visible Content Credential does not establish truth of the represented world state, authorship beyond its exact assertion, permission, safety, or adequacy. | Reopen only the content-provenance classifier row, the credential-display case, and checklist items 3 and 8 when C2PA changes manifest/assertion identity, validation, trust, or versioning rules. |
| Mitchell et al., [*Model Cards for Model Reporting*, FAT* 2019](https://doi.org/10.1145/3287560.3287596), and Gebru et al., [*Datasheets for Datasets*, CACM 64(12), 2021](https://doi.org/10.1145/3458723) — **adapt** intended use, evaluation conditions, performance/limitation, motivation, composition, collection, and maintenance disclosures as source-finding inputs. | §4.6b's generated-explanation/documentation row and checklist items 1, 3, and 6 require every relied-on operative claim to return to its exact source, work, local result, carrier, and bounded use rather than relying on the document's presence. | A model card, datasheet, polished summary, or disclosed limitation is not evidence for an unstated claim, performed evaluation, assurance, approval, or deployment permission. | Reopen only the documentation classifier row, the one model/data-document path that uses it, and checklist items 1, 3, and 6 when the adopted disclosure fields or their claim boundary change. |

The current source decisions deliberately do not import a credential, attestation, documentation, or provenance ontology as A.10 authority. Source refresh replays the named rule, case, and checklist rows first and widens only if that local replay exposes a direct contradiction.

### A.10:9 - Relations

- **Builds on:** C.2.1 for claim and result epistemes; E.17 for publication and carriers; A.15.1 and F.6 for dated Work and attribution; A.6.1 for actual operation bindings; A.15.PROD when entity inception or production completion is current; and E.10.ROLE plus the selected A.2-family pattern for any technical *role* claim.
- **Coordinates with:** A.2.4 for first-use evidence/status classification; G.11 for currentness; C.29 for representation; B.3 for assurance; C.16 for measurement; C.28 for causal use; A.19 for comparison/selection; G.4 for acceptance declarations and applications; C.11 and A.21 for decision/gate results.
- **Constrains:** provenance and reliance descriptions only. A.10 does not create another pattern's result, occurrence, participation, representation, currentness, assurance, permission, commitment, gate, or decision.

### A.10:10 - Older source text interpretation and neighboring-pattern notes

Treat legacy names such as `manifest`, `creator`, `observer`, `symbol register`, `SCR`, `RSCR`, `MIC`, `verifiedBy`, `validatedBy`, or evidence `path` as recovery prompts, not current relation names.

- A manifest or source register is a carrier/publication or provenance description; recover the exact source, edition, claim, and direct relations it represents.
- A `creator`, `observer`, producer, verifier, or maintainer participates as an admitted System only when the direct participation relation obtains. If dated Work is asserted, point to its complete A.15.1/F.6 basis and any exact direct or A.6.1 bindings used by the claim. Those labels and assignments supply neither participation, authority, nor responsibility.
- A method-instantiation note is not work. Recover the exact `U.Method`, generic MethodDescription claims, dated occurrence, enactment, ordering, participants, and result separately.
- A `work result`, `measurement result`, `validation result`, or `verification result` label requires the exact domain result and a separate C.2.1 episteme; the legacy field name establishes neither.
- Resource rosters remain separate from carriers and provenance records.

When older text also claims approval, permission, gate passage, assurance, causality, comparability, representation, publication effect, or decision, use the pattern that defines or tests that additional claim and let A.10 retain only source recovery, provenance, bounded reliance, and contestability.

### A.10:10a - Evidence carriers for quantum-like statements

Use A.10 when a quantum-like statement is being relied on. Name the minimal claim, selected source episteme and edition, any material publication occurrence, form, or carrier, time and currentness, rival explanation, bounded use, unsupported attempted use, and `RelianceDisposition`. Add producing or interpreting dated `U.Work`, Method, actual bindings, and a Work-to-value predicate only when those facts are independently current. Use C.16 for ordinary measurement, the relevant C.26 pattern for probe or frame effects, F.9 for Bridge loss, C.29 for representation, and B.3 for material assurance.

The `quantum-like` label has no evidence weight. A descriptive graph may represent the source and use relations only after those relations are established.

### A.10:10b - C.29 mathematical-lens use relation

When a mathematical lens is used in the evidence account, use C.29 for the representation correspondence and lens-use admissibility claim. A.10 may cite that C.29 episteme and record its provenance, currentness, bounded reliance, and later use; an A.10 graph edge does not establish the correspondence. Use C.16 for measurement construction and B.3 for assurance.

### A.10:End

