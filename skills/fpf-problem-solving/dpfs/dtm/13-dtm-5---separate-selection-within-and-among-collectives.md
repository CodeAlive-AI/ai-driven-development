## DTM.5 - Separate Selection Within and Among Collectives

**Type:** Method
**Status:** Stable

### DTM.5:1 - Problem frame

**Use this when** a variant becomes more common within each participating group, yet its overall prevalence changes differently—or when a claimed advantage of a collective is being used to explain which variants continue.

A shortcut can gain users inside every team while teams that use it less contribute more of the next period's procedures. Conversely, a practice can be costly to a current member while supporting a group's continued operation. These situations require distinguishing units of continuation and the processes that change their weights.

The first result is a decomposition of the observed or modeled change, followed by an account of which parts have a supported selection mechanism. The decomposition alone does not establish causation or justify privileging a higher level.

For comparing the current performance of two organizations without a question about differential continuation, use the existing evaluation and choice methods.

### DTM.5:2 - Problem

An overall mean mixes changes within groups with changes in the groups' contributions to what continues. Calling either component “group success” leaves its unit unclear: more copied methods, more learners, survival of the same organization, or more successor organizations.

The same arithmetic can also arise without selection. Reconstruction, unequal exposure, recruitment or a changed measurement can alter the mean. A useful account must therefore distinguish the bookkeeping identity from the causal explanation.

### DTM.5:3 - Forces

| Force | Tension |
| --- | --- |
| Groups influence continuation | A chosen grouping can create an apparent group effect without a group-level cause. |
| Aggregate change is observable | Its contributing events may have different sources or mixed parentage. |
| Within-group advantage matters | It may conflict with what makes a collective continue or contribute. |
| Selection language is compact | It can conceal changes of counted unit and normative recipient. |

### DTM.5:4 - Solution

**Choose the unit of continuation, trace its sources, separate the changes, then investigate the mechanisms behind them.**

#### DTM.5:4.1 - Decide what the next population counts

Name the earlier population, the receiving population and the interval or transition connecting them. Specify the continuing unit: an executed method variant, a learner retaining it, a transmitted procedure instance, or a collective with an identified successor relation.

A group can contribute many transmitted instances without producing a new group. Use the first kind of count for variant continuation and the second for collective reproduction. Survival, revenue or an externally assigned quality score does not automatically measure either.

C.36 supplies the cultural relations; DTM.1 identifies the variant and affected work. Return to DTM.2 if the available record shows only copies of descriptions while the claim concerns continued execution.

#### DTM.5:4.2 - Recover contribution weights and within-group change

Establish the source relation at the detail the question requires. For a particular procedure, trace which groups supplied its content. For a change in a population mean, supported group counts and means, or bounds on them, can suffice even when individual continuations cannot be identified. Use the actual source relation, rather than assuming that every present member contributes equally.

A resulting procedure may use the inspection method developed by one team and the scheduling rule developed by another. Trace what came from each team. If these are the only sources and the question asks which teams supplied material, naming both completes the answer. The one procedure enters each team's count of procedures it helped produce. To obtain the number of distinct procedures across the teams, account for the overlap.

For an additive decomposition of a total, account for every receiving unit once. Allocate a shared unit's weight according to a rule justified for that use. A convention can settle an accounting question. Actual inheritance or borrowing requires evidence of the source relation. Where shares remain unresolved, preserve the known sources and any justified bounds. Distinguish the part attributed to the identified groups, any external part and gaps in coverage.

Keep differences due to reconstruction, recruitment and observation visible. For example, a transmitted procedure may omit a check during reconstruction even if no recipient deliberately selected the unchecked variant.

#### DTM.5:4.3 - Decompose the aggregate change

For a scalar property, let π_g be the source population's weight in group g, z_g its initial mean, w_g its contribution per source unit to the covered part of the receiving population, and Δz_g the change in the corresponding transmitted mean. Weights π_g sum to one; the mean contribution w̄ is positive. The source-attributed contributions must cover that part without omission or double counting.

For a group assigned zero continuation weight in this decomposition, the weighted transmitted mean and `Δz_g` for that group are undefined. Keep its initial weight and mean in `z_old` and the covariance, with `w_g = 0`. Sum transmitted means and changes only over groups with positive contribution. A known source may receive zero weight under an accounting convention. If the weight denotes an observed count, a missing record warrants zero only when the evidence establishes absence.

