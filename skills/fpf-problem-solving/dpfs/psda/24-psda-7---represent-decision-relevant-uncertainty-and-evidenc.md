## PSDA.7 - Represent Decision-Relevant Uncertainty and Evidence Limits

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** a bounded account of the claim, consequences or eligibility the receiving inquiry asks about, the uncertainty that matters to it and any remaining question that could distinguish the possibilities.

### PSDA.7:1 - Problem frame

**Use this when** a point estimate, “high confidence” label, or model output makes a decision look more settled than its evidence permits. Also use it when a long uncertainty list does not say which unknown could reverse, narrow, defer, or invalidate the decision-support return.

Take a claim on which the inquiry relies. Vary its premise within the supported limits. Identify what changes in the consequence, eligibility, ordering or grounds for the conclusion. Report the result and any question the evidence leaves open.

Distinguish an uncertain consequence, an attributed belief, a model assumption, missing evidence and a disputed value. Identify the form and grounds appropriate to each. A common decision question need not give them a common scale.

If the question concerns only a source’s provenance or currentness, use `A.10` or the relevant source practice directly. Use an existing adequate uncertainty account within its scope. Measurement, forecasting, causal attribution and safety each need evidence appropriate to the particular claim.

### PSDA.7:2 - Problem

A numerical estimate can hide the conditions under which it is meaningful. An access model may estimate arrival time only when the road is open; a training study may concern an immediate test rather than later Work; an AI evaluation may concern a previous version or operating distribution. Averaging the results does not repair their missing applicability.

Conversely, a demand for certainty can stop every useful return. Some uncertainty cannot change the ordering, while another can show that all alternatives fail a protected condition. A useful account distinguishes those cases. It also separates a question that better evidence can answer from a disagreement about values or authority that evidence alone cannot settle.

### PSDA.7:3 - Forces

| Force | Tension |
| --- | --- |
| Qualification and action | A decision needs bounded support, not complete knowledge, while an unsupported premise can make action indefensible. |
| Probability and ignorance | Probabilities can represent uncertainty well when justified, while invented distributions hide model disagreement or lack of knowledge. |
| Reduction and relevance | A narrower estimate may strengthen a conclusion or answer a factual question even when the available action stays the same. Further precision can also leave the intended use unchanged. |
| Shared evidence and corroboration | Several sources can provide distinct support or merely repeat the same data and assumptions. |
| Stable comparison and changing conditions | Alternatives need a compatible basis, while source, holder, and environment changes can invalidate that basis. |

### PSDA.7:4 - Solution

Connect each material uncertainty to the claim or decision it can affect. Represent it on the available grounds, preserve dependencies and limits, and return the supported claim, a conditional answer or the specific question still open.

#### PSDA.7:4.1 - Identify the claim and the comparison at issue

Identify the subject, configuration, horizon, receiving question, any relevant alternatives and the claim at issue. Ask which premises affect its consequences, eligibility, relative standing or the strength of its grounds. If an alternative required for the question is unclear, identify the missing candidate information.

Use a `PSDA.3` model account where its evidence or assumptions bear on the configuration and horizon. A model can identify an uncertainty that it cannot resolve. A qualified direct source may already provide the missing premise.

Check absolute consequences where a requirement depends on them. A common uncertainty can leave the ranking fixed while revealing that none of the alternatives meets a required service or safety condition.

#### PSDA.7:4.2 - Represent the kind of uncertainty

Choose a form that answers the live question without claiming more knowledge than exists.

| Available basis | Useful representation | Limit that must remain visible |
| --- | --- | --- |
| Qualified stochastic model or elicited probabilistic judgement. | A distribution or probability statement tied to its event, population, conditions, and horizon. | Calibration, sampling, elicitation, model assumptions, and applicability still matter. Confidence in the analyst is not the event probability. |
| Supported bounds with no distribution. | An interval or set of admissible values. | Give the grounds for the bounds. Values outside the interval may be excluded, while a distribution within it or joint attainability with other quantities needs additional evidence. |
| Several materially different models or future conditions. | Conditional claims under named models or scenarios. | Their count or frequency in an ensemble does not supply real-world likelihood. |
| A decisive absent result or unrepresented mechanism. | The exact missing claim and the comparison it prevents. | A blank cell is neither zero effect nor equal performance. |
| Incompatible interpretations, preferences, or authority claims. | Attributed alternatives and the unresolved interpretation or judgement. | Statistical uncertainty reduction alone cannot reconcile them. |

