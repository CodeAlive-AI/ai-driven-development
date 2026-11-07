## PSDA.6 - Represent Values and Trade-Offs

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** a **decision-usable value account**: attributed concerns and objectives, their consequence measures, protected conditions, admitted trade-offs, unresolved disagreements, and limits for one named comparison.

### PSDA.6:1 - Problem frame

**Use this when** a scorecard's criteria came from a template, “importance” weights have no stated meaning, or the same benefit appears under several headings. Also use it when people agree that reliability, development, safety, or fairness matters but mean different consequences for different subjects, or when their consequence comparisons still need to become a justified numerical model.

Begin with one concern: important to whom, about which subject and situation, and why? Trace it to a consequence that could distinguish the live alternatives. Then state how that consequence will be represented and whether it may be traded against another. The gain is a comparison whose value assumptions can be understood and challenged.

The governed object is the value account for that comparison. An objective expresses what is wanted; a measure describes a characteristic; a preference orders consequences; a protected condition limits permissible trade-offs. They can be related without becoming the same thing. Neither an expressed preference nor a numerical weight supplies authority to waive a duty or another person's rights.

**Do not use this pattern** when a current, qualified value account already answers the exact comparison question. Use the direct measurement practice for a missing measurement alone, the appropriate authority or domain practice for a condition's current force, and `C.11.DUA` for a disputed requirement's justification. Use the authorized choice owner for the later decision. This pattern does not determine universally correct values.

### PSDA.6:2 - Problem

Criteria can appear neutral while deciding the result. “Install more pumps” embeds an action in an objective. “Service quality” may count the same avoided outage again under reliability, satisfaction, and reputation. Equal weights may silently favor the concern represented by the largest number of criteria.

Numbers can conceal a second substitution. A budget amount, a probability, an ordinal judgement, and a protected condition become interchangeable entries in a spreadsheet. Normalizing each to zero–one does not establish comparable value. A mean of participants' weights can erase a disagreement about who bears the consequence or what may be traded at all.

### PSDA.6:3 - Forces

| Force | Tension |
| --- | --- |
| Completeness and usability | Material values must remain visible, while an enormous hierarchy burdens elicitation and repeats consequences. |
| Measurement and meaning | Observable measures help comparison, while easily measured proxies can displace the actual concern. |
| Trade-offs and protection | Some sacrifices are legitimate within the question; others require a separate authority or are outside permissible compensation. |
| Individual and collective values | A common comparison is useful, while unlike participants need not share one value function. |
| Precision and honest incompleteness | Explicit scales and preference questions can clarify a choice, while unsupported weights create false precision. |

### PSDA.6:4 - Solution

Recover the values behind the decision, organize them around consequences, and declare only the measurement and trade-off structure that the receiving comparison can support. Keep unresolved preferences and protected conditions visible rather than completing a score by assumption.

#### PSDA.6:4.1 - Recover whose concern changes the comparison

Name the subject, affected people or Systems, configuration, horizon, and receiving question. Use `PSDA.12`'s participation and concern account where it supplies relevant attributed concerns, duties, interests, missing voices, or representation limits. That input is not already a value model or a mandate to aggregate preferences.

For each material concern, ask who expresses or bears it, what consequence matters, and under what conditions. Recover an actual assignment, local system-role classification, or authority relation only where the concern's meaning or governing force depends on it. A title such as resident, manager, or expert does not establish representation or decision rights.

If a needed concern or binding condition is unavailable, use a qualified direct source or return the exact gap. Do not treat non-response as indifference. Distinguish participants' current statements from the analyst's proposed interpretation and from an established obligation.

#### PSDA.6:4.2 - Distinguish ends, means, and repeated consequences

Ask “Why does this matter here?” to identify the consequence sought. Ask “How might it be achieved?” to expose possible means. “Provide training” may be one means; reliable performance in representative later Work may be the relevant end. The distinction is local to the question: a process experience can itself be valued when participants actually care about it.

Organize objectives only as far as the structure helps. For a small decision, a few attributed statements may be enough. A hierarchy or means–ends map is useful when several levels or overlaps would otherwise be lost.

Test apparent duplicates through their meaning and consequence path. Avoid counting one consequence twice under different names. But statistical correlation alone is not duplication: service loss and distribution of that loss can remain different values even when their observed measures covary. Conversely, statistical independence does not prove that a preference model may add the values.

Retain an objective only if it represents a material value, protected condition, or decision-changing distinction. When simplifying, state the lost distinction and check that it cannot reverse the intended comparison. Do not delete a concern merely because it is difficult to measure.

#### PSDA.6:4.3 - Give each measure a usable meaning

For every consequential measure, state the characteristic, subject or participant tuple, scale and unit where applicable, direction of preference, horizon, source, and missingness rule. Distinguish a direct measure from a proxy and say what the proxy cannot establish.

Use `C.16` for measurement and `A.19` when a declared multi-characteristic space or reusable predicate is needed. A.19 supplies coordinate and scale meanings; it does not perform scoring, aggregation, comparison, or selection.

Keep raw consequence descriptions alongside any value transformation that the comparison uses. A performance scale and a value scale answer different questions. If an ordinal judgement is used, preserve its ordering without assuming equal intervals or averaging categories. If a numerical value function is used, state the consequence range, anchors, interpolation or shape, and the elicitation basis that makes the transformation meaningful.

