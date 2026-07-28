# Foundations Knowledge

> **Source note:** This book-derived theme includes 2026 editorial reframing for agent-driven development. Agent-specific additions are not from Seemann.

Why understandable code, explicit architecture, and technical-debt control remain essential when agents write much of the implementation.

## Sustainability

Sustainability is the ability to keep supporting an organisation through code changes as effectively in six months or six years as today. Software becomes expensive when each change requires reconstructing hidden context, crossing unstable boundaries, or working around accumulated compromises.

The central constraint is no longer typing capacity. Agentic development makes implementation abundant while human ownership, architectural judgment, verification, and operational responsibility remain scarce.

## Code as Liability

Code is useful only through the behavior it provides. Every additional abstraction, branch, dependency, and configuration path creates something that must be understood, tested, secured, upgraded, and eventually removed.

Generated volume therefore is not an asset by itself. The desirable output is a coherent capability with the least accidental machinery and a clear path for future change.

## Human Comprehension Still Matters

Humans have limited working memory and rely on incomplete mental models. The book uses seven as a memorable symbol for this constraint, not as a universal scientific limit for every dependency, variable, or branch.

Agents have different limits: context can be externalised through files and tools, but long context does not guarantee correct architecture or lifecycle stewardship. Both humans and agents benefit from cohesion, explicit boundaries, good names, executable contracts, and progressive disclosure.

## Complexity and Big Ball of Mud

Accidental complexity is structure that the problem does not require. It accumulates through:

- responsibilities that change for different reasons living together;
- implicit dependencies and side effects;
- duplicated logic and competing abstractions;
- cycles between modules or layers;
- temporary migrations, flags, and compatibility paths that never disappear;
- local fixes that ignore system-wide architecture.

A Big Ball of Mud is the system-level outcome: boundaries stop constraining change, so every feature can touch everything. Small methods do not prevent it. The defence combines local decomposition with module boundaries, dependency direction, verification, and active deletion of obsolete paths.

## Technical Debt

Technical debt is a deliberate or accidental choice that increases future change cost. Not all debt is forbidden, but invisible debt compounds.

A responsible compromise records:

- what was traded away;
- why the compromise is acceptable now;
- what risk it creates;
- who owns it;
- the condition or date for repayment.

Agents must not create speculative abstractions, TODOs, disabled checks, or permanent compatibility branches merely because they are cheap to generate.

## Large Tasks

Task size is not a maintainability metric. Agents can complete migrations and implementations spanning tens of thousands of lines when the work has:

- a coherent target architecture;
- explicit boundaries and dependency direction;
- clear acceptance and non-regression criteria;
- trustworthy automated verification;
- observable checkpoints and rollback or recovery paths.

The smell is unstructured scope: unclear ownership, mixed concerns, unverifiable behavior, or changes whose architectural effect cannot be explained.

## Key Principles

| Principle | Meaning |
|---|---|
| Code is a liability | Maintain only machinery that earns its lifecycle cost |
| Optimize for change | Prefer designs that keep future modifications local |
| Cohesion over arbitrary size | Keep related behavior together and conflicting responsibilities apart |
| Explicit boundaries | Make dependencies, effects, and ownership visible |
| Verification is design | Types, tests, schemas, and architecture checks constrain change |
| Debt must be visible | Temporary compromises need an owner and exit condition |
| Large is not automatically complex | Architecture and verification matter more than line count |

## How It Relates To

- **Decomposition** controls complexity inside methods, types, modules, and dependency graphs.
- **Encapsulation** protects invariants so callers need less defensive knowledge.
- **API design** makes intended use and side effects explicit.
- **Evolution** prevents migrations, flags, and compatibility layers from becoming permanent mud.
- **Agent-native guidance** protects verification integrity and human ownership when generation is cheap.