The covered mean and its difference from the initial mean satisfy:

~~~text
z_cov = Σ_{g: w_g > 0} π_g w_g (z_g + Δz_g) / w̄
z_cov − z_old
  = Cov_π(w,z) / w̄ + Σ_{g: w_g > 0} π_g w_g Δz_g / w̄.
~~~

The first term expresses the effect of different contribution weights associated with the earlier property. The second expresses changes along those contributions. If those contributions cover the whole receiving population, z_new = z_cov.

Otherwise let c be the covered fraction of the receiving population and z_ext the mean property in the rest, using the same counted unit and weighting convention. Include that contribution:

~~~text
z_new = c z_cov + (1−c) z_ext
z_new − z_old = c (z_cov − z_old) + (1−c)(z_ext − z_old).
~~~

An unknown external composition remains unknown; it is not zero. For a binary variant share and known c, the possible new share lies between c z_cov and c z_cov + 1−c until the external composition is constrained. If the receiving population is nonempty and entirely external to the identified groups, its mean is the external mean. If there are no receiving units at all, the count of continuations is zero. A mean property among those continuations and a change to that mean are undefined. MMP and the relevant mathematical methods supply the calculation.

This identity does not tell why w or Δz has the observed value. Call them between-source and within-contribution changes until the causal interpretation is established. If the units are collectives, redefine z and w for collective continuation; do not carry over a particle count while silently changing the claim.

For a question needing no scalar aggregate, retain the corresponding source and change table. Do not invent a total score solely to use the formula.

#### DTM.5:4.4 - Test the proposed selection mechanisms

For within-group selection, identify the process by which variants contribute differently under the group's conditions. For a between-group explanation, identify what group property changes survival, contribution, recruitment or successor formation.

Consider an alternative that could reproduce the same decomposition: groups may encounter different audiences, receive unequal support, have different ages, or be observed with different completeness. Choose the distinguishing observation or comparison with MMP.16 and the applicable research method.

The response to a change must follow the mechanism. If a group's larger contribution comes from privileged broadcast access, altering an internal learning method may leave that advantage unchanged. If the advantage comes from reliable results that others adopt, changing access alone can hide the relevant production difference.

#### DTM.5:4.5 - Return the decomposition to the work question

For a question about who supplied a practice, return the identified source relations and any material uncertainty about their coverage. For a question about aggregate change, state the counted units, source weights, population covered, components of the change and any supported explanation. If coverage or external composition is unresolved, return the supported range or restrict the claim to the covered part. If the commission includes changing the practice, ask which feasible change addresses the relation that matters.

A practice favored within teams but associated with lower total contribution can persist locally. A collective's growth can also coexist with costs to its members. D.3/D.4 and the existing decision methods retain those conflicts; no arithmetic term grants moral priority to its level.

Use DTM.3/.4 to examine dynamic continuation and DTM.6 when another variant changes the contribution mechanism. Stop with the descriptive decomposition when causality remains unresolved and that description is sufficient for the receiving use.

### DTM.5:5 - Archetypal Grounding

#### DTM.5:5.1 - Within-group increase is canceled by changing contribution weights

Take two equally weighted source groups. Their initial shares of variant B are 0.2 and 0.8. Along each group's transmitted contribution the B share increases by 0.1. The groups supply relative transmitted-instance counts of 2 and 1.

The initial overall B share is 0.5. The receiving share is:

~~~text
(2 × 0.3 + 1 × 0.9) / 3 = 0.5.
~~~

The contribution-weight change is −0.1; the within-contribution change is +0.1. They cancel. An unchanged aggregate would therefore conceal two material changes.

The weights count transmitted instances, not new organizations and not usefulness. The result does not establish why the low-B group supplied twice as much. Better results, broader access or a sampling difference are possible explanations requiring different follow-up.

If the two groups instead supply equal counts, the new B share becomes 0.6. This changed condition shows which contribution the aggregate depended on.

#### DTM.5:5.2 - A copied method can change without being selected

