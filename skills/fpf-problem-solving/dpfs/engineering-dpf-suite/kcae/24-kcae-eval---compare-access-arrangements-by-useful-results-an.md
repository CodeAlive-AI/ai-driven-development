## KCAE.EVAL - Compare Access Arrangements by Useful Results and Full Cost

> **Type:** Method pattern
> **Status:** Stable

### KCAE.EVAL:1 - Problem frame

**Use this when** adopting, replacing or repairing an access arrangement requires evidence of its practical gain, or a failure needs attribution to the operation that can be repaired. A benchmark score, successful API call or convincing demonstration cannot answer every such question.

The gain is a bounded decision to adopt, retain, change or stop an arrangement on the evidence that can support it. Do not run a large study for a harmless reversible lookup whose adequacy is already inspectable. Scale the comparison to the consequence and uncertainty of the receiving choice.

### KCAE.EVAL:2 - Problem

Retrieval can improve while the final answer remains wrong. A better assessor can appear worse because it receives poorer candidates. An inexpensive model can raise human review or refresh costs. A synthetic test set derived from the same summaries as the index can hide the distinctions the arrangement was meant to recover.

### KCAE.EVAL:3 - Forces

Real episodes have greater practical relevance and less convenient labels. Whole-use comparisons establish value but can hide the cause. Controlled component comparisons explain a difference but narrow its reach. Broad coverage, independent judging and repeated trials consume the same resources the system is meant to save.

### KCAE.EVAL:4 - Solution

#### KCAE.EVAL:4.1 - State the decision and serious alternatives

Recover the receiving use, population, corpus editions, permitted data flows and adoption consequence from KCAE.USE. For a comparison, choose a credible arrangement a capable practitioner would use, including the incumbent where relevant. A threshold question can be settled by direct evidence or a bound on the arrangement in question. Depending on the work, a credible alternative may be manual reading, exact or lexical search, a hybrid retriever, an established long-context workflow or a competent existing agent. A weak toy baseline makes an addition easy to justify and hard to trust.

For a gain attributed to a change, state the proposed difference and compare complete feasible arrangements, including the required extraction, source reading, assessment and delivery. Keep common components, instructions and sources equal when the question is one component's contribution; disclose changes when equality is impossible. A provider comparison confounded by different prompts or missing tools does not isolate the provider's effect.

Choose whether the decision requires better useful results at a fixed resource boundary, lower cost at a required quality, or a transparent tradeoff. Keep non-negotiable permission and safety constraints separate from preferences; cheap unauthorized processing is not a feasible alternative.

#### KCAE.EVAL:4.2 - Build episodes that can defeat the design

Use episodes when the remaining question concerns what readers or services can actually obtain, when they can distinguish the competing arrangements, or when an episode is itself required. An established access restriction or a reliable upper bound on service time may already settle its corresponding question. For an empirical evaluation, use actual episodes where access permits, or independently construct cases representing the intended conditions. Retain the original request, relevant sources, case facts and required result. To estimate performance on new work, keep evaluation cases independent of those used to design queries or tune thresholds, accounting for near duplicates.

When work episodes or test cases are needed, select challenges from the uses the evaluation must cover. They can include unknown source names, cross-language wording, useful non-pattern prose, distant prerequisites, misleading vocabulary, an important exception, missing facts and no useful corpus contribution. Where the service promises to recognize that it cannot help, include naturally answerless cases from the receiving work. Add source changes, stale indexes, revoked access and partial availability when the intended installation must handle them. Select proportions from the expected workload or report separate strata; a hand-balanced set is not automatically representative.

Gold material may be incomplete. Pool candidates from several credible routes and obtain source-based judgements from appropriate readers; sample beyond the pool where practical. Record uncertainty about unjudged material. Do not label every unpooled passage irrelevant. When several answers can serve the work, judge sufficiency and conditions rather than exact string agreement with one preferred answer.

Synthetic questions generated from an index can be useful development probes. Keep that origin visible and do not use them as the only evidence that the same index finds unfamiliar distinctions. For an English-primary assessor serving another language, test that language and important negation/condition forms rather than assuming a good English average transfers.

For a broad synthesis, vary the underlying evidence independently of its presentation. Duplicating an old edition or adding an overlapping summary must not create another population member or inflate a count. A new current counterexample or changed qualifying note must be able to alter the claim it defeats. Inspect whether a rare consequential position survives the map, reduction and delivery, and whether unknown membership remains unknown. Compare the final claims with original-source coding on a manageable dossier; merely counting processed summaries cannot test this contribution. KCAE.SEARCH:5.2 provides a constructed example, not an empirical success rate.

#### KCAE.EVAL:4.3 - Observe the complete useful result and full cost

