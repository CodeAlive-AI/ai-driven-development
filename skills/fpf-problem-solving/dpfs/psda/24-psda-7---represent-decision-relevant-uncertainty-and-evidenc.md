## PSDA.7 - Represent Decision-Relevant Uncertainty and Evidence Limits

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** **bounded decision claims and unresolved discriminating questions**: what the evidence supports about the live alternatives, what could change that comparison, and which uncertainty cannot presently be resolved.

### PSDA.7:1 - Problem frame

**Use this when** a point estimate, “high confidence” label, or model output makes a decision look more settled than its evidence permits. Also use it when a long uncertainty list does not say which unknown could reverse, narrow, defer, or invalidate the decision-support return.

Take one relied-on claim and ask: if this claim were different within its supported limits, what would change about these alternatives or their admissibility? State the supported claim and the remaining question together. The gain is a useful uncertainty account.

The governed object is that decision-linked account. A claim about an uncertain consequence, an attributed belief, a model assumption, missing evidence, and a disputed value are different inputs. Their relevance to one decision does not turn them into one probability or a common confidence score.

**Do not use this pattern** when the only question is a source's provenance or currentness and no decision-support comparison changes; use `A.10` or the direct source practice. If the uncertainty account already supports the present use, reuse it. Direct domain practices retain their own measurement, forecasting, causal, safety, and evidential conclusions.

### PSDA.7:2 - Problem

A numerical estimate can hide the conditions under which it is meaningful. An access model may estimate arrival time only when the road is open; a training study may concern an immediate test rather than later Work; an AI evaluation may concern a previous version or operating distribution. Averaging the results does not repair their missing applicability.

Conversely, a demand for certainty can stop every useful return. Some uncertainty cannot change the ordering, while another can show that all alternatives fail a protected condition. A useful account distinguishes those cases. It also separates a question that better evidence can answer from a disagreement about values or authority that evidence alone cannot settle.

### PSDA.7:3 - Forces

| Force | Tension |
| --- | --- |
| Qualification and action | A decision needs bounded support, not complete knowledge, while an unsupported premise can make action indefensible. |
| Probability and ignorance | Probabilities can represent uncertainty well when justified, while invented distributions hide model disagreement or lack of knowledge. |
| Reduction and relevance | More information may narrow an estimate without changing any available decision. |
| Shared evidence and corroboration | Several sources can provide distinct support or merely repeat the same data and assumptions. |
| Stable comparison and changing conditions | Alternatives need a compatible basis, while source, holder, and environment changes can invalidate that basis. |

### PSDA.7:4 - Solution

Connect each material uncertainty to the exact claim and decision it can change. Use a representation justified by the available knowledge, retain dependencies and limits, and return a bounded claim, discriminating question, narrowed use, or blocker.

#### PSDA.7:4.1 - Start from a comparison that could change

Name the subject, configuration, horizon, receiving question, considered alternatives, and result currently being claimed. Ask which premise could change their consequences, relative standing, eligibility, or the need for a probe. If the alternatives themselves are unclear, return that candidate question.

Use `PSDA.3`'s model account only where its evidence or assumptions bear on this same configuration and horizon. The model can expose an uncertainty without resolving it. A current qualified direct result can supply the same premise without requiring a model-building exercise.

Check both relative and absolute consequences. An uncertainty shared by all alternatives can leave their order unchanged yet show that none meets a required service or safety condition. Do not dismiss it as irrelevant merely because it is not a ranking discriminator.

#### PSDA.7:4.2 - Represent what is unknown at its actual kind

Choose a form that answers the live question without claiming more knowledge than exists.

