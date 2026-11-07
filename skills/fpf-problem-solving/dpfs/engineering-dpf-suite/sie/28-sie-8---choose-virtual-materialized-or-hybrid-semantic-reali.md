## SIE.8 - Choose Virtual, Materialized, or Hybrid Semantic Realization

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `SemanticRealizationDecision@Use`: a supported choice, sufficient rejection, worthwhile probe, or missing-input result for a named semantic-integration use. A positive choice identifies the implementation results it still requires.

### SIE.8:1 - Problem Frame

**Use this when** accepted semantic mappings exist and the current question is whether to evaluate them at query time, persist integrated results, or combine both. Enter also when a graph database, warehouse, federation, cache, search index, API composition, or “virtual knowledge graph” has already been proposed and its semantic consequences need comparison.

The primary EntityOfConcern is one realization decision for a named semantic-integration use. The first move is to derive realization-sensitive criteria from the use contract and mapping specification. The first result is a bounded choice, probe, rejection, or missing-input return that leaves physical implementation and operation with their owners.

The payoff is a realization selected because it preserves the required meanings and service conditions, not because one carrier is fashionable or already available. Do not use SIE.8 to build, deploy, or operate a data service, select a whole enterprise platform, authorize access, or prove that the interface works. Data Engineering, platform, security, provider, finance, and other direct owners supply those results.

### SIE.8:2 - Problem

Materialization can improve latency and independence from source availability but creates copied state, invalidation, custody, storage, and refresh obligations. Virtual access can preserve source currency and authority but inherits source latency, availability, access, and query-capability limits. A hybrid can isolate hot or stable subsets but adds coherence and branch complexity.

When the choice is made from technology labels, these consequences remain hidden until operation. A copied graph is described as semantic truth, a federation as automatically current, or a cache as harmless optimization. The same mapping semantics can yield different provenance, currentness, error, and recovery behavior in each realization.

### SIE.8:3 - Forces

| Force | Tension |
| --- | --- |
| Freshness | Virtual reads can observe current source state, while network and source delays can still make answers stale or inconsistent. |
| Latency | Materialization and caching can respond quickly, while refresh and invalidation may violate the use's time boundary. |
| Availability | Copies can survive source outages, while they can conceal that authority or access conditions changed. |
| Source authority | Querying the source keeps custody visible, while a receiver may need stable snapshots and reproducible answers. |
| Security and permission | Fewer copies reduce exposure, while live federation can broaden runtime credentials and cross-source disclosure. |
| Provenance and reproducibility | Materialized snapshots aid replay, while virtual results need captured queries, source versions, and occurrence metadata. |
| Operability and recovery | A simpler runtime can reduce failure modes, while hybrid arrangements add invalidation and coherence responsibilities. |
| Cost | Storage, compute, licenses, egress, support, and provider dependency trade differently across cases. |

### SIE.8:4 - Solution

First use decisive conditions to exclude arrangements that cannot serve the contract. Describe and compare the serious remaining alternatives as complete arrangements, including source access, rule execution, state/copy behavior, provenance, currentness, failure branches, security, operation, recovery, exit, and joint resource demand. Return a supported choice, sufficient rejection, worthwhile probe, or missing-input result for the named use.

#### SIE.8:4.1 - Pattern-Use Unfolding

1. **Fix the receiving result.** Reference the `SIE.1` answer, `SIE.7` rules, required source/identity/claim branches, and validation conditions that a successful candidate must preserve.
2. **Apply decisive exclusions.** A known source prohibition or other sufficient condition can defeat an arrangement. Record the condition and evidence needed for that conclusion and stop developing the excluded alternative. If no serious candidate remains, return the bounded rejection or the exact missing result.
3. **Describe a serious virtual alternative.** When query-time access remains a candidate, state source access, rule evaluation, pushdown or mediation, credentials, latency/availability behavior, provenance capture, and failure return.
4. **Describe a serious materialized alternative.** When copying remains a candidate, state copied or derived state, snapshot identity, refresh/invalidation, storage and custody, source deletion/correction behavior, provenance, recovery, and exit.
5. **Describe a hybrid where warranted.** Identify which permitted subset is materialized and which source-sensitive part remains virtual. State coherence, invalidation, and fallback behavior. Confirm permission for each subset selected for copying.
6. **Compare complete remaining arrangements.** Use the conditions that can change the receiving result: freshness, latency, availability, access, protection, source authority, reproducibility, provenance, operability, recovery, cost, and semantic loss. Include concurrent source calls, shared credentials, trace, retries, support, and other demands within each applicable resource envelope. Pairwise feasibility cannot establish a jointly infeasible arrangement.
7. **Examine relevant failure and change cases.** Use the source outages, corrections, access changes, mapping changes, stale or partial refresh, provenance loss, and recovery cases needed for the proposed conclusion. Earlier sufficient evidence can support a bounded rejection; a positive selection needs its load-bearing conditions.
8. **Choose or identify worthwhile further work.** Select a supported arrangement, reject it, or return the missing result. Commission a discriminating probe only when its obtainable result can change the decision enough to justify its full burden and displaced work. Keep an unresolved comparison explicit when further inquiry is unavailable or not worthwhile. State the reasons for the disposition that its receiver needs.
9. **Name implementation returns for a selected choice.** Identify the Data Engineering, platform, provider, security, legal, finance, or operating results required to realize that choice.
10. **Return the conditions needed by this result.** For a selected realization or supplied receiving result, give `SIE.9` its service, error, currentness, and fallback meanings. Retain observations that can reopen the conclusion where they change continued reliance.

