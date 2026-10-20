## C.41.QC - Qualify Checklist Criteria and Checking Means

> **Type:** Method pattern
> **Status:** Stable


### C.41.QC:1 - Problem frame

**Use this when** a proposed criterion or checking means may fail to distinguish the difference that matters. This is common with inherited lists, generated criteria, model judgements, new tools and changed operating conditions. A checker can say “pass” while an importer replaces A17 with 1.

This Method establishes a bounded basis for using a criterion and its checking means, or returns a counterexample or unresolved qualification question. Start with one claim the proposed check is supposed to support and one plausible case where it could be wrong.

Reuse an applicable qualification when available. A second agent, a formal experiment or a broad benchmark is useful only when it answers a live uncertainty at worthwhile cost.

### C.41.QC:2 - Problem

A criterion can be irrelevant, vague or based on a mistaken description. A checker can implement a sensible criterion badly or observe a convenient proxy. Agreement among judges and high aggregate scores can hide the individual failure that matters to the work.

The problem is to examine both the criterion and the means of checking it before placing more reliance on their answers than the evidence supports. This differs from selecting which questions belong in the aid and from checking the actual subject on one occasion.

### C.41.QC:3 - Forces

| Tension | Practical implication |
| --- | --- |
| Useful coverage and cheap proxies | Test the consequential distinction rather than the easiest correlated signal. |
| Improvement speed and qualification cost | Start with a discriminating counterexample; expand only for the intended reliance. |
| Human judgement and executable checks | Use the means capable of observing the relevant property; neither is universally superior. |
| Aggregate evaluation and individual failures | Inspect the cases that could defeat the intended use. |
| Stable reuse and changing models or tools | Bound the qualification and identify what would reopen it. |

### C.41.QC:4 - Solution

A.10 governs evidence reliance; A.19.ULSAM governs an actual numerical aggregation. This qualification constructs the cases and expected distinctions needed to judge a criterion and its checking means. Separate answers need no aggregate, and an applicable earlier qualification needs no repetition merely because the questions are now carried in a checklist.

#### C.41.QC:4.1 - Recover the claim, basis and intended reliance

Name the criterion, the question it interprets and the subject of that question. Recover the description and the assumption connecting it to useful work. Use [C.39.RQ](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c39rq---construct-situated-method-requirements) when the criterion needs construction from the subject and situation.

Then name the checking means: a person applying a judgement, a comparison script, an observation tool or a model-based evaluator. What does it actually observe or consume? What answer does it produce? What will another person or system infer from that answer? Administrative claim-checking Methods supply the distinctions needed for that domain. A method name or test file is not itself proof that the intended check occurred.

For a model judge, include the supplied evidence and instructions, the criteria grouped in each call, and any rule combining repeated verdicts when these can change the relied-on answer.

Separate two uncertainties. A criterion can faithfully express the description while the description poorly serves the work. A checking means can also fail to apply that otherwise useful criterion. Investigate the uncertainty that changes the intended use.

A cheap indirect signal can justify further examination without certifying the larger result when it passes. An obsolete edition label on the card box can prompt inspection of its contents; a current label alone does not establish that every card was replaced. Name this intended inference and next move. Challenge both false reassurance and unnecessary alarms. If people can satisfy the visible signal while bypassing the substantive work, examine whether the signal remains informative for the intended use.

#### C.41.QC:4.2 - Construct a discriminating challenge

Choose cases with known or competently established differences relevant to the criterion. Include a satisfactory case and a plausible failure. Vary the property of interest while holding irrelevant differences small enough to interpret the result. For a subjective criterion, recover the judgement basis and a meaningful disagreement rather than inventing a false objective threshold.

Predict which answers those differences support before inspecting the checker output. Then compare the outputs with adequate grounds for those expected distinctions. A false pass and a false failure can have different costs; inspect both where they affect the work.

Where a rubric may drive the verdict independently of the subject, also hold the subject facts fixed and change the question. Establish what answer the new predicate supports before asking the checker. A reversed condition can call for the opposite answer; if only wording changes and the question stays the same, the expected answer stays the same. This distinction tests responsiveness to meaning without requiring every wording change to reverse a result.