| Available basis | Useful representation | Limit that must remain visible |
| --- | --- | --- |
| Qualified stochastic model or elicited probabilistic judgement. | A distribution or probability statement tied to its event, population, conditions, and horizon. | Calibration, sampling, elicitation, model assumptions, and applicability still matter. Confidence in the analyst is not the event probability. |
| Supported bounds but no distribution. | An interval or set of admissible values. | An interval is not a uniform distribution; state what supports its endpoints and what lies outside its claim. |
| Several materially different models or future conditions. | Conditional claims under named models or scenarios. | Their count or frequency in an ensemble does not supply real-world likelihood. |
| A decisive absent result or unrepresented mechanism. | The exact missing claim and the comparison it prevents. | A blank cell is neither zero effect nor equal performance. |
| Incompatible interpretations, preferences, or authority claims. | Attributed alternatives and the unresolved interpretation or judgement. | Statistical uncertainty reduction alone cannot reconcile them. |

These are use choices. Different forms may coexist in one account. Distinguish a physical or behavioral variability claim from uncertainty about its model, data, or applicability whenever the distinction changes the return.

If a probability is useful but unsupported, state the conditional comparison it would enable and identify the needed basis. Do not assign equal probabilities to scenarios simply to make an expected-value calculation run.

#### PSDA.7:4.3 - Qualify the relied-on claims

For each decision-bearing source result, keep the claim, subject, supplying result kind, source edition or effective window, assumptions, evidence, intended use, exclusions, and material dissent recoverable. Use `A.10` when the source-to-use account remains implicit or a needed reproducible account is missing; its disposition does not establish the source claim's truth or authorize the decision.

Ask whether the evidence concerns the same holder, intervention, environment, and horizon. Separate observed results, forecasts, expert judgements, and unsupported extrapolations. An observation of a benefit is not automatically a causal effect; the direct causal or domain Method supplies that support.

Use an already-qualified result within its limit. If a consequential cross-practice result is still missing, `A.15.9` supports the smallest request or blocker. Do not ask another practice to “remove the uncertainty”; ask for the specific claim, bound, interpretation, or test that could change this comparison.

#### PSDA.7:4.4 - Preserve dependency and model disagreement

Recover shared data, common causes, conditional assumptions, and other dependencies when they affect the consequence comparison. Evidence repeated by several models is not several independent confirmations. Expert or model aggregation needs its own justified Method; the number of voices alone does not determine a probability.

Keep incompatible assumptions separate until a direct result supports their combination. For example, a scenario with a failed access route and a scenario with a functioning route can test different claims; combining their most favorable outcomes produces no realizable case.

Where alternative models disagree, identify the overlapping proposition and what explains the difference: scope, input, representation, mechanism, or unresolved evidence. A new measurement may discriminate the models; sometimes the honest answer is that the present use must retain both. Do not turn disagreement into a narrow average solely because a downstream table expects one number.

#### PSDA.7:4.5 - Form a discriminating question

Write the question in terms of its possible consequences for the current return:

> For this subject and horizon, establish whether this premise lies inside the region supporting alternative A, outside it, or remains unresolved; state the evidence and limits needed for that use.

The requested result may concern eligibility rather than ranking. It may also show that no available alternative works, that a different formulation is needed, or that only a reversible analytical use is supported.

Name a feasible observation, calculation, interpretation, or comparison that might answer the question, its supplying practice, and the relevant time or access limit. If no feasible inquiry can answer before the decision window closes, say so. Do not promise that more data will settle structural ignorance.

This pattern identifies decision-linked questions. `PSDA.9` can later examine reversals and information priorities; `C.11` or the direct choice owner decides whether an actual next probe is worth its cost and authorized. A question with high uncertainty is not automatically the best probe.

#### PSDA.7:4.6 - Return the strongest supported claim and no stronger

A short return states:

- what claim about which alternatives is supported, for which configuration and horizon;
- its uncertainty representation, source limits, and dependencies;
- what different answer could change the comparison, admissibility, or receiving use;
- the exact unanswered question or blocker; and
- what source, observation, candidate, value, or configuration change would reopen the account.

Return “unchanged within the tested bounds” only when those bounds cannot alter the stated result. Return a conditional or narrowed claim when support covers only part of the use. If a required protected-condition premise is unsupported, preserve the direct domain stop rather than compensating with confidence elsewhere.

Recognition may begin with one unexplained estimate. Consequential reliance requires the evidence and assurance demanded by the direct practice, including its independent checks when applicable.

