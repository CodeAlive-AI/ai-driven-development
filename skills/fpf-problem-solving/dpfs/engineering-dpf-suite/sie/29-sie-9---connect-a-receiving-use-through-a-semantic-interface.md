## SIE.9 - Connect a Receiving Use through a Semantic Interface

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `ReceivingSemanticInterface@Use` defining the smallest query, view, API, message, schema, report, or other boundary that carries the required meanings and branches to the receiver with interpretation, source and provenance, currentness, accepted loss, access assumptions, errors, unresolved returns, and a path back to the owning source or decision.

### SIE.9:1 - Problem Frame

**Use this when** semantic mappings or integrated state exist but the receiving Work still cannot obtain, interpret, challenge, or return the bounded result. Enter when a technically reachable endpoint hides source meanings, currentness, unmatched rows, conflicts, or the difference between “no value” and “source unavailable”.

For the named receiving use, start with the action the result is meant to support. Choose the smallest interaction and result form that connects the maintained integration arrangement to that use and carries every branch the receiver needs. Supply an interface contract and a candidate interface. Establish the receiver’s authorization and the service’s operating adequacy separately when the use requires them.

The payoff is a boundary at which semantic meaning, failure, and provenance are usable by ordinary Work. Do not use SIE.9 to design the application's whole user experience, make its decision, operate the service, or accept engineering/quality results. Those owners consume the interface under their own Methods and authority. Stop rather than return a positive interface when a required semantic branch, interpretation, provenance/currentness condition, source-return path, or receiver-side use test cannot be represented or traced.

### SIE.9:2 - Problem

Integrated data can remain unusable because the receiver cannot ask the relevant question or distinguish the answer's conditions. An API may omit source edition and effectivity; a report may list a fused value without conflict; a schema may use one null for unknown, not applicable, stale, and timeout; a user may have no path to challenge an identity or mapping premise.

When the interface is treated as transport only, semantic obligations remain in internal documentation. The receiving Work either overtrusts the result or reconstructs meanings informally, creating a second uncontrolled integration at the boundary.

### SIE.9:3 - Forces

| Force | Tension |
| --- | --- |
| Minimality | A small interface is easier to use and maintain, while hiding source, loss, or failure makes it unsafe. |
| Receiving the result | The receiver needs to interpret the result and be able to return a disputed premise for review. A programmatic interface needs a stable schema, stable branch codes and a return path the caller can follow. A human-readable interface needs to explain the branch and show where to raise the question. |
| Abstraction | Receiver-friendly names reduce burden, while source identifiers and meanings must remain recoverable. |
| Performance | Rich provenance and alternative claims cost bandwidth and attention, while omitted trace defeats challenge and validation. |
| Security | The receiver needs enough source information to rely, while disclosure can violate provider, privacy, or protection conditions. |
| Evolution | Stable interface promises aid use, while source or mapping changes must not be hidden behind unchanged field names. |

### SIE.9:4 - Solution

Design the interface from receiving actions and semantic branches, not from the internal store. Expose the smallest result that preserves interpretation, source/version, currentness, accepted loss, identity and claim status, provenance, access assumptions, errors, unresolved returns, and source-return paths. Bind every field and branch to the use contract, mapping rules, and selected realization.

#### SIE.9:4.1 - Pattern-Use Unfolding

1. **Name the receiver interaction.** State who or what asks, the query/message/report action, timing, input parameters, and the next Work or decision that consumes the answer. For several recipients, specify what each may receive and act on, and when. Check a shared delivery against all its required users. A joint decision may also need them to exchange results or authorize a common action.
2. **Select the interface form.** Choose query, view, API, message, schema, report, file, or mixed human/machine form based on the receiving Work. Do not inherit the internal realization shape automatically.
3. **Define semantic inputs.** State the identifiers a request accepts, how the interface validates their form and how it resolves them. Supply any required issuer, assignment context, configuration or effectivity, time window, units, locale or code context, and permissions.
4. **Define result claims and interpretation.** For each output, state meaning, grain, scope, interval/effectivity, units/codes, source identifier behavior, accepted loss, and permitted use. For an interface used in a decision, consider the proposed response together with the rules, records and other context each recipient is entitled and able to use before choosing. Hold that whole body of information fixed and vary the admissible source state (SIE.3:4.1). Establish that the premises used for a positive conclusion admit a possible situation. The information may determine the requested answer, justify a particular choice under the agreed criterion, or support a guaranteed action throughout the remaining possibilities. Preserve any grounds the recipient is asked to give. Where a necessary distinction remains unavailable, establish how it could reach the decision in time. A qualified result computed at the source or an authorized lookup may suffice. Distinguish conflicting claims from missing or inaccessible evidence. Return the branch the contract provides, together with any answer that has sufficient independent grounds. A single response can serve different questions when it supplies what each needs.
5. **Expose qualified branches.** Represent matched/qualified, unmatched, incompatible, unresolved identity, source-qualified conflict, non-comparability, stale, inaccessible, timeout/source error, and partial result where applicable.
6. **Expose provenance and currentness.** Provide source/edition or a stable reference, observation/retrieval time, mapping/composition rule version, derivation/trace reference, and freshness status needed by the receiver.
7. **State access, protection, and authority assumptions.** Explain what the interface verifies, what the caller supplies, what may be disclosed, and which actions remain unauthorized by the semantic result.
8. **Provide challenge and return paths.** A receiver must be able to identify which source, correspondence, identity disposition, composition, mapping or operational result needs examination and where to return the issue.
9. **Bind service behavior without claiming it.** State latency, availability, pagination/volume, ordering, idempotence or snapshot expectations only where semantic use depends on them; obtain implementation/operation evidence separately.
10. **Define conformance and reopen.** Give representative requests, responses, error branches, compatibility conditions, deprecation/change behavior, and observations that reopen the interface.

