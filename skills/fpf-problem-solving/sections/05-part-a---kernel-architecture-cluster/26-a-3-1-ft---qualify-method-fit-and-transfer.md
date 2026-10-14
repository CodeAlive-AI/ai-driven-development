## A.3.1.FT - Qualify Method Fit and Transfer

> **Type:** Method pattern
> **Status:** Stable

> **Primary working result:** a bounded fit, failure, applicability, transfer, or missing-evidence result for an admitted Method; or bounded situation evidence about a candidate proposal whose status remains unchanged. A change in reusable Method semantics returns a variant question instead of being hidden inside a transfer claim.

### A.3.1.FT:0 - Use This When

Use this pattern when actual Work has supplied evidence in one or more situations and a practitioner must decide whether an admitted Method fits a named receiving situation, where its applicability stops, or whether a supported claim transfers from a source situation family. Begin with the source and receiving situations and the claim whose truth could change between them.

The first useful result is a situation-comparison row. It names the Method or candidate status, source and receiving situation families, actual Work used as evidence, matched and changed conditions, holder capabilities, Systems and direct relations, adaptations, domain results, semantic changes, evidence reach, and the bounded result or missing premise.

Here *fit* and *transfer* are Plain practice names for two different decisions. Fit concerns a Method and a bounded situation or situation family. Transfer concerns whether a supported claim survives a stated move from source to receiving conditions. Neither word creates a universal FPF predicate or statistical generalization.

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
| transfer result | A bounded result about whether a source-supported claim survives the named change in conditions. | One receiving occurrence rarely supports a broad situation family; return the narrower result or missing evidence. |

### A.3.1.FT:1 - Problem Frame

Methods are often moved by name: a team says that a Method worked in one project, industry, or organization and applies it to another. The label hides the conditions that mattered—project purpose, development phase, technical problem, performer capability, support Systems, direct relations, adaptations, and the domain result being judged.

The opposite error is equally common. Any adaptation or local failure is treated as evidence that the Method cannot transfer, even when the changed condition, support defect, or altered Method semantics has not been identified. A useful validation result must show what stayed the same, what changed, what actual Work occurred, and what claim survives.

### A.3.1.FT:2 - Problem

A favourable source case can be generalized without a discriminating receiving situation. A candidate account can be called enacted. Training or expert help can be hidden inside “same conditions”. A changed representation or operation can be called tailoring even though reusable Method semantics changed. Immediate self-report can become lasting transfer, and fit can become worth.

These shortcuts produce confident but unreplayable applicability claims. Practitioners cannot tell which condition matters, whether the same Method was used, whether the evidence came from actual Work, or what result should be revised after a failure.

### A.3.1.FT:3 - Forces

| Force | Tension |
| --- | --- |
| Local usefulness | A narrow fit result can guide current Work, while sponsors often ask for broad transfer. |
| Unlike situations | Difference can reveal a boundary, while too many simultaneous changes defeat interpretation. |
| Method identity | Adaptation may be necessary, while semantic change can create a different variant. |
| Natural Work | Workplace evidence has practical relevance, while conditions and contribution are less controlled. |
| Capability and support | They can determine outcomes, while their presence is easily attributed to the Method. |
| Positive and negative evidence | Success and failure both matter, while selective reporting favours one direction. |
| Decision speed | Teams need a bounded answer, while missing Work or comparability must remain a reason to stop. |

### A.3.1.FT:4 - Solution

Method identity under A.3.1 and one successful Work occurrence do not establish fit in another situation. The operation below compares source and receiving conditions, necessary adaptations and retained evidence, so that an independently usable transfer conclusion can be returned without silently inheriting the source qualification.

Compare actual source and receiving Work through a decision-relative situation account, include one condition capable of defeating the claim, preserve Method semantics and status, and return only the fit or transfer result supported by that comparison.

#### A.3.1.FT:4.1 - Pattern-Use Unfolding