When a relied-on source actually changes, revalidate the affected use. Use `G.11` for a currentness question and `A.10.1` when the changed claim must be traced through several actual uses. Do not discard unrelated claims merely because they share a source file.

### PSDA.7:5 - Archetypal Grounding

#### PSDA.7:5.1 - Which flood-pump uncertainty matters now?

In the illustrative pre-season inquiry, nominal permanent and mobile capacity meets the assumed inflow only with the stated units operating. The model omits arrival delay. The team cannot turn that conditional result into “mobile service is reliable”.

| Relied-on or proposed claim | Evidence limit | Decision-linked return |
| --- | --- | --- |
| Nominal mobile capacity is adequate. | The capacity calculation assumes operating units on site. | Use for capacity only. It does not discriminate the missing deployment arrangement. |
| Mobile units can serve the district after road loss. | No qualified arrival and deployment result exists for that condition. | Ask for the route-loss deployment result; M remains conditional for the service comparison. |
| The two technical models corroborate the inflow assumption. | They reuse the same inflow dataset. | Retain one shared evidence dependency, not two confirmations. |
| Pumping-service hours represent all affected residents' loss. | Reachable assistance and property protection have different meanings. | Return the missing consequence relation or keep separate accounts; a tighter inflow estimate will not settle the value question. |

If a direct deployment result later supports a bounded arrival range, the account changes only the affected claim and its uses. If the range still spans service failure, the result is a discriminating question for robustness, not an unconditional feasibility claim. If all arrangements share an unsupported power-supply assumption, that common uncertainty can invalidate all of them even while their relative order stays fixed.

#### PSDA.7:5.2 - Development evidence with three different limits

For a ninety-day organization recommendation, suppose the adviser has an immediate human assessment, a queue model for the current team, and an offline AI benchmark. Each can inform a different bounded claim.

The human assessment does not establish retention or transfer to later service Work. The queue model does not establish the performance of a reallocated or mixed arrangement without its staffing and interaction premises. The benchmark does not establish current-version service reliability under the operating distribution and oversight arrangement.

The return names three possible supplier questions at their own grain: representative later-Work capability, changed-arrangement service consequences, and exact-version operating evaluation. Only questions that could change the live recommendation are pursued. Averaging the three “confidence” labels would repair none of these gaps.

#### PSDA.7:5.3 - A bounded input to SensorCo's strategic commitment

SensorCo's illustrative twelve-month question concerns defending devices, offering an integrated service, licensing data, or exiting a segment as generic AI inspection prices fall. The strategy team owns the strategic comparison; the board separately holds commitment authority.

Suppose the integrated-service direction relies on an uncertain repeat-demand claim, while the licensing direction relies on a still-unqualified permission premise. The PSDA return names the repeat-demand conditions that could alter the service comparison and the exact rights interpretation missing for licensing. It supplies neither the strategic facts nor a permission judgement by itself.

Under the decision-linked uncertainty relation, `STR.11` may use the supplied result only for this commitment and compatible horizon. A changed alternative, claim scope, demand question, evidence window, or commitment reopens that use. If the result is unavailable or incompatible, the strategic receiver uses a qualified direct source or keeps the exact gap.

#### PSDA.7:5.4 - Cheap non-use

An analyst needs to recover which calibration edition a measurement cites, and no candidate comparison is being made. Use the source and evidence practice directly. A decision-linked uncertainty account would add no current result.

### PSDA.7:6 - Bias-Annotation

**Scope:** uncertainties that can change a bounded decision-support return. **Lenses:** **Epist** separates evidence and belief; **Prag** tests action-changing relevance; **Arch** exposes dependencies; **Gov** preserves direct authority and protected conditions; **Did** makes an unknown into a useful question.

Precision bias favors a number over an honest set or gap. Confidence rhetoric can substitute reputation for evidence. Model averaging can conceal shared errors. Certainty seeking can consume the entire decision window. Counter these with exact conditional claims and an explicit account of what a different answer would change.

