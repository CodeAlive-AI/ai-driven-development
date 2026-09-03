## E.10.LRN - Recovering What “Learning” Means in the Current Claim

> **Type:** lexical and ontological precision restoration (E)
>
> **Status:** Stable
>
> **Plain name:** recover what “learning” means here
>
> **Placement:** Part E, under `E.10` and `E.10.ARCH`

### E.10.LRN:0 - Use This When

Use this pattern when claim-bearing wording says *learn*, *learning*, *learned*, *taught*, or *trained*, and the sentence does not yet reveal which participant, changed subject, Work, Method, result, evidence, or receiving use is meant.

**First useful result.** Rewrite or split the sentence so that each exact subject claim is recognizable, then continue with the direct pattern for that claim. A local repair normally ends with an exact capability claim, teaching-Work claim, training/model-result claim, inference result, information-acquisition result, representation claim, cultural-change claim, product claim, or ordinary non-use. It does not end with a generic `LearningResult`.

**Cheap exit.** Keep ordinary wording when no FPF inference or action depends on which sense is meant. If the changed subject, operation, result, evidence, and direct pattern are already explicit, use that pattern directly.

**Not this pattern when.** Do not use this pattern to choose a teaching or training Method, assess a capability, fit a statistical model, design an experiment, perform inference, measure a result, or decide what to do next. It only restores the claim that those practices must govern.

`LRN` remains in this PatternID because the ambiguous source wording opens the recovery. It is not a Tech designation for one governed process or value and is not a UTS-row precedent.

### E.10.LRN:1 - Problem Frame

The same word family is used for importantly different situations:

- a person inquires, notices, remembers, or reorganizes an episteme;
- another System performs teaching, coaching, demonstration, or feedback Work;
- a person acquires a capability for later Work;
- an algorithm performs parameter-estimation or optimization Work and returns a fitted model;
- an inference Method returns a posterior or approximate distribution;
- a query policy acquires data or reduces uncertainty;
- a probe decodes a representation from system-side phenomena;
- an organization or culture retains, reconstructs, selects, or loses a practice variant;
- a course, lesson, dataset, artifact, or guide is produced; or
- ordinary prose says only that someone found something out.

These uses can occur together without becoming one process. A teacher can teach while no capability is acquired. A person can acquire a capability without the sentence identifying a teacher. A model can be trained without a deployed System satisfying its capability claim. A posterior can be approximated without any human or machine capability changing.

### E.10.LRN:2 - Problem

When the umbrella word remains load-bearing, authors silently transfer evidence and conclusions across subjects. A lesson becomes a capability; an artifact becomes proof of authorship or transfer; benchmark improvement becomes generalization; information gain becomes competence gain; model fitting becomes inference; an organizational slogan becomes changed practice; and a repeated pattern becomes a universal atom of knowledge.

The repair must preserve familiar language while preventing those transfers. It must also stay thin: the direct subject patterns, not this wording pattern, define capabilities, Work, Methods, epistemes, evidence, models, representations, cultures, and decisions.

### E.10.LRN:3 - Forces

| Force | Tension |
| --- | --- |
| Useful umbrella vs distinct subjects | Ordinary language needs *learning*; action-bearing claims need the exact changed subject and result. |
| Occurrence vs outcome | Teaching or training Work can occur without establishing the intended capability or generalization result. |
| Human and machine cases | Wet and dry substrates can implement several different operations; substrate material does not classify the claim. |
| Internal change vs inspectable construction | An external artifact or performance can expose reasoning without proving capability, authorship, transfer, or retention. |
| Source fidelity vs FPF ontology | A paper may deliberately use one label across several quantities; FPF preserves that quotation while recovering distinct claims for use. |
| Precision vs paperwork | One local rewrite should suffice when no durable recovery record is needed. |

### E.10.LRN:4 - Solution

Recover the current claim from its participants, subject, operation, result, and use rather than from the word *learning*.

