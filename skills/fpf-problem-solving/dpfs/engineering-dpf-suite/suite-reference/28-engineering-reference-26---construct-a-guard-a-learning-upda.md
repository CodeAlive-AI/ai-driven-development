## Engineering.Reference:26 - Construct a guard, a learning update and an audit policy

**Use this when an agent's proposed action must be checked, its repeated choices need improvement, or scarce checking effort must be allocated.** A control requirement does not yet supply an executable check. Logged feedback does not yet supply a learning update. A good detector does not yet say which actions to inspect. The constructions below fill these three gaps on a service-configuration example. The learning applications address decisions separated by tool observations (26.4.1), allocation of training attempts (26.4.2), strategy and conditional execution (26.4.3), consequences retained across sessions (26.4.4), teacher-guided procedure transfer (26.4.5), and selective acquisition with remaining support (26.4.6). Enter at the gap you have; obtaining a guard does not require training a model or calculating an audit policy.

The reader is an agent-system engineer who can inspect typed calls and run short Python calculations. The example supplies a local policy, a finite learner and a two-step decision model. For deployment, the engineer still needs the actual authority, authenticated service facts, qualified execution interface and evidence about the receiving task population. The numbers below are stipulated teaching inputs. A calculation or a fixture run establishes its conditional result, not deployed protection or successful training of a language model.

[ADM.14](../../management-dpf-suite/adm/23-adm-14---connect-an-administrative-control-to-its-purpose-an.md) guides recovery of the protected purpose, requirement and competent interpretation; [ADM.8](../../management-dpf-suite/adm/18-adm-8---establish-and-exercise-the-required-permission-for-a.md) guides obtaining and exercising permission. [SYSE.28](../syse/48-syse-28---place-qualified-controls-in-a-supported-platform-u.md) explains how to place the resulting check on the real use path. [SYSE.45](../syse/66-syse-45---train-an-llm-policy-from-qualified-interaction-exp.md) and [CMP.7](../../foundational-thinking-dpf-suite/cmp/15-cmp-7---construct-a-learner-from-examples-and-feedback.md) develop the learner; [SYSE.51](../syse/72-syse-51---construct-adaptive-control-of-reasoning-and-tool-e.md) and [MMP.8.SD](../../foundational-thinking-dpf-suite/mmp/15-mmp-8-sd---construct-a-sequential-decision-model-from-inform.md) construct an affordable allocation with its future consequences. Their results can support the same execution procedure while retaining different meanings and reasons for change.

### Engineering.Reference:26.1 - Derive the check that the executor needs

Suppose the service owner has granted agent `M` permission `G1` to set `timeout_ms` on staging service `S`, to an integer from 1 through 60000 inclusive, during the interval `10 <= time < 20` on the gateway's stipulated clock. The supported interface is `timeout/ms-v1`; every mutation must name the service revision it expects. Other services, fields and operations are outside this grant. The instruction for the present job is “set the timeout to five seconds.” It requires 5000 milliseconds. A call setting 5 milliseconds can satisfy G1 and still perform the job incorrectly.

First derive the observations needed by the executor's decision. “Staging” must mean the namespace in the owner's registry, rather than a word in the agent's explanation. “Agent M” must mean the principal authenticated by the gateway. “During the interval” must hold when the mutation takes effect. The expected revision must match the same service at that point. If the owner instead meant that only submission must occur before time 20, that changes the rule; the programmer cannot settle this distinction by choosing whichever timestamp is easiest to read.

This yields separate predicates: authenticated principal is M; the proposed service, operation and field are S, `set` and `timeout_ms`; the current service evidence concerns S in staging; the schema is `timeout/ms-v1`; the proposed value is an integer in range; current time is inside the interval; and the current revision equals the proposal's expected revision. The binary admission question has three useful returns: **admit**, **deny for a known mismatch**, and **missing for unavailable required evidence**. The last two both withhold this mutation, but require different remedies. This check does not judge whether 5000 is the correct interpretation of the work request.

Here is a complete predicate evaluator for that supplied policy. Its typed evidence is supplied by a qualified gateway adapter; the evaluator does not authenticate arbitrary caller-supplied dictionaries. `now` and `revision` are integers in this fixture's clock and revision scheme.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Call:
    service: str
    operation: str
    field: str
    value: int
    expected_revision: int

@dataclass(frozen=True)
class Facts:
    principal: str | None
    service: str | None
    namespace: str | None
    schema: str | None
    revision: int | None
    now: int | None

def guard(a: Call, e: Facts):
    if any(v is None for v in vars(e).values()):
        return "missing", "obtain current authenticated facts"
    if e.service != a.service:
        return "missing", "evidence concerns another service"
    if e.principal != "M":
        return "deny", "principal outside G1"
    if (a.service, a.operation, a.field) != ("S", "set", "timeout_ms"):
        return "deny", "action outside G1"
    if (e.namespace, e.schema) != ("staging", "timeout/ms-v1"):
        return "deny", "namespace or interface outside G1"
    if type(a.value) is not int or not 1 <= a.value <= 60000:
        return "deny", "value outside G1"
    if type(a.expected_revision) is not int or a.expected_revision != e.revision:
        return "deny", "revision changed or unspecified"
    if not 10 <= e.now < 20:
        return "deny", "outside the effective interval"
    return "admit", "G1 predicates satisfied for this call and these facts"

proposal = Call("S", "set", "timeout_ms", 5000, 17)
facts = Facts("M", "S", "staging", "timeout/ms-v1", 17, 12)
assert guard(proposal, facts)[0] == "admit"
```

The construction is small enough to write directly. For a larger supplied policy, recover its constructors, names, precedence, defaults and intended observations through [CMP.12](../../foundational-thinking-dpf-suite/cmp/20-cmp-12---construct-an-interpreter-or-a-meaning-preserving-tr.md). For example, an ordered rule interpreter evaluates each rule against the bound action and facts, uses the first applicable decision, and denies if no rule admits the action. A missing fact needed to decide an earlier rule cannot silently become “rule does not match” so that a later permissive rule wins. Resolve it or return missing. A domain definition or an ordering decision absent from the policy returns to its competent interpreter.

When model assistance is useful, give the generator the interpreted requirement, typed action/evidence interfaces, available trusted queries, expected decisions and counterexamples. Ask for a plan linking each required predicate to its inputs, then executable predicates using only the provided operations. Check the generated program's imports, types, control flow and correspondence with that plan before running it in an isolated fixture. Reject invented evidence queries and self-attested authorization. A code generator can help obtain this evaluator; it does not supply the missing policy meaning or qualify its own result.

This route draws on distinct source constructions. [Progent](https://arxiv.org/html/2504.11703v3) supplies a programmable policy and mediated tool-use arrangement. [GuardAgent](https://arxiv.org/html/2406.09187v3) develops planning and code generation with retrieved examples and executable checking support. Where its retrieval is adopted, retrieve comparable input/output cases with their plans and code; its edit-distance choice is one concrete baseline, not proof of semantic relevance. Compare the relevant examples with a less relevant selection while keeping executable support available. A changed demonstration set and a removed toolbox change different contributions. The direct evaluator above needs neither retrieval nor generated code.

When the receiving work needs an ordered diagnostic category instead of admission, define the category meanings, their ordering and the action each supports before aggregating predicate results. Counting violated predicates does not establish severity, and a low diagnostic category grants no permission. Different binary guards, intent judges and categorical detectors cannot be substituted solely because each is called a verifier.

### Engineering.Reference:26.2 - Put the check on the action path and revise it under authority

Choose a mediation arrangement that actually covers the relevant tools. An embedded library can work when the developer controls the agent runtime and all protected calls. A gateway or endpoint proxy can mediate an existing agent if the execution service accepts protected calls only through that path. In this example choose the gateway: it authenticates the caller, reads the service registry and supported schema through its configured trusted interfaces, and obtains the current revision and clock value. It validates those returns before constructing `Facts`. An unavailable registry or an invalid return becomes missing evidence, not a guessed namespace.

Bind the result to the exact immutable `Call`, G1 edition and service facts used. The gateway submits that same call through an execution operation that atomically checks the expected revision and effective permission conditions before committing. A stale precheck can save work, but the authority window and namespace still have to hold at the actual effect. If the service cannot check them there, supply a qualified lock, lease or other preservation arrangement. Otherwise return the specific platform gap: this check cannot establish the required condition across the intervening change. An `admit` string handed back to an agent is not such an arrangement.

Use [SYSE.47](../syse/68-syse-47---construct-and-revise-an-agent-s-execution-procedur.md) to construct these continuations. Admission enables the bound mutation, followed by outcome reconciliation under [SYSE.42](../syse/63-syse-42---use-a-selected-tool-and-apply-its-result.md). Denial returns the specific mismatch to the actor or competent decision maker. Missing evidence calls the appropriate trusted source when that acquisition is permitted and affordable; an unavailable source leaves the mutation held. A malformed detector result likewise provides no admission. A revised proposal starts a fresh check. A rejected correction never falls back to executing the original unapproved proposal. If the actor has already halted and cannot consume a correction, a designated recovery performer must obtain and submit the continuation; feedback alone does not restart it.

The following cases exercise different dependencies. Keep the task's value requirement separate from G1's permitted range.

| Case | Obtained check and actual continuation |
| --- | --- |
| S, 5000 ms, authenticated M, staging, schema v1, revision 17, time 12 | Admit this bound call; the gateway's at-use check permits the mutation. Reconcile that S is actually at 5000 ms. |
| Same call, value 70000 | Deny the range violation. Return a revised job or authorized policy decision; do not clamp the value silently. |
| Same call, registry unavailable | Missing. Obtain the registry fact or return that gap; no protected mutation follows. |
| Same call for S, facts belonging to service T | Missing subject-bound evidence. Fetch S's facts; T's valid state cannot qualify S. |
| Check at revision 17, service changes to 18 before use | The conditional mutation refuses the old revision. Obtain current state and reconsider the intended change. |
| Check at time 19, effect would occur at 20 | At-use admission fails. A new window needs its competent grant; the earlier pass has expired. |
| Schema changes from millisecond v1 to second v2 | The old evaluator denies its out-of-scope interface. Obtain its meaning and construct the affected translation and check. |
| S, 5 ms, all G1 conditions satisfied | Admission is correct for G1; the job is wrong. Repair interpretation or action selection, as in section 26.3. |

When several agents act for one user with the same delegated rights, one shared boundary can suffice if the grant really covers their actions. Agents acting for different users or with different privileges need principal-specific decisions. Calling them one team cannot confer the broadest member's rights on everyone.

Finally, distinguish repairing a mistranslated rule from changing what the rule admits. Suppose the old policy allows `(S, set timeout)` and `(S, restart)`, while a proposed new policy allows only `(P, set timeout)` on production service P. The new set is smaller, but it adds an action outside the old set. Compute the newly admitted set `new_allowed - old_allowed`; its non-emptiness exposes the expansion. Return that addition to the production authority even if removing staging permissions is locally permitted. More generally compare admitted action sets, not rule counts: changed intervals, ranges and predicates can expand them. An authorized amendment then requires interpretation, evaluator qualification and at-use installation for the changed meaning. Better evidence about an existing case does not itself amend the grant.

### Engineering.Reference:26.3 - Prepare experience that can change the intended choice

The job family is setting staging timeouts from requests that state an integer duration from 1 through 60 seconds, or the corresponding milliseconds. These values fit G1. The worked failure is a five-second request producing 5 ms. First compare fixing a deterministic parser/converter, supplying the missing interface meaning, improving the controller, and learning an interpretation rule. If a reliable converter already answers the actual request form, use it. Training is an alternative when a recurrent choice remains, not a prerequisite for executing a known conversion. [Section 19.7](21-engineering-reference-19---make-an-available-contribution-wo.md#engineeringreference197---develop-the-arrangement-across-attempts) develops that whole-arrangement decision.

For the numerical learning example, deliberately restrict the missing choice. The prepared input contains an integer duration, an explicit unit and the available target schema. For known seconds under schema v1, the learner chooses among three program templates: A multiplies the duration by 1000; B leaves it unchanged; C asks for an already supplied unit. A is the desired choice for the specified task family. Direct millisecond requests and unknown-unit requests use separately supplied handling; the experiment does not teach arbitrary language interpretation. This finite learner exposes a real feedback-to-action update without pretending to reproduce a language-model training run.

Construct the experience with [SYSE.49](../syse/70-syse-49---construct-informative-tasks-and-feedback-environme.md). Prepare a resettable staging-service fixture with the same relevant schema, subject identity and effect semantics. For each request preserve what was visible before the proposal, the raw proposed call, guard observations, actual execution or non-execution, observed successor and independent task verdict. Reset before comparing alternative actions; a successor from another action or another revision is not interchangeable.

For “five seconds,” execute A and B separately in the authorized fixture: the resulting timeouts are 5000 and 5. Both pass the range guard, but the independently interpreted task target is 5000. Assign task reward 1 to A and 0 to B. C obtains no completed change and receives 0 for this fully specified case. For a request with no recoverable unit, asking is instead the useful action; copying C's zero reward into that case would train the wrong behavior. A teacher's corrected A call must obtain A's own qualified successor, or be retained explicitly as an action label without a claimed observed consequence.

A cached success receipt from an earlier 5000-ms change does not show the consequence of the present 5-ms proposal. Reuse a cached response as an observed successor only when its subject, action, initial state and environmental conditions support that equivalence. Otherwise obtain the new result or retain the response as a labeled model prediction. The arithmetic conversion target can remain valid while a claimed current service state is unsupported.

Two blocked proposals demonstrate why successful guarded traces are insufficient learning evidence:

| Observation | Useful evidence and warranted repair |
| --- | --- |
| The actor proposes changing production P, which G1 does not admit. | The raw proposal and policy comparison support a permission-violation label. There is no observed live effect of the blocked call. A separately authorized fixture may show its simulated consequence; record that scope. Preserve the live guard while changing the actor's proposal choice. |
| The actor correctly proposes 5000 ms, but an obsolete guard implements a maximum of 1000 despite the supplied G1 maximum of 60000. | Comparison with the interpreted requirement identifies a false rejection. Correct and requalify the guard. Labeling the proposal as task failure because execution was blocked would reward the wrong repair. The refused run alone provides no actual successor. |

Retain these observations separately from post-guard successes. A low observed failure rate after controls says something about the controlled arrangement. It does not establish that the raw actor learned the constraint. If counterfactual feedback is needed, obtain a qualified model or a permitted experiment and preserve its conditions; removing the required live guard does not follow from the learning need.

### Engineering.Reference:26.4 - Compute the update and use the changed rule

Represent the finite learner by three logits, initially zero. Softmax therefore chooses A, B and C with probability 1/3 each. Consider one sampled group containing one instance of each choice under the same prepared seconds request. Such a group is possible under the old policy; the example conditions on this realized group rather than asserting every draw contains it. Rewards are `(1, 0, 0)`. Their mean is 1/3 and population standard deviation is `sqrt(2)/3`. Normalizing by that deviation yields advantages `(sqrt(2), -1/sqrt(2), -1/sqrt(2))`.

This calculation uses a group-relative first update without reference-policy regularization. At the old policy, the importance ratio is 1 and clipping is inactive. For a mean objective over the three sampled actions, the gradient for logit j is `sum_i advantage_i * (indicator(i=j) - p_j) / 3`. Since these advantages sum to zero, it equals `advantage_j / 3`. A gradient-ascent step of size 0.3 gives logits approximately `(0.141421, -0.070711, -0.070711)` and probabilities `(0.382012, 0.308994, 0.308994)`.

The following code computes the step and consumes the result. A fixed draw of 0.35, chosen only to expose a changed selection, previously selected B and now selects A. The resulting proposal changes from 5 to 5000 ms. A live executor must still apply the guard and reconcile the effect.

```python
from math import exp, sqrt

def softmax(z):
    weights = [exp(v - max(z)) for v in z]
    return [w / sum(weights) for w in weights]

def first_group_step(rewards, rate=0.3):
    # This fixture has one old-policy sample of each of the three actions.
    mean = sum(rewards) / 3
    sd = sqrt(sum((r - mean) ** 2 for r in rewards) / 3)
    if sd == 0:
        return [0.0, 0.0, 0.0]  # No contrast in this group's feedback.
    advantages = [(r - mean) / sd for r in rewards]
    old = [1 / 3] * 3
    gradient = [sum(advantages[i] * ((i == j) - old[j])
                    for i in range(3)) / 3 for j in range(3)]
    return [rate * g for g in gradient]

def select(p, draw):
    cumulative = 0.0
    for i, probability in enumerate(p):
        cumulative += probability
        if draw < cumulative:
            return i
    return len(p) - 1

def propose_seconds(duration, action):
    return (1000 * duration, duration, "ask for unit")[action]