#### PSDA.6:4.4 - Separate conditions from compensable objectives

Identify which conditions are binding, which are aspirations, and which are uncertain claims requiring a competent result. Record the source and use of each condition. A participant's request for a minimum service level is a value claim; a separately established legal or safety requirement has its own governing basis.

Do not compensate for a failed protected condition by adding benefits elsewhere. If its meaning, applicability, or authority is disputed, retain that dispute and ask for the exact interpretation rather than choosing a convenient threshold. A comparison may proceed on an explicitly narrower slice while the whole-decision conclusion remains blocked.

When the live question is whether the requirement itself should be retained or changed, use `C.11.DUA` §4.3 with the competent domain contribution. Identify the protected person or System and interest, unwanted outcome, governed quantity or activity, conditions and horizon. Distinguish background, attributable increment and total exposure where they affect the judgement. Examine the causal and measurement basis, uncertainty, threshold or precision choice, marginal protection, full burden and displaced protective work. Compare retention, tightening, revision, replacement or removal only where they are meaningful alternatives. A safety label does not supply that basis, and expense alone does not defeat a protective requirement.

Return the supported requirement recommendation and the reason or limit the recipient needs, together with its present force, amendment authority and feasible time window. The appraisal can finish even when amendment is unavailable; the currently binding condition still constrains action. State a resulting impasse when no acceptable alternative or timely amendment is feasible. A later correction does not restore an already lost opportunity. Use this return only for the disputed requirement; an adequate ordinary value account needs no new appraisal.

Some thresholds are preference choices rather than prohibitions: an aspiration level, budget preference, or tolerated inconvenience. Say which they are and whose judgement they express. A threshold crossing is not automatically a decision or permission to act.

#### PSDA.6:4.5 - Construct preferences from comparisons of consequences

Ask the value holder to compare concrete consequence profiles, with the same people, horizon and conditions in view. Record whether one profile is **no worse**, **strictly better**, or **indifferent** to another, or whether the holder leaves the comparison open. Retain the profiles and the reason given. An open comparison imposes no equality. Use actual alternatives or understandable hypothetical profiles within the declared ranges; a fictitious combination is useful only if the holder can judge its meaning.

Sections 4.5.1–4.5.5 construct preferences over known consequences. Section 4.5.6 develops a finite expected-utility branch when the receiving comparison concerns uncertain outcomes: it obtains lottery judgements, retains all compatible utility functions and connects them to the consequence probabilities. Choose the form from the holder's comparisons and the distinctions the receiving work needs; deterministic trade-offs alone do not determine preferences over uncertain outcomes.

##### PSDA.6:4.5.1 - Choose and challenge the representation

Separate protected conditions under §4.4 before considering compensation. Then ask what the preference must preserve. Choose the least burdensome form that preserves the distinctions needed by the receiving comparison. These are usable alternatives, not stages every decision must pass through:

| Available judgement and intended use | Construction and return |
| --- | --- |
| Only directions of improvement and some pairwise comparisons are justified. | Keep those comparisons and coordinate dominance. Infer further comparisons only through an admitted rule, such as transitivity. Return the resulting partial relation and the pairs still open. |
| A priority or threshold is explicitly noncompensatory. | Write and apply that rule, including its order and tie treatment. For example, prefer every profile with waiting time at most two hours to every profile above two hours, then prefer lower cost within each class. This is a preference rule only if the holder says so; its threshold does not become a duty. |
| Improvements can compensate for one another, with constant value increments and a constant exchange over the stated ranges. | Construct the affine family in §4.5.2. Its coefficients express the admitted exchange, not the importance of criterion names. |
| Compensation is acceptable but marginal values may curve. | Test the additive assumption and use the finite-level construction in §4.5.3 when it fits. Preserve interactions through a suitable non-additive family or explicit rules when addition fails. A qualified outranking Method can instead supply a relation with incomparability; its thresholds and aggregation conditions must be supplied with it. |

For a proposed additive form, compare profiles that differ on a subset of criteria while holding the others equal. Repeat the comparison at materially different common levels of those other criteria. A reversal challenges preferential independence: the preference over that subset depends on its background. Ask also about complementarities, thresholds and refusals to compensate. With two criteria, unchanged directions of preference alone give little support for addition; ask about the exchanges themselves. Statistical independence of measurements answers neither question.

For an affine form, ask the stronger question: does the holder value the same physical increment equally at different positions on each scale, and does the compensating amount remain the same at different starting profiles? Within a one-to-five-hour range, compare reducing two hours to one with reducing five hours to four, and repeat a cost-for-time exchange at a different cost level. A stated constant exchange is a substantive modelling assumption over that range. Finite elicitation can challenge it and check its local fit; it does not prove a universal preference law. Preserve that qualification when the assumption is accepted for use, and return the unresolved form choice when it is not.

Keep materially different holders' accounts separate. Combining them requires a legitimately governed aggregation or reconciliation Method. Neither averaging nor choosing the sponsor's account follows from the construction below.

##### PSDA.6:4.5.2 - Construct a family for a constant exchange