### PSDA.7:7 - Conformance Checklist

- [ ] Each material uncertainty is linked to a claim, alternatives, configuration, horizon, and receiving use.
- [ ] The account tests eligibility and shared failure as well as ranking changes.
- [ ] Probabilities, intervals, scenarios, missing results, and disputes retain their different meanings.
- [ ] Every probability or bound has an adequate basis; scenario counts are not probabilities by default.
- [ ] Source, holder, intervention, and environment limits accompany relied-on evidence.
- [ ] Shared evidence, common causes, and incompatible model assumptions remain visible.
- [ ] Each proposed inquiry names a result that could change the return and a feasible limit or honest inability.
- [ ] The disposition is bounded, conditional, narrowed, or blocked as the actual support requires.
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
| Replace missing holder evidence with another holder's success. | Request the exact transfer or applicability result; retain the blocker if it is unavailable. |

### PSDA.7:9 - Consequences

The recipient can see what is known well enough for this decision and which unknown deserves attention. Some numerical precision is lost, but unsupported certainty is removed. The work can become smaller: once an uncertainty cannot change the bounded return, further refinement needs another justification.

### PSDA.7:10 - Rationale

Uncertainty matters through its effect on a decision claim, not through its size alone. Preserving the source, representation, and dependency of each premise makes that effect inspectable. A bounded unknown can support useful inquiry without pretending to supply the missing fact or the eventual choice.

### PSDA.7:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| When should uncertainty be probabilistic, and when should alternatives remain conditional? | Use qualified probabilistic analysis where its premises hold; retain multiple plausible conditions when decision-relevant probabilities or models are unsettled. | Predict-then-act under one agreed forecast, or reject all probabilistic reasoning whenever uncertainty is difficult. | **Adapt:** :4.1–:4.4 select the representation by the actual basis and test shared failure. Additional scenario work is accepted only when one forecast could conceal a material reversal. | Lempert et al.'s [2024 DMDU/IPCC analysis](https://doi.org/10.3389/fclim.2024.1380054) is the synthesis candidate for decision relevance despite low-confidence knowledge. It does not make scenarios equiprobable or provide a universal uncertainty taxonomy or local risk threshold. | Reopen when a qualified distribution becomes available, model disagreement changes, or an omitted future defeats the claimed bounds. |
| Which missing evidence deserves a question? | Connect elicitation, sensitivity, and information acquisition to the alternatives and consequences they can change. | Rank unknowns by variance or confidence alone. | **Adapt:** :4.5–:4.6 require a discriminating question before further inquiry. The practical trade-off is less general data collection for a more explicit decision boundary. | Borgonovo et al.'s [2026 review](https://doi.org/10.1016/j.ejor.2025.05.023) supplies the current decision-analysis connection among uncertainty, sensitivity, and information value. It is a synthesis, not validation of PSDA's particular evidence or a universal probe rule. `A.10` supplies only bounded reliance; `C.11` retains actual local probe choice. | Reopen if another unknown can change eligibility, a model revision changes the discriminator, or no feasible inquiry fits the decision window. |

### PSDA.7:12 - Relations

- `PSDA.3` may supply model evidence and assumptions for the same configuration and horizon. Representation alone establishes neither the subject condition nor this uncertainty judgement.
- `PSDA.8` may use the bounded claims and questions where they change its consequence comparison. Evidence neither entails that result nor authorizes the later decision.
- `STR.11` may use a supplied decision-linked uncertainty result only where it can change the strategic commitment comparison. The result carries its own scope and horizon; it imports neither the whole PSDA practice nor strategic facts or authority.
- `A.10` governs claim-bound evidence and reliance; `A.15.9` governs a needed outside-practice request or use. `G.11` and, for several actual changed uses, `A.10.1` govern currentness and affected-use revalidation.
- `PSDA.9` owns the distinct robustness and information-priority question. `C.11` or the direct decision owner governs an actual probe or choice. Missing, stale, or incompatible inputs remain exact gaps unless a qualified direct result supplies them.

### PSDA.7:End