before = softmax([0.0] * 3)
after = softmax(first_group_step([1, 0, 0]))
assert propose_seconds(5, select(before, 0.35)) == 5
assert propose_seconds(5, select(after, 0.35)) == 5000
assert first_group_step([1, 1, 1]) == [0.0] * 3
print([round(p, 6) for p in after])
```

This is an obtained update and one changed action of the finite selector. It raises A's probability by about 0.048679 under the given representation; it does not make A certain. The selected draw is a demonstration of consumption, not an evaluation sample. Under a reversed reward `(0, 1, 0)`, the same arithmetic favors the wrong conversion. Under a format-only reward `(1, 1, 1)`, all choices are equally well formed and there is no relative update. More identical groups cannot repair that missing distinction. Diagnose the target and feedback before increasing compute.

[ToolRL](https://papers.nips.cc/paper_files/paper/2025/file/97c5b2707228e7e3fb67e4ecc2e0e607-Paper-Conference.pdf) develops structured format/correctness rewards, group normalization and clipped policy optimization for tool calls. The finite construction above adopts that distinction and explicitly specializes the first gradient step; it is not its complete algorithm. For further updates, retain the rollout policy and its action probabilities, recompute current-to-rollout probability ratios, apply the selected clipping rule, and resample when that recipe requires it. Do not repeat this first-step gradient as if every later ratio remained 1. A numerical implementation also needs its stated zero-variance convention, token/action aggregation and trainable parameters. For a language model, use the selected trainer's actual masking, tokenizer, optimizer and rollout implementation through SYSE.45; that implementation is an additional supplier.

Reward design and regularization are different choices. ToolRL removes the reference-policy KL term and compares that choice with keeping it; its observations concern its tested setup. To compare the alternatives in a receiving implementation, keep the task feedback, rollout preparation and assessment cases fixed, then vary the stated reference, coefficient and regularization rule. Observe retained useful behavior and complete training effort as well as task success. Removing the term does not remove runtime permission or imply that every previously useful behavior survives.

Test further use on held-out values and request forms, including explicit milliseconds, absent units, changed service identities and previously useful refusal behavior. Split related templates and trajectories together when their dependence would leak the answer. Keep assessment cases out of reward and policy selection; after using a failure to revise the learner, obtain an appropriate new assessment basis. Compare the trained configuration with the deterministic converter and supplied-support configuration, including preparation, annotation, training, retries and execution costs. An improvement in the sampled objective alone cannot settle this comparison.

If the interface changes to seconds in schema v2, the old multiply-by-1000 template is wrong for that output. Repair the target-schema translation and the affected learning examples or parameter branch; continue asking when the input unit is unavailable and retain principal, service and permission checks. If only the input value changes from five to twelve seconds under v1, A's same operation produces 12000 ms without a new unit rule. These changes expose different dependencies.

Here the retained logit update is the finite learner's training result. An update within the current task can instead serve episode adaptation; state whether its learned state resets at the next task or carries across tasks, and assess that choice under its actual conditions. Adding a fact or a teacher's instruction to the next context supplies support. Grammar restriction controls the possible output language. Each can improve a run, but a successful supported or constrained run is not by itself evidence of durable learning.


#### Engineering.Reference:26.4.1 - Learn from interleaved actions and observations

Use this application when a policy makes several decisions during an attempt, tools supply intervening observations, and the engineer must turn those attempts into a parameter update. A final failure can follow a useful earlier call. The work is to construct a learning signal whose meaning survives that distinction, update the selected policy, and use it with the support it still needs. The reader can use the finite calculation below directly; training a language model additionally requires the tokenizer, rollout engine and optimizer selected under SYSE.45.

The earlier conversion example has one learned choice. Here the choices are separated by an observation. [CMP.7](../../foundational-thinking-dpf-suite/cmp/15-cmp-7---construct-a-learner-from-examples-and-feedback.md) supplies the learner construction, [SYSE.45:4.2 through SYSE.45:4.3](../syse/66-syse-45---train-an-llm-policy-from-qualified-interaction-exp.md#syse4542---obtain-experience-with-interpretable-feedback) the experience transformation and selected training intervention, and [SYSE.49](../syse/70-syse-49---construct-informative-tasks-and-feedback-environme.md) the qualification of tasks and feedback. The calculation makes their connection explicit. For an actual calculator service, a direct arithmetic controller is the obvious competing way to obtain the answer; use this deliberately small learner to understand and test the update construction.

##### Engineering.Reference:26.4.1.1 - Keep the generated choices and their available histories

The task is to return `(n*m)+k`. The supplied calculator evaluates multiplication or addition exactly. A finite policy has two trainable scalar logits, initially zero. The first chooses `n*m` with probability `sigmoid(z1)` and `n+m` otherwise. After receiving the calculator's return `o`, the second chooses the answer `o+k` with probability `sigmoid(z2)` and `o+k+1` otherwise. The second logit is shared across these histories, but its answer still consumes the actual observation. The input supplies `n`, `m`, `k` and the calculator's meaning. The arithmetic operations and the available choices are provided capabilities; only their choice probabilities are being learned.

The worked example stipulates the following four recorded episodes, sampled in this deterministic fixture with the same unchanged old policy. Each generated choice had probability 0.5. The example conditions on this realized group; another four draws need not cover all four combinations.

| Episode | Generated calculator call | Observed return | Generated answer | Independently checked terminal reward |
| --- | --- | --- | --- | --- |
| A | `17*19` | 323 | 328 | 1 |
| B | `17*19` | 323 | 329 | 0 |
| C | `17+19` | 36 | 41 | 0 |
| D | `17+19` | 36 | 42 | 0 |

For B, the first learning record contains the request, tool meaning, selected multiplication call and its old probability. The second contains that same request, the actual call, its observed return 323, the selected answer 329 and its old probability. The result checker supplies reward 0 outside those decision inputs. It does not put the correct answer into the policy's earlier history. Preserve the producing configuration and the observations needed to interpret each record.

Select the two generated decisions as policy-output positions. The calculator return stays in the second decision's input and has no policy-output target of its own. For a language model, the same distinction concerns generated tokens and externally supplied tokens; the selected trainer must implement both the mask and the intended loss normalization. A tag that the model can forge does not authenticate a tool result. Obtain observations through the execution interface and preserve their provenance. A missing or altered return requires repairing the experience or defining the resulting different input condition.

##### Engineering.Reference:26.4.1.2 - Calculate an outcome update and consume it

Choose a mean of separate generated-decision terms. Let `A_i` be episode i's reward minus the group mean, divided by the population standard deviation. Use zero advantages for a zero-deviation group. For this group the advantages are `(sqrt(3), -1/sqrt(3), -1/sqrt(3), -1/sqrt(3))`. Each episode has two generated decisions. A complete surrogate for this finite adaptation is:

```text
rho_it = current_probability(action_it | history_it)
         / old_probability(action_it | history_it)
J = mean_over_episodes[
      mean_over_generated_decisions[
        min(rho_it*A_i, clip(rho_it, 0.8, 1.2)*A_i)
      ]
    ]
```

Maximize J. This example uses no reference-policy regularizer. Keep the old probabilities fixed during this update. At the old policy all ratios are 1 and clipping is inactive. For either logit, the derivative of a chosen binary action's log probability is `choice_bit - 0.5`, where bit 1 denotes multiplication or `o+k`. Averaging both decisions and all four episodes gives gradient `(1/(4*sqrt(3)), 1/(4*sqrt(3)))`. An ascent step of size 0.3 gives logits `(0.0433012702, 0.0433012702)` and choice probabilities `(0.5108236264, 0.5108236264)`.

This code prepares the histories, obtains the first update and uses the resulting probabilities on a new input. It also shows which parts of the operation are supplied by the fixture.

```python
from math import exp, sqrt

def sigmoid(z):
    return 1 / (1 + exp(-z))

def calculator(n, m, multiply):
    return n * m if multiply else n + m

# Recorded choices, returns and answers; the old logits are (0, 0).
raw = [(1, 1, 323, 328), (1, 0, 323, 329),
       (0, 1, 36, 41), (0, 0, 36, 42)]
request = (17, 19, 5, "calculator evaluates the selected expression exactly")
batch = []
for call_bit, answer_bit, observed, answer in raw:
    n, m, k, tool_meaning = request
    expression = f"{n}*{m}" if call_bit else f"{n}+{m}"
    assert observed == calculator(n, m, call_bit)
    assert answer == observed + k + (1 - answer_bit)
    batch.append({
        "generated": [
            {"history": request, "action": ("call", expression),
             "bit": call_bit, "old_probability": 0.5},
            {"history": (request, ("call", expression), ("return", observed)),
             "action": ("answer", answer), "bit": answer_bit,
             "old_probability": 0.5}],
        "reward": int(answer == n * m + k)})

def first_step(records, rewards, rate=0.3):
    # Only this frozen zero-logit policy's first step; two selected positions.
    count = len(records)
    mean = sum(rewards) / count
    sd = sqrt(sum((r - mean)**2 for r in rewards) / count)
    advantages = [(r - mean) / sd for r in rewards] if sd else [0.0] * count
    gradient = [sum(advantages[i] * (records[i]["generated"][j]["bit"] - 0.5)
                    / 2 for i in range(count)) / count for j in range(2)]
    return [rate * g for g in gradient]

def act(probabilities, n, m, k, draws):
    multiply = draws[0] < probabilities[0]
    observed = calculator(n, m, multiply)
    unshifted = draws[1] < probabilities[1]
    return observed + k + (0 if unshifted else 1)

old = [0.5, 0.5]
logits = first_step(batch, [row["reward"] for row in batch])
new = [sigmoid(z) for z in logits]
assert act(old, 12, 13, 5, (0.51, 0.51)) == 31
assert act(new, 12, 13, 5, (0.51, 0.51)) == 161
assert first_step(batch, [1, 1, 1, 1]) == [0.0, 0.0]
wrong = [sigmoid(z) for z in first_step(batch, [0, 0, 1, 0])]
assert wrong[0] < 0.5  # Rewarding C would encourage addition.
print([round(p, 10) for p in new])
```

Both runs retain the calculator. Reset the task's history for the new input; retain the updated logits. Under these supplied choices, the probability of selecting multiplication and the unshifted answer rises from 0.25 to approximately 0.260941. The fixed draws expose one changed action; they are deliberately chosen and supply no independent estimate of performance. The representation already makes the same choices applicable to new n, m and k. The calculation establishes a finite update and its consumption, rather than acquisition of those arithmetic operations by a language model.

B's useful multiplication call receives B's negative terminal advantage. The total group can nevertheless favor multiplication because it combines that contribution with A's success and the failed addition choices. Terminal weighting therefore supplies learning pressure to intermediate decisions without separately assessing the usefulness of each decision. [ToRL v1, §§2–3](https://arxiv.org/pdf/2503.23383v1) trains tool-interleaved math solutions with final-answer reward, retaining interpreter output as context while masking it from loss; its tested execution-error penalty was omitted from the main recipe. [Search-R1 v5, §3 and Appendix B.2](https://arxiv.org/html/2503.09516v5) likewise retains retrieved observations while optimizing generated output from terminal feedback. Its main implementation uses PPO, with GRPO as an alternative. These sources support the separation of observation, generated decision and outcome signal. The two-logit objective above is an explicit receiving construction.

Aggregation changes that construction. Including the tool return as a third item in this example's averaging denominator would multiply each gradient by 2/3, producing probability 0.507216 rather than 0.510824; the displayed draws would still yield 31. Alternatively, form a product of the two action ratios and clip that whole-episode ratio. With the same four rewards, its first gradient is twice the displayed gradient, giving probability 0.521637 at rate 0.3. Subsequent whole-episode clipping also differs from clipping each decision. Choose and document the objective actually implemented. In a language model, token lengths, generated-token normalization and observation masks must agree with that objective. Lengthening a return leaves this finite calculation unchanged only because its representation consumes the same integer observation and still has two generated decisions.

For further training, evaluate current-to-old ratios, clipping and any selected regularization under the actual trainer. Resample under a new rollout policy when that recipe requires it. This first-step derivative cannot be repeated as though every later ratio stayed 1. Retain a recoverable baseline, decide when learned parameters persist or reset, and assess changed and older useful behavior on separate cases as in section 26.4.

##### Engineering.Reference:26.4.1.3 - Obtain a separate reason to credit a call

If the work needs a positive assessment of B's first call, select what that assessment means and obtain its grounds. Three different inputs can support three different operations:

| Available ground | Construction and first usable result | What remains to establish |
| --- | --- | --- |
| The domain requires obtaining the product `n*m`, and the observed return can be checked against it. | Compare each actual return with `n*m`. The call-subresult labels are `(1, 1, 0, 0)`. Use these as a separately qualified call-only target. | Obtaining the product establishes neither the final answer nor the necessity of using a calculator. A legitimate different solution may not need this subresult. |
| An independently qualified next-call annotation is available at the decision history. | Construct `(history, permitted tool definitions, gold call set)`. For this exercise the declared method supplies `calculator(expression="17*19")`. Both A and B match; C and D do not. | Establish that the annotation fits the chosen method and available input, including legitimate alternative calls. A final reward does not supply this gold set. |
| A qualified transition and continuation model is available. | Evaluate each first call with the old continuation under [MMP.8.SD:4.2 through MMP.8.SD:4.4](../../foundational-thinking-dpf-suite/mmp/15-mmp-8-sd---construct-a-sequential-decision-model-from-inform.md#mmp8sd42---construct-how-an-action-changes-the-world-and-the-available-information). Here multiplication's success probability is 0.5 and addition's is 0; the old mixture is worth 0.25. Subtracting that baseline yields call credits `(+0.25, +0.25, -0.25, -0.25)`. | These values require the supplied deterministic law, all available action combinations and the old second-choice probabilities. Sparse stochastic logs alone do not establish them. A changed continuation requires reevaluation. |

The first two rows assess a call against a checked subresult or a qualified annotation. The third compares its expected consequence under a specified continuation. None overwrites B's recorded final failure. The baseline subtraction and the choice to update only the first logit are receiving choices. Starting again from the zero logits, a call-only mean of probability-ratio terms using those continuation credits has first gradient 0.125 for z1 and zero for z2. At rate 0.3 it gives `z1=0.0375`; the answer decision still needs its own learning signal.

[ToolRL, NeurIPS 2025, §§2.1–2.4 and Appendix C](https://papers.nips.cc/paper_files/paper/2025/file/97c5b2707228e7e3fb67e4ecc2e0e607-Paper-Conference.pdf) supplies an annotated-call branch. It turns multi-step records into next-step tasks with preceding history, compares predicted and gold call sets using maximum matching over tool names, parameter keys and values, and normalizes the attainable score before scaling correctness to −3 through +3 and adding format reward. Group-relative advantages feed clipped policy optimization. Thus the first engineering input is a history with qualified call annotations. The source's exact scoring and trainer consume it. If only the four terminal rewards are available, either construct and qualify the additional annotations or continue with the outcome branch; silently calling those rewards gold calls would change the evidence. Call agreement still needs a separate check of the resulting effect in the receiving work.

##### Engineering.Reference:26.4.1.4 - Supply preparation and preference inputs when those branches are selected

When the starting policy rarely produces a usable tool interaction, demonstrations can make subsequent exploration feasible. Obtain successful executions with available task inputs, actual observations and checked outcomes. From A, construct a supervised pair from the initial history to the multiplication call, and another from the resulting history including 323 to answer 328. Fit the generated actions; supply the return in the later input. A corrected first call in C would need its own execution or other qualified consequence evidence. A label for that correction may be usable before such evidence exists, but it does not inherit C's return 36. The correction of B's final answer can instead use the already available 323 if the stated method warrants it.

[ReTool, ICLR 2026, §2 and Appendix A](https://proceedings.iclr.cc/paper_files/paper/2026/file/4038c9208dfc22644c60ad39c24e5c53-Paper-Conference.pdf) develops a preparation-to-update route: produce tool-interleaved traces from checked math solutions, retain their reasoning and failed attempts, filter format and final answers, and perform cold-start supervised training before PPO on new executed trajectories. Its main reward checks final correctness rather than code executability; interpreter output remains context and is masked from loss. For an adaptation, choose one executable parser contract and exercise it on the prepared examples. Figure 9 contains conflicting instructions about Markdown fences inside code tags. A receiving choice such as raw code inside those tags, with no Markdown fences, resolves that conflict locally; it cannot be attributed to an unambiguous source instruction. If checked demonstrations or an executable serialization are unavailable, return that precise preparation gap before claiming the policy was prepared.

A preference update requires two available, comparable outputs and a justified ordering. For the same request, A and B provide a simple qualified pair: prefer the checked correct answer over the checked incorrect one. They share the same first call and observation. Retain both histories, their generated actions, the ordering grounds and a fixed reference policy. If sampling supplies only rejected outputs, obtain a warranted preferred one or use a different available feedback regime. Relabeling one of the failures as preferred would teach a different objective.

For a concrete finite preference update, let `P(A)` and `P(B)` be products of policy probabilities of the generated decisions, conditional on each recorded history. The tool return has no generated-output probability in these products. With reference probabilities from the old zero-logit policy, minimize:

```text
loss = -log(sigmoid(beta * (
       (log P_current(A) - log P_current(B))
       - (log P_reference(A) - log P_reference(B)))))