1. **Name the decision, subject, and status.** State whether the question concerns fit in one receiving situation, an applicability boundary, or transfer of one supported claim. Identify the `A.3.1`-admitted Method, or preserve the candidate account and name only separately admitted constituent Methods whose enactment is claimed.
2. **Bound the source and receiving situation families.** Record project purpose, development phase, technical or domain problem characteristics, performer population, holder capabilities, participating Systems, Agent-performed Work, direct relations, constraints, support conditions, qualification window, and the domain result relevant to the claim.
3. **Recover source Work and evidence.** Use A.3.1.WT evidence only for actual Work whose performers, enacted admitted Method, temporal extent, containing System, conditions, deviations, burdens, adaptations, results, and evidence path are recoverable. A report can support the account but does not admit Work by citation.
4. **Select a receiving or held-out situation that can discriminate.** Select or seek one named condition change capable of defeating the claim: technical coupling, project phase, domain, performer or capability envelope, support relation, organizational condition, information availability, authority boundary, or another named condition. State why it matters. If minimality matters, name the alternatives, ordering criterion, and basis for treating one change as smaller or weaker; otherwise record concurrent changes and unknowns without ranking them.
5. **Separate matched, changed, and unknown conditions.** Do not call conditions controlled unless the basis supports it. Record concurrent changes and missing facts; use `missing-comparability-basis` when the comparison cannot distinguish the claimed boundary.
6. **Recover receiving Work independently.** Admit the receiving Work occurrence and every claimed enacted Method under their direct governors. Preserve WorkPlan, simulation, demonstration, report, training, and support tasks as separate results. If receiving Work did not occur, return `missing-performed-work` rather than a transfer claim.
7. **Track adaptations and Method semantics.** Record changes to operations, dependencies, roles, stops, representations, support, and local Work. Ask whether reusable Method semantics stayed within the admitted Method. If they changed, return `variant-question[...]` to A.3.1.MV and evaluate the unchanged and changed branches separately.
8. **Compare domain results and evidence reach.** Compare the result relevant to the fit claim together with burdens, deviations, failures, and limitations needed to interpret it. Distinguish direct observation, report, association, contribution, and causality. Do not use immediate self-report as long-term transfer without the missing time evidence.
9. **Classify the bounded result.** Return `fit-within[...]`, `failure-within[...]`, `applicable-if[...]`, `transfer-supported-between[...]`, `transfer-not-supported`, `missing-performed-work`, `missing-comparability-basis`, or the named missing premise. Plain labels may be used, but the situation, claim, evidence, and window must remain inspectable.
10. **Route a defeated claim by result kind.** Return a failure directly only to the C.39.RQ situational requirement, C.32.MWA.PP architecture decision, B.1.5.CM construction result or admitted Method claim, or A.3.1.MV applicability or variant entry that the evidence contradicts. When the evidence may contradict an A.3.2.DE description, C.37.MP Method representation profile row, or A.15.8.MS support claim, return the bounded observation to A.3.1.CC; A.3.1.CC identifies and rechecks the maintained correction owner, including the direct governor of any lower representation result. Do not reopen every carrier.
11. **State non-transfer and reopen conditions.** Name the populations, domains, capability envelopes, support arrangements, times, alternatives, and causal claims not covered. Reopen when one condition crosses the declared boundary, Method semantics change, evidence currentness expires, or a new unlike situation defeats the claim.

#### A.3.1.FT:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| validation use | Fit, applicability, or transfer question; receiver; decision; claim; qualification window; stop. |
| subject status | Admitted Method, or candidate account plus separately admitted enacted constituent Methods. |
| source situation | Situation-family conditions, actual Work, performers, capability inputs, Systems, Agent-performed Work, direct relations, adaptations, domain results, burdens, and evidence reach. |
| receiving situation | The same positions for actual receiving or held-out Work, including missing facts. |
| discrimination | Condition selected to challenge the claim, why it matters, matched conditions, changed conditions, and unknowns. |
| semantic continuity | Preserved Method semantics, local Work or support changes, and any reusable semantic change returned as a variant question. |
| comparison | Result differences, burdens and deviations needed for interpretation, evidence strength, and unsupported contribution or causal claims. |
| return | Bounded fit, failure, applicability, transfer, or missing-evidence result; direct C.39.RQ, C.32.MWA.PP, B.1.5.CM, or A.3.1.MV return, or a bounded A.3.1.CC observation for a possible A.3.2.DE description, C.37.MP Method representation profile-row, or A.15.8.MS support contradiction; non-transfer and reopen conditions; unaffected results preserved. |

