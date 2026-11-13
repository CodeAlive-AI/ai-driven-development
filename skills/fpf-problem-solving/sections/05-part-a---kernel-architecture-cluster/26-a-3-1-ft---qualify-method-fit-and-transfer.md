## A.3.1.FT - Qualify Method Fit and Transfer

> **Type:** Method pattern
> **Status:** Stable

### A.3.1.FT:0 - Use This When

Use this pattern when Work has supplied evidence in one or more situations and a practitioner must decide whether an admitted Method fits a named situation, where its applicability stops, or whether a supported claim transfers from a source situation family. Begin with the required result and the conditions of the situation in which the Method will be used. For a transfer question, also name the source situation and the claim whose support is being carried into the receiving situation.

The first useful result is a bounded assessment of fit, an applicability limit, or transfer, with the evidence used and any missing premise. Identify the Method or candidate status, the situation and required result, relevant actual Work, adaptations and evidence reach. Where the question requires comparison, also distinguish source and receiving situations, matched and changed conditions, and material differences in capability, support, domain results and burdens.

Here *fit* and *transfer* are Plain practice names for two different decisions. Fit concerns a Method and a bounded situation or situation family. Transfer concerns whether a supported claim survives a stated move from source to receiving conditions.

Do not use this pattern to infer practical worth, causal contribution, general effectiveness, capability, or cultural adoption. A Method can fit and still be a poor choice against current alternatives. C.11.MV owns that comparison. An account is never enacted, and a candidate whole remains a candidate even when separately admitted Work succeeds.

#### A.3.1.FT:0.1 - Working Distinctions

| Item | Working meaning here | Boundary |
| --- | --- | --- |
| source situation family | The bounded set of source conditions under which the relied-on Method claim has evidence. | A project label or industry name is insufficient; state the decision-relevant conditions. |
| receiving situation family | The bounded set of conditions in which the practitioner wants to rely on the claim. | It is not “everywhere else” or a population inferred from one case. |
| representative source slice | Actual source Work selected because its stated characteristics bear on the current claim. | Convenience or success alone does not make it representative. |
| discriminating unlike situation | A receiving or held-out situation whose changed condition can expose a limit in the claim. | Difference is useful only when the claim it can defeat is stated. |
| matched condition | A condition held comparable enough for the declared decision, with its evidence basis. | Unrecorded sameness is not a control and does not establish causality. |
| adaptation | A change made in performing or supporting Work for the receiving situation. | If reusable Method semantics change, the result opens an A.3.1.MV variant question; it is not evidence for unchanged transfer. |
| situational fit | A bounded result that the admitted Method is usable for the named situation and decision under stated conditions and limits. | Fit establishes neither superiority, worth, causal contribution, nor general effectiveness. |
| transfer result | A bounded result about whether a source-supported claim survives the named change in conditions. | A broader situation-family conclusion needs its own support; otherwise return the narrower result or missing evidence. |

### A.3.1.FT:1 - Problem Frame

Methods are often moved by name: a team says that a Method worked in one project, industry, or organization and applies it to another. The label hides the conditions that mattered—project purpose, development phase, technical problem, performer capability, support Systems, direct relations, adaptations, and the domain result being judged.

The reverse inference can also fail. Any adaptation or local failure is treated as evidence that the Method cannot transfer, even when the changed condition, support defect, or altered Method semantics has not been identified. A useful transfer result must show what stayed the same, what changed, what Work occurred, and what claim survives.

### A.3.1.FT:2 - Problem

A favourable source case can be generalized without a discriminating receiving situation. A candidate account can be called enacted. Training or expert help can be hidden inside “same conditions”. A changed representation or operation can be called tailoring even though reusable Method semantics changed. Immediate self-report can become lasting transfer, and fit can become worth.

These shortcuts produce confident but unreplayable applicability claims. Practitioners cannot tell which condition matters, whether the same Method was used, whether the evidence came from actual Work, or what result should be revised after a failure.

### A.3.1.FT:3 - Forces

| Force | Tension |
| --- | --- |
| Local usefulness | A narrow fit result can guide current Work, while a broader transfer claim needs further support. |
| Unlike situations | Difference can reveal a boundary, while too many simultaneous changes defeat interpretation. |
| Method identity | Adaptation may be necessary, while semantic change can create a different variant. |
| Natural Work | Workplace evidence has practical relevance, while conditions and contribution are less controlled. |
| Capability and support | They can determine outcomes, while their presence is easily attributed to the Method. |
| Positive and negative evidence | Success and failure both matter, while selective reporting favours one direction. |
| Decision speed | Teams need a bounded answer, while missing Work or comparability must remain a reason to stop. |