```

Set beta to 0.3. At the reference policy, gradient descent with rate 0.1 changes only z2, from 0 to 0.015, giving unshifted-answer probability 0.503750. The shared call cancels from the pair comparison, so z1 remains zero. On the new `(12,13,5)` input, draws `(0.49,0.501)` select multiplication in both policies, then answer 162 before this preference update and 161 after it. This adaptation exhibits the pair's particular information: it can change the answer choice without pretending to distinguish the shared calls.

[Tool-Star v1, §3.2, Algorithm 1 and Appendices B–E](https://arxiv.org/html/2505.16410v1) combines preparation, masked group-relative training and preference updates. It separates direct successes, tool-assisted successes and intended harder failed questions, then samples candidates after GRPO and uses scores at least 1 for preferred outputs and below 1 for rejected outputs. Keep the actual contrasting candidates and the executable reward grounds. The source's earlier correct-trace filter leaves the supply of both-failed questions underspecified; retaining their question IDs before filtering is an explicit receiving repair. Its printed negative DPO loss and ascent wording also conflict. The finite example above descends that loss: reversing the sign would reduce the preferred answer's probability to 0.496250. These repairs state how this application works without claiming what the authors' code did.

##### Engineering.Reference:26.4.1.5 - Change the learned objective deliberately

A policy may first need to learn the interaction protocol and later to solve the task. Label the stage and its objective when preparing feedback. [R1-Searcher v2, §§2–3](https://arxiv.org/html/2503.05592v2) first gives 0.5 for using retrieval at least once and 0.5 for acceptable format, with no answer reward. Its second stage removes the retrieval bonus, uses answer F1 and penalizes format violations by −2. This is a change in what receives reinforcement. The later policy still needs retrieval and its external evidence; a protocol reward has not taught all the reasoning required for the answer.

In the calculator example, all four episodes use a call and a well-formed answer. Giving each reward 1 for those properties produces zero group-relative update. Giving only C reward 1 makes addition more likely. Both calculations can be correct while their feedback fails the intended task. Preserve the original observations and identify the objective used to rescore or collect each batch. Decide the transition using actual usable interaction and later task behavior. A stage number alone supplies no evidence that the earlier capability was acquired.

Check the reward against the behavior it could make attractive. Tool-Star's collaboration bonus uses search and Python markers in a correct response; marker presence alone does not establish that either tool contributed. R1-Searcher's reported failures include fabricated document spans and long answers that collect likely gold-answer words. Bind tool observations to execution, check the required result independently and test plausible reward exploits. Redesign or narrow a defeated signal before extending reliance on its optimized value.

Finer intermediate feedback is another construction with its own costs. The [2026 outcome/process comparison, §§3–4 and Limitations](https://arxiv.org/html/2605.27881v2) finds that missing retrievable evidence can change the comparison; terminal-reward training remains competitive in its tested settings, while process signals trade query quality, redundancy and depth. First check that the receiving environment can supply the needed evidence and that the outcome baseline is usable. More detailed reward cannot retrieve a fact absent from the available corpus.

If long interactions still leave an important attribution problem, [TRACE v1, §§2–3 and Appendix A](https://arxiv.org/html/2607.13988v1) supplies a progress-estimation alternative. A frozen reference model scores the known answer at successive tool-boundary prefixes; changes in log likelihood contribute turn-level credit combined with outcome advantage. That route needs reference answers, prefix-scoring access and a qualified estimator. Increased answer predictability is the estimator's signal; it does not by itself establish causal usefulness of a call. Qualify it for the receiving outputs and preserve its aggregation with terminal feedback. A missing reference answer or unreliable scorer returns that branch to obtaining feedback, while a viable outcome method can remain usable.

The resulting engineering choice is between available, qualified learning constructions. Start with the signal and support the work can actually supply; obtain a missing prerequisite when the needed distinction depends on it. Carry the selected update into subsequent execution, then compare actual task results, preserved useful behavior and total cost on appropriate separate cases. A larger reward, more prepared examples or a changed parameter value alone does not establish the intended improvement.


#### Engineering.Reference:26.4.2 - Allocate training attempts and select the update

Use this application when an engineer can collect more interaction experience, but starts, tool calls and training share a limited budget. Another continuation can reveal a useful alternative; repeatedly exploring one uncertain history can also consume the budget without improving the learner. After collecting experience, ordinary clipped training can leave some rewarded actions on a plateau. Choosing where to collect experience and choosing how to update from it are two interventions with different inputs and consequences.

The construction below connects an affordable allocation to executed continuations, qualified feedback, a masked update and subsequent action. It specializes [ARPO, ICLR 2026, §§2–3 and Algorithm 1](https://proceedings.iclr.cc/paper_files/paper/2026/file/1c58e53bdf1fb045440256fd567531ae-Paper-Conference.pdf) and [AEPO, WWW 2026, §4 and Appendix A](https://playbigdata.ruc.edu.cn/dou/publication/2026_WWW_AEPO.pdf), with explicit receiving choices. The finite calculator and ordinary learning construction are those of [26.4.1](28-engineering-reference-26---construct-a-guard-a-learning-upda.md#engineeringreference2641---learn-from-interleaved-actions-and-observations). [SYSE.49](../syse/70-syse-49---construct-informative-tasks-and-feedback-environme.md) supplies the task and feedback arrangement; SYSE.45 and CMP.7 connect that experience to the chosen learner. The engineer needs probability access and an update implementation in addition to an interface that executes tools. A text-only generation endpoint can still help collect experience. Obtain full distributions and a parameter-update operation through facilities that provide them.

##### Engineering.Reference:26.4.2.1 - Obtain a measure that can support the proposed decision

At a model-generated position t, obtain the complete next-token distribution conditioned on the actual history: `p_t(v) = softmax(logits_t / temperature)[v]`. Fix the tokenizer, vocabulary, temperature and history used for the comparison. Shannon entropy in nats is `H_t = -sum_v p_t(v)*log(p_t(v))`, with zero-probability terms taken as zero. It concerns that conditional distribution. For example, several possible phrasings can raise it while all phrasings express the same known answer. The external return belongs in the next history; counting the characters or tokens of that return does not obtain the policy's next-token entropy.

Obtain the logits or a facility that returns a qualified estimate before using this quantity to rank histories. Store which history and generated positions the estimate describes. A next-token distribution available at a saved prefix can be inspected before taking the next action. An estimator that needs K sampled positions must generate them, retain their resulting history and charge that work; it cannot be treated as a free observation at an earlier prefix. Reset an initial baseline for each fresh trajectory and retain its relation to any branched continuation. Comparing a new question with a cached baseline from an earlier question changes the measure.

A selected-token log-probability can suffice for a recorded action's importance ratio and still be insufficient for entropy. Suppose a four-outcome interface reports only that the selected outcome had probability 0.5. Its surprisal is one bit. If q is the normalized distribution over the other three outcomes, the complete entropy is `1 + 0.5*H_bits(q)`, between 1 and 1.792481 bits. Both `(0.5, 0.49, 0.005, 0.005)` and `(0.5, 1/6, 1/6, 1/6)` fit the log, but their entropies differ. The same selected probabilities at two histories therefore cannot establish their entropy order. Obtain the missing distribution or a qualified estimator; otherwise retain a feasible fixed or randomized allocation.

##### Engineering.Reference:26.4.2.2 - Allocate attempts and reserve the work needed to finish them

Separate a count of complete training trajectories from resource limits such as generated tokens, tool calls and elapsed time. Set aside resources to finish and qualify the original attempts before admitting branches. For example, two extra trajectory places, six extra tool calls and an upper bound of three calls per continuation admit at most two new continuations. With three calls left, at most one fits. Include retries, probability extraction and any pilot in the resource account. Shared prefixes may save work, but their existence does not bound the cost of their continuations. SYSE.51's budgeting principles help retain completion resources; the training sampler described here is a further selected construction.

One ARPO-inspired receiving rule starts N trajectories and reserves M−N of M complete trajectories for branches. Measure K initial generated positions and K positions after actual tool feedback. For the conference paper's literal normalization, define `delta_H = sum_t(H_after,t - H_initial,t)/V`, where V is vocabulary size. This is a scaled change, not the average over K. Choose alpha, beta and a threshold tau; branch when `alpha + beta*delta_H > tau` and both count and resource capacity remain. The strict comparison is deterministic. A randomized rule that compares a draw with a probability needs its own bound to [0,1] and yields different behavior, including when delta_H is zero.

To limit repeated allocation to a lineage, this application adds AEPO's proposed linear penalty. Let l count consecutive accepted branches with positive delta_H along that lineage. Start l at zero, use `score = (alpha + beta*delta_H)*max(0,1-0.2*l)`, and require score > tau. On accepting a positive-change branch, increment l for both the continued parent and its new child. Reset it on a later measured transition with nonpositive delta_H. These counter and reset conventions are receiving choices that make the procedure executable. Keep counters per lineage; a fresh, unrelated start has its own counter. Finish existing attempts when capacity is exhausted; unused trajectory places may return to fresh starts only when those starts and their completion fit the remaining resources.

AEPO also proposes choosing the split with a pilot. With B available training trajectories after charging the pilot, its paper rule is `m_raw = B*sigmoid(beta*(H_root - H_tool_average))`; higher initial entropy favors fresh starts, and higher post-tool entropy favors branches. Specify comparable windows and the averaging rule. This example chooses `m = min(B,max(1,ceil(m_raw)))` and reserves B−m branch places. For B=16, beta=0.2, H_root=1 and H_tool_average=2 nats, m_raw is 7.202656, giving eight starts and eight branch places. The sigmoid is a proposed allocation heuristic; it is not the optimum of the paper's separate linear information-gain proxy.

The pilot must be affordable before it can inform that choice. Suppose the whole budget permits 48 calls, the completed pilot used three, and each retained training trajectory may require up to three further calls. A conservative count bound is now B=15, so the same rule gives seven starts and eight branch places. Sixteen trajectories plus that pilot would need capacity for 51 calls. This bound deliberately forgoes possible shared-prefix savings; a more precise allocation can use qualified remaining costs. When the pilot or probability extraction cannot fit, the fixed split remains an available baseline. The finite run below uses that fixed split and needs no pilot.

##### Engineering.Reference:26.4.2.3 - Execute the selected continuations and prepare their learning records

Use the same task `(n*m)+k` and exact calculator as in 26.4.1. For this run, the old policy selects multiplication with probability 0.9 and the unshifted answer `observed+k` with probability 0.5. Each choice is one generated position with a binary vocabulary. The first-position entropy is 0.325082973 nats; the answer-position entropy after the tool return is 0.693147181. With K=1 and V=2, delta_H is 0.184032104. The analytic policy supplies both full distributions; no sampled look-ahead or extra tool execution is needed to obtain them in this fixture.

Take M=4, N=2, alpha=tau=0.5 and beta=0.2. Two supplied draws, 0.2 and 0.95, select multiplication and addition on `(17,19,5)`. Execute those calls, obtaining 323 and 36. Each saved history now needs only an answer, so an additional continuation needs zero further tool calls in this particular task. Consider proposals from the first lineage, that same lineage again, and the second lineage. Their scores are 0.536806421, 0.429445137 after the first acceptance, and 0.536806421. Accepting the first and third proposals spends the two reserved places and avoids assigning both to the repeated lineage. Assess this trial priority against fresh starts or a fixed split on the receiving tasks.

Finish each original and its one child using answer draws 0.1 and 0.9. The executed finite environment supplies these records:

| Saved history | Continuation answer | Terminal reward from the task checker | Old probabilities of the two selected decisions |
| --- | --- | --- | --- |
| Multiplication returned 323 | 328 | 1 | (0.9, 0.5) |
| The same multiplication prefix | 329 | 0 | (0.9, 0.5) |
| Addition returned 36 | 41 | 0 | (0.1, 0.5) |
| The same addition prefix | 42 | 0 | (0.1, 0.5) |

Two calculator executions supplied four completed trajectories. A shared prefix is copied into its descendants' training records; its call was executed once. These are correlated trajectories, not four independent executions. A real branch must obtain its own later observations and qualified feedback. When those are unavailable, the sampler has produced an allocation or a prefix, not a completed learning example. Return that missing execution or feedback before assigning the branch a reward.

Choose a mean over the two generated decisions of each of these four trajectories. Keep the actual return in the answer decision's history and exclude it from both the output loss and this denominator. Use the population-standard-deviation convention of 26.4.1: rewards `(1,0,0,0)` give advantages `(sqrt(3),-1/sqrt(3),-1/sqrt(3),-1/sqrt(3))`. The code uses zero advantages when reward dispersion is at most 1e-12, including equal rewards. This convention differs from a sample-standard-deviation implementation, which gives `(1.5,-0.5,-0.5,-0.5)`. Choose one with the learning rate and aggregation that consume it. Reweighting a shared prefix or retaining it only once also changes this construction; averaging descendant advantages is not generally equivalent under signed clipping and unequal lengths.

##### Engineering.Reference:26.4.2.4 - Select modulation and the backward operation separately

A later training checkpoint may already differ from the sampling policy. For the same records, take current multiplication probability 0.9 and current unshifted-answer probability 0.65. Keep the old probabilities and reward advantages fixed. For each generated position let r be its current selected-action probability divided by its old selected-action probability. The ordinary contribution to the maximized objective is `min(r*A, clip(r,1-epsilon_low,1+epsilon_high)*A)`. Its sign matters: moving a negative advantage outside the minimum changes the operation.

An optional AEPO-inspired intervention forms `A_tilde = A*(1 + a*z_H)`, where z_H standardizes the current token-distribution entropy. Select its population explicitly. Here it consists of all eight generated positions, with population standard deviation, a=0.2 and zero standardized values when the deviation is at most 1e-12. The current call and answer entropies are 0.325082973 and 0.647446639 nats, so their standardized values are −1 and +1. Their multipliers are 0.8 and 1.2. Calculate these values at the checkpoint and hold them fixed during differentiation, as with the advantages. Obtaining entropy for this operation is distinct from adding an entropy regularization term; an implementation must request the required probability information even when the regularization coefficient is zero.

The multiplier magnifies both positive and negative advantages at higher-entropy positions. A zero advantage stays zero. It can even reverse the reward signal: one zero-entropy position among one hundred positions with entropy log(2) has population-standardized value −10, giving multiplier −1 at a=0.2. This receiving construction stops the modulation branch whenever a multiplier is nonpositive. The unmodulated update remains available. A positive exponential multiplier, a bound or another normalization would be a separately chosen modification. This stop and the neutral treatment of tiny dispersion are implementation choices, not additional feedback or a theorem about entropy.

The second intervention changes how an upper-clipped positive term contributes to the update. Define `stop_gradient(r)` to return r's current numerical value while holding that denominator constant during differentiation. Replace the constant upper bound by `(1+epsilon_high)*r/stop_gradient(r)`. The complete term is:

```text
J_t = min(r*A_tilde,
          clip(r, 1-epsilon_low,
               (1+epsilon_high)*r/stop_gradient(r))*A_tilde)
```

Its forward value equals ordinary clipping at the checkpoint. Its backward operation differs. Away from ties, the coefficient multiplying `A_tilde * grad(log current_probability)` is:

| Condition | Ordinary constant-bound clipping | Stopped-denominator upper bound |
| --- | --- | --- |
| A_tilde > 0 and r > 1+epsilon_high | 0 | 1+epsilon_high |
| A_tilde < 0 and r < 1−epsilon_low | 0 | 0 |
| Otherwise | r | r |

This is an explicitly selected update rule, not ordinary differentiation of an unchanged scalar function at every possible parameter value. A finite-difference check of its backward operation must keep the stopped denominator and entropy weights fixed at the original checkpoint while perturbing the numerator. Recomputing the stopped value at each perturbed point instead checks the ordinary forward function. The rule itself uses no entropy threshold; it applies to every positive upper-clipped term. Entropy modulation can be enabled or disabled independently. This application uses neither an additional dual-clip rule nor a reference-policy penalty.

Keep the two clipping widths separate. For adjusted advantage −1.2, ratio 0.75, epsilon_low=0.2 and epsilon_high=0.28, the selected term is −0.96 and its gradient is zero. The lower test uses 0.8. Substituting the high width would test against 0.72 and incorrectly allow an update. This receiving case follows the lower-width condition in AEPO's appendix and the displayed objective. For a positive advantage above the upper bound, the ordinary rule has a plateau while the selected backward alternative continues to reinforce it. Preserving that distinction does not establish which intervention improves the receiving task.

##### Engineering.Reference:26.4.2.5 - Run the finite construction and use the changed policy

The code executes the two calculator calls and four answer continuations, checks the results and constructs the reward-relative update. Its two bits are the selected generated positions; the actual return remains in their record and contributes no output term. It keeps the population convention, mean over eight terms, detached modulation and ascent rate 0.1 stated above. The repeated proposal is at the same saved prefix; its changed counter, rather than new probability evidence, changes admission. Terminal children need no further counter decisions in this fixture.

```python
from math import exp, log, sqrt

def sigmoid(z):
    return 1 / (1 + exp(-z))

def entropy(probabilities):
    assert all(p >= 0 for p in probabilities)
    assert abs(sum(probabilities) - 1) < 1e-12
    return -sum(p * log(p) for p in probabilities if p)

def standardized(values):
    mean = sum(values) / len(values)
    sd = sqrt(sum((x - mean)**2 for x in values) / len(values))
    return [(x - mean) / sd for x in values] if sd > 1e-12 else [0.0] * len(values)

old = (0.9, 0.5)  # Multiplication, then the unshifted answer.
request = (17, 19, 5)
baseline_H = entropy((old[0], 1 - old[0]))
after_H = entropy((old[1], 1 - old[1]))
delta_H = (after_H - baseline_H) / 2  # One position, vocabulary size two.

# Execute two starts. The exact calculator is retained external support.
roots = {}
training_calls = 0
for name, draw in (("A", 0.2), ("B", 0.95)):
    multiply = int(draw < old[0])
    n, m, k = request
    observed = n * m if multiply else n + m
    training_calls += 1
    roots[name] = {"bit": multiply, "observed": observed, "forks": 0}

# Only parent-lineage counters are needed before these terminal continuations.
reserve = 2
allocation = []
for name in ("A", "A", "B"):
    lineage = roots[name]
    score = (0.5 + 0.2 * delta_H) * max(0, 1 - 0.2 * lineage["forks"])
    accept = reserve > 0 and score > 0.5
    allocation.append((name, round(score, 9), accept))
    if accept:
        lineage["forks"] += 1
        reserve -= 1
assert [r[2] for r in allocation] == [True, False, True]
assert reserve == 0 and training_calls == 2

# Each saved prefix now has its original and one new continuation.
# Only answers remain in this fixture, so forks require no further tool call.
records = []
for name, prefix in roots.items():
    assert prefix["forks"] == 1
    for draw in (0.1, 0.9):
        answer_bit = int(draw < old[1])
        answer = prefix["observed"] + request[2] + (1 - answer_bit)
        records.append({
            "histories": (request, (request, ("call", prefix["bit"]),
                                    ("return", prefix["observed"]))),
            "bits": (prefix["bit"], answer_bit),
            "old_probabilities": (old[0] if prefix["bit"] else 1 - old[0],
                                  old[1] if answer_bit else 1 - old[1]),
            "answer": answer,
            "reward": int(answer == request[0] * request[1] + request[2])})
assert [r["reward"] for r in records] == [1, 0, 0, 0]

# A later training checkpoint, evaluated on the same old-policy records.
current = (0.9, 0.65)
logits = [log(p / (1 - p)) for p in current]
advantages = standardized([r["reward"] for r in records])
position_H = [entropy((p, 1 - p)) for p in current]
all_H = position_H * len(records)  # Eight generated positions; no return token.
z_H = standardized(all_H)

