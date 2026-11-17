# When the product itself calls an LLM

Read when non-deterministic model behaviour is part of the running product: generation, data
extraction, tool selection, an agent workflow. Code does not become stochastic because an agent
wrote it, so everything else in this skill applies unchanged to ordinary code.

## Split the system in two

- **Deterministic shell:** schemas, permissions, argument validation, persistence, routing. Check
  it with ordinary tests.
- **Model behaviour:** define a task set, quality criteria and typical errors. Record the
  conditions of every comparison: model version, prompt, tools, data, environment.

## Evaluating model behaviour

- Use ordinary, boundary and adversarial examples.
- Repeat trials where stability matters, and count every outcome. One lucky run is not stable
  behaviour: "succeeds at least once" and "succeeds every time" are different product goals.
- Compare with the previous version on the same tasks.
- Keep separate examples for tuning and for the final check, so the prompt is not fitted to one
  set.
- Check the result in the environment: the right object was created, permissions held, the goal
  was reached.
- Do not grade free text by exact match unless the format is the requirement.
- A model-based grader needs a clear rubric, calibration against expert judgment and analysis of
  the disputed cases.
- Deterministic gates block. Model-based judges advise.

## Boundary traps

- A fake model that returns a ready object tests the service flow, not the boundary. At least one
  test starts from raw output in the provider's shape and passes through the production parser
  and validator, the same way production does.
- Assert on the rendered prompt: the real input text is present and no unfilled placeholder
  remains. Do not mock the component that builds the prompt.
- For every "in progress" status, show that a provider error cannot leave the record in progress
  forever.
- A real-provider smoke path asserts the terminal state and the shape of the content, and cleans
  up remote artefacts.