### A.3.1.FT:4 - Solution

Method identity under A.3.1 does not establish fit for a use. Assess the required result against relevant Work and the conditions under which it occurred. A local fit result can be sufficient for the named decision. To claim transfer or a broader applicability boundary, recover the additional situation evidence and comparison on which that claim depends.

Preserve Method semantics and status throughout. Compare source and receiving conditions when carrying a claim between them; use a situation capable of testing the asserted limit when qualifying an applicability boundary. Return the supported result at that scope, or the specific missing basis.

#### A.3.1.FT:4.1 - Pattern-Use Unfolding

1. **Name the decision, subject, and status.** State whether the question concerns fit in one receiving situation, an applicability boundary, or transfer of one supported claim. Identify the `A.3.1`-admitted Method, or preserve the candidate account and name only separately admitted Methods whose enactment is claimed.
2. **Bound the situations needed for the decision.** For local fit, name the situation or situation family and required result. For transfer, name both source and receiving families; for an applicability boundary, name the situations that can establish that limit. Record the conditions that matter to the claim, such as project purpose, development phase, technical or domain problem, performer population, holder capabilities, participating Systems, direct relations, constraints, support, qualification window and domain result.
3. **Recover the relevant Work and evidence.** Use A.3.1.WT evidence only for actual Work whose performers, enacted admitted Method, temporal extent, containing System, conditions, deviations, burdens, adaptations, results, and evidence path are recoverable. Recover capability inputs and other direct relations on which the assessment relies. A report can support the account but does not admit Work by citation.
4. **Select discriminating evidence when the claim needs it.** To test a transfer or applicability boundary, select or seek a receiving or held-out situation with a condition capable of defeating the claim: technical coupling, project phase, domain, performer or capability envelope, support relation, organizational condition, information availability, authority boundary, or another named condition. State why it matters. If minimality matters, name the alternatives, ordering criterion, and basis for treating one change as smaller or weaker; otherwise record concurrent changes and unknowns without ranking them.
5. **Qualify comparability when making a comparison.** Separate matched, changed, and unknown conditions. Do not call conditions controlled unless the basis supports it. Record concurrent changes and missing facts; use `missing-comparability-basis` when the comparison cannot distinguish the claimed boundary.
6. **Establish any required receiving performance independently.** Admit receiving Work and every claimed enacted Method under their direct governors. Distinguish plans and reports from performed activity. For simulation, demonstration, training or support tasks, identify what was actually performed and what was only represented or planned; a demonstration may itself perform the Method in the required receiving situation. If the Work needed for the selected conclusion did not occur, return `missing-performed-work`.
7. **Track adaptations and Method semantics.** Record changes to operations, dependencies, participant or responsibility conditions, stops, representations, support, and local Work. Ask whether reusable Method semantics stayed within the admitted Method. If they changed, return `variant-question[...]` to A.3.1.MV and evaluate the unchanged and changed branches separately.
8. **Assess domain results and evidence reach.** Assess the required result and the burdens, deviations, failures and limitations that affect the fit decision. Compare results across situations when the selected claim requires it. Distinguish direct observation, report, association, contribution, and causality. Do not use immediate self-report as long-term transfer without the missing time evidence.
9. **Classify the bounded result.** Return `fit-within[...]`, `failure-within[...]`, `applicable-if[...]`, `transfer-supported-between[...]`, `transfer-not-supported`, `missing-performed-work`, `missing-comparability-basis`, or the named missing premise. Plain labels may be used, but the situation, claim, evidence, and window must remain inspectable.
10. **Route a defeated claim by result kind.** Return a failure directly only to the C.39.RQ situational requirement, C.32.MWA.PP architecture decision, B.1.5.CM construction result or admitted Method claim, or A.3.1.MV applicability or variant entry that the evidence contradicts. When the evidence may contradict an A.3.2.DE description, direct C.37 representation-use result or C.37.MP Method representation profile row, or A.15.8.MS support claim, return the bounded observation to A.3.1.CC; A.3.1.CC identifies and rechecks the maintained correction owner, including the direct governor of any lower representation result. Do not reopen every carrier.
11. **State non-transfer and reopen conditions.** State the supported applicability boundary and any uncovered use that matters to the receiving decision. Reopen when one condition crosses the declared boundary, Method semantics change, evidence currentness expires, or a new unlike situation defeats the claim.

