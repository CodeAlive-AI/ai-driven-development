## CMP.7 - Construct a Learner from Examples and Feedback

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### CMP.7:1 - Problem frame

**Use this when** examples or feedback are available and the required rule for further cases is missing, or an existing learning procedure must be changed for a different target, kind of feedback or resource limit. You need to construct the procedure that obtains the rule, rather than leave “learn the model” as an unexplained operation.

The situation occurs when learning a classifier, estimating a response, constructing a surrogate, discovering a program or updating a policy. The output may be a symbolic rule, a function represented by weights, a distribution or a retained set of candidate rules. Its required form follows from the intended use.

The gain is a learning procedure with explicit inputs, selection or update operations and a learned result that can be applied at its warranted scope. The reader needs functions, finite examples and a loss or another stated comparison. Probabilistic guarantees require the corresponding additional probability model.

Use an existing rule directly when it already serves the purpose. Use an established learner when its inputs, target, restrictions and costs fit. This pattern is needed when those choices or their connection to further use must be constructed or revised. Explaining a learned rule and teaching a person to apply it are distinct tasks, supplied by the explanation and development methods when required.

### CMP.7:2 - Problem

How can a computation turn examples and feedback into a useful rule for further cases, with a clear distinction between fitting the observed examples, obtaining the rule affordably and justifying its further use?

Many rules can agree on the available examples and disagree elsewhere. Faster optimization can obtain one of them more accurately while leaving that disagreement unresolved.

### CMP.7:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Expressive rules and learnability | A large rule family can represent more targets while requiring more information or search. |
| Available feedback and target use | Recorded labels or rewards may differ from the response the recipient needs. |
| Fit and generalization | Low loss on used examples leaves questions about unseen cases and changed conditions. |
| Statistical and computational efficiency | A class can be learnable in principle while obtaining its selected rule remains unaffordable. |
| Stability and adaptation | Retaining past information helps under stable conditions but can obstruct a changed target. |
| Point prediction and retained ambiguity | One chosen answer is convenient; unresolved alternatives can matter to the next action. |

### CMP.7:4 - Solution

**State the further use → identify available feedback → restrict the rule family → construct selection or update → establish its result → apply and revise.**

#### CMP.7:4.1 - State what a further application must obtain

Describe the input on which the learned rule will be used, the required response and the loss or gain that matters. Include the region, population, time or interaction conditions when they change that meaning. A rule predicting an observed label, a latent property and the consequence of an intervention answers different questions.

Separate the learning algorithm from the learned rule. In a batch setting, write `A(S)=h_S`: algorithm A consumes the examples S and returns rule `h_S`. A later application computes `h_S(x)` on a new input x. In an online setting, the learner also carries state and updates it as feedback arrives. The cost of obtaining a rule and the cost of applying it may favor different constructions.

State whether the recipient needs one rule, a set of alternatives, an uncertainty statement or an action selected from predictions. The output type changes what the learner must retain. A rule can be useful under a qualified assumption without an unconditional guarantee over all possible inputs.

#### CMP.7:4.2 - Recover the examples and feedback actually available

Identify the supplied inputs, labels, rewards, demonstrations or other observations and how they were obtained. For missing labels, delayed feedback, selection effects or dependence between examples, state what the learning procedure can observe. Distinguish information available when the prediction is due from feedback for later predictions. MMP.7 supplies the probability model of recorded data when such a model is needed.

Choose the feedback regime before deriving the update. In supervised learning, the supplied target response can evaluate a candidate prediction directly. In bandit feedback, only the consequence of a chosen action is observed; an update requiring all unchosen consequences is unavailable. A self-produced label remains the output of another rule and can propagate its errors.

State which conditions are fixed during the learning claim. Independent examples from one distribution, an arbitrary sequence generated by one stable target rule, and a changing target support different arguments. Data rows alone do not supply any of these assumptions.

#### CMP.7:4.3 - Construct the rule family and inductive restriction

Choose a family H of candidate rules and a representation in which they can be compared or updated. It may contain thresholds, programs, trees, parameterized functions or another suitable construction. Give the operations needed to apply a rule and obtain its response.