When uncertainty concerns the judging arrangement, compare it on those grounded cases with a cheaper or less interfering alternative. Grouping criteria can save calls; separating them can reveal interference. Repetition and a rule for combining verdicts may reduce sampling instability, but repeated agreement cannot correct a consistent error or supply independent truth. Select the arrangement from consequential errors and total effort; repeat only when that comparison can change reliance.

If the receiving use consumes a total or percentage, examine what that number means and how the questions affect it. Splitting one easy condition into ten items can increase its influence without improving the subject. Ten successful formatting checks may conceal one failed catalogue-preservation check. Challenge the implied priorities, duplicate contributions and treatment of missing answers. Keep consequential answers visible. Where a numerical aggregate is actually needed, [FPF A.19.ULSAM](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a19ulsam---unified-lawful-scale-aggregation-mechanism-ulsam) governs the admitted measures and lawful aggregation; a convenient average does not supply its own justification.

Start cheaply. One counterexample can defeat an overbroad claim. Use a direct executable comparison when the question and observable property admit it. A selective rubric or pairwise judgement can help with an interpretive or relative question, but choosing the better of two results does not establish that either meets an absolute condition. Qualify that judging arrangement on cases whose consequential answers have adequate independent grounds. Compare false passes, false failures and obtaining those grounds as well as the cost per judgement. Broader reliance may call for representative cases, independent judgement, executable observation or a field trial through [A.3.1.WT](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a31wt---design-and-interpret-a-method-work-trial). Choose another reader or agent when it supplies a materially different basis, expertise or observation. Mere duplication of the same unsupported inference does not establish independence.

When work is repeatedly optimized against a score, compare earlier and later actual results on consequential characteristics and suitable new cases. A rising score can reward surface changes while the intended result deteriorates. For the importer, a more persuasive success report leaves identifier loss unchanged. Inspect the proposed shortcut and obtain evidence beyond the optimized signal. A stronger second model can help investigate disagreement, but its score still needs grounds and does not become ground truth by rank.

#### C.41.QC:4.3 - State the bounded result and a return condition

State what the qualification supports: which criterion, checking means, cases, conditions and receiving use it covers. State detected defects and residual uncertainty in terms that change action. A narrow successful probe does not establish all-domain accuracy.

If the criterion misses a work question, return to C.41. If the form corrupts its meaning, return to C.41.TF. If access or capability is missing, return to C.41.OF or its supplier. If the checker fails, repair, replace or restrict its use and repeat the affected challenge. Compare the gain with the qualification and operating cost through [C.11.MV](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11mv---compare-the-worth-of-a-method-option).

Keep the qualification separate from actual subject answers. C.41.UA still establishes what is true of the subject on its occasion. Reopen qualification when a material criterion, model, tool, observation route or operating condition changes, or when a new counterexample defeats its scope. Changed evidence, instructions, criterion grouping or verdict combination can trigger this even with the same model and criterion. Retain qualification for the unaffected observations and inferences. Stop when further investigation cannot improve the intended reliance at worthwhile cost, and preserve the limit rather than extending the claim.

### C.41.QC:5 - Archetypal Grounding

A team describes an importer as preserving item identifiers, reporting duplicate identifiers and retaining the previous catalogue when parsing fails. The description embodies assumptions about the team's use. A proposed generated check asks only whether an input file was accepted.

That check establishes none of the three described properties. A17 can become 1 during an otherwise successful import. A successful run also says nothing about duplicate reporting or the state after a parse failure.

The team constructs these qualification cases:

| Case | Distinction to establish | Observation capable of supporting it |
| --- | --- | --- |
| Valid catalogue with identifier A17 | Identifier preserved, rather than replaced or normalized unexpectedly. | Compare the input identifier with the stored identifier for the corresponding item. |
| Two records with the same identifier | The described duplicate report occurs for that input. | Inspect the returned report and its association with the duplicate records. |
| Malformed input with a known prior catalogue | Parse failure leaves the prior catalogue intact. | Observe the failure and compare the relevant catalogue state before and after it. |

These are three separate questions. A candidate checker that observes only an exit code cannot settle the third unless an independently established relation makes that code sufficient for the stated use. The team tests its proposed before/after comparison against a deliberately altered catalogue and an unchanged one. If it passes both, it has failed the intended discrimination; if it distinguishes them, that supports the comparison for those cases.

