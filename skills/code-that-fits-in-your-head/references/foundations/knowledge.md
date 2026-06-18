# Foundations Knowledge

Core concepts that justify every other practice in the book: code exists to sustain an organisation, programming is hard because of brain limits (not CPU limits), and software engineering is the art of writing code that fits in a human head.

## Overview

Software is a long-lived liability, not an asset. The binding constraint on a code base is the human brain — roughly seven items in short-term memory, two systems of thought (fast-but-wrong and slow-but-effortful), and a strong bias toward jumping to conclusions. Good software engineering organises code so humans can understand it at a sustainable pace, and extends that discipline to how the programmer spends their day.

## Key Concepts

### Sustainability

**Definition**: The ability to keep supporting an organisation through code changes — adding features, fixing bugs — just as effectively in six months or six years as today.

Software typically lives for years or decades and undergoes constant change. Without attention to internal quality, progress is fast initially but slows until even small changes require understanding large, hard-to-understand areas of code.

**Key points**:
- Sustainability is the problem software engineering should solve.
- Poor internal quality is measurable — but often only after it is too late.
- Checklists, treating warnings as errors, and heuristics pull in the right direction without guaranteeing perfection.

### Value vs. Sustainability

**Definition**: Value is what the code produces for its organisation; sustainability is the middle ground between ignoring value (tech for tech's sake) and a myopic focus on immediately measurable results.

Some valuable work has no measurable output — only measurable *absence* (e.g. security, internal architecture). A "worse is better" fallacy arises when teams treat code that doesn't produce immediate value as prohibited.

### Short-Term Memory Limit (Seven)

**Definition**: The human brain's working memory holds roughly 4–7 pieces of information at once; this book uses seven as the canonical token for that limit.

A computer tracks millions of items in RAM; a brain tracks seven. Reading code is essentially running the language in your mind — if there are too many variables, branches, or dependencies, you cannot keep track.

**Key points**:
- Humane code keeps active concepts under seven.
- Applies to dependencies per class, cyclomatic complexity, arguments per method, etc.
- The exact number is less important than the fact that it is *orders of magnitude* smaller than a computer's memory.

### Code Read More Than Written

**Definition**: You read code far more times than you write it — when fixing bugs, adding features, or refactoring.

When writing, you have all the context. When reading, that context is gone. This is why "more code faster" is a bad strategy: more code means more to read.

**Key points**:
- Optimise code for readability, not writing speed.
- Every minute invested in readability pays back tenfold.
- Automated code generation compounds the reading burden.

### System 1 and System 2 (Kahneman)

**Definition**: Two modes of thought. System 1 is fast, automatic, effortless, and prone to wrong conclusions. System 2 is slow, effortful, and deliberate.

System 1 is always running in the background, trying to make sense of code. It jumps to conclusions. What You See Is All There Is (WYSIATI) — information not visible at the current cursor is effectively invisible, even if System 2 "knows" about it.

**Key points**:
- Hidden state (globals, side effects) defeats System 1 because it is not activated.
- Place related code close together so all relevant dependencies are visible at once.
- The bat-and-ball puzzle ($1.10 total, bat costs $1.00 more than ball — ball is 5¢, not 10¢) shows System 1 error on trivial problems.

### Humane Code

**Definition**: Code organised so it fits the cognitive constraints of a human brain, not just the execution model of a computer.

> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." — Martin Fowler

**In practice**:
- Small, self-contained functions.
- Fewer than seven dependencies.
- Cyclomatic complexity at most seven.
- All context needed to understand a piece of code is visible at the same time.

### Personal Rhythm

**Definition**: A loose daily structure — time-boxed work, deliberate breaks, deliberate learning time, and fundamental tool fluency — that treats the programmer's attention as the scarcest resource.

Intellectual work is not physical work: you cannot measure productivity by hours. Long hours cause *negative* productivity because mistakes compound. Subconscious processing ("System 1 in the background") produces insights when you step away from the keyboard.

**Key points**:
- Time-box in 25-minute intervals with 5-minute breaks (not full Pomodoro).
- Make breaks real: leave the room, walk, exercise.
- Being in the zone is not a guarantee of useful output.
- Touch typing matters because it frees the eyes to watch the screen and use IDE feedback.

## Terminology

| Term | Definition |
|------|------------|
| Sustainability | Capacity of a code base to keep supporting its organisation over years |
| Humane code | Code organised to fit human cognitive limits |
| Seven | Shorthand for the brain's short-term memory limit |
| System 1 / System 2 | Kahneman's fast/automatic and slow/deliberate modes of thought |
| WYSIATI | "What You See Is All There Is" — System 1 only reasons about activated information |
| Flow / the zone | Mental state of immersion; productive-feeling but not always productive |
| Complexity | "Assembled from parts" (Hickey) — the antonym of simplicity |
| Time-boxing | Working in fixed intervals (e.g. 25 min) with mandatory breaks |

## Key Principles

| Principle | One-Line Summary |
|-----------|------------------|
| Code is a liability | The less you write, the less there is to maintain |
| Optimise for readability | You will read this code many more times than you wrote it |
| Fit in the head | Keep active concepts under seven |
| Make dependencies visible | System 1 ignores what isn't on screen |
| Value ≠ immediate measurable value | Security, architecture, and quality reveal themselves by their absence |
| Sustainability beats speed | Faster typing produces more to maintain, not more value |
| Breaks are work | Insights come away from the keyboard, not at it |
| Don't work long hours | Negative productivity compounds after fatigue sets in |

## How It Relates To

- **Decomposition**: The seven-item limit drives function size, class size, and dependency counts.
- **Encapsulation**: Hides detail so each layer fits in the head.
- **Code navigation**: Tight cohesion supports WYSIATI — related code close together.
- **Teamwork**: Checklists and shared practices are how we compensate for individual brain limits.

## Common Misconceptions

- **Myth**: Being in the zone means you are being productive.
  **Reality**: Flow feels productive but is not contemplative; hours of flow can produce code that cannot work.

- **Myth**: Productivity is proportional to hours worked.
  **Reality**: Intellectual work degrades with fatigue; long hours can be net-negative.

- **Myth**: Fast typing makes you a faster programmer.
  **Reality**: You spend more time reading than typing; readability dominates.

- **Myth**: Code that produces no measurable value is waste.
  **Reality**: Security, quality, and architecture only become measurable by their absence.
