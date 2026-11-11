# Research and validation

Sources verified **2026-10-21**. Keep methodological sources separate from the workflow adopted by the skill.

## Match the method to the question

| Question | Method | What the result does not show |
|---|---|---|
| What task are people solving, and in what context? | Interviews, observation, analysis of support requests | The share of the whole audience with this need |
| Can people find a section or an item? | Findability tasks, tree testing; card sorting for grouping | A guarantee that the final navigation is usable |
| Can people complete the task? | Usability testing of a realistic scenario | The exact prevalence of a problem in the population |
| What is the level of a metric? | Quantitative measurement with a defined sample | The cause of a difference, without further research |
| Did the change improve the outcome? | A properly designed experiment | Universal benefit for all segments and tasks |

The table is a methodological synthesis. The methods complement each other; aesthetic preference does not replace task success.

## Methodology sources

**RE-03 — [Test Complex Interactions Earlier with AI Prototyping](https://www.nngroup.com/articles/test-earlier-with-ai/)**, Megan Chan / NN/g, 2026-09-11. Choose the fidelity of the prototype to fit the question. To test behavior, implement the necessary transitions, realistic anonymized data and edge states. Run a pilot. Do not mistake the visual finish of an AI prototype for release readiness of the product. For a question about structure or text, static material may be enough.

**RE-04 — [How Many Participants for a UX Interview?](https://www.nngroup.com/articles/interview-sample-size/)**, Maria Rosala / NN/g, 2021-10-31. Set the number of interviews by the question, the diversity of the audience and the emergence of new themes. Analyze the material as you collect it. Do not carry the "five users" rule over to every interview and do not estimate the prevalence of a problem from a small qualitative sample.

**RE-05 — [Quantitative Usability Studies: Sample-Size Recommendations](https://www.nngroup.com/articles/summary-quant-sample-sizes/)**, Raluca Budiu, Kate Moran / NN/g, 2021-07-25. Sample size depends on the metric, its variability and the acceptable uncertainty. For an experiment, fix the minimum effect of interest and the calculation parameters. Do not declare one number universal for proportions, task times and A/B tests.

**RE-02 — [Demand Accuracy in Your AI Tools](https://www.nngroup.com/articles/baymard-ai-tool-accuracy/)**, Kate Moran / NN/g, 2026-01-30. Separate detecting a visual feature from concluding that it is appropriate. Check an AI recommendation against the screen, the context and the evidence. This is analysis and interviews, not a current comparative benchmark of all models.

**RE-06 — [Synthetic Users](https://www.nngroup.com/articles/synthetic-users/)**, Maria Rosala, Kate Moran / NN/g, 2024-06-21. Use AI personas to prepare questions and hypotheses. Do not present a simulation as observation of people or as confirmation of a product decision. The article evaluated the tools and scenarios of its time; do not carry its results over into a numerical assessment of 2026 models.

## The skill's working protocol

1. Write down the hypothesis and an alternative explanation. "The filter label makes it hard to choose a category" is not yet a confirmed problem.
2. Define the audience and its differences: experience, language, device, accessibility, task frequency. Do not call a generated persona a researched segment.
3. Set a plausible task without words that give away the correct control. Prepare the data, the initial state and the completion criterion.
4. Record unaided completion, critical errors, requests for help and difficulties. Analyze time in context: careful comparison is not necessarily a problem.
5. For quantitative measurement, define the event, the unit of analysis, the denominator, the observation window and the segments. Do not change the rules after seeing the result unless explicitly instructed.
6. Compare with the baseline and with guardrail metrics: accessibility, errors, cancellation, data loss, unwanted action. Do not optimize only clicks or session length.
7. List the checks actually performed, the limitations and the next step. An AI walkthrough is useful as a preliminary check but is not research with real participants.

## Limits of conclusions

| Material | What can be assessed | What additional data is needed |
|---|---|---|
| Screenshot | Visible hierarchy, text, density, likely risks | Keyboard behavior, accessibility tree, hidden states, actual hit area, timing, conversion |
| Code/DOM | Structure, handlers, programmatic relationships, styles | Execution, real data, integration with the browser/AT |
| Interactive prototype | Available transitions under simulated conditions | Production behavior and task success for the audience |
| Logs and analytics | Specific measurable events and paths | People's motives, unlogged actions, causality |
| Research | Observations within the sample and conditions | All segments, scenarios and future versions |

Do not present the number of heuristic findings as a percentage of UX quality. Do not call an unverified risk an established violation. Without access, formulate a specific check for a person or the next tool.