Complement that changed-catalogue challenge with a changed-question challenge. Use a constructed fixture whose before and after catalogues are both C. For these fixed facts, “Are the before and after catalogue contents identical?” has the expected answer **Yes**, while “Do the after contents differ from the before contents?” has the expected answer **No**. “Do both snapshots contain the same catalogue content?” preserves the first question and therefore its expected Yes. These answers follow from the fixture before any checker is run. A checker that returns the same verdict for the opposite conditions misses the question; one that changes the first answer merely because it is reworded is unstable on that case. Passing these contrasts supports only this bounded discrimination.

To examine grouped judging, give a model the same before and after snapshots C, plus a report headed “Import summary”. Before any output, content identity has expected **Yes**, and the presence of that heading has its separate expected **Yes**. Compare the identity verdict when asked alone and when asked alongside the heading question, with the same evidence supplied. The extra question changes neither snapshot nor the identity predicate. Repeat the contrast with a fixture whose after snapshot changes A17 to 1: identity is then **No** in both arrangements, while the heading answer stays Yes. If grouping changes either identity verdict, investigate or restrict that arrangement; do not average the two distinct questions into a pass. Combining repeated identity verdicts still has to answer to these fixture facts. Where grouped judging preserves the needed distinctions at lower cost, keep it. For actual stored data, an adequate direct comparison remains the cheaper starting choice.

A known malformed-input case with an unobserved post-state remains unresolved. Tool failure is not an importer failure or success. Local parser correctness does not settle the encompassing response and catalogue state; C.41.SR connects those contributions.

For the workshop display, “readable” may be judged from a desktop preview while participants will read the projected content from the back of a room. Qualification varies the viewing condition relevant to the exercise and asks a representative participant to interpret the actual content. A font-size threshold can be a useful local proxy only if its basis supports that use. Reconsider that proxy if glare or contrast makes text unreadable despite the chosen size.

Both examples are constructed probes. They illustrate how to challenge a claim, not measured checker performance.

### C.41.QC:6 - Bias-Annotation

People tend to invent tests that confirm their implementation. Generated criteria and generated answers can share the same blind spot. Recover a failure from the receiving work, seek an unlike case where it matters, and distinguish the data used to tune a checker from the evidence used to judge its broader use.

A benchmark's accessible cases can underrepresent the domain or participants who bear false failures. Make that limit part of the reliance decision.

### C.41.QC:7 - Conformance Checklist

Inspect the qualification's actual claim and probes:

- Are criterion, checking means, subject and receiving inference separately recoverable?
- Do the challenge cases vary a consequential property with adequate grounds for the expected distinction?
- Have false passes, false failures and unresolved observation been interpreted at their actual costs?
- Does any independent contribution supply a different basis rather than repeated agreement?
- Is the resulting reliance bounded, with material change and counterexample triggers for reconsideration?

### C.41.QC:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| A fluent generated rubric is treated as qualified. | Recover provenance and challenge a consequential distinction. |
| Two agreeing agents establish an unobserved fact. | Obtain an adequate observation or a judgement supported by different grounds. |
| A high average hides a decisive false pass. | Inspect the case and receiving inference that the intended use cannot tolerate. |
| Training reward is treated as runtime assurance. | Test the actual current checking arrangement and subject question. |
| A checker is qualified once for all future models and tools. | Reopen the affected scope when observation or judgement behavior changes. |

### C.41.QC:9 - Consequences

The Method can replace an attractive but uninformative check with a defensible, limited one. A single counterexample may prevent large misplaced reliance. Qualification also costs representative data, judgement and maintenance. Some questions remain uncertain or too expensive to settle; the useful outcome can be a smaller reliance claim or a different work arrangement.

### C.41.QC:10 - Architectural Rationale

Qualification is independently triggered when the adequacy of criteria or checking means becomes uncertain. Folding it into every ordinary use wastes effort; omitting it from design lets repeated unsupported answers accumulate.

An applicable prior qualification can settle the uncertainty. Otherwise begin with a concrete difference and scale the evidence to the intended reliance, using direct executable tests or competent human judgement as appropriate.

### C.41.QC:11 - SoTA-Echoing

Which checking means and qualification effort fit the intended reliance? **Adopt** a direct comparison for an explicit observable property; **adapt** selective rubric or pairwise judging for a genuinely interpretive or relative question, with discriminating cases when its adequacy is uncertain. These are serious alternatives, not successive compulsory stages. In §§4.2 and 5, inspecting identifier or catalogue equality supplies the relevant grounds directly. Asking a model for a persuasive overall score adds cost without settling those properties. Pairwise judging can instead help choose between two explanations, but the preferred one still needs a separate answer to an absolute suitability question.