#### A.3.1.FT:4.3 - What Changes in Practice

Teams stop transferring a Method by title or rejecting it after an unexplained local failure. They can show the source conditions, receiving conditions, actual Work, semantic continuity, one discriminating change, and the exact claim that survived or failed.

A narrow result such as “Fits this decision for this holder and support window; transfer untested” can support a decision to use the Method now while protecting later teams from a universal claim.

#### A.3.1.FT:4.4 - Minimal Constructed Fit Replay

Continue the constructed A.3.1.WT evidence for admitted `M-Unit-Review-1`. The immediate decision is whether the Method fits pre-release review of temperature-sensor reports for `Reviewer-17` through day D30 when mixed Celsius/Kelvin inputs may occur. It is not yet a decision about another reviewer, product family, tool, or organization.

`W-Rep-1` and `W-Disc-1` are actual Work in `Calibration-Team-A`. The same reviewer, capability input `CAP-R17-1` with qualification record `QR-R17-1`, MethodDescription edition 4, manually retrieved conversion table, release boundary, and containing System are recorded. The discriminating change is the Celsius/Kelvin mismatch in `S-Disc-1`; it can defeat the claim that the Method exposes a unit mismatch before the release decision. In `W-Disc-1`, the reviewer normalizes values, detects the mismatch, stops release, and returns the report. A.3.1.CC has separately corrected direct use result `C37-UR-Flow-4` and its governed representation result `REP-UR-Flow-4`, which had omitted normalization for that named use.

Return `fit-within[Reviewer-17, temperature-sensor reports, edition 4, manual conversion table, through D30]` for the named release-review decision. Also return `transfer-not-tested` for other holders, product families, support routes, qualification windows, or organizations. The two occurrences do not establish causal superiority or practical worth.

If the reviewer had changed the reusable operation from unit normalization to an approximation rule absent from `M-Unit-Review-1`, preserve the observed Work but return `variant-question[approximation-rule]` to A.3.1.MV. Do not call the changed branch successful transfer of the unchanged Method.

### A.3.1.FT:5 - Archetypal Grounding - SSFD Situation Boundaries

The SSFD workplace evidence supplies varied actual-project reports and a decision-relevant unlike-situation probe. Project 11 concerns functional analysis of a new by-wire steering system and reports 48 failure modes, 44 requirements and design rules, 44 individual-system test cases, and 33 overall-system requirements and test cases. Project 32 reports difficulty representing the relation between a closed-loop sensor and controller.

Use Project 11 as a source situation only after the SSFD Method or candidate status, relevant Work evidence, performer and capability facts, support conditions, and relied-on claim are recovered. Use Project 32 as a discriminating unlike situation because the closed-loop relation can challenge a representation or applicability claim. Do not infer that Project 11 caused or preceded Project 32, that the same performers and capabilities were present, or that a difficulty establishes whole-Method failure.

A defensible result may be narrow: Project 11 supplies bounded evidence for one functional-analysis situation; Project 32 defeats or leaves unsupported a broader representation claim until the owner-specific A.3.1.CC correction and receiving Work basis are recovered. The 41-report set broadens the evidence pool but does not establish transfer across every project stratum or causal contribution by SSFD alone.

#### A.3.1.FT:5.1 - Unlike-Domain and Current-Alternative Probes

The Digital Vaccine action-research case supplies performed validation actions in an operating health-services ecosystem and three plan-perform-evaluate cycles. Use it to replay the A.3.1.FT architecture in another domain, not to claim that SSFD transfers to health services. Its evaluation is ex ante and case-specific.