#### SIE.9:4.2 - Record the Result

| Interface position | Required content |
| --- | --- |
| receiver interaction | caller/reader, receiving Work, request, timing, next action |
| interface form | query/view/API/message/schema/report/file and why it fits the Work |
| request semantics | parameters, acceptable identifier forms and resolution context, configuration/effectivity, windows, units/codes, permissions |
| response semantics | claims, grain, scope, interval, units/codes, source IDs, accepted loss, permitted use |
| branch model | qualified, unmatched, incompatible, unresolved identity, conflict, non-comparable, stale, inaccessible, source error, partial |
| provenance/currentness | source/edition, times, rule versions, derivation/trace, freshness status |
| protection/authority | verified and assumed conditions, disclosure limits, action not authorized |
| challenge/return | stable path to source, semantic premise, mapping, implementation, or direct decision owner |
| service/conformance | action-sensitive service conditions, examples, errors, compatibility/deprecation, reopen |

#### SIE.9:4.3 - What Changes in Practice

The receiver no longer has to infer semantic meaning from field names or call the integration team to understand a missing row. Qualified, incompatible, conflicting, stale, and source-error states become part of the normal interface contract, and every challenge can be returned to a specific premise or owner.

### SIE.9:5 - Archetypal Grounding - AP242/QIF Review Interface

The quality engineer uses a view or API with request parameters `productDefinitionRevision`, `configuration`, `featureIdentifier`, and `effectivity`. The candidate response preserves these positions:

| Response position | Constructed behavior |
| --- | --- |
| `feature` | AP242 source identifier, issuer/profile, configuration/effectivity, source edition, and receiver-friendly label |
| `inspectionCharacteristic` | QIF source identifier, plan and characteristic meanings, source edition, and the accepted correspondence-row reference |
| `inspectionResult` | source-qualified QIF claim, observation time/status, unit and original value, provenance, and any conversion rule |
| `identityDisposition` | referenced `SIE.5` result and its grain/interval, not a copied boolean |
| `claimStatus` | qualified, conflict, non-comparable, or unresolved with the `SIE.6` composition reference |
| `freshness` | released AP242 configuration/effectivity used, QIF observation window, retrieval time, and stale status |
| `rowDisposition` | matched, unmatched-feature, unmatched-characteristic, unresolved-assignment, no-assignment, incompatible, unresolved-identity, stale, source-error, or prohibited |
| `returnPath` | source record and mapping/correspondence/identity/composition rule references plus the direct engineering or quality owner for the decision |

A known match returns a qualified row. A feature absent at effectivity `E` returns unmatched rather than the nearest label. An unresolved identity returns that branch without claiming no inspection exists. Two identified objects can still have an unresolved assignment when only an excerpt of the plan is available. Return no-assignment when the complete applicable plan settles the question. A source timeout returns partial/incomplete only if the contract permits it. The responsible participants decide whether to accept the result or release the configuration.

### SIE.9:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | Interface access is mistaken for permission to act or disclose. | State verified/assumed permissions, disclosure limits, and the direct action authority. |
| Architecture | Internal graph or warehouse schema becomes the public contract. | Design from receiving actions and preserve realization independence where useful. |
| Ontology/Epistemology | Field name, status code, and claim meaning collapse. | Define every output and branch with scope, source, time, and permitted use. |
| Pragmatics | Full provenance overwhelms routine use. | Expose the action-changing summary and a stable trace path to detailed premises. |
| Didactics | Error branches look like exceptional implementation failures. | Teach unmatched, incompatible, conflict, and unresolved as normal semantic outcomes. |