The restriction expresses which unobserved continuations the learner will consider plausible. It can come from subject structure, invariances, a simplicity preference, regularization or a previously learned representation. State the basis and the limit of the restriction. Choosing a rule family is an inference commitment, not merely a software parameter.

MMP.11 can supply a subject-grounded function family. For a surrogate, state the source responses and input region that the learned rule must serve. This pattern supplies the algorithmic way of obtaining a member or a supported collection of members from examples. If no candidate can serve the target, improve the family or representation rather than trying to optimize within it indefinitely.

#### CMP.7:4.4 - Give an effective selection or update procedure

Choose how data and feedback change the candidate:

| Construction | Effective operation | Principal condition |
| --- | --- | --- |
| Select from a finite family | Evaluate each rule on the relevant examples and select by the stated criterion, with an explicit treatment of ties. | The family and evaluations must be affordable. |
| Retain consistent candidates | Remove rules contradicted by newly observed feedback; use or combine the survivors. | Every observed label used for elimination must agree with one fixed target rule in the initial family. |
| Optimize a parameterized criterion | Construct updates or search using CMP.6 or CMP.4, including initialization, constraint handling and stopping. | Optimization progress and the meaning of the learning criterion both need their stated conditions. |

For empirical risk minimization, a typical criterion is the average loss `L_S(h)=(1/n)*sum loss(h(x_i),y_i)`. Regularization or another restriction can change the criterion. An argmin expression specifies the desired rule; the learner needs a procedure for obtaining it, including what it does when the minimum is not obtained or several rules tie.

Look for shared work and useful ordering. For thresholds, sorting examples once can let successive threshold scores be updated from counts rather than reevaluated on the whole dataset. CMP.3 supplies sharing when its identity conditions hold. For a parameterized learner, compare the work of one update, the updates needed and the later cost of applying the result.

#### CMP.7:4.5 - Establish the learning result at the strength available

Distinguish three results:

1. **Obtaining:** the algorithm returns the stated rule or collection under its inputs and computational limits.
2. **Fit or update performance:** the returned rule achieves the stated empirical criterion, or the online procedure has the stated behavior on feedback.
3. **Further-use performance:** a bound, comparison, assumption or observation supports the response on the receiving cases.

Prove or check only the result needed for the use, with additional work selected through C.11.DUA. For example, a finite fixed H with a realizable target and independent examples from the receiving distribution permits a sample-based generalization argument. A finite online candidate family can instead support a mistake bound for an arbitrary sequence under a stable realizable target; independent sampling is then unnecessary for that bound.

In a statistical argument, retain the class, loss range, dependence and selection conditions used by the theorem. Repeatedly choosing rules against the same assessment examples changes what that assessment supports. In a changed environment, all historical observations need not have the same relevance to the future query.

When available examples leave candidates disagreeing at a consequential input, return that ambiguity or choose a rule under an explicit selection basis. Obtaining an additional response is one possible move, not a default obligation. Compare its likely effect with the cost of asking, delaying or acting under the remaining uncertainty.

#### CMP.7:4.6 - Apply the result and revise the part that fails

Use the learned output on the intended further case. A discrepancy can come from the rule family, data law, target definition, optimization, representation or application. Follow the dependency that failed rather than reflexively requesting more training examples or more optimization steps.

If the target changes over time, choose a forgetting, reweighting, windowing or adaptation procedure together with the relation to the new target. C.11.DUA helps decide whether a discrepancy warrants more examples or a changed procedure; the common portfolio methods can retain several useful rules. This pattern constructs the learning operation used in that arrangement.

Return the learned rule, its application method, the conditions material to its use and the narrow reason for reopening it.

#### CMP.7:4.7 - Train a primer for a fixed responder

Use this when a capable responder can produce worthwhile alternatives, yet direct requests repeatedly elicit similar answers. Keep a direct request and an adequate hand-written prompt as baselines. The adjustable component is a policy that writes an additional prompt, the *primer*. The original task and primer go to the fixed responder. Its response is what the recipient uses.