#### SIE.8:4.2 - Record the Result

The result follows the conclusion actually supplied. A sufficient rejection of one proposed arrangement is complete with the receiving use, named proposal, decisive grounds and evidence, scope, and material limits. It does not require a comparison with unrequested alternatives or an implementation and interface design.

| Decision content | When it is needed | Content supplied |
| --- | --- | --- |
| Receiving use and disposition | Every result | The question and proposed arrangement or comparison scope, supported choice/rejection/probe/missing-input result, grounds, and material limits. |
| Decisive exclusion | A proposed arrangement is rejected on sufficient grounds | The condition that defeats it, the evidence and applicability needed for that condition, and the scope of the rejection. |
| Candidate arrangements and comparison | A comparison remains live or a positive choice is made | Serious remaining alternatives as complete arrangements: required semantic branches, access, state, execution, currentness, latency, provenance, protection, failure, operation, recovery, exit, and joint resource demand. |
| Failure/change evidence | The supplied conclusion depends on it | Evidence for its load-bearing conditions. One qualified prohibition can suffice for rejection; positive selection needs the relevant failure and change cases for the claimed arrangement. |
| Further inquiry | A probe is proposed | Obtainability, possible decision contribution, full burden, displaced work, and how its result can change the decision. |
| Implementation returns | A realization has been selected | Exact required direct-owner results, what is supplied or still missing, and the acceptance evidence needed to realize that choice. |
| Interface semantics | A selected realization or receiving result needs them | Currentness, source/error, incomplete-result and fallback meanings supplied to SIE.9. |
| Continued reliance | A condition can materially change the result's use | The observation, source change, or receiving change that reopens the affected decision. |

A positive choice cannot use the rejection boundary to omit a condition on which that choice relies. The selected arrangement and its implementation returns remain qualified by all their actual semantic, service, access, and resource conditions.

#### SIE.8:4.3 - What Changes in Practice

The team compares ways to supply the same semantic result rather than comparing product categories. A graph store may survive as a materialized candidate, a federation as a virtual candidate, or neither. The selected decision states what still has to be implemented and operated before any service claim is made.

### SIE.8:5 - Archetypal Grounding - Provider Availability without Replication

Two providers expose current availability through governed APIs. Provider A means “on hand”; Provider B means “available to promise”. `SIE.4` preserves the semantic difference and `SIE.6` permits a qualified side-by-side answer but forbids arithmetic fusion. Neither provider permits replication of its availability state.

If the question is only whether a proposed copied availability store may serve that contract, the completed answer is: “Reject the proposed copied availability store for this purchasing use: the qualified provider conditions prohibit copying the required availability state.” The contract, proposal, and provider conditions identify its scope and grounds. This concludes that question without a latency study, credential design, recovery plan, or alternative selection.

When the receiving question also asks which remaining arrangement to use, continue with the following comparison:

| Candidate | Constructed comparison |
| --- | --- |
| materialized common graph | excluded by the providers' prohibition on copying availability state; that condition is sufficient without developing its implementation, recovery, and exit |
| query-time virtual mapping | retained alternative: preserves source custody and timestamps and can return provider-specific qualified rows; depends on runtime credentials, latency, provider availability, query limits, and explicit timeout/incomplete branches |
| hybrid metadata plus virtual values | selected conditionally: materialize stable product-family correspondences, mapping rules, and source metadata where their copying and maintenance are permitted; retrieve volatile availability values at query time; invalidate metadata when source definitions or product relations change |

The decision selects the hybrid arrangement because stable semantic premises can be inspected and volatile restricted values remain at their sources. It requires Data Engineering and security results for credential handling, concurrent calls, timeout behavior, observability, and recovery. SIE.9 receives separately attributed quantities and timestamps, provider errors, and the permitted incomplete-result and fallback behavior. No running interface or provider reliability is claimed.

### SIE.8:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | Materialization silently transfers custody, authority, or permission. | Record source rights, retention, correction, and use authority for every copied state. |
| Architecture | The incumbent platform determines the answer, or every conceivable alternative requires full design. | Use sufficient exclusions, then compare serious alternatives as complete arrangements on the receiving basis. |
| Ontology/Epistemology | A graph or warehouse is treated as the semantic arrangement itself. | Keep mapping premises, claims, provenance, and validation independent of carrier. |
| Pragmatics | Every unresolved comparison commissions a probe. | Compare obtainable decision benefit with the probe's full burden and displaced work. |
| Didactics | “Virtual is fresh; materialized is fast” becomes a universal rule. | Show source latency, snapshot reproducibility, invalidation, and failure conditions that reverse the slogan. |