1. **Bound the wording use.** Quote or locate only the sentence or source expression whose interpretation changes a claim, inference, or action.
2. **Recover the grammatical commitment.** Identify who or what is said to have taught, trained, learned, changed, produced, inferred, or acquired something. Grammar foregrounds a claim but does not fill missing causal participants or evidence.
3. **Name the changed subject.** State whether the current bearer is a person's capability, an episteme, a model and parameters, a probability distribution, a representation relation, an organization or population, a product, a Work occurrence, or another exact subject.
4. **Separate Work, Method, and result.** Name inquiry, teaching, practice, training, optimization, inference, experiment, data acquisition, assessment, publication, or cultural-continuation Work only when it is current. Keep its performer, Method, inputs, and dated occurrence separate from the result attributed to another subject.
5. **State the evidence and blocked transfer.** Name what was observed or assessed, for which task, population, configuration, window, support arrangement, and use. State the stronger nearby claim that this basis does not establish.
6. **Select one direct branch.** Use the branch table below. When one sentence contains several branches, split it into several ordinary sentences and route each one separately.
7. **Stop after recovery.** Return the repaired claim and direct pattern, or an exact missing-information, missing-governor, quote-only, ordinary-use, or blocker result. Do not create a generic learning record, role kind, process, progress scale, or causal relation.

#### E.10.LRN:4.1 - Direct branches

| Recovered current claim | Required route and boundary |
| --- | --- |
| A person or other System acquired or changed a capability for later Work | Use `A.2.2` and the direct capability-development/evaluation patterns. Name holder, target Work, conditions, support arrangement, performance evidence, transfer horizon, and uncertainty. Practice, teaching, a score, or one successful performance does not by itself establish the capability. |
| A teacher, coach, peer, tool-using System, or environment performed teaching, demonstration, feedback, or practice-support Work | Use A.15 for dated Work, A.3 for the enacted Method, and direct responsibility/authority relations when current. The occurrence and intended result do not entail capability acquisition by the recipient. |
| A person inquired, noticed, remembered, understood, or revised an episteme | Recover the exact episteme, representation, source use, inquiry Work, and claim change through `C.2.1`, `A.6.3.RT`, A.10, and the direct subject pattern. Do not infer a general capability from one reported insight. |
| A statistical or machine-learning system was trained or fitted | Identify target function, distribution, or policy; data and data-generating assumptions; model family; objective or estimator; training/optimization Work; resulting model edition; evaluation conditions; and deployment use. Parameter change, a low training loss, a generated sample, and deployed-system capability remain different claims. |
| A probabilistic inference Method returned a posterior or approximation | Identify the target model/distribution, observations, inference or approximation family, objective/divergence/bound, computation, diagnostics, and returned distribution. Variational inference is an inference/optimization branch, not human capability acquisition and not calculus-of-variations design by name. |
| Active learning, curiosity, exploration, question asking, or data mining selected or acquired information | Identify the query, observation, experiment, or data-acquisition option; current belief/model state; expected or observed information result; cost; and receiving decision. Information acquisition or uncertainty reduction does not by itself establish capability, transfer, useful action, or an evidence-qualified next choice. |
| A probe found a “learned representation” | Distinguish the system-side phenomenon, training history when relevant, probe-training Work, decoded rendering, representation relation under `A.6.3.RT` and `C.29`, and any admitted episteme. Decodability or a readable label does not establish causal use, internal semantic identity, or general capability. |
| An organization, community, or culture “learned” | Recover changed Methods, assignments, Work, carriers, population, transmission or reconstruction, selection, retention, loss, and consequences through their direct patterns and `C.36`. A report, policy, or lesson-learned entry does not establish changed enacted practice. |
| A course, lesson, guide, dataset, pattern, artifact, or other learning product was created or used | Identify the product episteme or artifact, production Work, publication/use relation, intended capability contribution, and observed result separately. The carrier is not the holder's capability or internal state. |
| Ordinary or quoted wording makes no FPF-governed claim | Preserve it. If relied on later, recover the exact branch then. |