For performance in use, examine what the arrangement enabled the recipient to obtain. A correct explanation, a usable conditional proposal, the missing fact that determines the next action or a completed application can each be the required result. Use an existing adequate record or obtain the judgement of the recipient or a qualified assessor. For a commission requiring independent acceptance, establish the agreed decision by an assessor who meets the applicable authority and independence conditions. An earlier acceptance can suffice when its scope and terms cover this use. Examine omissions or unsupported advice that could change that use. If a team may rely on its contracted search service for future requests, assess what the arrangement can supply with that service available and acting within its mandate. To establish the team’s ability to continue after the contract ends, examine its work with the sources, permissions and aids it will retain. A trial in which the service chose the source can demonstrate the team’s ability to judge the material it received. Evidence of the team’s own source selection must cover that choice. Learning attributed to the aid also requires a suitable comparison with the team’s earlier ability. A delivered answer can complete an order for advice.

Where costs enter the decision, measure or bound the relevant costs over its horizon, including preparation, extraction repair, indexing, storage, refresh, all model/tool calls, latency distribution, main-context consumption, human reading, interruptions, follow-up questions, application and recovery. Report total model input separately from residual main-window capacity. Report medians together with tails or failures where those change adoption. Support empirical claims with observations. State the assumptions behind any estimated costs or results.

For paired episodes, compare alternatives on the same case where this does not contaminate the reader. Randomize order or use separate recipients when the first exposure teaches the answer. Keep the judge's criteria independent of the preferred implementation. If a model judges outputs, test its agreement and failure cases against source-grounded human or otherwise competent judgement; do not assume self-evaluation is neutral.

Return distributions or uncertainty appropriate to the data and decision. A handful of designed examples can establish that a mechanism runs and expose failures; it does not estimate a population success rate reliably. A small useful trial can justify a reversible next trial while leaving broader performance open.

#### KCAE.EVAL:4.4 - Isolate the failed contribution before repairing

When a failure still needs locating, use a controlled substitution that can distinguish its possible sources. For example, compare the following changes under the conditions that matter to the receiving work.

- Supply an adequate source to the same assessor and delivery path, then compare with the original run. Was the source already among the candidates? Did the assessor receive its qualifying passage in usable form? What part of the judgement reached the recipient? If adding a previously absent candidate restores the result with the other relevant conditions held fixed, candidate availability contributed to the failure. Moving an existing passage into view or drawing attention to it tests a different change. Where several conditions changed together, report what the combined change achieved and what remains unlocated.
- Hold the candidate pool and source context fixed while comparing assessors. This separates candidate availability from ranking and condition judgement.
- Hold a qualified contribution fixed while varying delivery. A recipient who cannot recover or use the contribution can then expose omitted context, excessive compression, unavailable tools or missing preparation.
- Hold the source snapshot and queries fixed while varying representation or route. Inspect not only aggregate retrieval scores but unique useful discoveries and unique harmful omissions.
- Replay a controlled source change through build, persistence, reload and use. Compare the affected result with unchanged controls.
- Hold inquiry content fixed while changing the encounter occasion. Observe interruption and uptake, not merely whether a notification was sent.

These substitutions diagnose an operation under controlled inputs. They do not prove that the repaired whole will produce those inputs naturally. Follow the changed result back to the receiving use. Reuse a still applicable guarantee or observation. Re-run that use when its outcome remains open or a new run was commissioned. Components can interact: a larger pool can improve recall and overwhelm an assessor, while a more selective delivery can save context and remove a decisive exception. Do not add separate component gains as if they were independent benefits.

For an encounter implemented with retried events and stored claims, interrupt the implementation after claiming work, during execution and after committing the result. Present a concurrent duplicate and a later completed duplicate. Observe whether unfinished work has an actual continuation, whether a stale owner can publish, and whether an external effect can be repeated or remains unknown. A constructed state trace can expose a missing branch; it does not establish a real database's atomicity, scheduler behavior or recipient idempotency. Keep those implementation questions separate from a classifier's inquiry quality.

#### KCAE.EVAL:4.5 - Qualify scores for the decision they control

For retrieval, recall over known relevant units, rank-sensitive measures and coverage can help diagnose finding. Their meaning depends on the judgement set. For screening, inspect false positives, false negatives, abstentions and unknown inputs at the proposed threshold. For claimed probabilities, test calibration on the relevant population and scoring event. For typed group choice, retain its within-group meaning; test logical relations among questions separately when the application depends on them.

For a threshold chosen from performance data, use the costs of missed and incorrect actions on the development set. A threshold prescribed by the receiving agreement is an input to the evaluation. Freeze them for the held-out comparison, or account explicitly for adaptive tuning. Include near-boundary cases and no-use outcomes. A threshold that filters deliberately wrong repositories may fail on naturally difficult questions in the right repository. A calibrated score cannot create missing source evidence or domain permission.

Test the identity preserved across ranking, screening and return. Include a case where the ranking winner fails the adequacy threshold while another shortlisted candidate passes. The output must qualify its own candidate, choose a separately qualified alternative, or abstain; the maximum over the pool is not the returned candidate's adequacy. Also test a high-scoring candidate with a contradicted necessary source condition. These cases distinguish a working score interface from a correctly connected decision.