Suppose lower cost `c` and lower waiting time `t` are preferred, both matter, and the holder accepts the affine conditions above on the named ranges. Represent loss by `L(c,t) = a c + b t`, with `a > 0` and `b > 0`; lower loss is preferred. A common constant and positive scale do not change the ordering. Divide by `a` to obtain `L_r(c,t) = c + r t`, where `r = b/a > 0`. The unit of `r` is cost units per hour. It belongs to this holder and use, rather than being a measured market price.

For each statement that profile `(c_x,t_x)` is no worse than `(c_y,t_y)`, write `c_x + r t_x <= c_y + r t_y`. Use equality for stated indifference and a strict inequality for stated strict preference. Keep every statement on the same `r` and intersect its restrictions with `r > 0`. The resulting set `R` describes every admitted exchange in this form. A point selected for a convenient spreadsheet is additional preference information unless the holder actually supplied it.

Ranges still matter when scales are normalized. If the cost range is 20–60 thousand and the waiting range is 1–5 hours, normalized losses are `(c-20)/40` and `(t-1)/4`. A weighted sum with positive weights `w_c + w_t = 1` represents the same exchange only when `r = 10 w_t/w_c`. The weights compare the two whole range changes. A different range changes that correspondence; a change in the holder's marginal values can require a different function as well. Unit conversion alone must leave the represented comparisons unchanged.

##### PSDA.6:4.5.3 - Retain unknown marginal values when linearity is unwarranted

For a finite comparison with an admitted additive form, use the distinct consequence levels appearing in the reference profiles and live alternatives. Order each criterion's levels from least to most preferred. Assign an unknown value contribution `q_i(z)` to each level `z` of criterion `i`. Set the least preferred contribution on each criterion to zero, require the contributions to be nondecreasing along that criterion, and set the sum of the most preferred contributions to one. This normalization requires at least one valued improvement across the represented ranges; it fixes an arbitrary origin and unit without fixing relative criterion values. If the holder is indifferent across every represented profile, return that relation directly. If whether any difference matters is unresolved, retain that gap rather than normalizing it away.

Define `U(x) = sum_i q_i(x_i)`, with higher value preferred. Each no-worse statement `x` versus `y` adds `U(x) >= U(y)`; indifference adds equality; strict preference adds `U(x) > U(y)`. Add elicited bounds or comparisons of value differences only with their own meaning and source. All rows constrain the same contributions. Solving them jointly supplies a family of additive value functions, rather than independently chosen intervals for each criterion. Weak monotonicity permits a flat contribution; require strict increase only where the holder's judgement supports it.

This construction leaves unevaluated levels open. Add a new level with its monotonicity and preference constraints, or use an explicitly justified interpolation. Equal spacing on an ordinal performance scale is not equal spacing in value. A family that is feasible at the represented levels establishes compatibility there; use beyond them needs the stated shape or new elicitation.

The constraints are linear in the unknown contributions. Use direct algebra for a small family or a linear-programming solver for the finite system. When strict comparisons are present, a solver can replace each strict difference by a common positive slack `epsilon` and maximize that slack under the normalization: a feasible result with `epsilon > 0` witnesses joint strictness. A fixed arbitrary margin can exclude compatible models. Preserve weak equalities and numerical error limits when interpreting a computation. `MMP.10` and `MMP.11` supply the general formulation, representation and obtaining-method work; the consequence meanings and preference assumptions supplied here govern this instance.

##### PSDA.6:4.5.4 - Distinguish an open answer from a failed construction

First check whether at least one model satisfies the joint constraints. For a small interval family, exhibit an admitted parameter; for a larger system, obtain a feasible witness or a justified infeasibility result. A solver timeout leaves this question unanswered.

If the family is empty, locate a conflicting subset of the elicited rows and form assumptions. Check transcription, units, profile meanings and attribution with the holder. Two opposite weak comparisons may express indifference; they are not a contradiction. A strict preference for `x` over `y` together with `y` no worse than `x` under the same conditions conflicts with the claimed preference relation. Other failures can arise because the chosen form cannot express otherwise coherent judgements. Do not resolve either failure by silently deleting a row or returning the best fitting weights. Revise a judgement only with its holder, change the form with an explicit basis, or return the unresolved conflict. An approximate fit needs an admitted error interpretation before it can support advice.

For a **nonempty** family, distinguish what all compatible models support from what at least one supports:

- `x` is **necessarily no worse** than `y` when every compatible model gives that weak preference.
- `x` is **possibly no worse** than `y` when at least one compatible model gives it.

Test these claims on the joint family. For the loss family, necessary preference requires `L_r(x) <= L_r(y)` for every `r` in `R`; a possible preference needs one such `r`. A proof over the range establishes necessity; one feasible witness establishes possibility and one contrary witness defeats necessity. Use `MATH.20` for the required whole-domain bound. Separate strict preference from equality at a boundary. An empty family warrants neither kind of recommendation.

If the question asks for a best alternative, keep the quantifiers together. A necessary best is no worse than every rival in every compatible model. A possible best is no worse than every rival in **one and the same** compatible model. Separate pairwise witnesses against different rivals do not establish possible best. Return a common best when supported, the condition-dependent alternatives otherwise, or the precise comparison gap. No probability distribution over the compatible models is implied.

##### PSDA.6:4.5.5 - Reopen only what the changed judgement affects

