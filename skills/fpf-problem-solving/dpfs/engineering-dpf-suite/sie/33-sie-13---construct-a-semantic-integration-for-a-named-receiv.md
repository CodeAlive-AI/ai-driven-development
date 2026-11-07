## SIE.13 - Construct a Semantic Integration for a Named Receiving Use

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `SemanticIntegrationPackage@Use` whose required semantic contributions, implementation and evidence support one receiving use together, or a bounded partial result, unresolved question or stop that states what the receiver can now do.

### SIE.13:1 - Problem Frame

**Use this when** a query, decision or operation needs separately governed information to work together, but obtaining the individual meanings, correspondences or mappings still leaves the receiving answer unavailable. A team may already have good source inventories, a model, mapping rules and working endpoints. The remaining question is how to connect those results, obtain the missing contributions and make an answer usable under their joint conditions.

The working object is one semantic integration for a named receiving use. Its whole result is the connected package described in [SIE.Reference:4](05-sie-reference-4---the-first-whole-result.md): a use contract, source premises, warranted semantic relations and claim composition, mapping behavior, realization and interface, with validation of the claimed use. Identity premises and model development enter where the answer depends on them. The package can reference existing results; it need not be one document, database or graph.

Start with the action the receiver must be able to perform and the information that could change that action. Compare the available contributions with what that answer requires. The practical gain is a way to choose the next useful piece of work and know when the connected result is sufficient, rather than completing every SIE pattern in numerical order.

**Ordinary non-use.** Use the individual Method directly when its result finishes the question: SIE.4 can settle one correspondence, SIE.8 can reject a prohibited realization, and SIE.10 can identify a decisive defect in a supplied interface. An already adequate package can be used without reconstructing it. SIE.13 is needed when those local results still have to be made usable together. It does not select product configuration, establish master-data authority, operate a pipeline, authorize a purchase or accept a physical inspection result.

### SIE.13:2 - Problem

Local correctness does not compose automatically. A relation may be true but too lossy for the intended substitution. A mapping may preserve a meaning while consuming an identity disposition for another configuration. Two sources may be individually fresh yet concern different periods. Separately feasible retrievals may compete for one request allowance. A correct response can still be read as the wrong kind of claim.

The opposite failure is to treat the complete repertoire as a mandatory lifecycle. A practitioner repeats qualified source work, builds an ontology that already exists, or develops an excluded realization before answering a small question. This spends effort without supplying the missing connection.

Neither a list of completed tasks nor a collection of approved descriptions establishes a usable integration. Someone must determine which contributions the receiving answer depends on, whether their conditions match, what remains to obtain, and how the supplied result reaches the receiver.

### SIE.13:3 - Forces

| Force | Working consequence |
| --- | --- |
| Sufficient answer and wider reuse | The present contract bounds construction; a useful local answer need not anticipate every future consumer. |
| Source autonomy and combined meaning | Preserve source meanings and authority while establishing the relations the receiving use actually needs. |
| Reuse and changed conditions | Reuse a qualified result where its premises still match; a familiar result under a different interval or permission can need reopening. |
| Local feasibility and joint performance | Include shared limits and dependencies that no component can settle alone. |
| Useful partial result and misleading omission | Narrow only under the receiving contract, keeping excluded or unresolved branches interpretable. |
| Assurance and acquisition cost | Obtain evidence that can settle the current claim; a decisive rejection can finish without completing unrelated positive checks. |

### SIE.13:4 - Solution

Construct the integration by working backward from the receiving answer and forward through the contributions that can supply it. At each connection, establish what one result permits the next operation to do, under which conditions. Obtain or repair the missing contribution, bring its result back into the combination, and test the claimed receiving use. Revisit only dependencies affected by a changed premise.

The organization is conditional. Several contributions may be available already; one result can expose a different question; and construction can end with a warranted stop. The sections below explain these moves, not a compulsory sequence of completed forms.

#### SIE.13:4.1 - Establish what would let the receiver continue