def update(modulate=False, follow_upper=False):
    count = 2 * len(records)
    gradient = [0.0, 0.0]
    objective = 0.0
    for i, record in enumerate(records):
        for j, bit in enumerate(record["bits"]):
            multiplier = 1 + 0.2 * z_H[2*i + j] if modulate else 1.0
            if multiplier <= 0:
                raise ValueError("Linear modulation would reverse or erase the signal")
            advantage = advantages[i] * multiplier
            p = current[j]
            probability = p if bit else 1 - p
            ratio = probability / record["old_probabilities"][j]
            objective += min(ratio * advantage,
                             max(0.8, min(1.2, ratio)) * advantage) / count
            if advantage > 0 and ratio > 1.2:
                coefficient = 1.2 if follow_upper else 0.0
            elif advantage < 0 and ratio < 0.8:
                coefficient = 0.0
            else:
                coefficient = ratio
            gradient[j] += coefficient * advantage * (bit - p) / count
    changed = [sigmoid(z + 0.1*g) for z, g in zip(logits, gradient)]
    return objective, gradient, changed

def act(probabilities, request, draws):
    n, m, k = request
    observed = n * m if draws[0] < probabilities[0] else n + m
    return observed + k + (0 if draws[1] < probabilities[1] else 1)

print("allocation", allocation)
for modulate, follow_upper in ((False, False), (True, False), (False, True), (True, True)):
    objective, gradient, changed = update(modulate, follow_upper)
    print(modulate, follow_upper, round(objective, 9),
          [round(x, 9) for x in gradient], [round(x, 9) for x in changed])
assert act(update()[2], (12, 13, 5), (0.5, 0.65)) == 162
assert act(update(True, True)[2], (12, 13, 5), (0.5, 0.65)) == 161
```

The four alternatives start from the same current checkpoint and consume the same old-policy records. They do not run successively:

| Entropy modulation | Upper-bound backward operation | Mean forward value | New (multiplication, unshifted-answer) probabilities |
| --- | --- | --- | --- |
| Off | Ordinary clipping | 0.050518149 | (0.901291559, 0.649252595) |
| On | Ordinary clipping | 0.060621778 | (0.901034441, 0.649103026) |
| Off | Stopped denominator | 0.050518149 | (0.901291559, 0.651320527) |
| On | Stopped denominator | 0.060621778 | (0.901034441, 0.651584354) |

For the last row, the mean update direction is `(0.115470054,0.069715045)`. With ordinary clipping and no modulation it is `(0.144337567,-0.032836797)`. The successful unshifted answer is already upper-clipped, while a failed unshifted answer still contributes a negative term; this explains the ordinary answer probability's decrease in this particular batch. The alternative backward operation restores the successful term's positive contribution. The table also shows why equal forward values cannot identify the implemented backward operation.

Both changed policies still use the calculator. With the new request `(12,13,5)` and stipulated draws `(0.5,0.65)`, the ordinary update returns 162, while the last row returns 161. Reset the request history and retain the chosen parameters and tool. This exhibits consumption of the finite update; the chosen draws and one conditional batch do not estimate effectiveness. The independent arithmetic operations, interface meanings and task checker are supplied capabilities. A language-model implementation must accumulate the selected generated-token contributions through its actual shared parameters, execute its optimizer and retain the support on which its later behavior depends.

Change the probability-access condition before generalizing the example. The binary full distributions above make its entropy calculations possible. If a four-outcome API instead supplies only selected probabilities, the earlier one-bit example shows why an entropy ranking may become unavailable even while recorded action ratios remain usable. Preserve the available outcome update or fixed allocation, and obtain the missing information only if the intended intervention justifies its cost. Change the branch history separately: the same measured delta_H can admit an unbranched lineage and reject another with l=1. These are different reasons for changing the next action.

##### Engineering.Reference:26.4.2.6 - Compare another modulation and assess the complete arrangement

The direction and unit of entropy weighting are design choices. [AEM v3, 8 May 2026, §§3–5 and Algorithm 1](https://arxiv.org/abs/2605.00425v3) proposes a different one: average token entropy within each response ending before an environment transition, then compare those response averages across a prompt's rollout group. With range at least 0.1, min-max normalize the means to u, calculate `w = exp(-u/temperature)`, and divide each weight by the group's mean weight. Hold the resulting positive coefficients fixed and multiply a qualified advantage, using the same coefficient for the response's generated tokens. For example, retain the episode's terminal advantage on those positions; weighting it supplies no new judgement of that response's correctness. A range below 0.1 gives coefficients one. Select numerical stabilizers and response boundaries in the actual implementation.

For two response means 0.2 and 0.8 nats at temperature one, negligible stabilizers give coefficients 1.462117157 and 0.537882843. Advantages `(−1,+1)` become approximately `(−1.462117157,+0.537882843)`: the lower-entropy response receives stronger discouragement. Means 0.20 and 0.25 instead trigger the neutral case. This construction changes the measured unit, normalization population and weighting direction relative to the token-level linear choice above. Its source analysis uses a natural-gradient update while holding the visited-state distribution fixed; its practical proxy and shared-parameter setting retain limitations. A larger entropy, a positive coefficient or this later proposal's publication date cannot alone choose the better intervention for the receiving work.

Compare complete configurations on separate task instances and account for shared-prefix dependence when splitting data. Hold the task, reward meaning, available tools and assessment procedure fixed when testing a sampler, modulation or backward change; vary those interventions separately before attributing a gain to one. Count pilot generation, probability extraction, failed attempts, training and later execution. Include successful alternatives and older required behavior, and keep a recoverable baseline. When repeated adaptive comparison has consumed the assessment cases, obtain a suitable new assessment basis. Revert or repair the relevant operation if it costs more without improving the required result or loses previously useful behavior.

This application concerns collecting training experience and changing a specified policy. SYSE.51 governs later allocation of inference effort; SYSE.50 needs its own qualified basis for deciding assistance. The measured token or response entropy here does not establish either an agent's need for help or how much Method structure it can acquire. Those questions retain their performer, representation, support and learning conditions. Use the present construction when its measured input and intervention fit the work, and follow those other contributions when the object being changed is different.


#### Engineering.Reference:26.4.3 - Learn a strategy together with its execution

Use this application when an agent first chooses a way of solving a task and then makes decisions within that way. A promising strategy can initially be executed poorly. Rewarding only the average observed outcome may discard it; rewarding its best outcomes may instead favor luck. The engineer needs to decide what the strategy score estimates, learn the conditional execution, and examine the resulting complete policy.

The construction requires a policy that exposes a generated strategy, repeatable task starts, qualified outcome feedback, selected-action probabilities and access to update the policy. If the agent has only one undivided output, [26.4.1](28-engineering-reference-26---construct-a-guard-a-learning-upda.md#engineeringreference2641---learn-from-interleaved-actions-and-observations) supplies the outcome update without requiring a new plan variable. A known adequate controller can also settle the task without training.

[StraTA v2, §§3–4](https://arxiv.org/pdf/2605.06642v2) supplies the particular combination used here: generate several natural-language strategies from the initial task, keep each strategy fixed during its executions, compare strategies across that task, compare actions within each strategy, and train both. The plan is an input to execution. If observations require changing it during an episode, obtain a revision operation through [SYSE.47](../syse/68-syse-47---construct-and-revise-an-agent-s-execution-procedur.md); the fixed-plan construction does not perform that revision.

##### Engineering.Reference:26.4.3.1 - Choose what the strategy score is meant to improve

Begin with the later use. If deployment makes one attempt, its expected return includes the execution policy actually available then. If deployment selects the best of several attempts, retain those attempts, selection facilities and costs in the comparison. Training can use an optimistic score to explore a strategy whose execution may improve, while the receiving assessment still measures ordinary single-use performance.

For each task, generate N strategy decisions. For each sampled strategy, reset the task and execute M continuations under the same frozen old policy. Retain the generated strategy once, the M execution histories, their outcomes and their old action probabilities. A shared strategy followed by M continuations is one sampled strategy with M conditional executions. Resetting must restore the relevant environment as well as context; a repeated mutation against a live service is not such a reset.

Select the strategy statistic. The mean over all M outcomes estimates performance under the sampled execution arrangement. StraTA instead averages the best K outcomes to emphasize promising execution. Declare an integer `1 <= K <= M`. If K is derived from a fraction, specify rounding and reject an empty selection: [StraTA's implementation](https://github.com/xxyQwQ/StraTA/tree/592238b7dfd6fb51566cbd631be9c97b6fa34915) uses `int(delta*M)`, which can select zero outcomes.

The top-K statistic combines execution opportunity, uncontrolled variation and selection over attempts. To interpret a favorable tail as something the learner can acquire, obtain a discriminating intervention or a qualified consequence model. [MMP.8.SD:4.2 through MMP.8.SD:4.4](../../foundational-thinking-dpf-suite/mmp/15-mmp-8-sd---construct-a-sequential-decision-model-from-inform.md#mmp8sd42---construct-how-an-action-changes-the-world-and-the-available-information) compares actions with their available continuations. [FPF C.40:4.7](../../../sections/09-part-c---kernel-extension-specifications/105-c-40---develop-branching-search-from-reusable-material.md#c4047---develop-a-way-by-what-its-use-produces) requires performing allowed inner learning before crediting a candidate with the result it would produce after that learning. Specify that learning procedure and allowance, execute it, then compare its later policy. Declaring a better future action probability supplies no such learning.

##### Engineering.Reference:26.4.3.2 - Construct the two learning comparisons

Let `R_ij` be execution j's reward under strategy i, and `B_i` its chosen strategy statistic. Standardize the N values B to obtain strategy advantages `A_strategy_i`. Separately standardize the M rewards within each strategy to obtain `A_action_ij`. This application uses population standard deviations and zero advantages when dispersion is at most `1e-12`. A group with no variation supplies no relative preference; obtain discriminating experience when that missing preference matters.

For each recorded decision, divide its current probability by its fixed old probability, conditional on the same history. The strategy history contains the initial task. An execution history also contains its fixed strategy and any observations already received. Future outcomes enter the learning signal after execution, not the earlier decision input. Use the observation mask and historical conditioning of 26.4.1.

The finite construction below has one generated strategy position and one action position. Its complete surrogate is:

```text
f(r, A) = min(r*A, clip(r, 0.8, 1.2)*A)
J = mean_over_N_strategies[f(strategy_ratio, A_strategy)]
  + mean_over_N_strategies[
      mean_over_M_executions[f(action_ratio, A_action)]
    ]
```

Maximize J, keeping the two groupings intact. Their coefficients are both 1 here, with no reference-policy penalty. For a token implementation of this application, replace each strategy term by the mean of f over that strategy's generated tokens, and each execution term by the mean over all its generated action tokens. External observations condition later tokens and contribute no optimized position. This explicitly chosen reduction gives each strategy and each of its completed executions the stated weight. The source trainer's per-step, token-sum reduction is a different choice when lengths vary; select one implementation and carry its actual weighting into the comparison.

##### Engineering.Reference:26.4.3.3 - Generate attempts, update and use the result

Consider two supplied strategies P and Q, each admitting actions a and b. In the qualified deterministic fixture, P,a returns 1, P,b returns 0, and either Q action returns 0.4. Three independent logits determine `p=Pr(P)`, `s=Pr(a|P)` and `t=Pr(a|Q)`. All start at zero, so the probabilities are 0.5. The choices and their meanings are supplied capabilities; the learner changes how often it selects them.

The code uses declared draws to generate P and Q once each and four executions per strategy. Those draws make the finite calculation reproducible; they are not a random-sample performance assessment. With K=2, P's outcomes `(1,0,0,0)` give strategy score 0.5 and Q's `(0.4,0.4,0.4,0.4)` give 0.4. Strategy advantages are `(+1,-1)`. P's action advantages are `(sqrt(3),-1/sqrt(3),-1/sqrt(3),-1/sqrt(3))`; Q's are zero.

```python
from math import exp, sqrt

def sigmoid(z):
    return 1 / (1 + exp(-z))

def standardize(xs):
    mean = sum(xs) / len(xs)
    sd = sqrt(sum((x - mean)**2 for x in xs) / len(xs))
    return [(x - mean) / sd for x in xs] if sd > 1e-12 else [0.0] * len(xs)

def outcome(plan, action):
    return float(action == "a") if plan == "P" else 0.4

old_z = [0.0, 0.0, 0.0]
old = [sigmoid(z) for z in old_z]
task = "one P/Q task with the supplied action meanings"
groups = []
for draw in (0.2, 0.8):
    plan_bit = int(draw < old[0])
    plan = "P" if plan_bit else "Q"
    slot = 1 if plan_bit else 2
    group = {"bit": plan_bit, "history": task, "slot": slot,
             "old": old[0] if plan_bit else 1 - old[0], "runs": []}
    for action_draw in (0.1, 0.7, 0.8, 0.9):
        bit = int(action_draw < old[slot])
        action = "a" if bit else "b"
        group["runs"].append({
            "history": (task, plan), "bit": bit, "action": action,
            "old": old[slot] if bit else 1 - old[slot],
            "reward": outcome(plan, action)})
    groups.append(group)

K = 2
assert all(1 <= K <= len(g["runs"]) for g in groups)
scores = [sum(sorted((r["reward"] for r in g["runs"]), reverse=True)[:K]) / K
          for g in groups]
plan_advantages = standardize(scores)
for g in groups:
    g["advantages"] = standardize([r["reward"] for r in g["runs"]])

def term(probability, bit, old_selected, advantage):
    selected = probability if bit else 1 - probability
    ratio = selected / old_selected
    value = min(ratio * advantage, min(1.2, max(0.8, ratio)) * advantage)
    saturated = ((advantage > 0 and ratio > 1.2)
                 or (advantage < 0 and ratio < 0.8))
    derivative = 0.0 if saturated else ratio * advantage * (bit - probability)
    return value, derivative

def objective_and_gradient(zs):
    ps = [sigmoid(z) for z in zs]
    total, gradient = 0.0, [0.0, 0.0, 0.0]
    for g, advantage in zip(groups, plan_advantages):
        value, derivative = term(ps[0], g["bit"], g["old"], advantage)
        total += value / len(groups)
        gradient[0] += derivative / len(groups)
        for record, action_advantage in zip(g["runs"], g["advantages"]):
            value, derivative = term(ps[g["slot"]], record["bit"],
                                     record["old"], action_advantage)
            weight = 1 / (len(groups) * len(g["runs"]))
            total += weight * value
            gradient[g["slot"]] += weight * derivative
    return total, gradient

_, gradient = objective_and_gradient(old_z)
new_z = [z + 0.3 * g for z, g in zip(old_z, gradient)]
new = [sigmoid(z) for z in new_z]

def use(ps, draws):
    plan = "P" if draws[0] < ps[0] else "Q"
    slot = 1 if plan == "P" else 2
    action = "a" if draws[1] < ps[slot] else "b"
    return plan, action, outcome(plan, action)

def expected_return(ps):
    return ps[0] * ps[1] + (1 - ps[0]) * 0.4

assert use(old, (0.52, 0.51)) == ("Q", "b", 0.4)
assert use(new, (0.52, 0.51)) == ("P", "a", 1.0)
assert standardize([0.4] * 4) == [0.0] * 4
print(gradient)
print(new, expected_return(old), expected_return(new))
```

The gradient is `(0.5,sqrt(3)/8,0)`. One ascent step of 0.3 gives `(p,s,t)=(0.5374298453,0.5162322701,0.5)`. The complete policy's expected single-use return under the supplied model increases from 0.45 to 0.4624666909. The later run uses both the changed strategy probability and the changed conditional action probability. The known deterministic table also permits directly choosing P,a; the example teaches the learning construction rather than establishing a need to learn this table.

This run consumes two strategy generations and eight task executions before the two displayed later executions. A language-model trial must also budget generated tokens, resets, feedback and any selected judges. [26.4.2](28-engineering-reference-26---construct-a-guard-a-learning-upda.md#engineeringreference2642---allocate-training-attempts-and-select-the-update) makes that allocation explicit. Embedding-based strategy selection or a self-judge adds its own computation and qualification; neither facility is needed by this finite version. Continue training with the actual current-to-old ratios and chosen clipping rule, refreshing rollout policy and experience when required by the recipe.

##### Engineering.Reference:26.4.3.4 - Change the inference when success is not controllable

Now suppose qualified environment evidence says that P succeeds with probability 0.25 independently of a or b, while Q still returns 0.4. The same eight observations remain possible. The top-half update remains numerically the same, but single-use expected return is now `U=0.4-0.15*p`: it falls from 0.325 to 0.3193855232. Changing P's action distribution cannot raise its success probability under this model.

For this changed task, compare strategy values 0.25 and 0.4. At the old equal mixture, their credits are −0.075 and +0.075. A plan-only expected-credit update has gradient −0.0375 for the plan logit; a separate first step of 0.3 gives `p=0.4971875297` and `U=0.3254218706`. These figures describe an alternative update from the original policy. They do not follow the preceding top-half step. Averaging all four recorded outcomes would also favor Q here, but observations from one small group alone cannot establish either consequence model.

If controllability is unresolved, keep the optimistic score as an exploration choice with a bounded cost, obtain discriminating evidence when worthwhile, and assess the resulting learner on the intended later use. Retain the uncertainty if the available experiment cannot distinguish the models. An improved execution after an actual learning intervention, repeated under suitable task conditions, can support a learnability claim that a maximum observed reward cannot.

For a shared language model, strategy and execution updates can interfere through shared parameters even though the loss has separate groups. Compare the complete trained policy, older useful behavior and resource cost through SYSE.45:4.4. Reopen the affected construction when the plan stops matching current observations, the outcome checker rewards a proxy, or the later work changes from one attempt to best-of-many selection.



#### Engineering.Reference:26.4.4 - Learn actions whose value persists across sessions

Use this application when a present action costs effort but changes information that the agent can use after the current session ends. Consulting an expert may lose on today's reward and save later work; an obsolete or incorrect retained answer can cause later failures. To train that choice, include the continuation made possible by the resulting memory.

The immediate target here is a policy parameter controlling whether to consult. The consultation supplies an answer, a memory operation retains it, and a later controller uses it when applicable. [SYSE.50](../syse/71-syse-50---construct-and-calibrate-an-agent-s-assistance-poli.md) qualifies the help and its availability; [SYSE.43](../syse/64-syse-43---maintain-external-memory-for-continuing-work.md) supplies retained information and its further use. Parameter learning uses SYSE.45 and CMP.7. Keeping a new answer in memory can change performance with unchanged weights; train only when that additional intervention is warranted.

##### Engineering.Reference:26.4.4.1 - Obtain continuation credit at the session boundary

Select the horizon and reward meaning through MMP.8.SD. A session boundary may clear working context while retaining memory. Save the information needed to continue: memory contents and applicability, the next-session information already available, remaining resources and horizon. Two identical text memories can have different values when one has more opportunities for use or a different validity condition. Reset only what the intended later arrangement actually resets.

Freeze an old policy. Collect complete multi-session attempts with actual actions, observations, memory transitions and task rewards. From each relevant boundary state, obtain the old policy's remaining return: execute continuations from a saved state when resets are possible, evaluate a qualified transition model, or fit a value estimator to observed state/return-to-go pairs. Include the cost of obtaining these values. A changed query population or unavailable reset can require another estimator or a narrower conclusion.

For an undiscounted finite horizon, the session signal used by [AGILE, NeurIPS 2024, Appendix A](https://proceedings.neurips.cc/paper_files/paper/2024/file/097c514162ea7126d40671d23e12f51b-Paper-Conference.pdf) has the form:

```text
session_signal = observed_session_reward
               + V_old(after_state) - V_old(before_state)