[Selective Checklist Evaluation](https://aclanthology.org/2025.emnlp-main.538/) supplies a current rival to full-rubric/direct scoring, with effects that differ by setting and comparison mode. It warrants choosing and qualifying the mode for the receiving question, not declaring one universally superior. The study by [Hong and colleagues](https://arxiv.org/html/2607.12835v1) supplies counterevidence about detail and uneven emphasis in generated criteria. Section 4.2 therefore examines consequential errors, missing answers and induced weighting alongside judgement cost. The extra qualification is worthwhile when it can defeat misplaced reliance or select better means; an applicable prior qualification remains sufficient for its unchanged scope.

The study by [Bagaria and colleagues](https://arxiv.org/html/2609.02942v1) supplies bounded counterevidence about judges responding to changed answers and reversed criteria. Its generated and qualitatively inspected contrasts leave uncertainty about some expected verdicts. The adaptation in §§4.2 and 5 fixes expected answers from a simple fixture, then varies subject facts or question meaning separately. [RIPD](https://arxiv.org/html/2602.13576v1) supplies a further benchmark-versus-target counterexample motivating examination after rubric edits; it does not qualify a particular deployed judge.

For single, grouped or repeated model judgements, **adapt** protocol comparison to the consequential uncertainty in §§4.1–4.3 and the fixed-fixture case in §5. [RuVerBench v2](https://arxiv.org/html/2606.29920v2) supplies counterevidence about prompting, grouping and voting under long research/coding contexts; its selected binary cases exclude substantial ambiguity. [PReMISE v1](https://arxiv.org/html/2605.30803v1) separates stability from preference fit and robustness under model-mediated evaluation. Neither determines this deployment's best arrangement. Compare saved calls with consequential errors and examination effort; retain adequate prior qualification, and reopen its affected scope when a changed arrangement can alter a relied-on answer.

[AutoChecklist](https://arxiv.org/html/2603.07019v1) and [RLCF](https://arxiv.org/html/2507.18624v2) supply criterion refinement and checklist-feedback training alternatives. **Reject** their benchmark or training gains as substitutes for qualifying this checker. [CHERRL](https://arxiv.org/html/2606.04923v1) and [Rubric Dropout](https://arxiv.org/html/2608.11669v1) expose proxy exploitation and divergence in bounded training settings; the latter's single-run configurations and fallible external judge limit the result. Its training intervention gives no general reason to omit operational checks. Section 4.2 instead examines actual results and new cases beyond the optimized signal.

The deliberate trade-off is the cost of obtaining discriminating grounds against the cost of a consequential false answer. None of these studies supplies a common error/cost ranking for every domain. [Anthropic's harness-design account](https://www.anthropic.com/engineering/harness-design-long-running-apps) supplies a worked calibration candidate as models and tools change; [A.3.1.WT](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a31wt---design-and-interpret-a-method-work-trial) and [C.11.MV](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11mv---compare-the-worth-of-a-method-option) guide the local trial and worth comparison when the choice remains consequential. Reopen qualification for a material criterion, tool or use change, an unexplained verdict on a known contrast, or a cheaper adequate observation.

### C.41.QC:12 - Relations

C.41 supplies proposed work questions and receives coverage corrections. C.41.TF preserves qualified meanings, C.41.OF makes observations accessible, C.41.UA performs actual checks, and C.41.SR interprets their combined use. [FPF A.19.ULSAM](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a19ulsam---unified-lawful-scale-aggregation-mechanism-ulsam) is a conditional return when the receiving use needs numerical aggregation; ordinary separate answers require no such calculation.

[C.39.RQ](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c39rq---construct-situated-method-requirements) supplies criterion construction, [A.3.1.WT](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a31wt---design-and-interpret-a-method-work-trial) representative trial, and [C.11.MV](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11mv---compare-the-worth-of-a-method-option) worth appraisal. The actual subject examination supplies the observation or judgement whose adequacy is being tested; administrative claim checking is one domain example. Qualification uses the required results for the specific uncertainty in checklist criteria or means; it does not replace those Methods.

### C.41.QC:End