A further judgement by the same holder on the same profiles adds a constraint to the existing family. Intersect, check nonemptiness again, and recalculate the dependent comparisons. A correction replaces its old row and every restriction derived from it; retaining the superseded row could manufacture a conflict. Preserve consequence measurements, protected conditions and comparisons whose grounds remain valid.

A changed holder, horizon, range, consequence meaning or compensation rule can invalidate the representation itself. Reconsider that premise before intersecting parameters in the old form. State which results depend on it and which remain usable. Stop when the receiving comparison is settled to the needed strength or the missing judgement, form or authority is clear enough to obtain.

##### PSDA.6:4.5.6 - Construct preferences over finite uncertain outcomes

Use this branch when the comparison needs a preference between uncertain consequences and the holder accepts an expected-utility representation for the stated use. A *lottery* here is a probability distribution over described consequences; eliciting it means asking about those distributions, not exposing anyone to an actual gamble. Start with the consequence meanings, the holder and the receiving decision. An outcome can be a complete profile of cost, delay and service, rather than one numerical score.

**Choose the representation before estimating it.** Expected utility evaluates a lottery `P` by `sum_x P(x) u(x)`. Its utility values describe the holder's comparisons of lotteries. A function that merely orders certain outcomes need not do that: any increasing transformation preserves a certain-outcome ordering, but generally changes the ordering of expected values.

Ask whether mixing each of two compared lotteries with the same third lottery, in the same proportions, should preserve the comparison. For example, if L is preferred to M, would the holder retain that preference between a half chance of L plus a half chance of H and a half chance of M plus a half chance of H? Challenge this premise with material cases, including a move from certainty to a chance of failure. Ask whether small changes in probabilities should permit small changes in the comparison, or whether a strict priority or threshold must prevail. These questions make the representation's commitments discussable; finitely many answers cannot validate it for every lottery. If a common-mixture reversal, a noncompensatory rule or a material dependence on how the uncertainty is presented defeats the proposed form, retain the expressed comparisons and obtain a representation that preserves that feature. A probability-weighting or other non-expected-utility model needs its own construction; changing utility numbers alone cannot repair every failed form.

**Build one joint family.** For an accepted finite use, enumerate the complete consequence profiles appearing in the alternatives and elicitation questions. Obtain two intelligible reference consequences, w and b, that the holder treats as worst and best over this set and strictly distinguishes. Normalize `u(w) = 0` and `u(b) = 1`; require `0 <= u(x) <= 1` for the other represented profiles. This chooses an origin and unit, not the utility of an intermediate consequence. If common anchors are not supported, do not manufacture them: retain the direct comparisons or obtain a different representation. If every consequence is indifferent, return that simpler relation.

For each profile x, compare receiving x for certain with a lottery giving b with probability p and w otherwise. Stated indifference gives `u(x) = p`. If x is no worse than the lottery at p, add `u(x) >= p`; if the lottery at q is no worse than x, add `u(x) <= q`. Thus the holder can bound a comparison without identifying one exact probability of indifference. The probabilities in these questions describe the hypothetical lottery. They are not estimates of the real intervention's chance of success.

Retain all answers on the same utility variables. A comparison of two finite lotteries L and M adds `sum_x L(x) u(x) >= sum_x M(x) u(x)` when L is no worse, equality for indifference, or a strict inequality for strict preference. A comparison left open adds no equality. Certain-outcome comparisons are the special case with probability one on one consequence. These are linear constraints in the unknown utilities; use the feasibility and strictness treatment in §4.5.3 and the conflicting-subset diagnosis in §4.5.4. An inconsistent family calls for correcting the question or its interpretation, revisiting a judgement with its holder, or changing the form. It does not justify silently dropping a judgement.

This construction assigns utilities to complete profiles and requires no additive decomposition across their attributes. An additive multiattribute utility can reduce elicitation effort when its additional assumptions fit; the deterministic value model in §4.5.3 alone does not establish those assumptions for lotteries. Keep different holders' families separate unless the receiving work supplies a justified collective rule.

**Connect preference to the consequence model.** For each alternative a, obtain the distribution `P_a(x)` over these same profiles from the subject's probability model. Preserve shared causes, decision-dependent outcomes and the evidence limits described in PSDA.7 and PSDA.8. With one probability model and one utility function, compute `EU(a) = sum_x P_a(x) u(x)`. Comparing expected utility is generally different from applying utility to an average physical consequence.

When probabilities or utilities remain imprecise, retain the set K of compatible complete accounts `(P,u)`. Here P supplies a distribution for every alternative, and u is one utility function used across them. Use all combinations of the probability and utility families only when no joint restriction excludes them. If the meaning of a consequence, a model parameter or an elicited judgement links the two families, carry that restriction in K. Do not mix one alternative's favorable model with another's unfavorable model.

For each pair a and b, compare `D(P,u) = EU(a) - EU(b)` over K. Alternative a is necessarily no worse when every compatible account gives `D >= 0`; it is possibly no worse when at least one does. A contrary account defeats necessity; a feasible witness establishes possibility. The common-witness rule for possible best in §4.5.4 still applies. If K is empty, repair the failed basis before drawing a preference conclusion. No probability distribution over K follows from having retained it.