```

Here `V_old(state)` is expected remaining reward under the frozen old continuation, and terminal value is zero. The after-state includes the memory actually produced. Subtracting the before-value compares the session with the old policy from the same starting condition. Estimate and freeze these quantities for the selected update. Approximation error can reverse a small advantage; examine whether the estimated difference is adequate for the intended reliance.

Partition the collected attempts into sessions with those boundary states. Supply the signal to the generated decisions in the session, preserving their historical inputs and old probabilities. Use a specified update, such as the clipped generated-position mean in [26.4.1](28-engineering-reference-26---construct-a-guard-a-learning-upda.md#engineeringreference2641---learn-from-interleaved-actions-and-observations), then recollect experience or refit values as the selected training procedure requires. Sessions remain related through retained state; cutting the transcript into pieces does not make their observations independent. If a discounted criterion is chosen, derive the boundary discount for the elapsed duration instead of reusing the undiscounted equation unchanged.

##### Engineering.Reference:26.4.4.2 - Execute continuations, obtain a first update and retain its result

The finite fixture has two sessions. In either, the supplied self-answering operation succeeds with probability 0.75. Consulting in the first session obtains a correct answer at cost 0.3 and stores a verified entry. Only this action writes memory. After context reset, the second question is related with probability 0.4. A fixed controller uses the stored answer if related; otherwise it self-answers. There are no other costs or discounts. The learned logit controls only the first consultation probability, initially 0.5; answer generation, retrieval and applicability recognition are supplied operations.

The code obtains future values by executing a declared population of twenty continuations from each of two boundary states: empty memory and retained verified entry. Eight questions are related and twelve are new. Each block of four supplied self-answering outcomes has three successes. The resulting continuation means are 0.75 and 0.85. All repetitions of each boundary state have the same future law in this fixture, so one set of twenty continuations can supply that state's estimate. These forty executed continuations are additional training work; reusing their estimates creates no extra independent observations.

```python
from math import exp

def sigmoid(z):
    return 1 / (1 + exp(-z))

def first_session(consult, self_draw):
    # The fixture's expert is correct; only consultation stores its answer.
    memory = {"related": "verified answer"} if consult else {}
    reward = 0.7 if consult else float(self_draw < 0.75)
    return reward, {"memory": memory, "context": (), "remaining": 1}

def continue_session(state, query, self_draw):
    assert state["context"] == () and state["remaining"] == 1
    if query in state["memory"]:
        return 1.0
    return float(self_draw < 0.75)

def construct_update(related_count):
    assert 0 <= related_count <= 20 and related_count % 4 == 0
    self_draws = (0.1, 0.3, 0.6, 0.9)
    future_cases = [
        ("related" if i < related_count else "new", self_draws[i % 4])
        for i in range(20)]
    records = []
    for i, action_draw in enumerate((0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9)):
        bit = int(action_draw < 0.5)
        reward, after = first_session(bool(bit), self_draws[i % 4])
        records.append({
            "history": ("first question", "empty memory", "two sessions left"),
            "bit": bit, "old_probability": 0.5, "reward": reward, "after": after})
    # These two state classes are equivalent within each class in this fixture.
    after_states = {r["bit"]: r["after"] for r in records}
    values = {
        bit: sum(continue_session(state, query, draw)
                 for query, draw in future_cases) / len(future_cases)
        for bit, state in after_states.items()}
    targets = [r["reward"] + values[r["bit"]] for r in records]
    before_value = sum(targets) / len(targets)
    signals = [target - before_value for target in targets]
    # One initial ascent step at the unchanged rollout policy; ratios equal 1.
    gradient = sum(a * (r["bit"] - 0.5)
                   for a, r in zip(signals, records)) / len(records)
    probability = sigmoid(0.3 * gradient)
    return probability, gradient, values, before_value, records

new_probability, gradient, values, baseline, records = construct_update(8)
assert abs(values[0] - 0.75) < 1e-12
assert abs(values[1] - 0.85) < 1e-12
assert abs(baseline - 1.525) < 1e-12
assert abs(gradient - 0.0125) < 1e-12

def use(probability, action_draw, future_query_draw, self_draws):
    consult = action_draw < probability
    first_reward, after = first_session(consult, self_draws[0])
    query = "related" if future_query_draw < 0.4 else "new"
    second_reward = continue_session(after, query, self_draws[1])
    return consult, bool(after["memory"]), first_reward + second_reward

assert use(0.5, 0.5005, 0.2, (0.9, 0.9)) == (False, False, 0.0)
assert use(new_probability, 0.5005, 0.2, (0.9, 0.9)) == (True, True, 1.7)
without_recurrence = construct_update(0)
assert abs(without_recurrence[1] + 0.0125) < 1e-12
print(new_probability, gradient, values, baseline)
print(without_recurrence[:4])
```

The eight first-session records contain four consultations and four self-answers. Their mean immediate rewards are 0.7 and 0.75. Adding the estimated continuation yields conditional total values 1.55 and 1.5; their equal old mixture is 1.525. The code's centering uses that balanced fixture's empirical mixture. It illustrates a finite estimator and update; for sampled training data, select and qualify value and baseline estimation with the trainer rather than inferring an unbiased estimate from this balanced example.

The gradient 0.0125 changes the consultation probability to 0.5009374989. Under the stated law, expected two-session return changes from 1.525 to 1.5250468749. The displayed later runs deliberately choose draws near the changed decision boundary to expose the changed action and subsequent use of retained memory. They estimate no empirical improvement rate. The initial training run uses eight first sessions, including four consultations, and forty future continuations; the two later runs add four sessions and one consultation. The separate no-recurrence construction repeats those 48 training sessions under its changed condition.

The updated probability persists into the later run; context clears at the boundary and the stored answer persists. That separation is essential when checking which contribution changed. An experiment that removes the expert or changes memory retrieval at the same time needs a comparison that includes those different conditions.

##### Engineering.Reference:26.4.4.3 - Recalculate recurrence and the reliability of help

When no later question is related, both after-states have continuation value 0.75. Consulting then totals 1.45 and self-answering 1.5. The code performs a separate update from the original probability, with gradient −0.0125 and result 0.4990625011. Repeatedly paying for information that will not be used has no future benefit in this model. A different horizon, retention cost or query population changes the same continuation calculation.

Now change the expert condition. Suppose consultation is correct with probability q, its answer is stored without verification, and a related later question reuses that answer even when wrong. Let recurrence be r, self-answering success be s and consultation cost be c. Under these particular transitions:

```text
value_self = 2*s
value_consult = q - c + r*q + (1-r)*s
value_consult - value_self = (1+r)*(q-s) - c
```

At `s=0.75, r=0.4, c=0.3, q=0.9`, consultation has value 1.41, below 1.5. The consultation advantage reverses. This changed fixture stores unverified information; regenerate its feedback and memory transitions rather than reusing the earlier always-correct consultation records. Verification before storage would require its own accuracy, cost and possible rejection transition. Expiry or changed applicability similarly belongs in the future state and retrieval rule. SYSE.50 supplies the help qualification and SYSE.43 the corresponding retention/use repair.

When the consultation advantage is small compared with plausible value-estimation error, retain a supported baseline or obtain a discriminating continuation sample if its value warrants the work. Qualification of the expert alone cannot settle recurrence, and accurate recall cannot make an inapplicable answer useful.

##### Engineering.Reference:26.4.4.4 - Choose a different estimator or a different learned memory operation

AGILE Appendix B.4 uses a heuristic instead of an estimated continuation value: when a later similar question exists in the training sequence, give bonus `beta/(n+1)`, where n counts previous similar stored questions. In the initial fixture, beta=0.1 and n=0 give consultation proxy 0.8 against self-answering 0.75. With n=3 the proxy is 0.725; with no later recurrence it is 0.7. This bonus is a choice of training signal, not a measured future gain. Use it as an alternative to the value construction, or derive a justified combined objective; adding it to an already credited future benefit would count that presumed benefit twice. Later questions can supply training labels while remaining unavailable during live action selection.

AGILE's historical construction explains the session-value connection. Its [released runner](https://github.com/bytarnish/AGILE/tree/8213312983e8ba6787fd854b87d83b2776166884) supplies dataset-correct consultation answers and cached reflection; that repository edition does not supply the Appendix A PPO trainer. A receiving implementation must provide the selected optimizer and any uncached reflection operation it requires. Compare a direct decision rule when the relevant consequence model is already known, as it is in the finite fixture.

If the target is learning how to extract facts and edit persistent memory, [Memory-R2 v1, §§3–4 and Appendix A](https://arxiv.org/pdf/2605.21768v1) offers a different controlled-feedback construction. A shared model performs extraction and memory editing with different prompts. A fixed answering module evaluates the resulting memory on gold questions whose evidence is attributed to sessions. The construction proceeds as follows:

1. Generate several full memory-construction trajectories from the same conversation. Cache each pre-session memory. Evaluate each terminal memory on the question subsets associated with each session, subtract the selected memory-size penalty, and standardize these rewards across full trajectories separately for each session.
2. Select sessions for additional local trials. For each, choose one cached pre-session memory as the common starting point and generate several new executions of that session. Evaluate their resulting memories on that session's question subset, with the same reward meaning at the local horizon, and standardize within this local group.
3. Assign each extraction or editing step the advantage from its own global or local group. Keep old and current probabilities for its generated tokens and their actual histories. Train the shared model using the selected step reduction below; preserve the global branch because the session-local questions do not assess every later consequence.
4. Begin with an affordable shorter horizon, retain a candidate selected using separate validation, and extend the number of sessions when the resulting memory operations support that use. The source uses 8, then 16, then 32 sessions; another task needs its own justified allowance.

The source reward uses mean answer F1 on the selected question subset. Its size penalty is `max(0, memory_tokens - alpha*cumulative_input_tokens) / cumulative_input_tokens`, scaled by `lambda_comp` and subtracted from that F1. Global rewards use terminal memory and terminal input length; local rewards use the selected session's resulting memory and cumulative length through that session. Obtain nonempty evaluable question subsets and positive input length, or select a specified handling rule before computing this reward. Each advantage subtracts its own group's mean and divides by its standard deviation plus a chosen positive stabilizer. For a receiving implementation, use the population standard deviation and retain that convention with the learning rate; equal group rewards then yield zero advantages.

Memory-R2 also changes the reduction. For a generated step u it forms `rho_u = exp(mean_generated_tokens(log p_current - log p_old))`, a geometric mean of token ratios, and assigns the group's advantage to that step. Define `f_epsilon(r,A)=min(r*A,clip(r,1-epsilon,1+epsilon)*A)`. Its dual-clipped reward surrogate is `f_epsilon(rho_u,A)` for nonnegative A and `max(f_epsilon(rho_u,A),c*A)` for negative A, with `c>1`. Minimize the negative mean of those step terms over both branches, minus `beta_ent` times mean token entropy, plus `beta_kl` times mean token KL divergence from the selected reference policy. Keep that reference distinct from the rollout policy supplying the old probabilities. This differs from averaging individually clipped token terms in 26.4.1. Set the clipping, regularization, group sizes and local selection probability explicitly; the last changes both computation and the influence of local feedback.

This branch needs memory snapshots, a fixed answerer, gold answers with session-evidence attribution, and extra rollouts. With n full trajectories of T sessions and m local executions for each of b selected sessions, it uses `n*T + m*b` session executions before feedback costs. The local comparison isolates alternatives from one starting memory; it does not establish that full-trajectory learning is invalid whenever later states diverge. Different actions normally produce different later states. Select local trials for the attribution they can supply, and retain the full-horizon question.

Choose among a qualified value estimate, a heuristic and controlled memory trials according to the target operation, available observations and whole development cost. The learned consultation choice and the learned memory editor need different action records and feedback even when both serve later information use. Assess the resulting complete arrangement through SYSE.45:4.4, including stale entries, changed questions, fallible help and older useful behavior.



#### Engineering.Reference:26.4.5 - Transfer a procedure through teacher-guided learning

Use this application when repeated prompting, planning or expert assistance supplies a useful procedure, and the engineer needs to obtain a policy that can perform its decisions with less recurring guidance. Copying a final answer can lose the response to an intermediate observation. Copying every teacher decision can instead preserve an error. Choose what the student can learn from the available histories and feedback, compute the resulting update, then execute the changed policy with its retained support.

The construction needs qualified interaction records, access to change the student's parameters and an executor for subsequent trials. Ordinary Python, probabilities and differentiation are sufficient for the finite example below. A known direct rule can settle the example more cheaply; use learning in a receiving task only when its development and later-use costs warrant it. When the intended change is an external workflow or reusable instruction, follow SYSE.47 or SYSE.48 instead.

[FPF C.40:4.7](../../../sections/09-part-c---kernel-extension-specifications/105-c-40---develop-branching-search-from-reusable-material.md#c4047---develop-a-way-by-what-its-use-produces) supplies the loop of executing the student, obtaining teaching targets on its reached histories, fitting it and executing again. [CMP.7](../../foundational-thinking-dpf-suite/cmp/15-cmp-7---construct-a-learner-from-examples-and-feedback.md) constructs the learner; CMP.6 supplies finite update calculation. [MMP.8.SD](../../foundational-thinking-dpf-suite/mmp/15-mmp-8-sd---construct-a-sequential-decision-model-from-inform.md) determines which information is available before each decision. The additional work here is selecting and connecting hard targets, teacher distributions, outcome feedback and changes to the teaching arrangement.

##### Engineering.Reference:26.4.5.1 - Recover the procedure and the observations it needs

Suppose an assistant must report the checked status of a job. A read-only service returns `pending` or `committed`. A report of completion requires the latter observation; a request to inspect the job is not that observation. If the supplied interface has become obsolete, it returns `schema_error`. A supported recovery can obtain the current interface and inspect again.

The external teacher can demonstrate three useful executions:

- inspect → pending → report pending;
- inspect → committed → report complete;
- inspect → schema error → obtain the current interface → inspect again → pending → report pending.

Retain the third execution's failure and valid recovery. Its failed call produced information that the later decisions use. Repeating that call indefinitely, inventing a committed response or labelling its old observation as the result of a different action would change the procedure. Qualify the demonstrated decisions against the actual service contract and records, including where the information came from. A correct final report alone does not qualify an invented explanation or a leaked answer.

For a larger teacher arrangement, run its configured planner, executor and checking contributions; retain the ordered decisions and actual observations. Then select the recurring decisions to teach. [Chain-of-Agents v1, §§3–5](https://arxiv.org/pdf/2508.13167v1) serializes role-labelled contributions for supervised fitting, followed by a separate reward-learning stage. Its observation tokens condition later decisions but receive no direct prediction loss. The fitted model still uses a runner, tools and prompts; its web arrangement also retains an external summarizer. Role tags inside one policy therefore describe generated functions, not independent performers or transferred organizational authority.

Use [26.4.1](28-engineering-reference-26---construct-a-guard-a-learning-upda.md#engineeringreference2641---learn-from-interleaved-actions-and-observations) for the ordered-history and observation-mask construction. Preserve a correct recovery when qualifying demonstrations; choose any minimum-length, reflection or success filter for the actual receiving behavior. CoA's reported filters and configurations are research choices. Its published script and paper differ on web training durations, and one displayed investigation retrieves an evaluation dataset's answer. Reconcile the intended run and evidence provenance before using those records to demonstrate independent investigation or a faithful procedure.

The job-status example uses four decision histories. It deliberately aggregates histories only where the stipulated service contract makes the current state sufficient: inspections are read-only, no effect remains pending from an earlier failed call, and the recovered interface supplies the same status meaning.

| History available to the policy | Choice 1 | Choice 0 | Qualified demonstrated choice |
| --- | --- | --- | ---: |
| Start, before a status return | Inspect status | Claim completion without checking | 1 |
| A current pending return | Report complete | Report pending | 0 |
| A current committed return | Report complete | Report pending | 1 |
| A schema error | Obtain the current interface and inspect again | Repeat the obsolete call | 1 |

Each row has its own scalar logit θ_i and probability `p_i = sigmoid(θ_i)` of choice 1. The runner binds the job identifier and implements the supported calls; the policy chooses among the stated actions. Learning argument syntax, identifying a trustworthy service or obtaining permission for a mutation would require additional inputs and operations.

##### Engineering.Reference:26.4.5.2 - Choose the teaching target and its probability domain

Use the information actually supplied:

| Available teaching information | Executable choice | Consequential limit |
| --- | --- | --- |
| A qualified demonstrated action or generated token | Minimize its negative log probability under the student. | This hard-target loss does not supply the teacher's alternative probabilities. |
| A teacher distribution over the same alternatives at a compatible history | Minimize a specified distribution loss, such as teacher-to-student KL. | Tokenization, action meaning, history and probability support must match the comparison. |
| An independently grounded outcome for an executed attempt | Use the outcome update in 26.4.1, optionally with a separately specified teaching term. | An episode reward alone may penalize a useful action preceding a failure. |

For a language-model sequence, retain the original order `reason, action, observation, reason, action, …`. Align character annotations with the tokenizer's prediction positions. Specify whether delimiters are targets, exclude observations and padding from direct output loss, and check the masks after truncation. Keep observations in the input to later predictions. Concatenating all reasoning before all actions teaches another history. Masking an observation's label does not remove its influence through context or the shared model.

For reasoning and actions in one vocabulary, the teacher-to-student KL divergence is `D_KL(q || p) = sum_{a:q(a)>0} q(a) log(q(a)/p(a))`, summed over its alternatives a. Use it in the normalized objective

`L = sum_t w_t D_KL(q_t || p_theta,t) / sum_t w_t`.

Sum over the supervised positions t, with positive selected weights and compatible teacher distributions q_t. A one-hot q_t gives hard-target cross-entropy. For any fixed q_t, minimizing teacher-to-student KL is equivalent to minimizing cross-entropy with that q_t, since the teacher entropy is constant. Here w_t and q_t are held fixed during the update; the denominator includes the supervised weights, not observations. To imitate a teacher distribution, obtain its conditionals at the retained prefixes. A text-only teacher response, an unqualified truncated probability list or cached probabilities for a different history does not supply this objective.

[Structured Agent Distillation v5, §§3.1–3.9 and Appendices L–N](https://arxiv.org/pdf/2505.13820v5) motivates separate reasoning and action supervision, including an optional action head. Make the receiving choice explicit. With equal weights, one probability domain and one reduction, splitting the selected positions into two masks leaves their summed loss unchanged. A finite action head changes the representation; for a call with free-form arguments, provide an action/argument factorization or a compatible token distribution. A list of command names does not define probabilities over all argument strings.

Separate masks or heads also do not ensure independent parameter changes. Two binary heads sharing θ, each returning `sigmoid(θ)`, with teacher probabilities 0.9 and 0.1 have KL gradients −0.4 and +0.4 at zero: their inner product is −0.16. Weighting or changing architecture can alter that conflict; naming the spans cannot remove it. SAD's general orthogonality inference is therefore not a basis for choosing its update. The finite example below uses four independent logits.

Decide which histories to collect before choosing a curriculum. With a sufficient fixed dataset, score the stored teacher histories and fit offline. With student-generated histories, query the teacher on those actual prefixes or obtain compatible cached scores. SAD describes both paths without one consistent reproduction recipe; choose one and count its teacher calls. A curriculum additionally needs an explicit sampling or ordering rule. An entropy coefficient without such a rule is not a schedule.

When demonstration selection is the difficulty, [SmartAD, §3](https://aclanthology.org/2026.findings-acl.1349.pdf) offers a concrete hard-target alternative: generate several teacher executions per question, admit those passing the chosen correctness/tool checks, score them with the frozen initial student, and select the lowest NLL per question. Average token NLL within each assistant response, then average responses. Its training weights reasoning, intermediate code and final code by 1, 1.5 and 2, normalized by the sum of supervised-token weights. This needs no teacher logits, but requires extra generation and scoring. Low NLL measures compatibility, not correctness. Its tool-failure filter would remove the job-status recovery above; preserve that needed behavior through a revised admission/selection rule.

##### Engineering.Reference:26.4.5.3 - Fit a first policy and use the fresh return

For the four histories, stipulate teacher probabilities of choice 1 `q=(.8,.05,.9,.85)`. The service contract supports these target directions. Generate and qualify the three demonstrations above, then retain one representative per sufficient history. This four-row training set removes duplicate start/pending rows. SmartAD instead selects a demonstration per question by its stated NLL score.

Start all logits at zero. Choose weights `(1,2,2,1)` to give the two status-dependent decisions more of this small update, with Z=6, and a descent rate η=0.6. The normalized binary cross-entropy/KL gradient is `w_i(p_i-q_i)/Z`. Thus

`θ_i' = θ_i + η w_i(q_i-p_i)/Z`.