Suppose every teaching group sends one equally weighted procedure, but recipients reconstruct it with a different timing convention. A change in the receiving mean belongs to the within-contribution term. There is no differential contribution in this stipulated case.

The next action is to study reconstruction with DTM.2 and the relevant learning or notation method. Calling the change selection would direct attention away from how the recipient obtained the new variant.

#### DTM.5:5.3 - Counting successor collectives answers another question

A project network may form successor teams with different arrangements. If the question is which arrangement becomes common among successor teams, count those teams and recover their formation relations. If the question is which procedure most workers later use, count the corresponding use and contribution relations.

One prolific source team can dominate the latter count without dominating the former. The choice of unit is part of the question, not a defect to remove by finding one universal fitness number.

#### DTM.5:5.4 - External arrival changes the receiving mean

One procedure instance A continues from the identified source, with B-share z_old = z_cov = 0. One instance B arrives from outside that source set. The receiving population has two instances, so c=1/2 and z_ext=1. Its B-share is (1/2)×0 + (1/2)×1 = 1/2. A source-only calculation would return zero because it answers only for the covered part.

If the external instance's variant is unknown, the whole-population B-share lies between 0 and 1/2. Additional source tracing is needed only if that uncertainty changes the receiving decision. Neither result attributes the external arrival to selection within the original source.

### DTM.5:6 - Bias-Annotation

Grouping by a striking label can make an accounting effect look like a collective cause. Recover the source relations and plausible alternatives before asserting that causal level.

The phrase “higher-level success” also invites a value judgement. Name what continues and who benefits separately.

### DTM.5:7 - Conformance Checklist

- The earlier and receiving populations, interval and counted unit are identified.
- Group contribution is not confused with reproduction of the group itself.
- For a question about sources, establish the groups and the relations claimed. For an additive decomposition, justify the source weights or retain their uncertainty. The weighted within-source mean change in this decomposition is defined for groups with positive continuation weight.
- Does the conclusion cover the receiving population and count each contribution on the agreed basis? If part is unobserved, can a bound for the whole already settle the question? Otherwise give the supported result for the covered part and identify what remains open.
- The decomposition uses consistent units and does not serve as its own causal explanation.
- Reconstruction and differential exposure remain alternatives where they could change the answer.
- The practical conclusion retains conflicts among affected participants instead of assigning automatic priority to a level.

### DTM.5:8 - Common Anti-Patterns and How to Avoid Them

**The aggregate did not change, so nothing happened.** Recover both components and their possible cancellation.

**A profitable team has higher reproductive success.** Establish the continuation unit and contribution relation; profit may explain one, but does not define it.

**A covariance proves group selection.** Investigate the mechanism and a consequential competing explanation.

**Every inherited change is selection.** Keep reconstruction and transformation distinct from differential continuation.

### DTM.5:9 - Consequences

The method exposes conflicts hidden in a population mean and prevents intervention at the wrong mechanism. It also limits overclaiming: a valid decomposition may leave the causal question open. Source attribution and comparable observations can be costly; their required precision follows the receiving decision.

### DTM.5:10 - Rationale

Multilevel change is not simply the same selection calculation repeated at larger scales. The objects counted, their contribution relations and the causal mechanisms can differ. An explicit decomposition makes those differences inspectable.

### DTM.5:11 - SoTA-Echoing

[Bourrat, *Multilevel selection 1, multilevel selection 2, and the Price equation: a reappraisal* (2023)](https://doi.org/10.1007/s11229-023-04285-1) sharpens the distinction between contributions of particles from collectives and reproduction of collectives. This method adopts the unit distinction without resolving the paper's broader interpretation of multilevel selection.

Compared with following only aggregate prevalence, the decomposition can reveal offsetting changes at modest additional calculation cost. Compared with treating every group association as causal selection, it requires the source and causal relation that would change intervention. Existing mathematical and research methods supply those tests; DTM retains the units and continuation question.

### DTM.5:12 - Relations

- **DTM.1/.2** supply the variant, consequences, uptake and reconstruction distinctions.
- **DTM.3/.4** investigate coupled continuation and persistence.
- **DTM.6** models interactions that can change contribution weights.
- **C.36**, **MMP.16**, **D.3/D.4** retain cultural relations, discrimination of explanations and conflicts between interests.

### DTM.5:End