During training, sample several primers per task and several responses to each primer. Evaluate their quality, their difference from a declared reference collection and diversity among responses. Use the responses to give credit to the policy that produced each primer. Keep the responder fixed during that update. On held-out tasks, apply the trained primer policy and the same responder. For comparison with direct generation and the adequate hand-written prompt, give each task the same reference collection and acceptance criteria. Keep responses that meet both the quality criterion and the required difference from that collection, then count the semantically distinct responses among those retained. Report quality losses that matter to the recipient. Use comparable sampling budgets. Count policy training, responder samples, scoring and both calls at use. If an adequate supplied primer still fails, examine the responder's capability. A search over prompt text through an API is another implementation with its own update and cost.

[Albalak et al.](https://arxiv.org/html/2611.11740v1) used a reference set fixed before training. A distance from that set can reward repeated discoveries made after it was frozen. For a claim about continuing novelty, retain a common comparable set of tasks and update each practice’s own history under a stated rule. At each observation, establish how many different responses meet both its quality and novelty criteria. Compare those results and their costs under the same task conditions. Distances from different histories express different comparisons. Use a shared reference as well when the judgement requires novelty relative to the same prior collection. The extra cost of two-stage generation can make direct generation preferable for the intended use.

#### CMP.7:4.8 - Generate with restricted topic knowledge and refine with a knowledgeable model

Use this when familiar answers dominate and there is a way to assess proposals that depart from them. Specify which knowledge is restricted in the generator and how to check the restriction. Retain its ability to express a coherent proposal. In [D’Ambrosio et al.](https://arxiv.org/html/2611.11725v1), filtering topic material during training and continued training that induces partial forgetting were distinct interventions. Delaying access to documents or asking a knowledgeable model to simulate unfamiliarity makes a different intervention. Keep a knowledgeable generator as a comparator.

Give the original task and the initial proposal to a knowledgeable reviser. Ask it to preserve the proposal's distinctive idea while correcting errors or supplying missing conditions. Retain both versions. Examine what survived, then assess originality, fitness for use and feasibility separately. A replacement idea can enter a new branch. An incoherent initial proposal, an idea lost during revision and a preserved but infeasible idea call for changes to different components. Compare the complete arrangement with direct expert generation and with knowledgeable generation given the same revision and assessment budget. Count model preparation, generation, revision, judging and the cost of testing a proposal.

The experiments used model judgements of proposals. A feasibility judgement can select a trial. Feasibility in the intended practice needs its own demonstration. The study found no scoring advantage in neuroevolution at 1B or backpropagation at 7B under the reported conditions. Check the intended domain and the generator's capacity before paying for training.

#### CMP.7:4.9 - Train a function while changing its internal representation

Use this when current predictions fit but later changes or generalization matter, and the learner's internal computation can be examined and changed. Define the next task and any earlier responses that must survive. Compare ordinary training and an adequate familiar regularizer under stated budgets. Decide whether you need generalization to new inputs, adaptation within the present family, retention through an update or learning a new family. These require different observations.

A Unified Factored Organizer (UFO) is a low-capacity nonlinear autoencoder used during training. Choose the primary network's internal quantities, such as node activations or attention weights, and normalize them across the training batch by component. For intracomponent regularization, each vector records one component's responses at fixed input positions. Preserve those positions across batches. In the reported finite-domain experiment, absent inputs occupy zero-filled positions and contribute no reconstruction loss. Reordering a minibatch must preserve which input each position denotes. An intercomponent vector records one input's responses across a layer's fixed components. For attention, identify heads and query/key positions consistently. The reported fixed-length sequences preserve these roles; variable lengths require a further construction. Choose coordinates and storage that are feasible for the domain. Train the primary network on task loss plus a weighted reconstruction loss. Hold the organizer's parameters fixed in that update while passing the gradient through it. In a separate update, keep the primary network fixed. Within each intracomponent vector, select the lowest-error entries. For intercomponent regularization, select the lowest-error complete vectors within each layer. The organizer receives the complete vectors; selection determines which reconstruction errors contribute to its update. Specify the selection rule and how the reconstruction weight increases from its initial value. The primary network can then perform the task without running the organizer.

Compare the ability to solve the declared next task, retention of protected responses, successful runs and total training cost, including the organizer, its activations and both updates. A reduction in steps to a threshold can still be costly per step. Reconstruction loss alone cannot establish the ability to learn a different family. [Sheppard et al.](https://arxiv.org/html/2611.11862v1) give the training construction and its experimental conditions. [Lehman and Stanley](https://arxiv.org/html/2611.11020v1) separately compare how compatible and incompatible changes and the size of an update affect retention. Use a change whose required effect you can identify to decide whether the next intervention belongs in the representation, the update or the new training task.

### CMP.7:5 - Archetypal Grounding

#### CMP.7:5.1 - Construct a batch selector and expose an unresolved continuation

On nonnegative integer inputs, consider the two rules `f(x)=x` and `g(x)=x mod 2`. The supplied examples are `(0,0)` and `(1,1)`. Both rules have zero squared loss on those examples.

A learner can evaluate both rules and return the minimizing set `{f,g}`. The returned set retains the ambiguity. It can also return one rule under a declared preference, but the zero training loss alone gives no reason to prefer f over g at input 2. Their predictions there are 2 and 0.

Suppose a prediction at 2 is due before its response is revealed. The two original examples leave both 2 and 0 possible. Give a point prediction under a stated selection rule, or return both if the recipient can use that answer. With a fixed noiseless target in {f, g}, an earlier observation at 3 can settle the prediction. A response of 3 selects f and predicts 2 at input 2. A response of 1 selects g and predicts 0 there. Once the response at 2 arrives, it can answer a request for the observed value and update the rule for later inputs. To evaluate the prediction, compare the answer recorded before the deadline with the response subsequently observed at input 2.

**Changed response:** consider only the original two observations and a response of 1 at input 2. Each rule has mean squared loss 1/3 on these three observations. If an exact fit is required, revisit the two-rule family or the noiseless-target assumption.

#### CMP.7:5.2 - Construct an online learner and derive its mistake bound

Let H be a finite family of binary prediction rules and suppose one fixed rule in H gives every true label that will arrive. Retain the set V of rules consistent with all labels seen so far. On a new input, predict the majority label among rules in V, using a fixed tie rule. After receiving the true label, remove the rules that predicted otherwise.

On each mistaken prediction, at least half of V is removed. The true rule remains, so after M mistakes `1≤|H|/2^M`, giving `M≤log2|H|`. This establishes a bound on mistakes for an arbitrary input sequence under the stable-realizable-target assumption. It does not require independent random examples. Evaluating all survivors on each input costs up to `|H|` rule evaluations; the mistake guarantee alone does not make an enormous family affordable.

For a concrete instance, let inputs be integers 0 through 4 and let H contain six threshold rules `h_t(x)=1 if x≥t else 0`, for `t=0,...,5`. Break ties by predicting 1. At input 2, three rules predict each label, so predict 1. If the true label is 0, retain thresholds 3, 4 and 5. At input 3, the majority now predicts 0; if the true label is 1, retain only threshold 3. The two mistakes are within `floor(log2 6)=2`; subsequent predictions follow `h_3` correctly as long as the assumed target remains `h_3`.

**Changed feedback:** a later example gives label 1 at input 2. It contradicts the previously received label at 2. Eliminating the last rule would leave an empty set. The stable noiseless-target premise has failed: retain the discrepancy and choose a treatment for noise or change, such as weighting errors or using a recent-data learner. The earlier mistake proof cannot be carried through that change unchanged.

### CMP.7:6 - Bias-Annotation

Training loss and benchmark performance are visible and easy to optimize. The recipient may instead need a response in a different region or after an intervention. Keep that target explicit so that improving the visible criterion does not silently replace it.

A broad function class or large pretrained model can hide a strong inductive restriction in its representation, training history and obtaining procedure. The relevant question is which continuations it favors and how that choice fits the receiving use.

### CMP.7:7 - Conformance Checklist

- The future application, output type and relevant loss or gain are recoverable.
- Available examples and feedback match the operations the learner performs.
- The candidate family or other inductive restriction has a stated basis and boundary.
- Selection or update is effective, with tie, failure and stopping behavior specified.
- Obtaining, fit and further-use claims retain their distinct conditions.
- Statistical or online guarantees use the sampling, target and class assumptions they require.
- A contradictory or changed case leads to the relevant data, family, target or update revision rather than automatic extra training.

### CMP.7:8 - Common Anti-Patterns and How to Avoid Them

| Misstep exposed by the method | Consequence and repair |
| --- | --- |
| Use zero training error as a prediction argument | Identity and parity agree on the examples but disagree at 2. Retain the ambiguity or supply the selection basis relevant to further use. |
| Treat an optimization formula as the learning algorithm | The chosen rule can remain unobtainable. Supply effective selection or update with its computational cost. |
| Use feedback that the agent never receives | A bandit update can silently assume labels for unchosen actions. Match the operation to the actual observation regime. |
| Keep eliminating candidates after the fixed-target premise fails | The threshold example leaves no survivor. Revise the treatment of noise or change and its result conditions. |
| Assume more data or computation always resolves the failure | An inadequate family or wrong target can survive both. Locate the changed dependency before choosing more work. |

### CMP.7:9 - Consequences

Learning becomes an explicit algorithmic contribution: a reader can say what is supplied as feedback, how it changes a candidate, what rule is obtained and how that rule is used. The construction can be delegated or changed without leaving an unexplained “learn” step between modeling and computation.

The method can also expose a limit that further optimization cannot remove. New information, a better family, another target or a different receiving decision may be needed. The result remains useful when it identifies that choice without demanding unnecessary evidence.

### CMP.7:10 - Architectural Rationale

The learning algorithm and learned rule must remain distinct because their costs, inputs and failure modes differ. Inductive restriction belongs with the algorithm's construction: without it, agreement on examples leaves the future rule unspecified. Base the performance argument on the feedback and use in question.

MMP supplies data and subject-model accounts. CMP.4 and CMP.6 supply effective search or update; CMP.7 assembles those contributions into a learner. Further model assessment, explanation, development and portfolio choice use their existing methods.

### CMP.7:11 - SoTA-Echoing

[Shalev-Shwartz and Ben-David, *Understanding Machine Learning*](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf), chapters 2-5 and 21, supplies empirical selection, inductive restriction and online learning under different information assumptions. For a manageable finite family with a stable realizable target, adopt majority-and-elimination over choosing an arbitrary consistent rule when mistake reduction matters: one mistaken arbitrary choice may remove only one rule, while a mistaken majority removes at least half. Include the extra work of evaluating the surviving rules and counting their predictions. When enumeration is unaffordable or feedback is noisy, this finite-family construction requires replacement or qualification.

For a large parameterized family, [Bottou, Curtis and Nocedal](https://leon.bottou.org/publications/pdf/tr-optml-2016.pdf) supplies optimization procedures and separates their error from statistical error. Adopt an affordable update through CMP.6 when direct rule enumeration fails; retain the unclosed generalization question after numerical progress.

For changing environments, [Han, Huang and Wang, *Model Assessment and Selection under Temporal Distribution Shift*](https://proceedings.mlr.press/v235/han24b.html) develops adaptive recent-history comparison instead of treating all historical assessment data as equally representative. Adopt reconsideration of data relevance and the selected assessment window when time changes the target. The benefit trades reduced historical mismatch against fewer effective observations and depends on the paper's assessment conditions; it is not a guarantee under arbitrary unobserved change.

Revisit the learning construction when the assumed feedback ceases to be available, the target or admissible family changes, or another obtaining procedure improves the required result at comparable resources. Revisit only the affected selection, update or performance argument.

### CMP.7:12 - Relations

- **C.29.2:** supplies computational formulation and application conditions; **C.11.DUA** selects worthwhile additional information or computation.
- **MMP.7:** supplies the law of recorded data when probabilistic inference is used; **MMP.11** can supply the subject response family.
- **CMP.4, CMP.6 and CMP.3:** supply search, updates and reusable intermediate work for obtaining the rule.
- **C.2.8, EXD and the development DPFs:** address what a reader or learner must understand or acquire when using and explaining the resulting method.

### CMP.7:End