#### A.3.1.FT:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| validation use | Fit, applicability, or transfer question; receiver; decision; claim; qualification window; stop. |
| subject status | Admitted Method, or candidate account plus separately admitted enacted Methods. |
| situation and Work evidence | Conditions of the situation being assessed, actual Work, performers, relied-on capability inputs, Systems and direct relations, adaptations, domain results, burdens and evidence reach. |
| source and receiving situations | For transfer, identify both families and their Work evidence independently. For a broader applicability boundary, identify the situations needed to test it. Preserve missing facts. |
| discrimination | When a boundary or transfer claim needs a discriminating situation, state the selected condition and why it matters. In a comparison, separate matched, changed and unknown conditions. |
| semantic continuity | Preserved Method semantics, local Work or support changes, and any reusable semantic change returned as a variant question. |
| assessment | Result against the local fit criteria; differences across situations when needed; burdens and deviations needed for interpretation, evidence strength, and material limits on contribution or causal claims. |
| return | Bounded fit, failure, applicability, transfer, or missing-evidence result; direct C.39.RQ, C.32.MWA.PP, B.1.5.CM, or A.3.1.MV return, or a bounded A.3.1.CC observation for a possible A.3.2.DE description, direct C.37 representation-use result, C.37.MP Method representation profile-row, or A.15.8.MS support contradiction; non-transfer and reopen conditions; unaffected results preserved. |

Keep the distinctions needed for the selected decision in the assessment and its referenced evidence. A table is optional; no separate record is needed for each position.

#### A.3.1.FT:4.3 - What Changes in Practice

Practitioners can use a sufficient local fit result without arranging an unrelated comparison. When they transfer a claim or qualify an applicability boundary, they can show the relevant source and receiving conditions, actual Work, semantic continuity, discriminating evidence, and the claim that survived or failed.

A narrow result such as “Fits this decision for this holder and support window; transfer untested” can support a decision to use the Method now while protecting later teams from a universal claim.

#### A.3.1.FT:4.4 - Constructed Fit Case

Continue the constructed A.3.1.WT evidence for admitted `M-Unit-Review-1`. The immediate decision is whether the Method fits pre-release review of temperature-sensor reports for `Reviewer-17` through day D30 when mixed Celsius/Kelvin inputs may occur. It is not yet a decision about another reviewer, product family, tool, or organization.

`W-Rep-1` and `W-Disc-1` are actual Work in `Calibration-Team-A`. The same reviewer, capability input `CAP-R17-1` with qualification record `QR-R17-1`, MethodDescription edition 4, manually retrieved conversion table, release boundary, and containing System are recorded. The discriminating change is the Celsius/Kelvin mismatch in `S-Disc-1`; it can defeat the claim that the Method exposes a unit mismatch before the release decision. In `W-Disc-1`, the reviewer normalizes values, detects the mismatch, stops release, and returns the report. A.3.1.CC has separately corrected direct use result `C37-UR-Flow-4` and its governed representation result `REP-UR-Flow-4`, which had omitted normalization for that named use.

Return `fit-within[Reviewer-17, temperature-sensor reports, edition 4, manual conversion table, through D30]` for the named release-review decision. Also return `transfer-not-tested` for other holders, product families, support routes, qualification windows, or organizations. The two occurrences do not establish causal superiority or practical worth.

For the narrower decision about the same-unit report already reviewed in `W-Rep-1`, its observed acceptance can support fit for that named situation, reviewer and support window. `W-Disc-1` is not a prerequisite for this narrower result. Evidence about mixed-unit handling is needed when that condition enters the receiving question.

If the reviewer had changed the reusable operation from unit normalization to an approximation rule absent from `M-Unit-Review-1`, preserve the observed Work but return `variant-question[approximation-rule]` to A.3.1.MV. Do not call the changed branch successful transfer of the unchanged Method.

### A.3.1.FT:5 - Archetypal Grounding - SSFD Situation Boundaries

The SSFD workplace evidence supplies varied actual-project reports and a decision-relevant unlike-situation probe. Project 11 concerns functional analysis of a new by-wire steering system and reports 48 failure modes, 44 requirements and design rules, 44 individual-system test cases, and 33 overall-system requirements and test cases. Project 32 reports difficulty representing the relation between a closed-loop sensor and controller.

