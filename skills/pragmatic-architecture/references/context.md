# Context: the facts that decide a design

A design is good only relative to its task. The context is the smallest set of facts that
decides which design is admissible and which is best here. Gathering it is part of the method,
and so is stopping.

## Contents

- [The filter](#the-filter)
- [The eight groups](#the-eight-groups)
- [Label what is known](#label-what-is-known)
- [Where facts come from](#where-facts-come-from)
- [From adjectives to scenarios](#from-adjectives-to-scenarios)
- [The criteria](#the-criteria)
- [Cost over the horizon](#cost-over-the-horizon)
- [When the context is enough](#when-the-context-is-enough)
- [The passport](#the-passport)

## The filter

Ask of every candidate fact:

> Could another plausible value of this factor change what is admissible, which design is
> chosen, how it is built, how it is verified, or how it is recovered?

If not, drop it. The groups below are a map of questions, not a questionnaire: most tasks are
decided by three to six factors. Do not rebuild context that is already sufficient.

## The eight groups

| Group | Ask | A typical deciding fact |
|---|---|---|
| **1. Result and scope** | Who needs which result? What is observable success? What is out of scope? Which part of the request is the need and which is a suggested solution? Does something existing already give the result? | "The user asked for a cache; the need is a page under 300 ms." |
| **2. Meaning and invariants** | What do the domain words mean here? Which rules always hold? Which states and outcomes are forbidden? Who may define or change a rule? Which behaviour do callers already rely on, documented or not? | "An order is never charged twice." |
| **3. Data and load** | Volume, growth, distribution, the largest item, hot keys, read/write ratio, latency budget, lifetime of the data, how fresh a read must be. | "10^3 rows fit in memory; 10^8 do not." |
| **4. Quality and risk** | What does a failure cost in money, data, trust or safety? Which outcome is unacceptable and which is merely unwanted? What degradation is allowed? What is exposed to an attacker? | "A delayed email is fine; a lost payment is not." |
| **5. Variability and uncertainty** | Which change is confirmed to come next? Which is speculation? What is unknown, and when will it be known? Which decisions are expensive to change later? | "A second provider is signed for next quarter." |
| **6. Environment** | Runtime, deployment, the real contracts of dependencies (timeouts, ordering, durability, idempotency), versions that run at the same time, operational tooling, the conventions of this codebase. | "The queue delivers at least once." |
| **7. People and ownership** | Who owns the code, the data, the on-call? Who consumes the interface? What does the team already know how to run? Who carries the burden this design creates? | "Another team owns the table." |
| **8. Economics and reversibility** | Deadline, budget, how long this will live, the cost of being wrong, the cost of reversing, the cost of delay. | "A two-week experiment; a five-year ledger." |

Separate must-haves from preferences inside every group. Beauty, speed of delivery and low cost
do not compensate for a broken must. When it is unclear whether something is a must, find who
has the right to say.

## Label what is known

| Label | Carries |
|---|---|
| **Fact** | Where it was observed: file and line, command output, document, date |
| **Requirement** | Who set it, and whether it is a must or a preference |
| **Assumption** | How it could be checked, and what breaks if it is false |
| **Unknown** | Who can answer or which experiment would, and which decision waits on it |

An assumption written as a fact is the most common defect of a design document. Keep three more
things apart: what is required, what the system does today, and why it came to be so. Today's
behaviour may be a defect; the historical reason may no longer hold.

## Where facts come from

Look up technical facts: code, tests, schema, configuration, version history, issues, the
running system, vendor documentation for the version in use. Ask the user about what the code
cannot decide: the result they need, which outcome is unacceptable, and the product trade-offs
(allowed degradation, delay, loss, manual recovery). Do not ask the user for a fact that can be
read, and do not guess a trade-off that only they can set.

Ask at the moment a fork appears, with the options, a recommendation and the consequence of
each. A question whose every answer leads to the same design is not worth asking.

## From adjectives to scenarios

"Fast", "reliable", "scalable", "flexible" and "secure" decide nothing. Turn each one that
matters into a scenario:

| Part | Example |
|---|---|
| Source and event | A client repeats the same payment request |
| Conditions | after a timeout, while the first request is still running |
| Required response | exactly one charge; both requests get the same result |
| Measurable bound | within the 24-hour retention of request identities |

A scenario lets two designs be compared on the same ground and tells what evidence would
confirm it. If the bound is unknown, say so and ask or measure. An invented number is worse than
an open question, because later readers will treat it as a requirement.

Write scenarios only for qualities that can change the choice. For flexibility, the scenario is
a concrete next change: "add a third export format", not "be extensible".

## The criteria

Judge each property separately. No single score for elegance exists, and none should be
invented.

| Criterion | Question | Not the same as |
|---|---|---|
| **Correct** | Does it give the required result and keep every must? | Passing the tests that exist |
| **Simple** | How many independent concepts, states and hidden conditions must be held in mind to use or change it correctly? For which reader, which action, at which scale? | Short, familiar, few files |
| **Elegant** | Does a small consistent set of concepts explain many cases without exceptions? | Clever, novel, abstract |
| **Fitting** | Does its cost match the stakes, scale, deadline, team and lifetime of this task? | The best design in general |

Order of judgement: exclude designs that break a must; compare the rest on the scenarios that
matter here; state the trade-off accepted. This finds a good design for this context, not a
global optimum. Elegance is a diagnostic signal that the model fits the problem. It is not
evidence that the design works.

Checks, redundancy and explicit contracts add conditions and can still be right. What must go
is the *unneeded* state, dependency, variant or duty.

## Cost over the horizon

Compare whole ways of getting the result, over the time the solution is expected to live:

- creation: design, code, review, verification;
- operation: running, monitoring, on-call, learning;
- change: the next plausible changes;
- migration: getting from the current system to this one, and later away from it;
- failure: the consequences of realistic failures and the cost of recovery;
- delay: the value not delivered while this is being built.

This is a model for reasoning, not a formula. Hours, money, delay and the severity of a failure
do not add up on one scale; show them side by side and say who carries each. Work moved to the
caller, the operator or the next maintainer has not disappeared. A design that is cheapest to
write and most expensive to operate is a legitimate choice only when someone has chosen it
knowingly.

Keeping the current solution, reusing an existing component, narrowing the agreed scope and not
building at all are admissible outcomes. Narrowing the scope changes the requirement, so it
needs the consent of whoever set it.

## When the context is enough

Stop gathering when all of these hold:

- every deciding factor is a fact, or an assumption with a named check;
- no remaining unknown could change the choice, or the first step is cheap to reverse if it
  turns out wrong;
- the next safe step is clear.

Run an experiment only when one of its possible results would change the decision and it costs
less than being wrong. Use what is already known first. Required guarantees are not relaxed to
save research.

Reopen the context when a deciding fact changes: a new requirement, a dependency that behaves
differently from its documentation, a measurement off by an order of magnitude. Do not redo the
whole analysis after every step.

## The passport

For a design that needs a record, the context fits in a few lines:

```text
Result      who gets what; how success is observed; out of scope
Musts       invariants and forbidden outcomes, each with who set it
Deciders    the 3-6 facts that decide the choice, each labelled fact / requirement / assumption
Scenarios   the quality scenarios that matter, each with a bound or "bound unknown"
Unknowns    open questions, who or what answers each, which decision waits
Horizon     how long this lives; what is expected to change next; what is costly to reverse
```