For fixed probabilities, D is linear in the utilities, so the finite constraint method can find a bound or witness. If both probabilities and utilities vary, their products generally make the problem bilinear; separate interval bounds or one linear-programming call are not automatically an exact solution. Use direct algebra, a complete finite enumeration or an appropriate bounding method under MMP.10 and MATH.20. Report a computed bound only over the domain it actually covers. With strict constraints, distinguish an attained witness from an unattained limiting value.

Return the supported preference, conditional alternatives or unresolved pair, with the consequence meanings, elicited comparisons and form assumptions that determine it. A new probability estimate updates the consequence side; a new or corrected lottery comparison updates the utility family. Recompute the affected relations while retaining the other supported contributions. Stop when the receiving decision has the preference information it needs. If an open preference can change that decision, ask the distinguishing question; further factual measurement cannot supply the holder's answer.

#### PSDA.6:4.6 - Return the account and its exact incompleteness

Return the attributed concerns and objectives; consequence meanings and measures; protected conditions and their sources; admitted trade-offs or preference relations; material interactions and dissent; unsupported transformations; and what would change the account. When a requirement's merits were in question, include the bounded appraisal return and the limit imposed by its current force from §4.4.

For a numerical construction, include the chosen form and its assumptions, the profiles and judgements constraining it, the joint compatible family or identified conflict, and the scope of any necessary or possible preference. `PSDA.8` may use it only for the named comparison. The account can support a partial order or leave a comparison unresolved. Missing preference information is not automatically missing empirical evidence: a further experiment may estimate consequences without deciding how they should be valued.

Recognition needs only a material ambiguity, duplication, or unexplained trade-off. Before consequential reliance, qualify the measurement or elicitation results actually consumed, justify any aggregation Method, establish the authority for binding conditions, and obtain the applicable domain assurance.

### PSDA.6:5 - Archetypal Grounding

#### PSDA.6:5.1 - Two meanings of flood service

In the illustrative flood-pump engagement, a residents' association emphasizes property protection, while a separately heard group of mobility-constrained residents emphasizes reachable assistance. The board is the later choice owner, not an assumed representative of every value judgement.

The analyst replaces a generic “service quality” score with this account:

| Concern | Consequence representation | Trade-off or qualification boundary |
| --- | --- | --- |
| Reduce property loss. | A qualified loss estimate for the affected properties and flood conditions. | The estimate is not evidence of reachable assistance; its valuation and uncertainty remain explicit. |
| Keep assistance reachable. | Whether the defined assistance service can reach the named population under the relevant access conditions. | The expressed concern is retained. Any binding access or safety condition needs its direct competent basis; it is not inferred from participation. |
| Maintain pumping service. | Hours of unavailability for the specified pumping service over the season. | This operational measure does not cover all property or human consequences. |
| Limit resource use. | Resources required by each whole arrangement, including continuing obligations and transition. | A cost preference does not permit violation of a separately established protected condition. |

The analyst removes a second “reliability benefit” entry that merely repeats the same pumping-service hours. Reachable assistance stays separate even if failures often occur in the same storms. That is not duplicate value.

If the board adopts a trade-off between operating-service hours and budget units for a narrow analytical slice, the account names that value judgement, range, and limit. It does not present the slice as the residents' common value function. If the association and the other group reject a common trade-off, the return carries separate accounts and a stated disagreement; another hydraulic simulation cannot resolve that disagreement.

#### PSDA.6:5.2 - Development directions do not share a universal improvement score

For the ninety-day service-organization case, a qualified strategy result gives reliability priority over throughput for the current horizon. That premise helps frame the comparison but does not supply numerical weights or a causal effect estimate.

| Proposed holder-specific input | What the value account may use | What it must not infer |
| --- | --- | --- |
| Human capability result for representative later Work. | The supported performance distinction and the person's relevant protected conditions. | Course attendance, assessment performance, retention, and transfer are not one interchangeable development value. |
| Organization result for positions, interfaces, and continuing service. | Contribution and service consequences for the named arrangement. | A local team's gain is not automatically a gain for the organization or another team. |
| AI/model evaluation for a named version and environment. | The qualified performance, resource, oversight, and failure distinctions. | A benchmark percentage is not a person's capability measure or the whole service's reliability. |

The adviser keeps those premises in their own meanings. A common service-level comparison is possible only after qualified domain results connect each direction to that same service and horizon. Without that connection, “human 4, organization 4, AI 4” is not a meaningful equal score. The return requests the missing consequence relation rather than normalizing the three numbers.

#### PSDA.6:5.3 - Cheap non-use

Two qualified replacement parts have the same relevant consequences except for a directly comparable resource cost, and the authorized recipient's cost preference is already explicit. Reuse that account. An objectives hierarchy and a fresh weighting workshop would add no value distinction.

#### PSDA.6:5.4 - Retain a protective restriction or revise a redundant control

These constructed variants concern a service team's proposed use of an external inference provider. In the first, a qualified configuration result shows that the proposed route exposes identifiable confidential incident records to provider staff who have no part in serving those clients. An available internal route meets the current service need within its support budget. The restriction prevents that disclosure; relaxing it for the faster external route would expose those clients without a corresponding needed service gain. The value account therefore supports retaining the restriction and excludes this external route for the current use. It does not infer that all provider configurations are unsuitable.