### SIE.9:7 - Conformance Checklist

- [ ] The request and receiving Work identify who uses the answer, their permitted content, and the next action of each required recipient.
- [ ] The form is chosen for receiving use rather than copied from internal realization.
- [ ] The request identifies the accepted entries, how to resolve them, required configuration or effectivity, windows, units or codes, and permissions.
- [ ] Response claims state meaning, grain, scope, interval, source identifiers, loss, and permitted use.
- [ ] Qualified, unmatched, incompatible, unresolved identity, conflict, non-comparability, stale, inaccessible, source-error, and partial branches remain distinguishable where applicable.
- [ ] Source/edition, observation/retrieval time, rule versions, derivation/trace, and freshness are recoverable.
- [ ] Protection, disclosure, and authority assumptions are explicit; the interface grants no unstated authorization.
- [ ] The receiver can return a defect or gap to a specific source, semantic premise, mapping, implementation, or decision owner.
- [ ] Action-sensitive latency, availability, snapshot, and volume behavior are stated without claiming unobserved performance.
- [ ] Representative requests, responses, errors, compatibility/deprecation behavior, and reopen conditions are present.

### SIE.9:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Expose the integrated table | Start from the receiving action and design only the claims and branches it needs. |
| One null or HTTP error for every absence | Distinguish semantic absence/unresolved states from access, timeout, and implementation failure. |
| Provenance in internal logs only | Expose the action-changing provenance/currentness summary and stable trace reference. |
| Hide source IDs behind one key | Retain the source entries, the contexts or assignments used to interpret them and the disposition supporting any identity on which the interface relies. |
| Endpoint is available, therefore usable | Validate meanings, branches, currentness, service conditions, and representative Work through `SIE.10`. |
| Semantic result authorizes action | Name the application, engineering, quality, safety, legal, or other decision owner. |

### SIE.9:9 - Consequences

The semantic arrangement becomes directly usable and challengeable. Receivers can distinguish a negative semantic result from an operational failure, and implementations can evolve behind a stable bounded contract while preserving source and rule trace.

The cost is a richer branch model and deliberate presentation of uncertainty and provenance. Some internal schemas or protocols must be wrapped rather than exposed directly.

### SIE.9:10 - Rationale

An integration result has practical value only when it crosses into receiving Work without losing the conditions that make it meaningful. The interface carries interpretation, qualification and return paths. The receiving participant uses the result within its authority and refers other decisions to their designated owners.

### SIE.9:11 - SoTA-Echoing

The best-known line combines explicit API/data-contract practice, data-on-the-Web provenance/version guidance, event interfaces, and standards-based engineering exchange. The serious default is transport-first interface design. Its defect is that success is reduced to reachability and schema conformance. SIE.9 uses these contributions to make semantic branches, currentness, provenance, and challenge paths part of the receiving contract.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| [Data on the Web Best Practices](https://www.w3.org/TR/dwbp/) | adapt | Contributes metadata, provenance, version, access, and reuse questions; Web publication is optional. |
| [GS1 EPCIS 2.0.1](https://ref.gs1.org/standards/epcis/2.0.1/) | adapt | Supplies an event-oriented cross-enterprise interface case with identifiers and query semantics; it does not decide SIE identity or receiving action. |
| [ISO 10303-242:2025](https://www.iso.org/standard/84300.html?browse=tc) and [ISO 23952:2020](https://www.iso.org/standard/77461.html) | adapt | Supply unlike versioned engineering source/interface cases; their model scopes and direct authorities remain intact. |
| internal-schema or transport-first API | reject as sufficient | Reachability and schema shape cannot establish semantic interpretation, provenance, loss, branch behavior, or receiving-use fitness. |

Reopen when the receiver or action changes, a source/mapping/realization premise changes, observed service behavior violates a semantic condition, branch handling causes unsafe interpretation, or a protocol change defeats compatibility.

### SIE.9:12 - Relations

- `SIE.1` supplies the receiving action, answer claims, loss, service conditions, tests, and authority boundary.
- `SIE.2` supplies source meanings, identifiers, editions, access, provenance, and currentness.
- `SIE.4`–`SIE.7` supply correspondence, identity, composition, and executable mapping references and branches.
- `SIE.8` supplies selected realization, service assumptions, fallback, and missing implementation results.
- `SIE.10` validates the candidate interface and representative receiving workflow.
- The relevant application or professional participants decide on authorization and risk acceptance. Establish any claimed outcome from the receiving work. Data Engineering and Operations remain responsible for running the service.

### SIE.9:End