### SIE.8:7 - Conformance Checklist

Check the conclusion being returned. Only its applicable checks need an answer.

**For every result**

- [ ] The receiving question, named proposal or comparison scope, disposition, grounds, and material limits are recoverable.
- [ ] The evidence supports that disposition at its stated scope; it creates no broader feasibility, running-service, or achieved-performance claim.

**For a sufficient rejection**

- [ ] The decisive condition and its qualified evidence defeat the named proposal for this use.

That rejection completes the Method when it answers the requested question. The following comparison and implementation checks do not become prerequisites for it.

**For a live comparison or positive selection**

- [ ] A successful candidate preserves the receiving result, mapping rules, and required semantic branches.
- [ ] Serious remaining candidates expose access, state, execution, provenance, failure, operation, recovery, exit, and joint resource demand.
- [ ] Freshness and latency are defined for the receiving use.
- [ ] Source authority, custody, permissions, correction/deletion, and retention consequences are explicit.
- [ ] Security/privacy and runtime credential differences are compared where they can change the result.
- [ ] Reproducibility and provenance behavior are specified for the candidate's virtual occurrences and copied state.
- [ ] Relevant outage, access, mapping, correction, refresh, provenance-loss, and recovery cases support the proposed conclusion.
- [ ] For a selected realization, exact implementation and operating results remain with their direct owners, and SIE.9 receives the required currentness, error, incomplete-result, and fallback meanings.

**For a proposed inquiry**

- [ ] Its obtainable decision contribution justifies the full burden and displaced work.

### SIE.8:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Knowledge graph” as the requirement | Restate the receiving result and compare graph and non-graph realizations. |
| Virtual means no state | Record mappings, caches, credentials, query occurrences, source snapshots, and provenance state actually required. |
| Materialized means reliable | Test refresh, invalidation, correction/deletion, recovery, and source-authority changes. |
| Hybrid means best of both | Expose coherence, invalidation, fallback, and doubled operating responsibilities. |
| Product feature checklist | Compare serious arrangements on use-sensitive criteria, joint resource demand, and relevant failure cases. |
| Decision equals implementation | Name the exact build, provider, security, and operating results still missing. |

### SIE.8:9 - Consequences

The bounded realization decision exposes source, semantic, and operating trade-offs and the conditions for reconsidering it. Interface designers receive explicit currentness and error behavior, while implementers receive a clear invariant to preserve.

The cost is comparison beyond the preferred platform and coordination with operational owners. A selected candidate may still stop because access, security, service, provider, or cost evidence is missing.

### SIE.8:10 - Rationale

Virtual and materialized are not merely deployment choices: they change when and where mappings execute, which state is copied, how provenance and currentness are established, and which failures reach the receiver. Those changes can alter semantic adequacy, so SIE owns the bounded comparison while direct practices own implementation and operation.

### SIE.8:11 - SoTA-Echoing

The best-known line combines declarative mappings, virtual knowledge-graph systems, data federation, materialized integration, and operational data-product practice. The serious default alternatives are “materialize one canonical graph” and “federate everything live”. Each can be correct under conditions; each is defective as a universal answer because it hides a different set of currentness, access, provenance, and recovery obligations. SIE.8 uses these contributions to compare whole arrangements that supply the same semantic result.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| [Ontop virtual-KG line](https://ontop-vkg.org/research/publications.html) | adapt | Demonstrates query-time virtual realization over mappings; it does not make virtual RDF mandatory or supply source access and receiving acceptance. |
| [R2RML](https://www.w3.org/TR/r2rml/) | adapt | Supplies one declarative mapping form usable in virtual or materialized arrangements; relational/RDF technology is optional. |
| [Data on the Web Best Practices](https://www.w3.org/TR/dwbp/) | adapt | Contributes access, version, provenance, reuse, and persistence questions; Web publication is not required. |
| universal canonical graph | reject as default | Materialization is one candidate and cannot transfer source authority or erase incompatibility. |
| universal live federation | reject as default | Query-time access does not guarantee freshness, availability, permitted disclosure, or reproducibility. |

Reopen when source access or replication rights change, measured latency/availability defeats the use, refresh/invalidation fails, mapping or source semantics change, security/provenance conditions change, or a new candidate materially improves the comparison.

### SIE.8:12 - Relations

- `SIE.1` supplies the invariant result and use-sensitive service and protection conditions.
- `SIE.7` supplies executable semantic behavior and loss/error branches every candidate must preserve.
- `SIE.2`, `SIE.5`, and `SIE.6` supply source authority, identity, claim, provenance, and currentness conditions.
- `SIE.9` consumes the selected realization's currentness, latency, availability, provenance, error, access, and fallback semantics.
- `SIE.10` tests the realized candidate and receiving workflow; it can narrow or fail the decision's assumed conditions.
- Data Engineering, platform, provider, security, legal, finance, and Operations owners supply implementation and operating results.

### SIE.8:End