In the second variant, the configuration and access protection remain adequate. The disputed rule additionally requires three hours of manual transcription of an access log. Assume the competent review has established that the retained, inspectable electronic log covers the same events and that transcription adds no omitted event or distinct check. The same three hours would otherwise test a newly exposed, unreviewed access path to the same protected records. On these facts, retaining the extra transcription displaces more protective work without an identified protective gain. Recommend revising that requirement to use the qualified electronic record while keeping the actual access controls. If a missing event or an independent check is found, that premise changes the recommendation.

The rule owner cannot amend the transcription requirement before this decision. The recommendation is still complete, but it is not an exemption: present options must satisfy the rule or remain deferred. The lost testing opportunity remains a consequence of the present constraint. The contrasted results follow from the stipulated contribution and burden.

#### PSDA.6:5.5 - Obtain an exchange family and use a new judgement

A service manager supplies one legitimate value account for a four-week arrangement. Known costs are in thousands of resource units, waiting times in hours. The relevant ranges are 20–60 and 1–5. Lower values are preferred. The manager explicitly accepts constant value increments and a constant cost-for-time exchange within these ranges. Those are the form assumptions; the following comparisons constrain its parameters.

| Alternative | Cost `c` | Waiting time `t` | Eligibility for this comparison |
| --- | ---: | ---: | --- |
| A | 60 | 2 | Admissible. |
| B | 30 | 5 | Admissible. |
| C | 45 | 3 | Admissible. |
| D | — | — | Fails a currently binding access condition; no timely amendment is available. |

The manager says that `(60,1)` is no worse than `(20,5)`, and `(20,4)` is no worse than `(60,2)`. Applying §4.5.2 gives:

| Stated judgement | Joint constraint | Consequence for `r` |
| --- | --- | --- |
| `(60,1)` no worse than `(20,5)` | `60 + r <= 20 + 5r` | `r >= 10` |
| `(20,4)` no worse than `(60,2)` | `20 + 4r <= 60 + 2r` | `r <= 20` |

Thus `L_r(c,t) = c + r t` with `10 <= r <= 20` is the compatible family. It is nonempty: both endpoints satisfy both weak comparisons. No interview is available to choose a narrower exchange. In normalized range weights the same family has `1/3 <= w_c <= 1/2`, with `w_t = 1-w_c`; those numbers were derived from the profiles, not assigned to criterion labels.

The receiving `PSDA.8` comparison keeps one shared `r`:

| Difference over the whole family | Consequence |
| --- | --- |
| `L_B - L_C = 2r - 15`, between 5 and 25 | C is strictly preferred to B throughout. |
| `L_B - L_A = 3r - 30`, between 0 and 30 | A is no worse than B throughout, with a tie at `r = 10`. |
| `L_A - L_C = 15 - r`, between -5 and 5 | C is better below 15; A is better above 15; they tie at 15. |

These linear differences establish the signs over the entire interval. At `r = 10`, the losses for A, B and C are 80, 80 and 75; at `r = 20`, they are 100, 130 and 105. Both exchanges satisfy the elicited information but give different best alternatives. The `PSDA.9` sensitivity result is therefore the threshold 15 thousand per hour, and the `PSDA.14` return is the conditional set `{A,C}`. B cannot be best in any compatible model; D remains ineligible. Choosing `r = 15` merely because it is the interval's midpoint would add unsupported indifference.

Later the same manager states that C is no worse than A. Its new row is `45 + 3r <= 60 + 2r`, hence `r <= 15`. Intersecting gives `[10,15]`. Now `L_A-L_C` lies in `[0,5]` and `L_B-L_C` in `[5,15]`: C is no worse than A and strictly better than B for every compatible exchange. C is a necessary best, while `{A,C}` remains the set of possible best alternatives because A ties at 15. Return C as a supported direction with that tie intact. The new judgement changed the value family and its comparison; it changed neither the consequences nor D's access failure. The recommendation still leaves the authorized recipient's later choice distinct.

#### PSDA.6:5.6 - A failed affine form is not automatically contradictory judgement

Consider a different continuation from the original `[10,20]` family. The manager additionally says that `(20,5)` is no worse than `(44,2)`. In the affine form this yields `20 + 5r <= 44 + 2r`, or `r <= 8`. That row and the first original row `r >= 10` cannot hold together. Return this specific conflict; the former comparison no longer has a compatible affine basis.

Ask whether the equal-increment assumption still expresses the manager's values. They may care much more about reducing two hours to one than about reducing five hours to two. For example, a curved time-loss contribution taking values `0,20,28,36,44` at times `1,2,3,4,5`, with loss `c + h(t)`, satisfies all three profile comparisons: `60 <= 64`, `56 <= 80` and `64 <= 64`. This constructed witness proves only that those three judgements need not contradict one another. It is not an elicited curve and supplies no recommendation by itself.

If the manager withdraws constant time increments but retains addition, §4.5.3 constructs the whole compatible monotone family at the relevant levels. If the manager instead states the noncompensatory two-hour rule in §4.5.1, that different value account prefers A to B and C directly. Either change needs its stated basis; neither is a convenient parameter adjustment inside the old affine model. If no clarification is available, retain the attributed comparisons, D's independently established exclusion and the exact failed form. Return the numerical ranking as unresolved.

#### PSDA.6:5.7 - Separate an uncertain result from its value