Hard demonstrated targets (1,0,1,1) produce logits `(.05,-.10,.10,.05)`. The soft teacher targets produce `(.03,-.09,.08,.035)`. These are different first trained policies, even though both used the same decisions and support. Equal soft-target weights produce `(.045,-.0675,.06,.0525)`; selecting a weight changes the update, while renaming a mask would not.

The following finite simulator creates the demonstrations, constructs both updates and executes the changed policy. Its observations come from the service model. Each policy step retains the history and old probability needed by the next construction.

```python
from math import exp, log, sqrt


def sigmoid(x):
    return 1 / (1 + exp(-x))


Q = (.8, .05, .9, .85)  # probabilities of choice 1 at the four histories
WEIGHTS = (1., 2., 2., 1.)


def fit_targets(theta, targets, weights=WEIGHTS, rate=.6):
    z = sum(weights)
    return tuple(t + rate*w*(q-sigmoid(t))/z for t, q, w in zip(theta, targets, weights))


def execute(theta, status, draws, broken=False):
    assert status in ("pending", "committed")
    draws = iter(draws)
    steps, events = [], [("task", "report the checked job status")]
    calls = 0

    def choose(i):
        p = sigmoid(theta[i])
        y = int(next(draws) < p)
        steps.append({"i": i, "y": y, "p": p if y else 1-p,
                      "q": Q[i] if y else 1-Q[i], "history": tuple(events)})
        return y

    if not choose(0):
        events.append(("action", "claim_complete_without_check"))
        return {"reward": 0, "steps": steps, "events": events, "calls": calls}
    events.append(("action", "inspect_status"))
    calls += 1
    if broken:
        events.append(("observation", "schema_error"))
        if not choose(3):
            events += [("action", "repeat_old_call"), ("observation", "schema_error")]
            return {"reward": 0, "steps": steps, "events": events, "calls": calls+1}
        events += [("action", "obtain_current_interface"), ("observation", "status/v2"),
                   ("action", "inspect_with_current_interface")]
        calls += 2  # obtain supported interface, then read current status
    events.append(("observation", status))
    y = choose(1 if status == "pending" else 2)
    events.append(("action", "report_complete" if y else "report_pending"))
    return {"reward": int(bool(y) == (status == "committed")),
            "steps": steps, "events": events, "calls": calls}


def expected(theta, broken=False):
    p = tuple(map(sigmoid, theta))
    return p[0]*(p[3] if broken else 1)*((1-p[1])+p[2])/2


old = (0.,)*4
teacher = tuple(log(q/(1-q)) for q in Q)
demos = [
    execute(teacher, "pending", (.2,.2)),
    execute(teacher, "committed", (.2,.2)),
    execute(teacher, "pending", (.2,.2,.2), broken=True),
]
chosen = {}
for episode in demos:
    assert episode["reward"] == 1
    for s in episode["steps"]:
        if s["i"] in chosen:
            assert chosen[s["i"]]["y"] == s["y"]
        chosen.setdefault(s["i"], s)
hard = fit_targets(old, tuple(float(chosen[i]["y"]) for i in range(4)))
soft = fit_targets(old, Q)
equal_soft = fit_targets(old, Q, (1.,)*4)
for name, theta in (("old",old), ("hard",hard), ("soft",soft), ("equal",equal_soft)):
    print(name, tuple(map(sigmoid,theta)), expected(theta), expected(theta,True))
for theta in (old, soft):
    print(execute(theta,"pending",(.49,.49))["events"])
print(execute(soft,"committed",(.49,.49))["events"])
for theta in (old,soft):
    print(execute(theta,"pending",(.49,.505,.49),broken=True)["events"])
```

With equal probabilities of pending and committed in this stipulated later population, expected valid-report probability is `p_start * ((1-p_pending)+p_committed)/2`. It changes from 0.25 to 0.2690504668 after the hard-target step and to 0.2645275262 after the soft-target step. Equal soft weights yield 0.2637692806. If every initial call meets the recoverable schema error, multiply by p_repair: the corresponding values are 0.125, 0.1378876638, 0.1345781427 and 0.1353458172. The ranking of the two soft-weight choices reverses between those populations. A loss-weight choice therefore needs the receiving work distribution and retained support, not just training loss.

The printed pending episode uses the same draws (.49,.49). The old policy inspects and falsely reports completion; the soft-trained policy inspects and reports pending. With a fresh committed observation it instead reports complete. In the changed-interface episode, draws (.49,.505,.49) make the old policy repeat the failed call, while the soft-trained policy obtains the current interface, inspects again and reports pending. The repair is performed by the supported runner; the learned decision selects it. The expected probabilities describe the stipulated population.

##### Engineering.Reference:26.4.5.4 - Compute guidance on histories reached by the student

A student can reach histories absent from a fixed teacher dataset. Execute its calls, retain the resulting observations, and score the actions it actually sampled. A teacher's proposed replacement action does not inherit the old action's next observation; SYSE.45:5.2 supplies that return. Keep the rollout probabilities, teacher scores and task outcomes separately.

