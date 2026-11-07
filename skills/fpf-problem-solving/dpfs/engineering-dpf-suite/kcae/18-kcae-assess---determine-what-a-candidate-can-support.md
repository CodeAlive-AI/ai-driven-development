## KCAE.ASSESS - Determine What a Candidate Can Support

> **Type:** Method pattern
> **Status:** Stable

### KCAE.ASSESS:1 - Problem frame

Use this when a retrieved passage, document or method description might contribute to a concrete result, or when an automated score is to affect reading, recommendation or action. The governed object is that bounded contribution judgement and its obtaining procedure. The result states what the inspected source supports, contradicts or leaves unresolved under the receiving conditions. You need the question, source context and access to necessary domain criteria. Ranking already known adequate alternatives is a narrower use; it does not require repeating their unchanged qualification.

### KCAE.ASSESS:2 - Problem

Similarity, authority, truth, applicability and worthwhile intervention answer different questions. An assessor can rank candidates accurately while recommending the best of an entirely inadequate pool. A binary output can turn missing facts into rejection. A polished explanation can invent a criterion that the responsible domain never supplied.

### KCAE.ASSESS:3 - Forces

Cheap screening saves reading; decisive conditions can lie outside the screen. Explicit criteria improve repeatability; fixed criteria can omit a new kind of useful contribution. A typed result simplifies integration but cannot establish its own grounds. Stronger automation requires stronger evidence than ordering the next paragraphs to read.

### KCAE.ASSESS:4 - Solution

#### KCAE.ASSESS:4.1 - Derive the question from the receiving decision

Name the decision affected by this assessment. For screening, ask whether deeper reading could supply a needed contribution. For substantive use, ask which result the candidate can produce or support, under which conditions and with which available inputs. For a recommendation, add whether that result is still needed and worth the recipient's burden. Use separate results when these questions can have different answers.

Construct the criterion from the work and the source. Recover the source's claim or described operation, input requirements, result, scope and exceptions. Obtain domain-specific standards from the responsible source or expert. Compare these with the case facts. If the criterion itself is disputed, return that question to its owner; a general evaluator cannot create the domain's acceptance standard from confidence.

For open-ended material, allow an explanatory distinction or a useful question to count as a contribution. Do not filter everything through “does this call a tool?” A method for understanding a conflict can be useful even when its immediate result is prose. Conversely, mentioning the same topic does not show which missing result the material supplies.

#### KCAE.ASSESS:4.2 - Build an inspectable claim-and-condition reading

Extract the decisive source proposition with its exact location and necessary context. State the proposed correspondence to the case and why it matters. For every decisive premise, distinguish source support, contrary evidence, missing information and unresolved conflict. These states concern evidence for this use, not a universal many-valued logic.

In CedarBench, the inspected manual says that automated resend requires a deduplicating receiver and confirmed absence of a receipt. The case says that duplicates are being removed manually. It does not state receiver protocol or receipt status. The assessment therefore supports the source rule while leaving its applicability unresolved. “There are duplicates” neither proves nor disproves either prerequisite.

After a configuration read supplies protocol v1, the table contradicts the deduplication prerequisite. Automatic resend is unsuitable on that basis; receipt reconciliation can remain useful. A current correction to the table can reopen this judgement. If two authorized sources disagree and precedence is unresolved, return the conflict and its practical effect rather than quietly choosing the higher-scoring source.

Before treating passages as contradictory, align their product or entity, operation, time, scope and exceptions. A draft proposal and an approved rule have different roles; two instructions for different protocols may both hold. For multilingual claims, inspect the specific expression or relation that carries the difference, using a competent translator or established glossary when needed. If the original is unavailable, report the apparent disagreement in the accessible material and the original passage needed to settle it.

A negative reading must have its scope. “This paragraph supplies no evidence of receiver capability” does not imply “the receiver lacks capability.” Where the corpus is known exhaustive for a specific closed predicate, absence may have a defined meaning; obtain that contract explicitly. Most natural-language corpora are not closed in that way.

For a corpus-wide answer, assess two levels separately: whether the source passages support each intermediate claim, and whether their coverage, unit definitions and aggregation support the final scope. KCAE.SEARCH:4.6 supplies that construction. A correct quotation from one response cannot establish what most respondents say. Inspect the originals behind decisive generalizations and contrary cases, and check whether merged claims preserved time and conditions. Confirm that duplication, excluded material or unassessed units did not silently change the denominator or turn a selected overview into a population claim. Return the supported narrower answer when the broader inference remains unjustified.

#### KCAE.ASSESS:4.3 - Select the performer and output contract

Use deterministic code for an exact edition match, permitted identifier, numeric calculation or enumerated rule once its semantic inputs have been established. Use a person or language model for interpretation where needed. A typed assessor can answer bounded questions repeatedly at low cost; a generative reader can extract and explain the grounds. A domain specialist may be required for a disputed interpretation. Choose by the actual operation and evidence, rather than making one model perform everything.

A useful machine contract returns the criterion, relevant source addresses, established and unknown premises, proposed contribution, result kind and model/rule version where applicable. A small human answer can express the same information in ordinary prose. If the assessor cannot generate evidence spans, pair it with a separate retrieval/extraction operation and inspect their agreement. The numerical output alone does not supply provenance.