A team compares two ways to obtain optional machine time in a ten-hour window. Existing provision covers required service; this comparison concerns additional usable hours, with other material consequences held equal. S supplies four hours for certain. R supplies ten hours if a trial succeeds and zero otherwise. The team prefers more usable hours, but that ordering does not yet compare S with R.

For a success probability of one half, utility `u(x) = x/10` gives `EU(S) = 0.4` and `EU(R) = 0.5`; R is preferred. Utility `u(x) = sqrt(x/10)` preserves the same ordering of certain hours but gives `EU(S) = sqrt(0.4)`, approximately 0.632, and `EU(R) = 0.5`; S is preferred. These two constructed functions show why the certain-outcome ordering is insufficient. Neither is an elicited preference.

The team accepts the expected-utility form for this bounded comparison and uses zero and ten hours as its reference consequences. Let `q = u(4)`, with `u(0) = 0` and `u(10) = 1`. Asked about hypothetical chances, the team says that four certain hours are no worse than a 40 percent chance of ten hours, but a 70 percent chance of ten hours is no worse than four certain hours. Each lottery otherwise gives zero hours. These answers yield `0.4 <= q <= 0.7`; they supply no point estimate.

Separately, engineering evidence bounds R's success probability by `0.45 <= p <= 0.55`. In this constructed case the probability estimate and preference restrictions impose no additional joint constraint. Thus `EU(R) - EU(S) = p - q` ranges from `-0.25` to `0.15`. Neither alternative is necessarily no worse. The accounts `(p,q) = (0.55,0.4)` and `(0.45,0.7)` witness opposite preferences. The unresolved comparison is useful: a more precise success estimate alone need not settle what the team values.

The team can answer one further preference question: four certain hours are no worse than a 60 percent chance of ten hours, otherwise zero. Intersecting that answer with the previous family gives `0.6 <= q <= 0.7`. The difference now ranges from `-0.25` to `-0.05`, so S is strictly preferred throughout the joint family. No midpoint utility or invented probability over utility functions was needed.

A changed engineering result can reverse that conclusion without changing the preference account. If a genuinely different trial design raises the supported success range to `0.8 <= p <= 0.9`, while the consequence meanings and other consequences stay the same, the difference ranges from `0.1` to `0.3`: R is now strictly preferred. If the redesign also changes cost, timing or the meaning of usable hours, those omitted consequences must first enter the profiles; the old one-attribute calculation would no longer answer the whole comparison.

The construction concerns one attributed preference account. It neither aggregates conflicting team members' views nor establishes that the trial has the assumed success probability. Those are separate inputs whose absence would leave a different question open.

### PSDA.6:6 - Bias-Annotation

**Scope:** value representation for one bounded comparison. **Lenses:** **Onto/Epist** separates concern, measure, preference, and obligation; **Prag** preserves decision relevance; **Gov** exposes representation and authority; **Did** makes trade-offs concrete.

Template bias imports irrelevant criteria. Proxy bias rewards what is easy to count. Splitting one objective into many criteria can change its apparent importance. Sponsor averaging can conceal who bears a loss. Counter these by returning to attributed consequences, inspecting overlaps, and retaining disagreement and missingness.

### PSDA.6:7 - Conformance Checklist

- [ ] Values are attributed to the relevant subjects and receiving comparison, with representation limits intact.
- [ ] Objectives and possible means remain distinct at the grain that changes the decision.
- [ ] Repeated consequences are not counted twice; correlation alone does not justify deletion.
- [ ] Measures retain subject, scale, unit, horizon, evidence, proxy limits, and missingness.
- [ ] Binding conditions, aspirations, and unresolved authority questions are distinguished. A live merits question receives an appraisal of protective contribution and burden, with a supported recommendation and unchanged current force.
- [ ] Value transformations and weights have declared ranges and an elicitation basis; the chosen form is justified separately from fitting its parameters.
- [ ] The numerical family preserves the joint judgements, has a checked feasibility result, and distinguishes incomplete information from contradictory judgements or a failed form.
- [ ] Necessary and possible comparisons retain their quantifiers, ties and dependence on the same compatible model. A changed judgement reopens only dependent results unless it changes the form itself.
- [ ] For a finite expected-utility comparison, lottery judgements and the chosen representation justify the utility account; probability estimates come from the consequence model. Joint variation uses one compatible account across alternatives, and an unresolved preference is not filled by averaging unknown utilities.
- [ ] Interactions and refusals to compensate are preserved.
- [ ] Any collective aggregation has an explicit basis; incompatible accounts remain visible otherwise.
- [ ] The return states partiality, dissent, direct-source gaps, and exact reopen conditions.
- [ ] A supported preference comparison covers only its attributed account and supplied consequences; authorization of the later choice and a claim of effect need their own grounds.

### PSDA.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Everyone agrees safety is important, so give it twenty percent.” | Recover the actual condition, its source, and whether compensation is permitted. |
| “Equal weights are neutral.” | State the consequence ranges and inspect how criterion splitting changes the result. |
| “These two measures correlate, so one is redundant.” | Examine whether they represent the same valued consequence. |
| “Normalize everything to zero–one.” | Establish value meaning and admissible operations before any transformation. |
| “The workshop mean is the public preference.” | Preserve attribution and require an explicit aggregation basis. |
| “Collect more data to resolve the value dispute.” | Identify whether the missing input is evidence, preference, representation, or authority. |

### PSDA.6:9 - Consequences