Several forms may be useful in one account. Distinguish variation in a physical or behavioural process from uncertainty about a model, data or applicability where that difference matters to the finding.

Report what holds under each supported condition when its probability is unknown. If a calculation requires a probability distribution, identify the missing basis or calculate conditionally on explicitly stipulated probabilities. Equal scenario weights can serve a sensitivity calculation. Using them for an expected real-world result requires evidence for that distribution.

#### PSDA.7:4.3 - Qualify the relied-on claims

For a relied-on source result, identify its claim, subject, kind of result, edition or effective window, assumptions, evidence and relevant limits, including any dissent. Use `A.10` when the connection between source and use is unclear or the use requires a reproducible account of that connection and one is missing. Establish the subject claim and authority for any decision on their respective grounds.

Check that the evidence covers the relevant holder, intervention, environment and horizon. Distinguish observations, forecasts, expert judgements and extrapolations. To attribute an observed benefit to the intervention, use evidence that connects them.

Use a qualified result within its limits. If a material premise remains missing, identify the particular claim, bound, interpretation or test it would affect. Use `A.15.9` where an outside contribution is needed and worth obtaining, or return the limit.

#### PSDA.7:4.4 - Preserve dependency and model disagreement

Trace shared data, common causes, assumptions and dependencies where they affect the comparison. Treat repeated use of one dataset as a shared source. To combine independent or dependent judgements, state the aggregation Method, its assumptions and their fit.

Keep incompatible assumptions separate until a direct result supports their combination. For example, a scenario with a failed access route and a scenario with a functioning route can test different claims; combining their most favorable outcomes produces no realizable case. Ask what the recipient needs to infer from the remaining possibilities. Uncertainty about which participant will need help can leave the total needed known. To promise help by a deadline, preserve who can select the response and what they will know at that time. If either of two permitted calls can occur alone, providing for one call may suffice. If both can occur together, check the joint demand.

For disagreeing models, locate the overlapping claim and examine scope, input, representation, mechanism and evidence. Explain a mismatch where its source is established, or retain the distinct supported assumptions or models. A discriminating measurement can be worth obtaining when it would improve the intended result.

#### PSDA.7:4.5 - Form a discriminating question

Formulate an unanswered question where a different supported answer could matter to the current return. For example, a threshold question may take this form.

> For this subject and horizon, establish whether this premise lies inside the region supporting alternative A, outside it, or remains unresolved; state the evidence and limits needed for that use.

The requested result may concern eligibility rather than ranking. It may also show that no available alternative works, that a different formulation is needed, or that only a reversible analytical use is supported.

Identify an observation, calculation, interpretation or comparison that could answer the question, if one is available. Identify who can supply it and the time or access it needs where relevant. If no feasible inquiry can answer within the window, state the remaining limit.

Use `PSDA.9` for reversals and information priorities where that work is needed. For a choice about a probe, compare its attainable contribution and full burden. The authorized decision holder can use `C.11` to choose a feasible next step.

#### PSDA.7:4.6 - Return the strongest supported claim and no stronger

A short return states:

- what claim the evidence supports, for which subject, configuration and horizon, including any alternatives it compares;
- its uncertainty representation, source limits, and dependencies;
- what different answer could change the comparison, admissibility, or receiving use;
- any specific question or obstacle that remains; and
- any change in source, observation, candidate, value or configuration that would affect its intended use.

Return “unchanged within the tested bounds” only when those bounds cannot alter the stated result. Return a conditional or narrowed claim when support covers only part of the use. If a required protected-condition premise is unsupported, preserve the direct domain stop rather than compensating with confidence elsewhere.

An unexplained estimate can reveal the need for this work. For consequential reliance, use the evidence and assurance the relevant domain requires, including independent checks where applicable.

When the basis of a claim changes, revalidate the uses that depend on it. Use `G.11` for currentness and `A.10.1` when affected uses need discovery or a connected return. A known single dependency can be checked directly through `A.10`. Preserve independent claims whose basis still holds.

### PSDA.7:5 - Archetypal Grounding