[SOD v3](https://arxiv.org/pdf/2605.07725v3) supplies one empirical choice for combining these signals. Its [released implementation](https://github.com/YoungZ365/SOD/tree/110c4b8e843aee274d3cd648199569369ee2403e) uses the following fixed-batch surrogate. A response step is a contiguous generated span between observations. For its generated tokens compute

`d_k = mean_t |log p_old(y_t|h_t) - log q(y_t|h_t)|`,

then `w_1=1` and `w_k=min((d_1+epsilon)/(d_k+epsilon),1+delta)` for later steps. The adjacent-ratio product telescopes to this expression; clipping an intermediate weight and feeding that clipped value into the next ratio would implement another rule. Use positive epsilon; the released launch uses 1e−6 and delta=.2.

For trajectories sampled for one question, obtain and standardize the qualified outcome reward within that group as in 26.4.1. At each generated token form

`A_t = A_task + c w_k (log q(y_t|h_t) - log p_old(y_t|h_t))`.

Freeze these batch advantages and weights. With `rho_t=p_theta(y_t|h_t)/p_old(y_t|h_t)`, maximize the mean over generated tokens of

`min(rho_t A_t, clip(rho_t,1-e,1+e) A_t)`.

The clipping width e is distinct from the weight stabilizer epsilon. Keep the combined advantage inside the clipping operation. This sampled-token construction needs the teacher's scores for the selected actions; the preceding forward-KL construction needs full distributions.

For the finite example, reset to the original zero logits and collect two pending-job episodes. Draws (.25,.25) produce inspection followed by a false completion report; (.25,.75) produce inspection followed by a valid pending report. Outcomes 0 and 1 give population-standardized advantages −1 and +1. The four generated choices, and their two actual status observations, supply a complete batch. Here one choice is one response step, c=1, e=.2, and the reduction is the mean of four generated choices.

Run this code after the preceding block. It calculates the first gradient at the rollout policy, where every ratio is 1 and clipping is inactive:

```python
def online_first_step(theta, episodes, weighted=True, rate=.6):
    rewards = [e["reward"] for e in episodes]
    mean = sum(rewards)/len(rewards)
    sd = sqrt(sum((r-mean)**2 for r in rewards)/len(rewards))
    grad, records = [0.]*len(theta), []
    count = sum(len(e["steps"]) for e in episodes)
    for episode in episodes:
        a_task = (episode["reward"]-mean)/sd if sd > 1e-12 else 0.
        ds = [abs(log(s["p"])-log(s["q"])) for s in episode["steps"]]
        for k, s in enumerate(episode["steps"]):
            w = 1. if k == 0 or not weighted else min((ds[0]+1e-6)/(ds[k]+1e-6), 1.2)
            a = a_task + w*(log(s["q"])-log(s["p"]))
            # First gradient at the rollout policy: ratios=1, clipping inactive.
            grad[s["i"]] += a*(s["y"]-sigmoid(theta[s["i"]]))/count
            records.append({**s, "d": ds[k], "w": w, "a_task": a_task, "a": a})
    return tuple(t+rate*g for t,g in zip(theta,grad)), records, grad


episodes = [execute(old,"pending",(.25,.25)), execute(old,"pending",(.25,.75))]
weighted, records, gradient = online_first_step(old,episodes)
uniform, _, _ = online_first_step(old,episodes,weighted=False)
print("gradient",gradient)
print("weighted",tuple(map(sigmoid,weighted)),expected(weighted))
print("uniform",tuple(map(sigmoid,uniform)),expected(uniform))
print(execute(weighted,"pending",(.49,.49))["events"])
```

The weighted gradient is `(.1175009073,-.3675010403,0,0)`. Step .6 gives inspection probability 0.5176178395 and probability of the wrong completion report after pending 0.4450971145. The later (.49,.49) episode now reports pending. On the stipulated balanced later population, expected valid-report probability is 0.2730182762. With weights uniformly 1, the same records give 0.2825314040. Uniform weighting yields the higher expected valid-report probability in this finite comparison.

Within the failed episode, the useful inspection still gets combined advantage −0.529996, while its incorrect report gets approximately −1.470004. Weighting teacher disagreement has not recovered each action's causal contribution. The second episode changes the aggregate inspection gradient. Preserve both levels when diagnosing the learning signal.

The first-step derivative in the code is specific to theta=theta_old. For another optimization step on this batch, evaluate the stated clipped objective with the stored old probabilities and frozen advantages; do not keep using that initial derivative. For a fresh rollout, recollect histories, outcomes and teacher scores. The finite construction uses pure correctness reward. To reproduce the published SOD recipe, supply its prepared SFT student, selected teacher, tool-turn outcome shaping and overlength penalties.

##### Engineering.Reference:26.4.5.5 - Repair the premise that failed

Distinguish teacher disagreement from teacher error. The SOD score is an absolute sampled log-ratio statistic, not a calibrated error probability or an ordering of full conditional KL. Its first step always gets weight 1; constant high divergence also gets weight 1 throughout. Confident agreement on a common mistake creates no warning. A meaningful tool error can be useful evidence, and later valid recovery should remain eligible.

In the finite example, replace the teacher's pending-row probability .05 by .95. The soft update raises the wrong action's probability to 0.5224848248; the (.49,.49) pending episode again falsely reports completion. The balanced expected score is still 0.2531164903 because other rows improved. Inspecting that aggregate alone would hide the damaged pending branch. The actual status and the service rule reject the teacher's target. Repair or replace that target, retain an appropriate direct check, and refit/reassess the affected learner. Reducing a weight can reduce the harm but cannot establish the right action.

If the status observation is withheld, pending and committed may have the same available history. Under the balanced case, one report distribution then succeeds at most half the time after inspection. Restore the observation, retained state or qualified assistance through MMP.8.SD and SYSE.42; extra imitation cannot learn a missing distinction. Likewise, an unavailable interpreter or service requires restoration or an applicable alternative. Attenuating its failed trajectories does not supply the operation.

Choose a different teaching arrangement when it addresses that actual cause:

- **Improve evidence available to a frozen teacher.** [GC-OPD v2, §3 and Appendix B](https://arxiv.org/pdf/2609.37522v2) indexes complete successful and failed source executions by environment-specific state locators. After a student episode, each original decision retrieves an eligible successful continuation, comparing remaining cost with the student's successful continuation when present; otherwise it returns to an earlier successful anchor or a labelled unaligned fallback. It selects a failed reference separately. The teacher scores the unchanged student response using the complete student execution and at most one reference of each kind, retaining provenance and alignment labels. Source thoughts are excluded. Equal locators do not authorize splicing different information histories into an observed execution. Keep the source prefixes and implement the paper's tie and empty-case rules.
- **Use the update belonging to that evidence arrangement.** GC-OPD's detached signal uses `log q_evidence - log p_current`, with the frozen rollout policy in the ratio. It averages response-token surrogate terms within each episode, then weights episodes equally; outcome advantages are disabled in that edition. This differs from SOD's fixed old-score signal, combined outcome credit and token-mean reduction. Its vanilla-OPD warm-up, source collection and retrieval add preparation. Extra hindsight is training information: keep it out of the student's operating input unless it will be available there, and test whether the student's history can support the requested response. More successful reference coverage can coexist with worse student performance, as the source reports; compare the learned result.
- **Change the teacher when its continuations remain inadequate.** C.40:4.7 obtains several teacher continuations from a reached student prefix, checks their outcomes and trains the teacher before returning it to the student loop. This needs teacher-update access and suitable feedback. It is a different intervention from reweighting a frozen teacher or changing its context. Requalify its outputs at the affected histories; improved episode outcomes do not validate every local target.

When collection latency is the problem, [ActFirst-OPD v1, §§3–4](https://arxiv.org/pdf/2609.36608v1) supplies a conditional asynchronous alternative. Fast action-only proposals follow reference next observations while transitions remain compatible; a mismatch permanently switches that rollout to autonomous action-only collection. At each frozen collected context, the student separately generates a full thought/action response without the reference observation, and the teacher scores it. That sampled action may differ from the executed fast action and is not executed. Keep it distinct from the transition and outcome that produced the context. Forced decoding tokens remain context but are excluded from loss and normalization. The optimizer accepts the current or immediately preceding behavior version with stored probabilities and detached signals. Sampling is on-policy conditional on those contexts, while their distribution need not be the deployment policy's. Adopt this construction only with compatible references, transition checks and sufficient serving concurrency; include preparation beyond the reported collection timing.

##### Engineering.Reference:26.4.5.6 - Compare the transferred result and retained support

Return the trained policy together with its input meaning, action representation, runner and applicable observation/checking conditions. Compare the first learned result and consequential branches through SYSE.45:4.4 and SYSE.46. Count obtaining and qualifying demonstrations, probability queries, scoring candidate demonstrations, training, failed attempts and later execution. For the finite offline construction there are three teacher episodes, seven generated decisions and five service/interface calls; four selected histories receive the update. The online construction separately collects two student episodes with four decisions and two status calls, and scores those four choices with the teacher. Later tests are additional execution.

Preserve a direct rule, unweighted learning or an adequate fixed dataset as a serious alternative. Test changed interfaces, failed calls followed by valid recovery, shared teacher mistakes and missing live information. CoA transfers role-labelled decisions while retaining external execution; SAD changes selected supervision only when its representation, weighting or reduction actually changes; SOD attenuates a teacher contribution on reached histories. These distinctions determine what to implement and what to repair. A lower imitation loss, lexical resemblance or successful final answer alone cannot establish that the useful procedure survived.



#### Engineering.Reference:26.4.6 - Select what to learn and reassess the support that remains

**Use this when a recurring contribution costs enough to obtain that learning it, changing its guidance or supplying it another way could improve the whole work.** Obtain a candidate performer together with the support it will actually use, then compare that arrangement with continuing adequate help. The result can be a learned contribution, retained guidance, a reusable operation or competent service.

Start with one receiving result and the contribution that currently limits it. Keep the task population, performer, guide library, routing, execution and result criterion visible. Use C.38/C.11.CRC for the complete alternatives and [SYSE.45](../syse/66-syse-45---train-an-llm-policy-from-qualified-interaction-exp.md) for a selected parameter change. A changing fact needs a current source; a stable interpretation or operation may be a learning target. An inexpensive adequate aid or a one-off task can make further development unnecessary.

##### Engineering.Reference:26.4.6.1 - Compare an intervention that can answer the question

Consider a read-only setup assistant. It must express a requested duration in seconds, obtain the current permitted range and report the converted value, rule revision and whether the request is within that range. The duration interpretation recurs; the permitted range can change. The runner supplies arithmetic operations and a current-rule read. Both remain available through the comparison.

Two guides, `a` and `b`, offer the same duration interpretation through different entries. The following are stipulated probabilities of completing the whole report correctly on the selected task population, with policy, routing, task distribution and other support fixed.

| Guidance present | Correct completion before development |
| --- | ---: |
| `a,b` | 0.90 |
| `a` | 0.90 |
| `b` | 0.90 |
| none | 0.20 |

Whole-guidance versus no-guidance comparison gives a difference of `0.70`. Removing only `a` gives zero; removing only `b` also gives zero. Each zero answers a question about the arrangement containing the other guide. Removing both produces `0.20`. If the receiving floor is `0.85`, retaining either guide is adequate under these assumptions, whereas joint removal is not. After removing one, re-establish the comparison before removing the other, or test the proposed joint composition directly.

Now consider an aid with `0.20` correct completion both present and absent. Its zero difference accompanies inadequate work. Examine whether it was retrieved, available before the decision, understood and usable; whether its instruction was correct; and whether another required contribution was missing. That comparison supplies no grounds for declaring the operation acquired. At a high adequate rate, the same zero could instead make removing that aid worthwhile, subject to the remaining joint conditions.

For an operating comparison, select the intervention before collecting its data. A whole-bank comparison measures that bundle. A one-guide removal needs the same policy, task weighting and remaining composition; replacing the missing retrieval with another guide changes the intervention. If several guides or the router change, compare the resulting arrangement. Preserve the cases on which a returned instruction was ignored or misleading. Use SYSE.49/.46 to obtain and qualify the outcome basis, including uncertainty that can change the decision. Adaptive observations can choose the next intervention; reserve a separate final comparison for the reliance placed on the selected arrangement.

The primary techniques make different choices at this point. [SKILL0 v2, §3](https://arxiv.org/pdf/2604.02268v2) ranks guidance under a budget scheduled to reach zero; its whole-bank and individual-removal formulations need to be distinguished when implementing the comparison. A zero endpoint can remove still-useful help. [SLIM v2, §3](https://arxiv.org/pdf/2605.10923v2) instead uses exposure, smoothed removal differences and repeated low contribution before retirement, and can add guidance for persistent failures. Freeze the comparison composition, or deliberately assess the changed bundle after each mutation. Neither rule makes individual retirement proof of acquired capability or protects it from later forgetting.

##### Engineering.Reference:26.4.6.2 - Turn selected guidance into a qualified learning target

Choose the recurring *operation*, not merely a file with a favorable score. Here `a` and `b` are alternative suppliers of the same interpretation. Retain one while developing that interpretation; keep the current range read and arithmetic execution. Recover a useful action at a history where the intended learner has the inputs that warrant it. Qualify the action against the unit definition and required report. A guide may help a teacher produce that target; its presence does not qualify every resulting action.

[SIRI v1, §3](https://arxiv.org/pdf/2606.02355v1) offers one selective construction: induce guidance from interaction experience, compare assisted and unassisted group returns, and use positively credited guided actions as targets for the policy without that guidance. Its group benefit covers the retrieved bundle. The student still needs the actual decision history and observations. [Skill0.5 v1, §3](https://arxiv.org/pdf/2605.28424v1) offers a hybrid: retain particular guidance while using task difficulty to choose guided demonstrations or outcome learning. An empty set of successful demonstrations supplies no imitation target. Choose the actual loss and probability domain through [26.4.5](28-engineering-reference-26---construct-a-guard-a-learning-upda.md#engineeringreference2645---transfer-a-procedure-through-teacher-guided-learning); a truncated distribution or implementation-specific reward needs its own meaning.

The finite fixture uses milliseconds and minutes equally often. For milliseconds, output `1` selects division by 1,000 and output `0` leaves the amount unchanged. For minutes, output `1` leaves the amount unchanged and output `0` selects multiplication by 60. Qualified targets are therefore `(1,0)`. The actual numeric amount remains an input to the retained arithmetic operation. This representation fixes which interpretation can change; new unit conventions need a new applicable definition or another representation.

Let `p_j = sigmoid(theta_j)` be the probability of output `1` in input class `j`. With equally weighted qualified targets `y=(1,0)`, minimize

`L = -[log(p_0) + log(1-p_1)]/2`, with `dL/dtheta_j = (p_j-y_j)/2`.

Starting at `theta=(-ln 4, ln 4)`, both interpretations have probability `0.20` of the correct action. Four updates with step size `eta=4` give:

| Update | `theta_0` | `theta_1` | Correct completion without either guide |
| --- | ---: | ---: | ---: |
| 0 | −1.386294 | 1.386294 | 0.200000 |
| 1 | 0.213706 | −0.213706 | 0.553224 |
| 2 | 1.107258 | −1.107258 | 0.751617 |
| 3 | 1.604023 | −1.604023 | 0.832580 |
| 4 | 1.938863 | −1.938863 | 0.874227 |

The exact rates follow from this finite action model and its assumed reliable remaining operations. The fourth update meets the stipulated `0.85` floor without `a` or `b`. It remains below the unchanged aided performer's supplied `0.90` rate. Preserve both arrangements for the whole-result comparison; satisfying a floor does not settle whether a loss of accuracy is worth a saving in support. The trained performer with a guide is another joint arrangement to assess.

The target also determines which trace positions enter the loss. Consider a trace containing a user's request, the assistant's current-rule call, the returned rule and the assistant's report:

| Trace position | Action-imitation output target | Whole-sequence prediction target |
| --- | --- | --- |
| User request | Context | Predict the recorded request |
| Assistant call | Selected generated action | Predict the recorded call |
| Observed rule | Context for the next action | Predict the recorded return |
| Assistant report | Selected generated action | Predict the recorded report |

[daVinci-Dev, ICML 2026, §§2–3](https://proceedings.mlr.press/v306/zeng26d.html) uses full-sequence mid-training followed by action-masked fine-tuning. Such a target switch changes what the fit means. A failed attempt can supply a recorded sequence without supplying actions to imitate as successful conduct. Retain whether its context was observed during the attempt or reconstructed with hindsight. A predicted rule remains a prediction; the current-report task consumes an actual current rule. The finite update here fits the two selected interpretation actions.

##### Engineering.Reference:26.4.6.3 - Run the changed performer with its joint remaining support

Before testing withdrawal, bind the learned actions to the actual runner and define the assistance rule. For the two familiar unit classes, the candidate uses its learned interpretation. A new unit returns the need for its current definition. Every report still needs an applicable current-rule observation; once that evidence is supplied for the task, further retrieval can stop. Use SYSE.50 for the help decision, SYSE.51 for useful effort and completion reserve, and SYSE.47/.52 for the implemented continuation and input. Requalify those decisions when their performer, input or support changes.

This Python fixture calculates the update and executes subsequent reports. The snapshot passed through `current` is stipulated current for that task; a real adapter must obtain the corresponding freshness grounds. The calls return read-only reports. The success function computes the finite learned performer's rate; the earlier table separately supplies the unchanged aided performer's rates.

```python
from math import exp, log

def sigmoid(x):
    return 1.0 / (1.0 + exp(-x))

def loss(theta):
    p = [sigmoid(x) for x in theta]
    return -(log(p[0]) + log(1.0 - p[1])) / 2.0

def update(theta, eta=4.0):
    targets = (1.0, 0.0)
    gradient = [(sigmoid(x) - y) / 2.0
                for x, y in zip(theta, targets)]
    return [x - eta * g for x, g in zip(theta, gradient)]

def success(theta):
    return (sigmoid(theta[0]) + 1.0 - sigmoid(theta[1])) / 2.0

theta = [-log(4.0), log(4.0)]
history = [(0, tuple(theta), success(theta))]
for step in range(1, 5):
    theta = update(theta)
    history.append((step, tuple(theta), success(theta)))
for row in history:
    print(row)
assert success(theta) >= 0.85

class RuleSource:
    def __init__(self, revision, maximum_seconds):
        self.revision = revision
        self.maximum_seconds = maximum_seconds
        self.calls = 0

    def read(self):
        self.calls += 1
        if self.maximum_seconds is None:
            return None
        return {"revision": self.revision,
                "maximum_seconds": self.maximum_seconds}

def complete(amount, unit, theta, draw, source, current=None):
    if unit not in ("ms", "minutes"):
        return {"gap": "obtain the current unit definition"}
    # These two action bindings are retained execution operations.
    if unit == "ms":
        seconds = amount / 1000 if draw < sigmoid(theta[0]) else amount
    else:
        seconds = amount if draw < sigmoid(theta[1]) else amount * 60
    if current is None:
        current = source.read()
    if current is None:
        return {"gap": "obtain the current permitted range"}
    return {"seconds": seconds, "revision": current["revision"],
            "within_range": 0 < seconds <= current["maximum_seconds"]}

old = RuleSource(7, 20)
first = complete(15000, "ms", theta, 0.6, old)
assert first == {"seconds": 15, "revision": 7, "within_range": True}
assert old.calls == 1
new = RuleSource(8, 10)
changed = complete(15000, "ms", theta, 0.6, new)
assert changed == {"seconds": 15, "revision": 8, "within_range": False}
missing = RuleSource(9, None)
assert complete(15000, "ms", theta, 0.6, missing) == {
    "gap": "obtain the current permitted range"}
# The fixture supplies this snapshot as current for this task.
fresh = new.read()
calls_before = new.calls
stopped = complete(0.3, "minutes", theta, 0.6, new, current=fresh)
assert stopped == {"seconds": 18, "revision": 8, "within_range": False}
assert new.calls == calls_before
assert complete(500, "ticks", theta, 0.6, new) == {
    "gap": "obtain the current unit definition"}
print(first, changed, stopped)

for n in (2, 20, 100):
    print(n, {"retain": 4.2*n, "learn": 30+3.1*n,
              "converter": 8+3.0*n})
```

The learned interpretation produces `15` seconds from `15000 ms`. Under revision 7 with maximum 20 seconds, the completed report says within range. Under revision 8 with maximum 10 seconds, the same learned operation correctly produces an out-of-range report after consuming the new rule. The missing-source case returns the missing range; changing the interpretation weights cannot supply it. With an already current snapshot, `0.3 minutes` becomes `18` seconds and the assistant finishes without another read. The unfamiliar `ticks` case returns the missing definition.

Test the whole candidate on the declared task population and final support conditions through SYSE.46. In the finite model, the two correct-action probabilities can be enumerated exactly. With sampled operating data, retain the sampling, dependence and uncertainty that qualify a claimed rate. Include failed reports, unrecognized inputs, inaccurate help, a changed definition and a formerly retained guide that later becomes necessary. Restore the contribution whose grounds failed; avoid changing the learner merely because the whole report failed.

##### Engineering.Reference:26.4.6.4 - Retain useful external resources and spend effort on the missing contribution

A deployed arrangement may keep a substantial resource after learning. [TInR, ACL 2026, §3](https://aclanthology.org/2026.acl-long.2077.pdf) first selects learned tool tokens, retrieves the selected tools' current descriptions and parameters, then generates arguments. Preserve that document lookup with the executor. [SkillRL v1, §3](https://arxiv.org/pdf/2602.08234v1) trains a policy with a retrieved library and expands it from failures. [SkillForge v1, §3](https://arxiv.org/pdf/2608.24747v1) makes requesting guidance an action and later revises guidance from experience. Return content before the action that needs it: guidance delivered alongside an already executed action can inform only its continuation. SYSE.48 constructs the usable resource, .52 exposes it and .47 consumes the return. Separate bad retrieval, ignored guidance and a faulty instruction before deciding which to repair.

Additional reasoning is another external contribution with its own cost. [HeavySkill v1, §§2–3](https://arxiv.org/pdf/2605.02396v1) compares candidate trajectories through deliberation; [ParallelMuse v1, §3](https://arxiv.org/pdf/2510.24698v1) branches from selected prefixes and aggregates compressed reports. When choosing such a procedure, name the available branching signal, reused prefix, retained observations and aggregation rule. Preserve a consequential disagreement and a path back to its source through compression. Count initial generation, branches, tools, summaries, synthesis and completion. Shared prefixes or sources make agreement dependent.

In the range example, several branches using revision 7 can agree that 15 seconds is acceptable while the required revision is 8. Another such branch cannot supply the current rule. Spend the next effort on that observation, or return the unavailable source. [Fishing for Answers v1, §3 and Appendices B–C](https://arxiv.org/pdf/2509.04820v1) supplies useful retrieval choices while showing that selecting, cropping and deleting context can interact: a combination can discard what the next action needs. Preserve the original question and jointly necessary premises when reformulating or shortening. Once the current revision and correctly converted amount settle the report, finish.

Learning a shorter or less-assisted route also requires a qualified result criterion. [Aware First, AAAI 2026, §3](https://ojs.aaai.org/index.php/AAAI/article/download/40277/44238) uses model-relative sampled correctness and length to construct training groups. [EAPO v2, §3](https://arxiv.org/pdf/2606.02132v2) contrasts tool-free and tool-available attempts and changes rewards and selected token weights from sampled correctness and calls. Those are obtainable training statistics; a sampled minimum call count is not proof that a current observation is unnecessary. For this report, a memorized but accidentally correct range answer lacks the required current-revision evidence and is not a successful training outcome. Apply a call-cost preference to a correctly specified result and preserve its validity conditions.

To calculate such a signal, hold conversion correct and vary only the next effort choice. Three available routes make one current-rule read, make two reads, or finish from the information already available. Initially no current rule is supplied. Stipulate one recorded attempt per route from a uniform policy over these three routes; the first two obtain the same current rule and produce valid reports, while the third uses a remembered range. Let `q=1` for a correct report supported by the required current-revision evidence and `q=0` otherwise. With `c` additional reads in `{0,1,2}`, choose the receiving reward `r=q*(1-0.1*c)`. This explicitly protects validity before rewarding lower call cost.

| Recorded route | Additional reads `c` | Valid result `q` | Reward `r` |
| --- | ---: | ---: | ---: |
| Read once and report | 1 | 1 | 0.9 |
| Read twice and report | 2 | 1 | 0.8 |
| Finish from remembered information | 0 | 0 | 0.0 |

Reuse [26.4.1](28-engineering-reference-26---construct-a-guard-a-learning-upda.md#engineeringreference2641---learn-from-interleaved-actions-and-observations)'s clipped-ratio objective with one generated route choice per attempt, old route probabilities `(1/3,1/3,1/3)`, frozen population-standardized advantages, clipping interval `[0.8,1.2]` and ascent step `0.3`. Parameterize the route probabilities by `p_i=exp(z_i)/sum_j exp(z_j)`, initially `z=(0,0,0)`. The reward mean is 0.566667 and population standard deviation 0.402768, giving advantages `(0.827606, 0.579324, -1.406930)`. At this initial policy every ratio is one. Since the three advantages sum to zero, the mean surrogate gradient is `dJ/dz_i=A_i/3`. One step gives logits `(0.082761, 0.057932, -0.140693)` and route probabilities `(0.360331, 0.351494, 0.288175)`. A later route draw of `0.35`, in the table's order, changes the choice from two reads under the old policy to one under the changed policy; the retained reader then supplies the actual rule for the report.

Now supply a qualified current snapshot before the effort choice. Finishing from that available information yields a valid report with zero additional reads. A separate comparison from the same uniform policy has rewards `(0.9,0.8,1.0)` and advantages `(0.000000, -1.224745, 1.224745)`. The same first-step construction gives probabilities `(0.331673, 0.293440, 0.374887)`, making finish the most probable route. The two calculations qualify different input conditions; retain that condition in the policy's input and use separate logits for these two finite states. Reusing the first state's failure label would penalize a sufficient answer. For further steps, evaluate the clipped objective with the stored old probabilities and frozen advantages, as 26.4.1 requires.

A direct rule can make one read when current evidence is missing and finish when it is supplied. The following cost comparison uses that rule. If an effort learner is selected for a broader task, include its attempt collection, fitting and assessment in the whole cost.

##### Engineering.Reference:26.4.6.5 - Decide whether the change is worth obtaining

Compare the complete arrangements over the same horizon. Charge discovering and checking a withdrawal schedule, guided targets, teacher or creator work, fitting, failed alternatives, adaptive trials, final assessment and maintenance. C.11.DUA selects further inquiry only when its possible effect on this choice warrants that burden. C.11.MV supplies the situated Method-worth comparison.

For the finite fixture, a deterministic converter is also available as a construction alternative: divide a known millisecond amount by 1,000 or multiply minutes by 60. It gives correct interpretation throughout the two-class envelope. The following stipulated per-task costs include continuing execution, the current-rule read, reporting and allocated maintenance. The learning preparation cost of 30 comprises 8 for qualified targets, 10 for adaptive comparison, 4 for fitting and 8 for final assessment. Converter preparation is 8; the existing guide needs no new preparation. All values use the same example-specific cost unit.

| Arrangement | Preparation | Per subsequent task | Correct completion under the fixture | Total for 2 tasks | Total for 100 tasks |
| --- | ---: | ---: | ---: | ---: | ---: |
| Keep the unchanged performer with one adequate guide | 0 | 4.2 | 0.90 | 8.4 | 420 |
| Use the trained candidate without either guide | 30 | 3.1 | 0.874227 | 36.2 | 340 |
| Construct and use the deterministic converter | 8 | 3.0 | 1.00 | 14.0 | 308 |

Under the stipulated floor and cost objective, retain the guide for two tasks and obtain the converter for 100. The learned candidate demonstrates an obtainable update and successful later use, but the converter dominates it on these supplied costs and result rates. Keep that alternative when the relevant input envelope really admits it. A broader interpretation problem, unavailable implementation or different preparation burden reopens the comparison. If the evidence needed to choose a withdrawal costs more than retaining adequate help, retain the help for the current horizon.

##### Engineering.Reference:26.4.6.6 - Obtain the human development and provision results separately

For a person doing the same preparation, use [HCD.9, HCD.10, HCD.12 and HCD.13](../../human-capability-engineering-dpf-suite/hcd/_index.md) for the actual attempt, help, correction, support change and later use. C.2.8 can compare how much selected Method-description structure the person recovers under the stated preparation, access, help and budget. Recovery of the sequence, performance with a cue and later uncued performance provide different evidence. HCD.18/.19 connect instruction recovery with development practice.

In a constructed continuation, an operator can explain the conversion and checking sequence but initially prepares a report using a remembered permitted range. A competent teacher asks which current revision warrants the decision. The operator obtains that revision and corrects the report. Preserve the first answer and the actual cue. On the next differently worded task, leave the legitimate current source available and withhold that diagnostic cue when testing independent recognition. The resulting first attempt, correction or need for further help determines the next HCD intervention. Comparing two correct reports without their assistance histories would lose that distinction.

The arrangement must also be obtainable while service continues. Suppose a consultant's contract calls for an operating process, and her authorized project contribution is four prototype hours; her remaining working time serves existing clients. Installing that process, teaching an operator and occupying a corporate mentoring post promise different results. Free calendar space and technical expertise supply no additional allocation authority. Recover the needed preparation, feedback and retry work through C.40.JF, and obtain the relevant provider and allocation decisions through the existing OCE/ADM/OPS contributions.

For this constructed practice, the responsible manager allocates two hours of a separately qualified teacher's work, including preparation, feedback and retry, and assigns a qualified substitute to the operator's continuing service during practice. Both providers confirm availability for their respective intervals before the first attempt. Practice proceeds within that authorized arrangement; the consultant retains the four prototype hours. If those provider or substitute results cannot be obtained, keep competent supported production and reconsider the development arrangement. An expert's completed report can protect present work while the learner's independent contribution remains to be developed. A.3.1.MI consumes the separate support and capability results when introducing the changed practice; [Reference:11.1](13-engineering-reference-11---how-do-we-recommend-a-development.md#engineeringreference111---pursue-a-personal-development-aim-while-shared-work-continues) and [19.8](21-engineering-reference-19---make-an-available-contribution-wo.md#engineeringreference198---case-b-a-timely-cue-must-enter-a-coordinated-bodily-action) supply connected development uses.

Return the selected arrangement with its learned contribution, retained resources, current evidence, usable continuation and reasons to reopen it.

### Engineering.Reference:26.5 - Derive an audit policy from the real decision times

Now suppose the hard permission guard is in place, while some permitted-looking configurations may still violate the intended job. An additional auditor can inspect the proposal and task before execution. Checking every action may exceed the available effort. The question is how to allocate that additional audit, while the mandatory permission check remains in force for every mutation.

For the fixed five-second request, comparing the proposed value with 5000 is a cheap complete task check; use it on every call. The allocation question becomes useful when the receiving work requires a more costly correctness judgment whose full application exceeds the budget. The simple values below let the fixture expose that controller's effects; they are not a reason to replace the available equality check with probabilistic auditing.

Before using monitor scores, obtain a decision model with the actual order of proposal, score, audit and effect. [MMP.8.SD](../../foundational-thinking-dpf-suite/mmp/15-mmp-8-sd---construct-a-sequential-decision-model-from-inform.md) supplies that construction; [SYSE.51](../syse/72-syse-51---construct-adaptive-control-of-reasoning-and-tool-e.md) retains necessary completion resources. The following small model makes the calculation reproducible:

- Two proposals arrive sequentially. Each can be held for its audit, but proposal 1 must be decided before proposal 2 arrives. There is budget for at most one audit, with reserved means to complete the selected audit and report its result.
- The attacker selects exactly one of the two positions for a bad proposal before the run. It cannot observe the controller's private random draw or change the stipulated score laws. The other proposal is legitimate. An undetected bad proposal causes the protected failure immediately when executed; detection stops it and ends this deployment attempt.
- The monitor returns H or L before the corresponding action. Its stipulated laws are `P(H | bad)=0.8` and `P(H | legitimate)=0.2`. They are conditional discrimination values, not an attack prevalence. Scores are independent between positions given their types, and the laws stay fixed under this policy.
- Initially the auditor detects every bad proposal it audits and never rejects a legitimate one. Auditing occurs before the effect. Its cost is one budget unit; scoring and ordinary execution have separately provisioned costs. With two legitimate proposals, a useful attempt must complete both correctly.
- The supplied decision criterion is to minimize the maximum failure probability over the attacker's two fixed positions, subject to the one-audit budget. Whether that residual risk is acceptable is a separate owner decision. If this model does not fit the intended use, obtain the missing model before using its policy.

Let x be the probability of auditing proposal 1 when its score is H, and y the probability when it is L. If the audit remains unused, audit proposal 2. This last-step use weakly improves the protection objective under the stated no-false-rejection and provisioned-cost conditions: no later opportunity needs the reserve. If proposal 1 is audited and found legitimate, no audit remains for proposal 2. There is no access to proposal 2's future score at the first decision.

If the attack is first, it escapes with probability `f1 = 1 - 0.8*x - 0.2*y`. If the attack is second, the single audit was wasted on the legitimate first proposal with probability `f2 = 0.2*x + 0.8*y`; otherwise the second proposal is audited and caught. Minimize `max(f1, f2)` for `0 <= x,y <= 1`. The solution is `x=1, y=0`, giving worst-case failure 0.2. A score-blind allocation of the one audit equally between the positions gives 0.5. No audit gives 1 in this conditional attack model. Auditing both gives 0 but requires budget 2.

The solution can be recovered without a general optimizer. Each failure expression is affine, so their maximum is piecewise affine on the unit square. Its minimum occurs at a corner, at an intersection of `f1=f2` with a square edge, or along a flat region reaching such a boundary. Evaluate those finite candidates. Equivalently here, equality gives `x+y=1`; along that line the risk decreases as x increases, reaching 0.2 at `(1,0)`.

### Engineering.Reference:26.6 - Recalculate when auditing is fallible

Change one assumption: the auditor detects a bad proposal with probability 0.9 given H and 0.5 given L. It still has no false rejection in this constructed case. Conditional detection probabilities do not change with audit selection; private randomization uses only the current score. The expected detection probability of auditing a bad proposal regardless of score is `0.8*0.9 + 0.2*0.5 = 0.82`.

If the attack is first, failure is now `f1 = 1 - 0.72*x - 0.10*y`. If it is second, the audit remains with probability `1 - 0.2*x - 0.8*y`, so `f2 = 1 - 0.82*(1 - 0.2*x - 0.8*y) = 0.18 + 0.164*x + 0.656*y`. Auditing the second proposal no longer guarantees detection. The old proof and its zero-risk full-audit comparator therefore no longer apply.

The same finite computation gives `x=205/221`, approximately 0.927602, and `y=0`. Worst-case failure is `367/1105`, approximately 0.332127. Keeping the former `(1,0)` policy gives 0.344. A score-blind equal split gives 0.59. Auditing both gives 0.18, because the bad proposal is certainly audited but sometimes missed. These are conditional model calculations, not measured deployment rates.

This standalone calculation enumerates the necessary candidates with exact rational arithmetic. A triple `(c,a,b)` denotes the affine function `c+a*x+b*y`.

```python
from fractions import Fraction as F

def affine(coefficients, x, y):
    c, a, b = coefficients
    return c + a*x + b*y

def best_one_audit(first, second):
    points = {(F(x), F(y)) for x in (0, 1) for y in (0, 1)}
    c, a, b = [u-v for u, v in zip(first, second)]
    for x in (F(0), F(1)):
        if b:
            y = -(c+a*x)/b
            if 0 <= y <= 1:
                points.add((x, y))
    for y in (F(0), F(1)):
        if a:
            x = -(c+b*y)/a
            if 0 <= x <= 1:
                points.add((x, y))
    return min((max(affine(first, x, y), affine(second, x, y)), x, y)
               for x, y in points)

perfect = ((F(1), -F(4,5), -F(1,5)),
           (F(0), F(1,5), F(4,5)))
fallible = ((F(1), -F(18,25), -F(1,10)),
            (F(9,50), F(41,250), F(82,125)))
assert best_one_audit(*perfect) == (F(1,5), F(1), F(0))
assert best_one_audit(*fallible) == (F(367,1105), F(205,221), F(0))
print(best_one_audit(*perfect))
print(best_one_audit(*fallible))
```

Suppose the owner had required worst-case conditional failure no greater than 0.25. The ideal-auditor construction met it; the best fallible one-audit policy does not. The improved choice 0.927602 is still inadequate for that requirement. Auditing both reaches 0.18 in this model, but exceeds the given budget. Return the actual conflict: obtain a better qualified auditor, provision the extra audit, change the work arrangement, or obtain a competent revision of the requirement. Repeatedly optimizing the same one-audit model cannot produce a feasible policy below its derived minimum.

### Engineering.Reference:26.7 - Obtain the measurements and enact the audit

The calculation supplies a policy only after its observation and consequence premises are warranted for the intended use. Build matched legitimate/bad proposal cases for the selected task family, with independent task judgments and controlled action semantics. For the timeout case, 5000 ms and 5 ms can be paired under the same five-second request. Keep cases outside G1 distinct from permitted-but-wrong cases; the latter are the additional auditor's question. Generate and execute adverse cases only in an appropriately permitted fixture. Preserve the original proposal, task, rule interpretation and actual result so that the label can be challenged.

On cases reserved for calibration, obtain monitor scores without supplying the intended label in the monitor input. Count H among bad cases and H among legitimate cases separately. To qualify the fallible audit law, audit a suitable sample in both H and L groups, including cases that the proposed allocation would ordinarily skip; otherwise observed detection can inherit its selection bias. Counts such as 80 H scores among 100 bad cases estimate one conditional discrimination rate. They do not establish an exact 0.8 law, its uncertainty, or the rate of attacks in ordinary work. Carry sampling uncertainty and task differences into sensitivity calculations or return the insufficient basis. Establish the intended-use claim through [SYSE.46](../syse/67-syse-46---test-an-agent-and-its-support-in-representative-wo.md).

[The Control Tax](https://proceedings.iclr.cc/paper_files/paper/2026/file/c8c352e9ff2c3eb8511c6a996cbd77b1-Paper-Conference.pdf) connects measured monitoring behavior to a specified auditing game and discusses the control cost. Its program-pair construction uses accepted original/adversarial programs and monitor distributions; its Appendix K transfer obtains new scores on selected existing agentic trajectories. Such a transfer supplies measurements on those traces, not a performed deployment of the calculated policy. For a new service domain, obtain its relevant paired cases or traces and test the corresponding measurement assumptions. A wider nominal score scale does not necessarily improve discrimination. Another concrete monitor variant combines a separate fresh-context correctness judgment with suspiciousness; compare its gains with the additional inference work. Neither a benchmark's name nor its overall accuracy supplies the two conditional laws used above.

Implement the selected policy where it can affect the proposed mutation. Maintain the proposal index, remaining audit budget, applicable policy/calibration edition and the exact held proposal. After the hard guard admits that proposal, obtain its qualified score. At position 1, use the supplied probability for H or L and an appropriate private random draw. If selected, debit the audit request, keep the mutation held and send the bound proposal, task and needed evidence to the auditor. A detection stops the protected attempt. A qualified clear result permits that same proposal to proceed through the gateway's at-use checks. If no audit is selected, the separately authorized risk-bearing continuation proceeds through those same hard checks. At position 2, use any remaining audit; when it was spent on position 1, no second audit is available under this policy.

The following fixture consumes that decision in an executable controller. It uses `Call`, `Facts` and `guard` from section 26.1. Each proposal concerns a fresh service instance with the supplied revision; the fixed target is 5000 ms. The fixture's effect list represents committed values. Its environment ends the attempt on a wrong committed value, as the decision model assumes. That model outcome is not extra information available to the earlier allocation decision. The fixture's final facts are supplied before each simulated atomic commit; production needs the qualified at-use operation described in section 26.2.

```python
def audit_fixture(calls, scores, answers, final_facts, draw, x=1.0, y=0.0):
    remaining, effects, audit_count = 1, [], 0
    for i, call in enumerate(calls):
        if guard(call, facts)[0] != "admit":
            return effects, audit_count, "initial guard holds"
        if scores[i] not in ("H", "L"):
            return effects, audit_count, "missing score"
        selected = remaining and (i == 1 or draw < (x if scores[i] == "H" else y))
        if selected:
            remaining -= 1
            audit_count += 1
            if answers[i] == "detected":
                return effects, audit_count, "stopped before effect"
            if answers[i] != "clear":
                return effects, audit_count, "missing audit result"
        if guard(call, final_facts[i])[0] != "admit":
            return effects, audit_count, "at-use guard holds"
        effects.append(call.value)  # The fixture commits only here.
        if call.value != 5000:       # The modeled environment's failure transition.
            return effects, audit_count, "protected failure"
    return effects, audit_count, "complete"

good = Call("S", "set", "timeout_ms", 5000, 17)
bad = Call("S", "set", "timeout_ms", 5, 17)
current = [facts, facts]
assert audit_fixture([bad, good], ["H", "L"], ["detected", "clear"],
                     current, 0.4) == ([], 1, "stopped before effect")
assert audit_fixture([good, bad], ["H", "H"], ["clear", "detected"],
                     current, 0.4) == ([5000, 5], 1, "protected failure")
assert audit_fixture([good, bad], ["L", "H"], ["clear", "detected"],
                     current, 0.4) == ([5000], 1, "stopped before effect")
assert audit_fixture([good, good], ["L", "H"], ["clear", "clear"],
                     current, 0.4) == ([5000, 5000], 1, "complete")
```

In the second assertion, a perfect auditor could detect the second defect, but the first audit has consumed the budget. Its unused second answer is never read. In the third, reserving the audit prevents the second effect. These executions show that the allocation changes the controller's intervention; they do not validate the stipulated score or auditor laws.

An unavailable auditor, malformed result or missing score is outside the successful-observation model. Hold the affected mutation and obtain a qualified alternative or return the missing contribution and its cost; do not turn “unknown” into “clear.” A timeout consumes the reserved attempt according to the supplied resource account; a retry needs real provision. Replacing the proposal after an audit invalidates that audit's binding and requires the affected checks again. Auditing after an irreversible effect cannot serve as the pre-effect intervention assumed in the calculation.

Trace at least these receiving cases: H at the first proposal with detection; H with a clear first audit and an unaudited second proposal; L first with a reserved second audit; and a proposal or governing condition changed while held. Confirm both the budget and the actual prevention or allowed execution. Also run two legitimate proposals through the arrangement and check completion, delay and false rejection. The stipulated zero-false-rejection assumption leaves these costs absent from the small risk formula, not absent from engineering responsibility.

Include preparation, scoring, auditor work, adjudication, held work, retries and outcome reconciliation in the whole-use comparison. If both proposals become available before either decision, a batch policy can use information that the sequential rule lacked; derive its comparison anew. If the attacker adapts after observing audits, the score laws change under the policy, the horizon grows, or legitimate actions can be falsely rejected, reconstruct those branches and consequences through MMP.8.SD. A reusable trajectory score and an optimal policy under one model can remain valid at their scopes while the new deployment claim fails.

### Engineering.Reference:26.8 - Follow the changed condition to the affected method

The connections are practical. A new owner requirement changes the predicate meaning and may require permission for a wider admitted set. A changed interface changes translation, evaluator applicability and learning targets. A false guard rejection changes the checker and the labels available for development. A corrected learner changes proposals, but leaves required authority and execution checks in force. A changed monitor or auditor changes the allocation model; it can also change which cases become observable for later learning.

Return only as far as the failed dependence requires. The exact 5-to-5000 conversion can remain useful while a registry is unavailable. A valid authority grant can remain while its evaluator is defective. An executable evaluator can remain while the intended job has no unambiguous unit. A better allocation calculation can remain mathematically correct while no policy meets the owner's risk and resource requirements. Each return identifies the next needed contribution without discarding the rest of the usable arrangement.