#### E.10.LRN:4.2 - Grammar does not settle the route

| Wording | What it foregrounds | What remains unresolved |
| --- | --- | --- |
| “The teacher taught Mira to swim.” | Teaching Work, participants, and an intended capability result. | Whether Mira acquired, retained, or transferred the swimming capability; the exact causal contribution of the teaching. |
| “Mira learned to swim.” | Ordinarily, a changed capability of Mira. | Whether the route included a teacher, self-directed inquiry, practice, tool, peer, environment, or several contributors; the evidence and transfer boundary. |
| “Mira learned from the manual.” | A source-use or inquiry route may be claimed. | The exact episteme change, capability result, evidence, and whether the manual was merely available or actually used. |
| “The GAN learned the distribution.” | Source-local shorthand for adversarial training and a resulting model. | What distributional relation was established, which model edition, evaluation/generalization basis, and deployed capability. |
| “Learning progress increased.” | Some change over a window. | Whether the coordinate is performance, capability evidence, prediction error, information gain, model fit, compression, representation, or something else. |

Passive and active grammar can also shift attention without changing ontology. “Was taught” foregrounds an intervention received; “learned” foregrounds the attributed result. Neither wording alone establishes the full causal route.

#### E.10.LRN:4.3 - Construction, public results, and patterns

Constructivism and constructionism remain source-local theories and Method families. Constructionism shares the learner-side construction emphasis and adds a design commitment to making something public or shareable. For FPF this is a useful Method and evidence-design pressure: a model, program, explanation, dance, diagram, or other external construction can expose distinctions and Methods for inspection.

The construction still does not prove capability, authorship, independent use, transfer, or retention. Pair construction tasks with representative later-Work tasks and direct evidence when those claims matter. Reciting a poem or reproducing a pattern may establish a narrow remembered performance; it is not automatically action-guiding capability in a new situation.

An FPF pattern is an action-guiding episteme. In a named cultural case it can also be a retained, transmitted, selected, or reconstructed cultural variant under `C.36`. It is not the universal atomic unit of knowledge, a “meme” kind, the holder's internal state, or the holder's capability merely because it was copied or published.

#### E.10.LRN:4.4 - Lightweight local result

For a local repair, the result can remain this small:

```text
source wording: the GAN learned the target distribution
recovered claims:
  - adversarial training Work optimized two parameterized models under a minimax objective
  - trained model edition G-17 generated samples evaluated under tests T1–T3
direct routes: A.15, A.3, C.2.1, C.16, A.10, statistical-model-fitting practice
blocked overreads: no human capability claim; no exact target-distribution identity; no generalization beyond T1–T3
stop: deployment capability is a separate current question
```

No persistent record is required unless another use needs to inspect or reuse this recovery.

### E.10.LRN:5 - Worked Slices

#### E.10.LRN:5.1 - Taught to swim and learned to swim

“A coach taught Lee to swim” opens a teaching-Work claim. Recover coach and Lee as Systems, the dated coaching and practice Work, enacted Method, conditions, and intended result. “Lee learned to swim” opens a holder-capability claim. Recover target swimming Work, support conditions, observed performance, transfer conditions, and evidence. The second sentence does not identify the causal route; the first does not prove the second. A later causal question uses `C.28`.

#### E.10.LRN:5.2 - GAN training

A GAN training run is optimization Work over generator and discriminator parameters under a declared objective and data basis. The run, trained model editions, generated samples, benchmark results, and a deployed system's capability are separate. Calling all five “what the network learned” loses the decision-relevant boundaries.

#### E.10.LRN:5.3 - Variational inference

A variational-inference procedure selects an approximate distribution from a declared family by optimizing a divergence or bound against a target probabilistic model. It returns an inferential approximation and diagnostics. It does not establish capability acquisition, and its use of optimization does not make it a calculus-of-variations design of a physical trajectory or field.

#### E.10.LRN:5.4 - Active learning