Keep retrieved text as source data. Pass controlling instructions and allowed actions through the trusted interface. A passage that asks the system to rank it first is not an authority over the evaluator. Test adversarial additions actually delivered to the model; deleting them before the call tests the filter instead. New relevant evidence can legitimately change the judgement, so distinguish it from unsupported persuasion.

#### KCAE.ASSESS:4.4 - Qualify scores for their intended decision

Ranking, calibration, classification at a threshold and agreement among logically related questions are separate properties. A probability distribution over a supplied group is conditional on that group. It can confidently prefer an inadequate candidate when none of the choices is suitable. Keep an explicit adequacy question and permit unresolved/no-useful-candidate results.

When candidates are split into groups, do not compare their locally normalized Choice probabilities as one global distribution. Screen with stable pointwise criteria or jointly reconsider finalists under the same question. For a multi-contribution result, assess the actual composition; multiplying unrelated usefulness probabilities assumes dependence facts that the model has not supplied.

Bind an adequacy result to the candidate actually returned. Suppose a ranking selects A, adequacy scores are A = 0.2 and B = 0.8, and an illustrative screening threshold is 0.3. The maximum score establishes only that some candidate passed; it cannot qualify A. Test the selected candidate's score and source conditions, choose an independently qualified alternative, or return the shortlist for another judgement. Preserve candidate identity, criterion and source context across that selection boundary.

Choose thresholds on development cases representative of the action and evaluate them on separate cases. Retain model, prompt/question, option order/wording, preprocessing, language, source scope and decision cost with the setting. Test near misses, unknown facts, late conditions, all-inadequate pools, longer inputs and meaningful negations. Recheck the affected qualification after a model or criterion change. The same threshold need not govern cheap further reading and a costly user interruption.

Where a score is useful only for ordering inspection, keep that limited claim and avoid pretending to have calibrated adequacy. A human can read the highest-ranked candidates and make the stronger judgement from source evidence. This often provides a viable first arrangement before fully automated recommendation is justified.

#### KCAE.ASSESS:4.5 - Return the contribution and the next useful move

Return an accepted bounded contribution, a reasoned rejection, an information request, a conflict or a need for deeper reading. State what would change the result. If the selected method requires a missing intermediate result, send that requirement to KCAE.COMPOSE or KCAE.SEARCH. If the contribution is already available, reuse it and avoid an unnecessary recommendation. Keep recommendation and application distinct: explaining why reconciliation would help does not reconcile the receipts.

### KCAE.ASSESS:5 - Archetypal Grounding

An assessor gives the retry article a high score for the duplicate-report query. Its first valid use is to order reading. Full reading reveals the receiver and receipt prerequisites. With neither case fact available, the returned result is “Potentially relevant rule; obtain destination protocol and receipt state before selecting automatic resend.” Protocol v1 then defeats the automation branch while retaining reconciliation. The useful result changes because a premise was established, not because the model became more confident.

### KCAE.ASSESS:6 - Bias-Annotation

An option list can force every case into familiar contributions. Include an unresolved outcome and inspect a sample without the existing labels. Fluent models can conceal missing domain criteria; require the source or responsible judgement that supplies the criterion. Repeated calls reveal variability but are not independent evidence of truth.

### KCAE.ASSESS:7 - Conformance Checklist

What decision will consume the result? Where did its criterion come from? Are source claims and case facts separate? Are missing and contradictory conditions distinguished? Can the grounds be inspected? Does score qualification match this model, question, language and action? Is an adequate existing result allowed to end the process?

### KCAE.ASSESS:8 - Common Anti-Patterns and How to Avoid Them

Promoting a screening score into an action approval skips source reading and domain criteria. Using low confidence as proof of corpus absence confuses assessment with search coverage. Summing group probabilities creates a fictitious common scale. An action-only filter discards explanatory methods; assess the needed contribution instead.

### KCAE.ASSESS:9 - Consequences

The recipient receives a usable conditional judgement rather than a mysterious rank. More premises can remain visibly unresolved, which is preferable to silently guessing them. Full automation may be narrower than the set of cases the system can assist.

### KCAE.ASSESS:10 - Architectural Rationale

The criterion, evidence and decision are separate so that a component can be replaced without changing the meaning of its output. Open unknowns allow an information-acquisition operation to complete a case; a single positive/negative score would obscure that continuation.

### KCAE.ASSESS:11 - SoTA-Echoing

Current typed-decision practice offers cheap bounded outputs, but the Jev documentation and recent audits distinguish input-output capability from comparative accuracy and logical coherence. KCAE.Profiles:2 gives their bounded contribution. This pattern adopts typed screening where qualified, adds explicit source/condition recovery, and retains a generative or expert reader as a serious alternative. The audit evidence changes score interpretation, not the public domain's acceptance criteria. Reopen the qualification when its inputs, model, question form or action costs change.

### KCAE.ASSESS:12 - Relations

KCAE.SEARCH supplies candidates and coverage limits; KCAE.SOURCE supplies context; KCAE.COMPOSE consumes qualified contributions; KCAE.DELIVER conveys the result. For FPF methods, E.11.PUR remains the owner of fit, recommendation and coordination judgement; A.3.1.DR, A.3.1.QM, C.32.MWA.PP and A.3.1.FT supply their declared method-recovery and transfer contributions.

### KCAE.ASSESS:End