#### PSDA.7:5.1 - Which flood-pump uncertainty matters now?

In the illustrative pre-season inquiry, nominal permanent and mobile capacity meets the assumed inflow only with the stated units operating. The model omits arrival delay. The team cannot turn that conditional result into “mobile service is reliable”.

| Relied-on or proposed claim | Evidence limit | Decision-linked return |
| --- | --- | --- |
| Nominal mobile capacity is adequate. | The capacity calculation assumes operating units on site. | Use for capacity only. It does not discriminate the missing deployment arrangement. |
| Mobile units can serve the district after road loss. | No qualified arrival and deployment result exists for that condition. | Keep M conditional for service. A qualified route-loss deployment result could close the gap. Seek it if the intended use warrants the effort. |
| The two technical models corroborate the inflow assumption. | Both use the same inflow dataset. | Record the shared evidence dependency. Independent corroboration would require a separate basis. |
| Pumping-service hours represent all affected residents' loss. | Reachable assistance and property protection have different meanings. | Return the missing consequence relation or keep separate accounts; a tighter inflow estimate will not settle the value question. |

A later qualified deployment result can narrow the arrival range and change the claims that depend on it. If the range includes conditions where service fails, identify the condition for robustness rather than asserting unconditional feasibility. A common power-supply uncertainty can leave all arrangements unqualified even where their relative order is fixed. Evidence of a common failure can establish that they all fail.

#### PSDA.7:5.2 - Development evidence with three different limits

For a ninety-day organization recommendation, suppose the adviser has an immediate human assessment, a queue model for the current team, and an offline AI benchmark. Each can inform a different bounded claim.

The human assessment does not establish retention or transfer to later service Work. The queue model does not establish the performance of a reallocated or mixed arrangement without its staffing and interaction premises. The benchmark does not establish current-version service reliability under the operating distribution and oversight arrangement.

Identify the separate questions about representative later work, service in the changed staffing arrangement and the version used under operating conditions. Seek a missing result if its attainable contribution to the recommendation or its grounds warrants the burden. Keep the three evidence limits separate.

#### PSDA.7:5.3 - A bounded input to SensorCo's strategic commitment

SensorCo's illustrative twelve-month question concerns defending devices, offering an integrated service, licensing data, or exiting a segment as generic AI inspection prices fall. The strategy team owns the strategic comparison; the board separately holds commitment authority.

Suppose the integrated-service direction depends on uncertain repeat demand and the licence depends on an unsettled permission question. State the demand conditions that could change the service comparison and identify the missing rights interpretation for licensing. Obtain the corresponding evidence or ruling when the intended use needs it.

`STR.11` can use this uncertainty result for the specified commitment and compatible horizon. Recheck affected uses if the alternative, claim, demand question, evidence window or commitment changes. For an unavailable or incompatible result, use a qualified direct source or report the remaining gap.

#### PSDA.7:5.4 - Cheap non-use

An analyst needs to recover which calibration edition a measurement cites, and no candidate comparison is being made. Use the source and evidence practice directly. A decision-linked uncertainty account would add no current result.

### PSDA.7:6 - Bias-Annotation

**Scope:** uncertainties that can change a bounded decision-support return. **Lenses:** **Epist** separates evidence and belief; **Prag** tests action-changing relevance; **Arch** exposes dependencies; **Gov** preserves direct authority and protected conditions; **Did** makes an unknown into a useful question.

Precision bias favors a number over an honest set or gap. Confidence rhetoric can substitute reputation for evidence. Model averaging can conceal shared errors. Certainty seeking can consume the entire decision window. Counter these with exact conditional claims and an explicit account of what a different answer would change.

### PSDA.7:7 - Conformance Checklist

- [ ] Each material uncertainty is linked to the claim, configuration, horizon and intended use, including the affected alternatives where relevant.
- [ ] The account examines eligibility, shared failure or a ranking change where it affects the claim in question.
- [ ] Probabilities, intervals, scenarios, missing results, and disputes retain their different meanings.
- [ ] Every probability or bound has an adequate basis; scenario counts are not probabilities by default.
- [ ] Source, holder, intervention, and environment limits accompany relied-on evidence.
- [ ] Shared evidence, common causes, and incompatible model assumptions remain visible.
- [ ] A proposed inquiry identifies the result it could supply and its attainable conditions. If no inquiry is feasible in time, the account gives the outstanding limit.
- [ ] The result states the conclusion within its evidential scope or the condition that prevents a conclusion.
- [ ] Direct assurance, permission, and choice are not inferred from an uncertainty account.
- [ ] Changed sources reopen only affected uses, with their own subject judgements.