An active-learning policy chooses a query or observation because its expected result may improve a model or decision. Recover the current model state, acquisition option, expected information or decision value, cost, returned observation, update, and next decision separately. The data-acquisition choice is closer to inquiry or mining in this branch than to a claim that a holder acquired a capability.

#### E.10.LRN:5.5 - Public construction

A participant builds and explains a working pump simulation. The artifact and explanation make some model choices inspectable. Assessment Work may use them as evidence for bounded claims. Independent diagnosis of a changed pump configuration is a different representative task; only direct evidence from that task can support the corresponding transfer or capability claim.

#### E.10.LRN:5.6 - Organizational learning

An organization publishes a “lessons learned” report. Publication establishes an available episteme, not changed enacted practice. Recover later Method changes, assignments, Work occurrences, selection, retention, and operating consequences before claiming organizational or cultural change.

### E.10.LRN:6 - Bias Annotation

- **Human-default bias:** do not assume every use concerns a person's capability.
- **Machine-anthropomorphism bias:** do not translate model fitting into human cognition or agency.
- **Substrate bias:** wet and dry neural networks can participate in several kinds of Work and result; material substrate does not choose the branch.
- **Artifact bias:** public construction improves inspectability but does not prove authorship, capability, or transfer.
- **English-grammar bias:** active/passive voice and English lexical convention do not establish causal structure.
- **Metric bias:** a changed score or loss does not identify which subject changed or which stronger claim it supports.

### E.10.LRN:7 - Conformance Checklist

1. Is the word family claim-bearing for the current use?
2. Are participants, changed subject, Work or Method, result, and receiving use explicit enough to choose a direct pattern?
3. Are teaching/training occurrences separated from capability, model, inference, or generalization results?
4. Does the evidence name task or population, conditions, support arrangement, window, and blocked transfer?
5. Are information acquisition, belief/model update, statistical fitting, and capability change kept distinct?
6. Are public constructions, recall performances, patterns, and cultural variants kept distinct from holder capability and internal state?
7. Is source-local wording preserved as quotation where needed without becoming FPF ontology?
8. Did the repair avoid a generic `Learning`, `Learner`, `Teacher`, `LearningProgress`, or `LearningResult` kind or UTS row?
9. Did each recovered claim return to its direct pattern and stop there?

### E.10.LRN:8 - Common Anti-Patterns and Repairs

| Anti-pattern | Repair |
| --- | --- |
| One `Learning` process joins teaching, capability, training, inference, and data acquisition | Split by changed subject, Work, result, evidence, and receiving use. |
| “The teacher taught it, therefore the person can do it” | Separate teaching Work from capability evidence and transfer. |
| “The model learned it, therefore the deployed System can do it” | Separate training, model edition, evaluation, deployment, and capability. |
| “Information gain is learning progress” | Name the belief/model update and keep capability change separate. |
| “A public artifact proves knowledge” | Treat it as inspectable evidence input; test representative independent use separately. |
| “A pattern is the atom of knowledge or a meme” | Treat the pattern as an episteme and, only in a named case, a cultural variant under `C.36`. |
| Replace *learning* with one preferred synonym | Recover the subject claim; vocabulary replacement alone does not close the ambiguity. |

### E.10.LRN:9 - Consequences and Reopen Condition

**Benefits.** Education, human capability, machine learning, inference, inquiry, representation, organizational, and cultural claims can share readable prose without sharing false identity. Evidence stays attached to the result it actually supports. Downstream DPFs can specialize Methods without inheriting an ambiguous FPF process.

**Costs.** A load-bearing umbrella use needs one bounded recovery, and some sentences must be split. Domain methods and evidence still need their direct products.

Reopen this pattern when a recurring claim-bearing use cannot reach one direct subject pattern, ordinary non-use, or exact blocker with the recovery fields above; when cold readers still transfer evidence among branches after the repair; or when a direct pattern absorbs the same entry, action, first result, and stop without losing discoverability.

### E.10.LRN:10 - Rationale