Use Project 11 as a source situation only after the SSFD Method or candidate status, relevant Work evidence, performer and capability facts, support conditions, and relied-on claim are recovered. Use Project 32 as a discriminating unlike situation because the closed-loop relation can challenge a representation or applicability claim. Do not infer that Project 11 preceded Project 32, that the same performers and capabilities were present, or that a difficulty establishes whole-Method failure.

A result may be narrow: Project 11 supplies bounded evidence for one functional-analysis situation; Project 32 raises a question about a broader representation claim. A.3.1.CC can determine whether correction is needed when the relevant claim and evidence are recoverable; a transfer conclusion requires the receiving Work and comparison basis. The 41-report set broadens the evidence pool but does not establish transfer across every project stratum or causal contribution by SSFD alone.

#### A.3.1.FT:5.1 - Unlike-Domain and Current-Alternative Probes

The Digital Vaccine action-research case supplies performed validation actions in an operating health-services ecosystem and three plan-perform-evaluate cycles. Use it to examine the A.3.1.FT comparison in another domain, not to claim that SSFD transfers to health services. Its evaluation is ex ante and case-specific.

The sustainable-design workshops supply bounded applications of The Natural Step, Whole System Mapping, and Biomimicry across consumer electronics, furniture, and clothing. They can expose industry and activity differences, but immediate participant self-reports do not establish long-term transfer. The Halogen case shows that practitioner skill, project demands, and organization can accompany cyclic Method adaptation; if reusable semantics changed, route the result to A.3.1.MV instead of expanding one fit claim.

#### A.3.1.FT:5.2 - EC-417 Early Stop