Name the receiver's question and the next action or judgement that the answer must support. Recover the required answer claims and the circumstances in which a partial, conflicting or unavailable answer is still useful. If these are unsettled, use [SIE.1:4](21-sie-1---bound-the-receiving-use-and-semantic-contract.md#sie14---solution) to obtain the receiving-use contract. Otherwise use the supplied contract and reopen only a condition that no longer fits.

Distinguish the answer from its downstream authority. “These inspection observations concern this configured feature” can be a needed integration result; “release this product” remains an engineering or quality decision. This distinction determines which premises the integration must supply and which judgement remains with the receiving decision owner.

Compare the current available result with that continuation. If it already suffices, return it with its applicable limits. If only one correspondence or one failed conversion matters, obtain that result from its Method and finish the bounded question. When the receiver still lacks a usable combination, retain the whole receiving need while identifying a smaller next contribution.

#### SIE.13:4.2 - Derive the required contributions from the answer

Take each answer claim that can change the receiving action and ask how it would be obtained. Follow it to the source meanings, represented claims, relations and transformations it relies on. For a query row, for example, recover why the selected records belong together, what each value means, which rule produces the output, and how an unavailable or incompatible input is represented. For a semantic exchange between organizations, recover the corresponding interpretation and use of each supplied statement.

Use the following returns where that dependency occurs:

| The receiving answer depends on… | Contribution to obtain or reuse | What returns to the construction |
| --- | --- | --- |
| A source's meaning, applicability or authority | [SIE.2:4](22-sie-2---recover-and-qualify-source-semantics-and-authority.md#sie24---solution) | Qualified source-local premises and the gaps that limit their use. |
| A distinction the available model may not express | [SIE.3:4](23-sie-3---construct-or-reuse-a-semantic-model-for-a-named-use.md#sie34---solution) | Sufficient model reuse, an extension or a different model, qualified for the required questions. |
| A relation between source meanings | [SIE.4:4](24-sie-4---judge-cross-source-correspondences-and-their-permitt.md#sie44---solution) | A warranted relation, difference or incompatibility, with its permitted operations and loss. |
| Records concerning the same entity | [SIE.5:4](25-sie-5---resolve-cross-source-identity-without-erasing-identi.md#sie54---solution) | An identity disposition at the required grain and interval, retaining source identifiers and authority. |
| Several source claims contributing to an answer | [SIE.6:4](26-sie-6---fuse-source-qualified-claims-without-erasing-conflic.md#sie64---solution) | A qualified composition, conflict, non-comparability or unresolved branch. |
| Executable extraction or transformation | [SIE.7:4](27-sie-7---specify-semantic-extraction-and-transformation-mappi.md#sie74---solution) | Rules tied to those premises, including selection, conversion, absence, errors, loss and trace. |
| Obtaining and presenting the result in practice | [SIE.8:4](28-sie-8---choose-virtual-materialized-or-hybrid-semantic-reali.md#sie84---solution), [SIE.9:4](29-sie-9---connect-a-receiving-use-through-a-semantic-interface.md#sie94---solution) and the implementation supplier | A feasible realization choice, the implementation obtained from its supplier, and a receiving interface with defined interpretations. |

This is a dependency account, not a demand to perform every row. For example, two already distinguished subjects can retain separately attributed claims without a cross-source identity merge. A qualified existing model can supply the required distinction without new model construction. A supplied mapping may already carry the relevant source and correspondence references.

For each required contribution, determine whether it is available under the needed conditions, unavailable, or not yet qualified. An inaccessible definition, a missing distinction, a false correspondence, a missing implementation and an incompatible access condition are different obstacles. State which dependent answer each obstacle prevents; do not reduce them all to “more data needed”.

Keep the account in the working material the participants can use. A short annotated query or mapping specification can be sufficient. A larger integration may need linked descriptions. Their form matters only insofar as the actual dependencies and unresolved questions remain recoverable.

#### SIE.13:4.3 - Make the connections valid for this use

Before consuming a result, compare its subject and conditions with the operation that will use it. Match the relevant meaning, entity grain, configuration or time, source and rule versions, authority, permitted loss and failure behavior. A qualified result for one use is a candidate for reuse, not a universal permission.

Keep these three questions distinct:

1. **What relation or claim is supported?** A characteristic can concern a feature without being that feature. Two descriptions can concern the same feature while their claims conflict.
2. **What does that result permit here?** A broader relation may support navigation but not value substitution. An accepted loss for an overview may be unacceptable for an inspection calculation.
3. **Can the required contributions hold together?** A mapping qualified for one effectivity interval cannot borrow an identity judgement from another interval merely because the labels match.

When a connection fails, identify the premise that would have to change. Obtain a narrower warranted relation, a different mapping, an applicable source edition or an authorized change to the receiving contract. Preserve useful alternatives separately while their conditions differ. Do not combine one alternative's semantics with another's permissions or performance evidence.

The connected explanation should make a resulting branch understandable. If a claim is non-comparable, show the distinction that prevents comparison. If an input is not retrieved, preserve that absence through the mapping and interface. A missing source becomes neither a zero value nor evidence against that source's claim.

#### SIE.13:4.4 - Choose and obtain the next missing result

Choose the next contribution by what it can change in the receiving answer, using the dependencies just recovered. Start with a known decisive constraint when it can exclude an option without further construction. Otherwise prefer an obtainable result that resolves a consequential uncertainty or enables the next required operation at a justified cost. Publication order supplies no such priority.

For example, an existing prohibition on replication is enough to reject a copied store. It does not reject a permitted live query. An unknown definition that determines whether two quantities may be compared can matter before implementing either comparison. If the definition cannot be obtained, decide whether the contract permits separately attributed claims or whether the dependent answer must stop.

Perform or request the work that obtains the missing result. State its receiving purpose, required distinction or behavior, available inputs and acceptance condition. Use the relevant SIE Method for semantic work and the actual supplying practice for other work. A platform owner can establish the request allowance; an implementer can supply and test a query; a domain owner can settle a source definition. The integration practitioner connects those results but does not acquire the suppliers' authority by requesting them.

On return, inspect the supplied result and its conditions against the dependent operation. A selected realization is not its implementation, and a specification is not evidence of that implementation's behavior. If the contribution is still absent, retain the precise blocker. If it supplies the needed result, reconnect it and determine what remains for the whole answer. When the recipient already has enough to continue, stop expanding the work.

Necessary coordination is part of obtaining the result: establish who can perform the required work, with which access and means, and how the result will reach its consumer. Existing skills in parsing and databases may still leave nobody able to resolve a temporal-identity question. Supply that contribution or leave the dependent answer unresolved.

#### SIE.13:4.5 - Compare the complete arrangement and its permitted branches

Use [SIE.8:4](28-sie-8---choose-virtual-materialized-or-hybrid-semantic-reali.md#sie84---solution) to compare the viable ways of realizing the accepted mapping behavior and supplying the result. Bring the semantic dependencies and the actual shared conditions into that comparison. Include required trace, failure and recovery behavior in the workload. Query permission, replication permission and disclosure permission remain separate inputs.

Test the combined demand against each applicable limit. Count the distinct requests in one allowance window, including the retry behavior on which the service promise depends. For time, follow the operations that must finish before the receiver can act; parallel operations and serial dependencies have different effects. For storage or access, use the conditions that govern the actual retained or exposed information. A common resource limit concerns the combination even when every component fits alone.

Keep a common source or derivation visible when several contributions rely on it. Agreement among results that share a premise is not independent corroboration of that premise. Likewise, several pairwise comparisons do not establish a condition over all contributions together.

If the proposed whole fails, compare the continuations the contract permits. A narrower answer must retain the semantic premises, trace, access and interpretation required for that answer. An authorized contract change or a different realization can reopen the choice. Dropping a required provenance contribution or quietly redefining completeness cannot repair the same promise.

A decisive failure can finish the comparison for one alternative. Stop the whole requested use only when that failure defeats every continuation still allowed by the contract, or when the needed continuation remains unavailable. Distinguish a known impossibility under the stated conditions from an unresolved option that would need another contribution.

#### SIE.13:4.6 - Supply the interface and establish the bounded use result

Use [SIE.9:4](29-sie-9---connect-a-receiving-use-through-a-semantic-interface.md#sie94---solution) to specify and supply the interface that carries the qualified meanings and branches into the receiver's work. Obtain the implementation needed by that interface and the selected realization. Develop their specifications together where their dependencies require it; a changed semantic or service condition returns to the contribution that supplies it. Check that the actual input and output behavior preserves the rules and that the receiver can interpret the result as intended. Depending on the use, the interface can be a query, service, exchange file or a documented human-facing view.

Use [SIE.10:4](30-sie-10---validate-a-semantic-integration-result-for-its-rece.md#sie104---solution) to validate the claim now being made. For a positive whole-use or contract-permitted subset conclusion, every load-bearing premise and required joint condition needs matching evidence. Reuse evidence whose subjects, versions, use and conditions still fit. One decisive conversion error can establish a bounded failure without testing unrelated layers; correcting it alone does not establish the full positive claim.

Return the answer, its disposition and its consequences for the receiver together. A qualified partial answer states what is covered and what remains unavailable. An unresolved answer states the missing result and the use it prevents. A stop states the defeated obligation and the change that could make reconsideration useful. A semantic integration result supplies a premise to the receiving decision; its authorization and outcome remain with the receiving owner.

#### SIE.13:4.7 - Reopen changed reliance and reconnect the result

Retain the dependencies needed to recognize a change that can alter the answer: the source meaning or edition used, identity and composition premises, mapping rule, access or resource condition, and receiving interpretation. Preserve them where their consumers can retrieve them, rather than copying an unexplained final value.

When one changes, use [SIE.11:4](31-sie-11---trace-semantic-change-and-revalidate-affected-uses.md#sie114---solution) to determine the affected uses and obtain the contributions that must be revised or revalidated. A changed promise horizon may affect a purchasing interpretation and its mapping while leaving product descriptions usable. A changed gateway allowance may reopen realization and validation while leaving correspondence evidence unchanged.

Bring each affected result back into the combination and repeat only the comparisons and use checks whose premises changed. Check the new whole's joint conditions; a local repair can move demand to a shared limit. Where the set of consumers is unknown, keep that reach unresolved instead of treating the known consumers as exhaustive. Use SIE.12 only when actual shared-module users need common maintenance and decision arrangements.

#### SIE.13:4.8 - Keep the result inspectable

The result must let the receiver recover the answer and its allowed use, the relied-on semantic contributions, their operative connections, the realization and interface actually supplied, and the evidence for the returned disposition. Keep material missing contributions and change conditions visible. The [package anatomy](14-sie-reference-13---package-anatomy-and-direct-result-relatio.md) locates the supplying results; it need not be duplicated in a new record.

For a small use, links from the returned query rows to a contract, mapping and qualified source material can carry this account. For a larger use, maintained specifications and implementation evidence may be necessary.

### SIE.13:5 - Archetypal Grounding

#### SIE.13:5.1 - Connect configured product meaning to inspection evidence

A quality engineer needs the QIF inspection plan and observations concerning AP242 feature `F17` in released configuration `R` at effectivity `E`. The constructed contract in [SIE.1:5](21-sie-1---bound-the-receiving-use-and-semantic-contract.md#sie15---archetypal-grounding---ap242qif-configuration-query) permits qualified rows with separately visible unresolved local-extension and unknown-unit branches. It retains the 24-hour observation window and two-second response limit. These are stipulated receiving conditions, not properties guaranteed by either standard.

Suppose the source owners have supplied applicable product and inspection definitions, and an available model can distinguish a configured feature, an inspection characteristic, a plan and an observation. A proposed mapping currently equates characteristic `C17` with product feature `F17`. Executing that mapping faster would not supply the requested meaning. The next useful contribution is the relation judgement, not another platform trial.

SIE.4 establishes that `C17` concerns a feature; it is not itself that feature. The proposed connection also relies on a QIF feature description and the AP242 feature description concerning the same feature at `R/E`. SIE.5 supplies that separate identity premise from the applicable source evidence. If this required identity cannot be established, withhold the dependent inspection answer. A similar label or an observation for another configuration cannot fill the gap.

The claim composition can now retain the product-definition and plan-applicability claims with their owners, and attach the qualified observation to the configured feature. SIE.7 specifies the selection by `R/E`, the warranted characteristic relation, unit conversion, trace and error branches. The mapping may expose an observation in a requested unit; it does not thereby decide that the product conforms.

Assume SIE.8 has selected a permitted realization and the implementer supplies it. The supplied test evidence must show the requested query, the observation-age and response conditions, and the required negative branches. SIE.9's receiving view keeps an unknown unit visibly unresolved instead of returning a converted value. SIE.10 checks those behaviors and the semantic premises against the contract. Under matching positive evidence, the result is the qualified row set and the stated unresolved branches, not an engineering release decision.

The complete construction changed two connected operations: it replaced an invalid equality with a warranted relation and required a distinct feature-identity contribution before the join. The realization and receiving tests then exercised that corrected meaning. Merely collecting a correspondence file, an identity file and a passing parser would not establish their connection to this query.

Now let the released configuration change to `R2`. SIE.11 follows the change to the feature identity, plan applicability, selection rule and dependent query evidence. An unchanged unit-conversion rule can retain its qualification. The new configured answer remains unavailable until its affected premises and receiving behavior are supplied; the earlier answer can remain a qualified answer about `R`.

#### SIE.13:5.2 - A permitted incomplete provider answer under a shared limit

A purchasing receiver needs attributed availability claims from providers A and B. A means “on hand”; B means “available to promise”. The receiving contract permits an explicitly incomplete answer and does not permit treating the quantities as one interchangeable measure. Assume their required meanings, models and composition rules are already qualified.

Replication is prohibited, so SIE.8 rejects a copied store without building one. Live retrieval and immediate presentation are permitted. For the constructed arrangement, A needs four requests, B needs four, and the source and rule trace needs three. All distinct requests consume one gateway allowance of ten in the same window. The trace is required even for a partial answer; no requests are shared or counted twice; the contract accepts neither a copied cache nor deferral to another window.

The full result needs at least `4 + 4 + 3 = 11` requests before retries. Each pair fits, but the combination does not. The semantic premises can remain correct while this realization fails to supply the complete answer. More correspondence checking cannot remove that resource conflict.

An A-only answer requires `4 + 3 = 7` requests before retries. It is a candidate permitted continuation, not yet a positive use conclusion. The implementation must preserve the required trace and the agreed response, freshness and failure behavior; retries consume the same allowance. The interface must say, for example, `A: 12 on hand at T; B: not retrieved under the request limit`, with the required attribution and trace. It must not say `21 available`, `B: 0`, or “complete provider comparison”.

If matching implementation and use evidence establishes those remaining obligations, SIE.10 can qualify the A-only branch. The receiver then decides what action an incomplete answer permits. If both providers instead become mandatory, the same seven-request branch no longer answers the contract. Return the stop and the needed change: an access-owner decision altering the allowance, or a demonstrated implementation reduction that preserves the meanings and trace. Merely omitting the trace is not the same result.

If the allowance changes from ten to twelve, the full arrangement becomes possible on the stated minimum request count, but its retry and other service conditions still need comparison. Reuse unchanged semantic premises; reopen the affected realization and receiving-use evidence. These numbers are construction assumptions, not measured provider performance.

#### SIE.13:5.3 - An unchanged field with a changed meaning

An existing interface has been qualified for a source definition in which provider B's `available` field states a present commitment. B later changes its definition to include quantities promised within seven days while leaving the JSON field and numeric type unchanged. A parser test can still pass.

SIE.11 traces the relied-on meaning to the composition, mapping and receiving interpretation. A request about immediate availability can no longer use the old substitution. Obtain a supported present-availability contribution, return an explicitly permitted non-comparable or incomplete branch, or stop that answer. A future-planning receiver may use the changed meaning after its own conditions and interface interpretation are qualified. Source identifiers and unrelated product descriptions need not be reconstructed merely because this claim changed.

The whole Method reconnects the repaired semantic contribution to the receiving use; notification alone leaves that work unfinished. If all that was requested was whether the old present-availability substitution remains valid, the bounded incompatibility result can finish without rebuilding an interface.

### SIE.13:6 - Bias-Annotation

A common schema, a merged key, a populated store or a completed query can look like completion while hiding a changed meaning or an unsupported use. Compare the resulting claim with the receiver's question and include a case that separates the tempting interpretations.

The requested integration can reflect one consumer's needs while other affected consumers have different conditions. Recover the actual source and receiving authorities, and keep other consumers' conditions separate. A contract change can justify a narrower answer only through the applicable agreement; the integrator's preference for an easier result does not change that agreement.

Retain a dependency or distinction because it changes construction, interpretation, reliance or return after change. Reuse adequate explanations and evidence.

### SIE.13:7 - Conformance Checklist

Recognize this problem when the receiver still cannot obtain an answer from otherwise useful local contributions. Assurance concerns the actual answer claimed under actual conditions. A worked example of this Method establishes neither a production service nor an observed improvement in its users' performance.

- The receiving continuation and its acceptable answer branches are explicit; an adequate supplied contract is reused.
- Each required answer claim can be followed to its semantic premises and the operations that produce it.
- Every consumed result permits the actual operation under matching subjects and conditions; correspondence, identity and claim composition retain their different contributions.
- The next missing result is chosen for its effect on the receiving answer, with an obtainable supplier or an explicit blocker.
- The complete arrangement is compared under relevant shared limits, permissions, trace and failure conditions; local or pairwise feasibility is not substituted for that comparison.
- The supplied interface preserves the qualified meanings, material absence and conflict branches, and the receiver's required interpretation.
- A positive use claim has evidence for every load-bearing premise and joint condition within its scope. A negative conclusion states the obligation it defeats and the reach left unexamined.
- A partial answer is permitted by the contract and retains its own required premises. A changed premise reopens its dependent contributions and uses while adequate unaffected results remain reusable.
- The result returns to the receiving owner without claiming that semantic integration grants downstream decision authority.

### SIE.13:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it changes the result | Repair |
| --- | --- | --- |
| Twelve completed boxes | Independently completed contributions may use incompatible premises, while some boxes may be unnecessary. | Work from the answer's dependencies and inspect the connections actually used. |
| One common field means one common quantity | The carrier hides different source meanings or horizons. | Retain source-qualified meanings and qualify the permitted composition. |
| A design stands in for its supplied result | A realization decision or mapping specification leaves the receiving behavior unimplemented. | Obtain the implementation and matching behavior evidence, or keep that gap explicit. |
| Every pair fits, so the whole fits | Shared demand or incompatible conditions can emerge only in the complete combination. | Compare the required contributions together under the same use and resource conditions. |
| Quiet partial success | Omitted sources or provenance make the response look more complete or better supported than it is. | Return only a contract-permitted subset, with its excluded branches and required trace. |
| Start everything again after a change | Unaffected meanings and evidence are discarded while the actual dependent use may still be overlooked. | Trace changed reliance through SIE.11 and reconnect the affected results. |

### SIE.13:9 - Consequences

The practitioner can explain why the available contributions do or do not supply the receiving answer, choose the next useful work and return a supported branch. Source owners and implementers receive a concrete missing result rather than an undifferentiated request to “finish integration”. A later change can return to the contribution that matters.

The cost is maintaining enough dependency and condition information to support those choices. The Method is excessive when a supplied local result already finishes the question. Its scope grows with actual reliance, not with the number of available sources or patterns. It supplies a way to construct and qualify an integration; obtaining inaccessible meanings, rights, implementation capability or authoritative decisions remains contingent on their suppliers.

### SIE.13:10 - Architectural Rationale

The whole is organized around the receiving claim because that claim determines which distinctions and contributions are necessary. A list of source fields cannot determine permissible loss; a storage choice cannot determine identity; and a passed local test cannot determine whether another result may consume the tested premise.

Working backward exposes required contributions. Working forward checks whether those contributions actually yield the promised answer. Comparing their connections and shared conditions closes the gap between individual adequacy and whole use. Selecting the next missing result keeps that construction practicable when only part of the answer is unsettled.

The distinct local Methods remain useful: SIE.1 bounds the use; SIE.2–SIE.7 supply semantic and executable premises; SIE.8 chooses realization; SIE.9 supplies the interface; SIE.10 qualifies its use; SIE.11 follows change; SIE.12 governs an actual commons. Their actions can constitute parts of this construction when needed. None must be performed anew merely because it has a PatternID.

A linear project plan may organize one implementation, but it cannot replace these dependency and qualification judgements. Conversely, recognizing dependencies does not require one universal process model. A small integration can make the same connections through a short contract, qualified mapping and receiving test.

### SIE.13:11 - SoTA-Echoing

The selected practice combines the use-led semantic construction developed in SIE.2–SIE.7 with realization, receiver interpretation and affected-use qualification. SIE.3 supplies model reuse or development where a distinction is missing; SIE.13 adds no requirement to develop an ontology or materialize a knowledge graph. The domain sources and their transfer limits remain in those supplying Methods.

One practical alternative is to fix a shared model and source set, complete their mappings and service, then validate the receiving query. This can support reuse across several consumers and provide a workable project plan when the shared meanings, applicability and joint conditions are settled. Compare it with the present construction at the same receiving question and available resources. In §5.1 the model is already adequate, but the correspondence and identity connection is still missing. In §5.2 completing the two-source implementation cannot overcome the ten-request allowance; a permitted partial branch can supply a useful answer. If both sources are mandatory, neither arrangement delivers without another contribution or changed condition.

**Adopt** sufficient shared models, mappings and implementation plans. **Reject** making their complete construction a prerequisite for every local answer. When an already qualified service answers the present question under unchanged conditions, reuse it directly; no additional construction account is needed. When its meanings, permissions or receiving branches change, obtain and reconnect the affected contribution.

The [W3C Data on the Web Best Practices](https://www.w3.org/TR/dwbp/) supplies relevant established guidance: choose formalization for the application (BP16), retain provenance (BP5), and communicate interface changes (BP26). **Adapt** these contributions to the named receiving use. Their publication and interface guidance does not by itself establish cross-source identity, semantic comparability or joint feasibility. The construction in §§4.2–4.7 is a domain synthesis of those separately needed judgements, not a claim that one W3C recommendation specifies this whole Method.

Compare a graph or copied-store realization with live or hybrid access at the same receiving claim, semantic obligations, trace and service conditions through SIE.8. A store may support repeated queries; a live arrangement may preserve access to rapidly changing source-owned claims or avoid prohibited copying. **Reject** choosing either by technical preference alone. In §5.2 the permission excludes copying and the joint request demand changes the permitted answer; no empirical superiority of virtual integration is inferred.

The trade-off is explicit connection work where local results do not yet support the receiving answer, in exchange for avoiding both silent composition assumptions and an obligatory full lifecycle. Reopen that choice when an adequate supplied arrangement makes the work redundant, a new dependency defeats the current construction, or actual use shows that its coordination burden exceeds what the receiving question warrants.

### SIE.13:12 - Relations

- [SIE.Reference:4–6](05-sie-reference-4---the-first-whole-result.md) explains the whole result and combined arrangement; [SIE.Reference:13–14](14-sie-reference-13---package-anatomy-and-direct-result-relatio.md) locates its supplying results and local entries.
- SIE.1–SIE.7 supply the contract and semantic contributions under the conditions in §4.2. They remain directly usable for their own questions.
- SIE.8 and SIE.9 supply realization and receiving interface; their implementation dependencies return actual results rather than design decisions alone.
- SIE.10 supplies bounded use validation. SIE.11 supplies affected-use returns after change; SIE.12 is conditional on actual commons users.
- FPF C.39 supplies general construction of a way to obtain a result; B.1.5 distinguishes Method composition, and B.1.5.EW distinguishes constituent performance in ongoing work. SIE.13 supplies the semantic-integration content of those connections.
- Systems Engineering, Data Engineering, domain and source owners, and receiving decision owners retain the non-SIE results and authorities identified in [SIE.Reference:16](17-sie-reference-16---fpf-neighboring-practice-and-authority-bo.md).

### SIE.13:End