The recurring transdisciplinary problem is lexical recovery, not a common learning substance. A stable thin action survives across the unlike cases: recover who or what changed, separate Work and Method from result, state evidence and blocked transfer, split unlike claims, and route each claim to its owner. That action changes practice while leaving every substantive ontology and Method with its direct pattern.

This also explains the UTS decision. Familiar spelling is insufficient for one `UnifiedTermRow`. A durable public row is considered only for an independently governed value after its own naming and use tests; the umbrella word creates neither that value nor a Bridge among the branches.

### E.10.LRN:11 - SoTA Echoing

| Source line | Adopted distinction | Limit retained here |
| --- | --- | --- |
| OECD, [*Teaching Compass*](https://www.oecd.org/en/publications/oecd-teaching-compass_8297a24a-en.html), 2025 | Keep teaching agency and practice distinct from student competency development. | The framework does not define FPF kinds or prove capability from teaching occurrence. |
| ISO/IEC 22989:2022 terminology as reused by [ISO/IEC TS 42119-2:2025](https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso-iec%3Ats%3A42119%3A-2%3Aed-1%3Av1%3Aen) | Treat ML as computational optimization of model parameters and keep the resulting model and testing distinct. | Source-local terminology does not settle human learning, deployment capability, or generalization evidence. |
| Goodfellow et al., [*Generative Adversarial Nets*](https://arxiv.org/abs/1406.2661), 2014 | Separate minimax training Work, trained models, and generated samples. | Historical anchor; it does not establish every current GAN evaluation or deployment claim. |
| de Boer et al., [*Guiding Curiosity*](https://onlinelibrary.wiley.com/doi/10.1111/desc.70229), 2026 | Preserve the current empirical contrast between performance-based and information-based uses of “learning progress.” | Shared source wording does not make capability change and information gain the same FPF result. |
| Tajwar et al., [*Training a Generally Curious Agent*](https://proceedings.mlr.press/v267/tajwar25a.html), 2025 | Keep trained information-gathering capability, interaction data, environment feedback, and transfer conditions explicit. | One agent-training line does not supply a universal curiosity or learning objective. |
| Papert and Harel, [*Situating Constructionism*](https://web.eecs.umich.edu/~mjguz/csl/home.cc.gatech.edu/allison/uploads/4/papert91.html), 1991, and Kafai et al., [*Designing Constructionist Futures*](https://mitpress.mit.edu/9780262361095/designing-constructionist-futures/), 2020 | Treat public/shareable construction as a Method and evidence-design commitment, not a synonym for incremental constructivism. | Artifact existence does not prove authorship, capability, transfer, or retention. |
| Segovia-Martin et al., [cultural-evolution review](https://www.cambridge.org/core/journals/evolutionary-human-sciences/article/cultural-evolution-a-review-of-theoretical-challenges/F1DAA0367EBB4F7866F9B624DB2D9BEA), 2024 | Keep copying and reconstructive transmission alternatives and the unit-of-transmission question open. | A pattern can be one named cultural variant without becoming a universal meme or knowledge atom. |

Recheck a source line only when a newer edition changes a distinction used by this Solution or when contrary evidence shows that the current branch boundary changes a practitioner action. Recency alone does not merge branches.

### E.10.LRN:12 - Relations

- **Selected by:** `E.10` and `E.10.ARCH` when learning-word recovery is current.
- **Builds on:** `F.0.1`, `F.0.2`, `F.1`, `F.17`, `F.18`, `C.2.1`, A.3, A.15, `A.2.2`, `A.10`, `A.6.3.RT`, `C.16`, `C.29`, and `C.36`.
- **Returns to:** the direct human-capability, Work, Method, statistical-model-fitting, inference, experiment/data-acquisition, representation, product, publication, organizational, cultural, evidence, or decision pattern selected by the recovered claim.
- **Keeps outside:** one generic Learning process, learner/teacher role kinds, teaching or training Method selection, capability assessment, model fitting, inference, experiment design, evidence qualification, causal explanation, and choice.

### E.10.LRN:End