Use executable calculation for counts, ratios, confidence intervals or cost arithmetic where needed. Preserve denominators and the treatment of unknowns. Report “not assessed” separately from failure and success. If a metric cannot distinguish the practical failure that motivated the change, add an appropriate receiving-result observation rather than decorating the same metric.

#### KCAE.EVAL:4.6 - Make the adoption and refresh decision

Relate observed gains and losses to the original use. Keep the incumbent when it still meets the receiving requirements and the proposed change does not earn its build and maintenance burden. Adopt a narrower profile when it helps one stratum but not another. Change the source preparation, route, assessor, delivery, observer or memory indicated by the evidence. A source gap may require obtaining a source rather than improving retrieval.

Name what the evidence supports, what it leaves untested and which condition reopens the decision. A changed corpus, model, language population, authority rule, workload or privacy constraint can defeat the original comparison. Preserve an operational fallback and observation during a bounded rollout if that is the selected use. A favorable laboratory result alone is not deployment or human benefit.

### KCAE.EVAL:5 - Archetypal Grounding

Suppose CedarBench compares an existing hybrid search workflow with a proposed direct-block supplement on 40 withheld support episodes. These are invented study conditions, not reported measurements. Cases include protocol ambiguity, old translations, useful table notes and naturally unsupported requests. Both alternatives use the same source snapshot, assessor, delivery and recipient rules. Include the proposed route’s additional call and maintenance costs in the comparison.

Suppose the correct exception appears when a reviewer supplies its source. Inspect the original run before choosing a repair. If the finder missed the source and adding that candidate under otherwise equivalent conditions restores the qualified answer, repair the finding route. If the candidate pool already contained it, find out whether the assessor saw the protocol v1 condition and how that condition figured in the judgement. A correct judgement whose delivery preserves only an upbeat first sentence calls for a delivery repair. If the original trace cannot distinguish these accounts, the manual result shows one workable arrangement. A comparison that changes just the disputed contribution can locate the fault if the decision warrants it. For adoption, use the evidence that covers the intended arrangement and its receiving conditions. Repeat the affected use where that evidence is missing or a new trial is commissioned.

### KCAE.EVAL:6 - Bias-Annotation

Authors tend to select examples their design can answer and count improvement where it is easiest to measure. Start from the receiving work and include natural failures and no-use cases. Avoid tuning on the final test, treating model agreement as independent truth, or omitting preparation and interruption costs. Readers can more reliably reuse a conclusion limited to the cases tested than a score that overstates the evidence.

### KCAE.EVAL:7 - Conformance Checklist

What decision about adoption, assurance or repair does the evidence settle? For a comparative claim, are the alternatives credible and their results and costs comparable? If new-use performance is at issue, could the evaluation expose a missing or unsupported answer, and was it independent of the development cases? If independent acceptance was commissioned, is the required decision established for this use? If a particular operation failed, does the evidence identify where intervention can help? After a repair, establish its effect on the receiving use. State which conditions the conclusion covers and what change would reopen it.

### KCAE.EVAL:8 - Common Anti-Patterns and How to Avoid Them

A green API test establishes interface behavior, not useful advice. A stronger retriever with a weaker prompt is not a clean model comparison. An oracle candidate trial is a diagnosis, not end-to-end performance. A gold-free case is not necessarily a true no-answer case; inspect its source basis. A cheap query does not make an expensive maintained service cheap.

### KCAE.EVAL:9 - Consequences

Engineering choices become revisable on evidence relevant to the receiving work. Some promising additions will be rejected or narrowed. Evaluation itself costs work, so reuse current matching results and inspect only changes that can alter the decision. Choose the measures and number of cases for the decision: the method requires neither every possible metric nor a fixed sample size.

### KCAE.EVAL:10 - Architectural Rationale

A requirement can be decided directly from evidence about the whole arrangement. A claim of advantage depends on what another feasible arrangement would provide. Where a consequential failure still has several possible causes, controlled substitutions can identify which operation to change. Return that repair to the result its recipient needs.

### KCAE.EVAL:11 - SoTA-Echoing

AgentRetrievalBench contributes a concrete warning about natural no-gold retrieval and limited evidence from artificial controls. Typed-decision audits expose confounding and coherence questions that an output schema alone cannot resolve. KCAE.Reference:9 preserves their scope; neither establishes support-library efficacy. Classical information-retrieval evaluation remains useful for component diagnosis. This pattern adds receiving use, source change, reader sufficiency, encounter and full lifecycle cost to the adoption question. Reopen metrics when they cease to distinguish the failure that matters.

### KCAE.EVAL:12 - Relations

KCAE.USE supplies the decision and workload. Every other KCAE method supplies an operation that can be examined without making its local success the whole result. C.11.DUA supplies advice and evidence burden; A.3.1.FT supplies qualified method-transfer questions when transfer is claimed.

### KCAE.EVAL:End
