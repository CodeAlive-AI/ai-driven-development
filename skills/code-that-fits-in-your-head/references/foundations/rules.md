# Foundations Rules

> **Source note:** This book-derived theme includes 2026 editorial reframing for agent-driven development. Agent-specific additions are not from Seemann.

Rules for keeping software understandable, maintainable, and resistant to accidental complexity.

## Core Rules

### 1. Write for the Next Reader and Changer

Code is read, reviewed, debugged, and extended far more often than it is authored.

- Prefer plain code over clever compression.
- Make intent, dependencies, invariants, and side effects discoverable.
- Optimise for future modification, not generation speed.
- Treat code that is easy to generate but difficult to own as a liability.

### 2. Keep Each Unit Conceptually Cohesive

Human working memory is limited, but no universal item count defines good design.

- Give each function, type, module, and service a coherent responsibility.
- Keep dependencies and interacting concepts few enough to name and explain.
- Split code when branches, state, effects, or responsibilities interfere with one another.
- Do not split cohesive logic merely to satisfy a superficial size metric.

### 3. Make Context Discoverable and Effects Explicit

A reader or agent should be able to find the information required to change a unit safely.

- Avoid ambient mutable state and hidden side effects.
- Prefer explicit inputs, outputs, dependencies, and ownership boundaries.
- Keep repository-local architecture, contracts, and verification commands current.
- Use progressive disclosure: provide a short map to authoritative details instead of duplicating every fact locally.

### 4. Treat Code as a Liability, Not an Asset

More code means more behavior to understand, verify, secure, and maintain.

- Delete dead, duplicated, speculative, and obsolete code.
- Reuse an existing coherent abstraction before adding another.
- Reject boilerplate and generated volume that do not improve the design.
- Prefer the smallest complete solution, not the smallest diff at the cost of architecture.

### 5. Optimize for Sustainability

Sustainable software remains affordable to change after years of maintenance.

- Preserve cohesion and explicit boundaries before local delivery pressure erodes them.
- Treat refactoring, security, architecture, and observability as lifecycle work, not optional polish.
- Use mechanical checks for stable objective constraints and human judgment for intent and architecture.
- Record debt deliberately with an owner and removal condition; do not let temporary compromises become invisible defaults.

### 6. Deliberate Before Accepting, Not Before Generating

Agents can produce large changes quickly. Artificially slowing generation is not the goal.

- Plan large work around stable architectural boundaries and explicit acceptance criteria.
- Verify meaningful checkpoints and preserve evidence of correctness.
- Pause or revise the plan when evidence contradicts assumptions.
- Do not confuse task size with complexity: a large systematic migration may be safer than a small tangled patch.

## Guidelines

- Prefer established libraries over reinventing solved infrastructure.
- Re-check conclusions that look obvious but depend on hidden assumptions.
- Prefer written, versioned rationale over transient conversation for important decisions.
- Keep terminology consistent across code, tests, documentation, and product language.

## Exceptions

- **Exploratory spike**: readability may be relaxed only when the spike is isolated and will be discarded or deliberately rewritten.
- **Fixed external contract**: awkward shapes may be unavoidable at a boundary; translate them into cleaner internal types.
- **Production emergency**: accept temporary debt only with explicit follow-up, owner, and verification of the narrow fix.

## Quick Reference

| Rule | Summary |
|---|---|
| Next reader and changer | Optimize for ownership, not authorship speed |
| Conceptual cohesion | Split conflicting responsibilities, not cohesive work |
| Discoverable context | Make dependencies, effects, and sources of truth findable |
| Code is liability | Delete duplication and speculative volume |
| Sustainability | Resist erosion and make debt explicit |
| Deliberate acceptance | Large work is fine when architecture and verification are sound |