The [full EC-417 application](../04-first-principles-framework-architectural-reference/16-fpf-reference-16---big-fpf-storylines.md#fpfreference169---choose-the-method-development-result-needed-for-release-ec-417) supplies the receiving problem, alternatives, calculations and the distinct limits used below.

`C-EC-Release-v2` remains a candidate account. The three support-use Work occurrences from A.15.8.MS do not perform a release and cannot support release fit or transfer. To assess local release fit, recover actual release Work, its performers, separately admitted enacted Methods, capability inputs, Systems and direct relations, support conditions, domain result, burdens, deviations and authority facts needed for that decision. A transfer or applicability-boundary claim additionally requires the receiving or held-out release evidence capable of testing that claim.

While the required release Work is absent, return `missing-performed-work`. Return `missing-held-out-situation` only when the selected boundary or transfer claim needs that missing situation. Preserve the candidate branch and the unsupported `CUR-EC417-CadenceEffect-1`; no cadence or transfer claim becomes supported by planning three releases.

### A.3.1.FT:6 - Bias-Annotation

| Bias | Likely drift | Repair |
| --- | --- | --- |
| label-transfer bias | The same Method name is treated as evidence of the same Method and conditions. | Recover Method status, semantics, actual Work, and situation positions. |
| success-generalization bias | One favourable occurrence becomes a situation-family claim. | Return the narrow fit result and name the missing transfer evidence. |
| uncontrolled-sameness bias | Unrecorded capability, support, and organizational conditions are called matched. | Separate matched, changed, and unknown positions with their bases. |
| adaptation laundering | Changed reusable semantics are called local tailoring. | Return an A.3.1.MV variant question and preserve both branches. |
| failure-totalization bias | One difficulty becomes whole-Method failure. | Determine which claim, if any, the evidence contradicts, and identify that claim's situation boundary and correction owner. |
| fit-as-worth bias | Usability in one situation becomes a keep or adoption decision. | Send results, burdens, alternatives, and evidence limits to C.11.MV. |
| account-enactment bias | A candidate account is said to be enacted in receiving Work. | Admit Work and enacted Methods separately; preserve candidate status. |

### A.3.1.FT:7 - Conformance Checklist

- [ ] The decision is explicitly fit, applicability, or transfer for one claim.
- [ ] The Method is admitted or the proposed whole remains a candidate account.
- [ ] The situation being assessed names decision-relevant conditions; transfer identifies source and receiving families, and an applicability boundary identifies the situations needed to test it.
- [ ] Actual Work needed for the conclusion, performers, enacted admitted Methods, relied-on capability inputs, Systems, direct relations, results and evidence paths are recoverable or returned as gaps.
- [ ] Any required discriminating situation is selected because its condition can expose a limit in the claim.
- [ ] When situations are compared, matched, changed and unknown conditions are separate.
- [ ] Adaptations are recorded, and reusable semantic change opens a variant question.
- [ ] Direct observation, self-report, association, contribution, and causality are not merged.
- [ ] The result is bounded by holder, situation, support, time, and evidence.
- [ ] Fit is not overread as practical worth, general effectiveness, capability, or cultural adoption.

### A.3.1.FT:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “It worked in automotive, so it transfers to health services.” | Recover evidence for the same Method under the receiving conditions. Tests of another Method in health services do not establish this transfer. |
| “Project 32 proves the Method failed.” | Identify the representation or applicability claim and the missing receiving evidence first. |
| “We tailored it, therefore it transferred.” | Check whether reusable semantics changed; if so, return a variant question. |
| “The workshop participants liked it, so transfer is established.” | Return only what the immediate self-report supports; identify any missing Work, result or time evidence required by the transfer claim. |
| “The candidate was enacted successfully.” | Admit the Work and enacted Methods, not the candidate account. |

### A.3.1.FT:9 - Consequences

Fit and transfer claims become inspectable and narrow enough to guide decisions. Practitioners can see which conditions matter, what actual Work supports the result, whether the same Method persisted, and where another situation must reopen the claim.

The cost is that many plausible transfers end as missing evidence or a smaller applicability envelope. A semantic adaptation may also leave a separate variant to maintain.

### A.3.1.FT:10 - Rationale

Transfer is not a property carried by a Method name. It is a claim about preserved reliance across a stated change in conditions, supported by actual Work and bounded evidence. A discriminating unlike situation is valuable because it can defeat the claim; it need not resemble a statistically representative sample.

Separating semantic continuity from local Work and support changes protects Method identity. It also lets a failure improve the applicability account without forcing rejection of the Method in situations for which evidence remains valid.

### A.3.1.FT:11 - SoTA-Echoing

| Source | Contribution | Boundary and practitioner implication |
| --- | --- | --- |
| Yildirim, Campean, and Uddin, [function-modeling evaluation in industry practice](https://doi.org/10.1017/dsj.2026.10056) | Workplace-project strata, reported applications and limitations, later report analysis, and the comparison of Project 11 and Project 32 supply an unlike-situation probe. | One automotive OEM, retrospective reports, and SSFD use within a broader methodology establish neither SSFD-only causality nor general transfer. |
| Schønheyder and Nordby, [design-Method use and evolution in professional practice](https://doi.org/10.1016/j.destud.2018.04.001) | Project demands, practitioner skill sets, organization, and cyclic adaptation are conditions that can change a fit or variant decision. | Keep the findings bounded to the studied firm and conditions; establish any causal claim or Method-variant identity separately. |
| Tsai, Zdravkovic, and Söder, [DBE-design Method action research](https://doi.org/10.1007/s10270-022-01068-z) | Repeated plan-perform-evaluate cycles in an operating health-services ecosystem provide an unlike-domain example for the comparison method. | The evaluation is ex ante and case-specific; it does not prove long-term effect or transfer to the other elicited domains. |
| Faludi, Yiu, and Agogino, [empirical tests of sustainable-design Methods](https://doi.org/10.1017/dsj.2020.17) | Several Methods, industries, activities, and immediate participant reports supply bounded situation-comparison inputs. | Immediate self-report establishes neither long-term product results nor causal superiority or transfer of recombined variants. |

### A.3.1.FT:12 - Relations

- A.3.1.WT supplies occurrence-level evidence for the selected situations and explicit gaps. It does not make the fit or transfer conclusion.
- A.3.1.CC consumes any bounded observation that may contradict an A.3.2.DE description, direct C.37 representation-use result, C.37.MP Method representation profile row, A.15.8.MS support claim, or directly governed lower representation result; it identifies and rechecks the maintained correction owner. Passing coherence does not establish fit.
- C.11.MV consumes fit, failure, applicability, burdens, alternatives, and evidence limits for a separate practical-worth decision.
- A.3.1.MV owns reusable Method variants, provenance, applicability entries, and retirement. A semantic change returns there; a local Work, support, description, or representation change alone need not create a variant.
- `A.3.1` governs Method admission, `A.15.1` each Work occurrence, `A.2.2` capability inputs, and `A.10` claim-bound evidence. Cite the direct governor for every System, Agent-performed Work, relation, permission, authority, or result claim relied on.
- A.3.1.MI may later consume a bounded fit or transfer result when introducing a Method in practice; it does not inherit a causal or worth conclusion.

### A.3.1.FT:End