The sustainable-design workshops supply bounded applications of The Natural Step, Whole System Mapping, and Biomimicry across consumer electronics, furniture, and clothing. They can expose industry and activity differences, but immediate participant self-reports do not establish long-term transfer. The Halogen case shows that practitioner skill, project demands, and organization can accompany cyclic Method adaptation; if reusable semantics changed, route the result to A.3.1.MV instead of expanding one fit claim.

#### A.3.1.FT:5.2 - EC-417 Early Stop

The [full EC-417 application](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#fpfreference169---choose-the-smallest-method-development-result-needed-for-release-ec-417) supplies the receiving problem, alternatives, calculations and the distinct limits used below.

`C-EC-Release-v2` remains a candidate account. The three support-use Work occurrences from A.15.8.MS do not perform a release and cannot support release fit or transfer. Before any such result, recover one actual release Work occurrence, its performers, separately admitted enacted constituent Methods, capability inputs, Systems, Agent-performed Work, direct relations, support conditions, domain result, burdens, deviations, authority facts, and a performed held-out release situation.

Until then return `missing-performed-work` and `missing-held-out-situation`. Preserve the candidate branch and the unsupported `CUR-EC417-CadenceEffect-1`; no cadence or transfer claim becomes supported by planning three releases.

### A.3.1.FT:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| label-transfer bias | The same Method name is treated as evidence of the same Method and conditions. | Recover Method status, semantics, actual Work, and situation positions. |
| success-generalization bias | One favourable occurrence becomes a situation-family claim. | Return the narrow fit result and name transfer evidence still missing. |
| uncontrolled-sameness bias | Unrecorded capability, support, and organizational conditions are called matched. | Separate matched, changed, and unknown positions with their bases. |
| adaptation laundering | Changed reusable semantics are called local tailoring. | Return an A.3.1.MV variant question and preserve both branches. |
| failure-totalization bias | One difficulty becomes whole-Method failure. | Identify the claim, situation boundary, and repair owner actually defeated. |
| fit-as-worth bias | Usability in one situation becomes a keep or adoption decision. | Send results, burdens, alternatives, and evidence limits to C.11.MV. |
| account-enactment bias | A candidate account is said to be enacted in receiving Work. | Admit Work and enacted constituent Methods separately; preserve candidate status. |

### A.3.1.FT:7 - Conformance Checklist

- [ ] The decision is explicitly fit, applicability, or transfer for one claim.
- [ ] The Method is admitted or the proposed whole remains a candidate account.
- [ ] Source and receiving situation families name decision-relevant conditions rather than labels alone.
- [ ] Actual source and receiving Work, performers, enacted admitted Methods, capability inputs, Systems, direct relations, results, and evidence paths are recoverable or returned as gaps.
- [ ] One changed condition is selected because it can expose a limit in the claim.
- [ ] Matched, changed, and unknown conditions are separate.
- [ ] Adaptations are recorded, and reusable semantic change opens a variant question.
- [ ] Direct observation, self-report, association, contribution, and causality are not merged.
- [ ] The result is bounded by holder, situation, support, time, and evidence.
- [ ] Fit is not overread as practical worth, general effectiveness, capability, or cultural adoption.

### A.3.1.FT:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “It worked in automotive, so it transfers to health services.” | Replay the comparison architecture in the unlike domain; do not join Method, population, or history. |
| “Project 32 proves the Method failed.” | Identify the representation or applicability claim and the missing receiving evidence first. |
| “We tailored it, therefore it transferred.” | Check whether reusable semantics changed; if so, return a variant question. |
| “The workshop participants liked it, so transfer is established.” | Preserve immediate self-report and return missing long-term Work and result evidence. |
| “The candidate was enacted successfully.” | Admit the Work and enacted constituent Methods, not the candidate account. |

### A.3.1.FT:9 - Consequences

Fit and transfer claims become inspectable and narrow enough to guide real decisions. Practitioners can see which conditions matter, what actual Work supports the result, whether the same Method persisted, and where another situation must reopen the claim.

The cost is that many plausible transfers end as missing evidence or a smaller applicability envelope. Adaptation may also create a variant-maintenance obligation.

### A.3.1.FT:10 - Rationale

Transfer is not a property carried by a Method name. It is a claim about preserved reliance across a stated change in conditions, supported by actual Work and bounded evidence. A discriminating unlike situation is valuable because it can defeat the claim; it need not resemble a statistically representative sample.

Separating semantic continuity from local Work and support changes protects Method identity. It also lets a failure improve the applicability account without forcing rejection of the Method in situations for which evidence remains valid.

### A.3.1.FT:11 - SoTA-Echoing

| Source | Adopted or adapted contribution | Boundary and practitioner implication |
| --- | --- | --- |
| Yildirim, Campean, and Uddin, [function-modeling evaluation in industry practice](https://doi.org/10.1017/dsj.2026.10056) | Adopt workplace-project strata, reported applications and limitations, later report analysis, and the Project 11 to Project 32 unlike-situation probe. | One automotive OEM, retrospective reports, and SSFD use within a broader methodology establish neither SSFD-only causality nor general transfer. |
| Schønheyder and Nordby, [design-Method use and evolution in professional practice](https://doi.org/10.1016/j.destud.2018.04.001) | Adopt project demands, practitioner skill sets, organization, and cyclic adaptation as conditions that can change a fit or variant decision. | One multidisciplinary design firm supplies no universal situation taxonomy, causal result, or admitted variant family. |
| Tsai, Zdravkovic, and Söder, [DBE-design Method action research](https://doi.org/10.1007/s10270-022-01068-z) | Adopt repeated plan-perform-evaluate cycles in an operating health-services ecosystem as an unlike-domain replay of the comparison method. | The evaluation is ex ante and case-specific; it does not prove long-term effect or transfer to the other elicited domains. |
| Faludi, Yiu, and Agogino, [empirical tests of sustainable-design Methods](https://doi.org/10.1017/dsj.2020.17) | Adopt several Methods, industries, activities, and immediate participant reports as bounded situation-comparison inputs. | Immediate self-report establishes neither long-term product results nor causal superiority or transfer of recombined variants. |
| Current FPF `A.3.1`, `A.15.1`, `A.2.2`, and `A.10` | Reuse Method admission, actual Work admission, holder-dependent capability, and claim-bound evidence. | A.3.1.FT contributes the source-to-receiving situation comparison and semantic-continuity return; it does not redefine those governors. |

Reopen the pattern when a stronger field method changes which situation dimensions test the limits of the claim, when practitioners cannot separate semantic adaptation from local Work, when transfer decisions repeatedly require another independent result, or when governing FPF identities change the comparison.

### A.3.1.FT:12 - Relations

- A.3.1.WT supplies occurrence-level source and receiving evidence and explicit gaps. It does not make the fit or transfer conclusion.
- A.3.1.CC consumes any bounded observation that may contradict an A.3.2.DE description, C.37.MP Method representation profile row, A.15.8.MS support claim, or directly governed lower representation result; it identifies and rechecks the maintained correction owner. Passing coherence does not establish fit.
- C.11.MV consumes fit, failure, applicability, burdens, alternatives, and evidence limits for a separate practical-worth decision.
- A.3.1.MV owns reusable Method variants, provenance, applicability entries, and retirement. A semantic change returns there; a local Work, support, description, or representation change alone need not create a variant.
- `A.3.1` governs Method admission, `A.15.1` each Work occurrence, `A.2.2` capability inputs, and `A.10` claim-bound evidence. Cite the direct governor for every System, Agent-performed Work, relation, permission, authority, or result claim relied on.
- A.3.1.MI may later consume a bounded fit or transfer result when introducing a Method in practice; it does not inherit a causal or worth conclusion.

### A.3.1.FT:End
