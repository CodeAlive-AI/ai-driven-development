# Sources

Read when the authority behind a rule is needed, or to go deeper on one topic. The rules of this
skill are a synthesis: not every instruction belongs to a single author.

## Contents

- [Foundation: Khorikov](#foundation-khorikov)
- [Test design and other schools](#test-design-and-other-schools)
- [Test analysis and case design](#test-analysis-and-case-design)
- [Real boundaries and strength of checks](#real-boundaries-and-strength-of-checks)
- [UI, reliability and exploratory QA](#ui-reliability-and-exploratory-qa)
- [AI-assisted development](#ai-assisted-development)

## Foundation: Khorikov

- Vladimir Khorikov, [Unit Testing: Principles, Practices, and Patterns](https://www.manning.com/books/unit-testing), Manning, 2020. Goal of testing, cost of test code, limits of coverage, the four criteria of a good test.
- [How to Assert Database State](https://enterprisecraftsmanship.com/posts/how-to-assert-database-state/). Which state to observe.
- [When to Mock](https://enterprisecraftsmanship.com/posts/when-to-mock/). Doubles, outgoing effects, managed dependencies.
- [Should you always mock unmanaged dependencies?](https://khorikov.org/posts/2021-12-06-unmanaged-dependencies-docker/). Real unmanaged dependencies are allowed when justified.
- [Unit Testing Dependencies: The Complete Guide](https://enterprisecraftsmanship.com/posts/unit-testing-dependencies/). Axes for classifying dependencies.
- [Pragmatic integration testing](https://enterprisecraftsmanship.com/posts/pragmatic-integration-testing/). Checking orchestration with real dependencies.
- [Structural Inspection](https://enterprisecraftsmanship.com/posts/structural-inspection/). Risks of pinning internal structure.

## Test design and other schools

- Martin Fowler, [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html). Kinds of doubles; classical and mockist styles.
- Martin Fowler, [Test Pyramid](https://martinfowler.com/bliki/TestPyramid.html). Economics of levels, with the stated exception for cheap and reliable broad tests.
- Ham Vocke, [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html). Boundaries, contracts, avoiding duplication across levels.
- Kent Beck, [Canon TDD](https://newsletter.kentbeck.com/p/canon-tdd). The small test and implementation loop; copying the actual result into expected destroys the check.
- Kent Beck, [Test Desiderata](https://medium.com/@kentbeck_7670/test-desiderata-94150638a4b3). Competing properties of tests and deliberate trade-offs.
- Software Engineering at Google, [Testing Overview](https://abseil.io/resources/swe-book/html/ch11.html) and [Unit Testing](https://abseil.io/resources/swe-book/html/ch12.html). Size and scope of a test; behaviour and clarity over removing repetition.
- Kent C. Dodds, [Testing Implementation Details](https://kentcdodds.com/blog/testing-implementation-details) and [Write tests. Not too many. Mostly integration](https://kentcdodds.com/blog/write-tests). Testing through the consumer's interface; coverage targets are not a norm.
- Sandi Metz, [Magic Tricks of Testing](https://speakerdeck.com/skmetz/magic-tricks-of-testing-railsconf). Messages of an object; mind the scale of the boundary.
- Michael Feathers, [Characterization Testing](https://michaelfeathers.silvrback.com/characterization-testing). Pinning existing behaviour in legacy code.
- Steve Freeman and Nat Pryce, [Growing Object-Oriented Software, Guided by Tests](https://growing-object-oriented-software.com/). The mock-object design tradition.
- Gerard Meszaros, [xUnit Test Patterns](https://www.informit.com/store/xunit-test-patterns-refactoring-test-code-9780131495050). Catalogue of test smells, fixtures, assertions and doubles, for diagnosing a found problem.

## Test analysis and case design

- ISTQB, [Certified Tester Foundation Level Syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf). Test analysis versus test design; definitions of the techniques and their coverage.
- James Bach, [Heuristic Test Strategy Model](https://www.satisfice.com/download/heuristic-test-strategy-model). Looking at a product through context, elements, quality criteria and techniques.
- Gojko Adzic, Specification by Example, Manning, 2011. From general wording to concrete examples of behaviour.
- Mark Utting and Bruno Legeard, Practical Model-Based Testing, Morgan Kaufmann, 2007. Building models and deriving test sets from them.
- NIST, [SP 800-142 Practical Combinatorial Testing](https://csrc.nist.gov/pubs/sp/800/142/final). Factors, interactions, constraints; limits of pairwise.
- NIST, [Ordered t-way Combinations for Testing State-based Systems](https://www.nist.gov/publications/ordered-t-way-combinations-testing-state-based-systems). Why the order of inputs needs its own design.

## Real boundaries and strength of checks

- Microsoft, [Choosing a testing strategy (EF Core)](https://learn.microsoft.com/en-us/ef/core/testing/choosing-a-testing-strategy). Limits of fake databases and differences between engines.
- Pact, [Contract Tests vs Functional Tests](https://docs.pact.io/consumer/contract_tests_not_functional_tests). Message compatibility does not confirm side effects.
- Hypothesis, [Introduction](https://hypothesis.readthedocs.io/en/latest/tutorial/introduction.html). Properties, generators, shrunk counterexamples.
- Koen Claessen and John Hughes, [QuickCheck](https://www.cs.tufts.edu/comp/150FP/archive/john-hughes/quick.pdf), ICFP 2000. Properties and the limits of input distribution.
- Petrović, Fraser, Ivanković and Just, [Practical Mutation Testing at Scale](https://research.google/pubs/practical-mutation-testing-at-scale-a-view-from-google/), 2021. Mutating changed code and filtering unhelpful mutants.
- OWASP, [Testing for Bypassing Authorization Schema](https://wstg.owasp.org/v4.2/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema/). Horizontal and vertical access checks.

## UI, reliability and exploratory QA

- Playwright: [Best Practices](https://playwright.dev/docs/best-practices), [Auto-waiting](https://playwright.dev/docs/actionability), [Assertions](https://playwright.dev/docs/test-assertions), [Retries](https://playwright.dev/docs/test-retries), [Emulation](https://playwright.dev/docs/emulation).
- John Micco, [Flaky Tests at Google and How We Mitigate Them](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html). Limits of retries and quarantine.
- Martin Fowler, [Eradicating Non-Determinism in Tests](https://martinfowler.com/articles/nonDeterminism.html). Causes of instability and how to remove them.
- Elisabeth Hendrickson, [Explore It!, charters excerpt](https://media.pragprog.com/titles/ehxta/charters.pdf). Directing exploration without scripting it.
- James Bach, [Exploratory Testing](https://www.satisfice.com/exploratory-testing). Exploration as learning.
- Michael Bolton, [Oracles Are About Problems, Not Correctness](https://developsense.com/blog/2015/03/oracles-are-about-problems-not-correctness). Limits of test oracles.
- Android: [Test your app's activities](https://developer.android.com/guide/components/activities/testing), [Testing strategies](https://developer.android.com/training/testing/fundamentals/strategies), [Run apps on a hardware device](https://developer.android.com/studio/run/device).
- Apple: [Running your app on simulated or physical devices](https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices), [Testing a release build](https://developer.apple.com/documentation/xcode/testing-a-release-build), [Performing accessibility audits for your app](https://developer.apple.com/documentation/accessibility/performing-accessibility-audits-for-your-app).
- W3C, [WCAG-EM 2.0](https://www.w3.org/TR/2026/NOTE-wcag-em-2-20260723/). Representative samples, complete processes, revising the sample by findings; the method itself concerns accessibility.

## AI-assisted development

These are case studies, small experiments and preprints, collected in a research pass in
November 2026. They motivate a rule. They do not set a universal number.

- Xiong, Guo and Chen, [The Program Testing Ability of Large Language Models for Code](https://aclanthology.org/2024.emnlp-industry.3/), EMNLP Industry 2024. Quality of generated tests depends on the code shown.
- Konstantinou, Tambon and Papadakis, [On the risk of coding before testing](https://arxiv.org/html/2607.05139v1), preprint. Tests generated after a buggy implementation detect fewer defects than tests generated from the task.
- Zhao, Zhou and Cohen, [Evaluating and Mitigating the Misguidance Effect of Buggy Code in LLM-Generated Unit Tests](https://arxiv.org/abs/2607.22883). Wrong code steers the model to wrong assertions.
- Zhao, Zhou and Cohen, [Do Coverage and Mutation Scores of LLM-Generated Test Suites Correlate With Their Effectiveness?](https://arxiv.org/pdf/2607.22880). The usefulness of both metrics depends on the task.
- Charoosaei, Richter and Papadakis, [On the Risks of using LLM-Generated Tests for Regression Testing](https://arxiv.org/html/2610.11835v1), preprint. Generated tests can pin a defect as required behaviour.
- Milanese and co-authors, [Testing with Coding Agents](https://arxiv.org/abs/2610.35297), preprint. Agent-supported changes add tests more often and maintain them less often.
- Birgitta Böckeler, [TDD inside the agent loop](https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html). Test-first does not exclude self-confirming assertions.
- Matteo Vaccari, [Tests as data](https://martinfowler.com/articles/tests-as-data.html). A readable acceptance contract separated from the implementation and the runner.
- Naresh Jain, [Are Harnesses Worth the Cost?](https://martinfowler.com/articles/are-harnesses-worth-the-cost.html). The value of extra verification loops depends on the model and the task.
- OpenAI, [Separating signal from noise in coding evaluations](https://openai.com/index/separating-signal-from-noise-coding-evaluations/). Independent tests can also be incomplete, too strict or contradict the task.
- Jeff An, [Your coding agent shouldn't grade its own homework](https://stackoverflow.blog/2026/11/13/your-coding-agent-shouldn-t-grade-its-own-homework). Useless generated tests and independent checking of the running product; one vendor's experience.
- Swaminathan Sivasubramanian, [AWS Emulator and the engineer's job when agents write the code](https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineers-job-when-agents-write-the-code.html). Emulator behaviour verified against scenarios confirmed on the real service.
- Osmani, Lunt and Wang, [How the Claude Code team does code review](https://claude.dev/blog/solving-code-review-at-anthropic/). Evaluating the reviewer and limiting repeated review rounds.
- Sachin Malhotra, [Agentic coding is straining CI](https://claude.com/resources/articles/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic). Freshness of test selection data is part of the reliability of a check.
- Delba de Oliveira, [Building verification loops in Claude Code with skills](https://claude.com/resources/articles/building-verification-loops-in-claude-code-with-skills). Checks are triggered by applicability conditions.
- Timo Reimann, [How Cloudflare enforces engineering standards using AI](https://blog.cloudflare.com/engineering-standards-enforcement/). Mechanically checkable rules move into fast linters.
- Lagar-Cavilla, Voutsina and Ranganathan, [Using agentic AI to secure infrastructure code](https://cloud.google.com/blog/topics/systems/using-ai-agents-to-secure-google-infrastructure). Finding a problem is separated from structurally confirming it.
- Prithvi Rajasekaran, [Harness design for long-running application development](https://www.anthropic.com/research/harness-design-long-running-apps). An evaluator working with UI, API and data state needs calibration.
- Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents). Final state, repeated trials and limits of graders, for products with real LLM features.