The comparison becomes open about what it values and what it cannot exchange. Simplifying the account can reduce burden without losing material distinctions. Some decisions remain partially ordered or disputed; that is a truthful result, although it may be less convenient than a single score.

### PSDA.6:10 - Rationale

Value representation makes consequences decision-relevant without confusing description with preference or preference with permission. Concrete trade-off questions expose assumptions hidden by criterion labels. Preserving multiple admissible accounts lets later comparison show where a conclusion is shared and where it depends on a disputed judgement.

### PSDA.6:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How can objectives be concise without omitting what matters? | Inspect means–ends structure, relevance, overlaps, and sensitivity to simplification. | Retain an exhaustive descriptive hierarchy, or delete criteria by correlation alone. | **Adapt:** :4.2–:4.3 keep a small consequence-led account and test any lost distinction. More analyst attention is accepted where it prevents double counting; small clear cases remain short. | Marttunen et al.'s [2019 objectives-hierarchy study](https://doi.org/10.1016/j.ejor.2019.02.039) supplies the comparative methods and retrospective environmental cases. It supports disciplined simplification, not one optimal hierarchy or a statistical license to discard values. | Reopen when a removed distinction can reverse the comparison or a lighter structure preserves the same concerns. |
| Must incomplete preferences become one weighted score? | Construct the preference model from consequence comparisons and use all compatible instances. | Fit one additive score, average weights, or retain a noncompensatory rule when that better expresses the judgement. | **Adapt:** :4.5.1–:4.5.5 develop form selection, joint constraints, feasibility, necessary/possible comparison and local revision; :5.5–:5.6 show a complete use and failure of the affine form. The trade-off is a potentially less decisive answer for less invented precision. | Greco, Słowiński and Wallenius's [2025 MCDA review](https://doi.org/10.1016/j.ejor.2024.07.038), especially §3.1.2 and §7.1 ([accessible author-hosted PDF](https://www.iris.unict.it/retrieve/cb6fc63a-f16d-4c14-a163-46b863c27dc9/1-s2.0-S0377221724005988-main.pdf)), supplies preference assessment and robust ordinal regression. Its rules and non-additive families remain serious alternatives. The two-criterion derivation and service cases here are bounded applications, not its empirical findings or a universal additive-representation theorem. | Reopen when new judgement changes the compatible set, an interaction defeats the form, or the holder, range or governing condition changes. |
| How can incomplete risk preferences become a usable comparison? | Elicit finite lottery comparisons, construct the compatible utility family and compare expected utilities over compatible probability and utility accounts. | Assume risk neutrality from a certain-outcome score, fit one curve despite open judgements, or retain a different explicit preference rule. | **Adapt:** :4.5.6 supplies the general construction and :5.7 shows elicitation, an open result and a changed comparison. More elicitation or computation is warranted only when it can change the receiving decision. | [Sahlin, Troffaes and Edsman (2021), §§3.3–3.5 and Appendix B](https://arxiv.org/html/2103.04721v1) demonstrate imprecise lottery-based elicitation with imprecise consequence probabilities. Their additive environmental model is not assumed here. [McCarthy, Mikkola and Thomas (2021)](https://arxiv.org/abs/2102.06898) develop the representation question for incomplete mixture preferences; retaining a family does not remove independence and continuity premises. [Breig and Feldman (2026, online 2025)](https://doi.org/10.1007/s11238-025-10089-1) test expected-utility consistency in a specific elicitation design, supporting scrutiny of the form rather than universal use. The finite profile construction and machine-time calculation here are explicit adaptations, not empirical findings from those studies. | Reopen when lottery judgements conflict with the form, a consequence is omitted, the probability model or holder changes, or an unresolved joint restriction changes the comparison. |
| Can common coordinates perform the value judgement? | Declare meanings and scales separately from preference, comparison, and selection. | Treat a dashboard or normalized vector as the decision model. | **Adopt:** :4.3 uses A.19 only for the declared space or predicate and leaves value elicitation here. The distinction adds little effort to an existing table and prevents a false consumer result. | Current `A.19`, `C.16`, and the direct comparison patterns supply the relevant typing and operation boundaries. They do not elicit the engagement's values or authorize a trade-off. | Reopen when the scale, predicate, consequence range, or receiving use changes. |

### PSDA.6:12 - Relations

- `PSDA.12` may supply the participation and concern account that changes the value question. That contribution is not already a weight set or a collective mandate.
- `PSDA.8` consumes the value account and its admitted preference relation for the named comparison; `PSDA.9` tests its dependence on the compatible family, and `PSDA.14` uses the supported direction, conditional set or gap.
- `MMP.10` and `MMP.11` supply general constraint and model-family construction after the value meanings and form conditions in §4.5 are established. `MATH.20` supplies bounds over the admitted domain; none of these suppliers elicits the holder's preferences.
- `C.16` governs measurements; `A.19` supplies a declared characteristic space or predicate when needed. Scoring, aggregation, comparison, and selection remain separate direct operations.
- Direct ethics, law, safety, governance, finance, and holder practices supply the particular conditions and claims they own. `A.15.9` helps obtain a missing qualified contribution without transferring that authority.
- If a required value or source premise is absent, stale, or incompatible, use a qualified direct result or return its exact gap.

### PSDA.6:End