### PSDA.7:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Confidence is eighty percent.” | Say whose judgement, about which proposition, under what evidence and probability interpretation. |
| Give three scenarios equal probability because three were drawn. | Retain scenario-conditional claims until a distribution is justified. |
| Average incompatible model outputs. | Locate the disputed proposition and keep the alternative assumptions or exact gap. |
| Discard uncertainty common to all candidates. | Check whether it changes absolute admissibility or shows that all fail. |
| Commission more data without a decision question. | State which possible answer could change the comparison or its use. |
| Replace missing holder evidence with another holder’s success. | Use evidence of transfer or applicability to the receiving holder. Seek a missing qualified result when warranted, or give the limit. |

### PSDA.7:9 - Consequences

The recipient can see what the evidence supports and which issues remain consequential. A bound or set may convey less numerical precision than a single estimate while identifying what the evidence leaves open. Refine it when the attainable gain for the receiving task warrants the effort.

### PSDA.7:10 - Rationale

Uncertainty matters through its effect on a decision claim, not through its size alone. Preserving the source, representation, and dependency of each premise makes that effect inspectable. A bounded unknown can support useful inquiry without pretending to supply the missing fact or the eventual choice.

### PSDA.7:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| When should uncertainty be probabilistic, and when should alternatives remain conditional? | Use qualified probabilistic analysis where its premises hold; retain multiple plausible conditions when decision-relevant probabilities or models are unsettled. | Predict-then-act under one agreed forecast, or reject all probabilistic reasoning whenever uncertainty is difficult. | **Adapt:** :4.1–:4.4 select a representation from its evidence and test consequential shared failure. Compare further scenarios when a single forecast could conceal a consequential difference in eligibility, exposure or the conclusion requested. | Lempert et al.'s [2024 DMDU/IPCC analysis](https://doi.org/10.3389/fclim.2024.1380054) is the synthesis candidate for decision relevance despite low-confidence knowledge. It does not make scenarios equiprobable or provide a universal uncertainty taxonomy or local risk threshold. | Reopen when a qualified distribution becomes available, model disagreement changes, or an omitted future defeats the claimed bounds. |
| Which missing evidence deserves a question? | Connect elicitation, sensitivity, and information acquisition to the alternatives and consequences they can change. | Rank unknowns by variance or confidence alone. | **Adapt:** :4.5–:4.6 require a discriminating question before further inquiry. The practical trade-off is less general data collection for a more explicit decision boundary. | Borgonovo et al.'s [2026 review](https://doi.org/10.1016/j.ejor.2025.05.023) supplies the current decision-analysis connection among uncertainty, sensitivity, and information value. It is a synthesis, not validation of PSDA's particular evidence or a universal probe rule. `A.10` supplies only bounded reliance; the authorized holder can use `C.11` for a local choice about a probe. | Reopen if another unknown can change eligibility, a model revision changes the discriminator, or no feasible inquiry fits the decision window. |

### PSDA.7:12 - Relations

- `PSDA.3` may supply model evidence and assumptions for the same configuration and horizon. Representation alone establishes neither the subject condition nor this uncertainty judgement.
- `PSDA.8` may use the bounded claims and questions where they change its consequence comparison. Evidence neither entails that result nor authorizes the later decision.
- `STR.11` may use a supplied decision-linked uncertainty result where it informs the strategic commitment comparison or its grounds. The result carries its own scope and horizon; it imports neither the whole PSDA practice nor strategic facts or authority.
- `A.10` addresses reliance on a claim, and `A.15.9` the use of an outside contribution. `G.11` addresses the currentness of a maintained result. Use `A.10.1` where affected uses need discovery or a connected return.
- `PSDA.9` addresses robustness and information priorities. Use `C.11` where the authorized holder needs to choose a probe or another action. Use a qualified source for a missing or incompatible premise, or state the particular gap.

### PSDA.7:End
