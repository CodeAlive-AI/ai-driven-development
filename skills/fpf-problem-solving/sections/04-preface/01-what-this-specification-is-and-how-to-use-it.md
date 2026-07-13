## What This Specification Is And How To Use It

This document is the Core Conceptual Specification of the First Principles Framework (FPF). It defines a standards-style pattern language for explicit, reviewable, improvable conceptual work in engineering, research, management, governance, and mixed human and AI projects.

The reader should not need FPF vocabulary before this Preface becomes useful. Here an FPF term should first name an ordinary engineering distinction, then point to the pattern that gives the stricter form.

FPF is not a domain encyclopedia and not a project-management method. It is a framework for making hard project reasoning coherent when many kinds of project entities are easy to mix: systems, bodies of knowledge and models, architecture, descriptions, publications, concern-specific views, roles, methods, plans, performed work, evidence, decisions, options, commitments, and improvement criteria.

FPF starts from holons: project entities that can be treated as wholes and as parts. A holon can be a physical system, software system, organization-as-system, publication system, body of knowledge or model, research program, AI-agent arrangement, work occurrence, discipline, or another entity admitted by a pattern under part-whole treatment. `U.Method` is an admitted non-agentive holon kind: methods can be assembled from method parts into whole methods with whole-level preconditions, effects, constraints, and interfaces, and a whole method can become a part of a larger method. This does not make a method an actor, description, plan, or dated work occurrence. Systems can enact methods while holding roles; `U.Role` uses its own role ontology and is not admitted as a holon merely from role wording. Descriptions of methods or roles may be epistemes, but the description does not acquire the described value's kind.

FPF is written as a pattern language. A pattern is not a tutorial, blog post, checklist bureaucracy, or local process script. It is a reusable action-guidance form. A mature FPF pattern lets a working practitioner recover:

- the working situation where the pattern is useful;
- the project entity under concern, which FPF calls the EntityOfConcern, and the relation, claim, or work object being handled;
- what goes wrong when the distinction is missed;
- the forces that make the problem hard;
- the solution and first useful result;
- the consequences and related patterns;
- the checks that keep the result reviewable.

The standard pattern form is governed by `E.8`. Review and refresh discipline is governed by `E.19`. Pattern-quality evaluation is governed by `E.21`. Decision-rationale records, or DRRs, are short records explaining why one bounded FPF content decision changed; they are governed by `E.9` and its specializations. Those patterns matter because the FPF corpus itself evolves by the same discipline it asks other projects to use: explicit decisions, visible losses, recoverable meanings, and repeated improvement.

The FPF `readme` section presents fifteen semantic practical-use cards. They are not numbered entrances or one route through the framework. Each card starts from a recognizable working situation and a current practical question, points to one or more direct patterns under explicit conditions, names the kind of first useful result, and says when to stop, return, or inspect a stronger neighboring pattern.

When several cards seem plausible, compare them by the situation they recognize, the difference between their first results, and their stop or return conditions. That comparison may remain in the conversation. Before selecting a pattern, inspect its Problem frame, Problem, Forces, Solution, Consequences, and ordinary non-use boundary. Once one direct pattern is current, `E.11.PUA` governs applying its Solution to the first exact result and its receiving use. `E.11.PUR` governs applicability, recommendation, coordination, or ordering when those relations are current.

Ordinary bounded use does not begin by filling a shortlist, candidate form, five fit findings, or recommendation record. Those epistemes become useful only when a named receiving use relies on addressable comparison history, transfer between people or agents, automation, audit, durable reuse, delayed feedback, expensive feedback, or costly reversal. Even then, materialize only the candidate, fit, recommendation, closure, or provenance records that the receiving use needs. The semantic schemas are reference models, not user-interface forms or serialization instructions.

The first useful result is governed by the selected direct pattern. It may be a changed physical or clinical state, a capability, an episteme, a relation, dated `U.Work`, or another exact subject-governed value. A note, measurement, dashboard, or card is the result only when producing that episteme was the intended result. `Working product` is not a durable FPF term because it does not identify one governed value across these cases.

Keep three coupled flows distinct. Pattern-selection work may produce a fit finding, recommendation, or selected candidate. Applying the selected pattern produces its own directly governed result. That result may later become an input, tool, context, or constraint for downstream subject work without becoming the result of that later flow. Across these flows, an acting `U.System` under a `U.RoleAssignment` may select, construct, or refine a `U.Method`, plan dated work when preparation is current, and perform `U.Work` that affects the real EntityOfConcern. Public and project epistemes can guide that line without becoming the acting system, method, plan, work, or subject result. When a receiving use relies on durable cross-flow provenance, E.18 keeps the flow position, `PathSliceId`, and `DesignRunTag` recoverable. Otherwise that apparatus stays absent. A plan or selection episteme does not become machining, treatment, organizational change, learning, or another downstream subject result.

FPF can repeat this use as the project changes: ask the current question, compare when needed, inspect a direct pattern, apply its Solution, obtain the first useful result, and return when a stronger claim or unresolved relation becomes current. A pattern may give this use a local `mantra`: a short repeatable formulation that keeps its Solution in attention. For example, A.6.P's local mantra recalls the order of relation repair without creating a new method or unfolding structure. When a local mantra instead presents admissible conditional continuations through a wider constraint-governed unfolding structure, A.22.CGUS can admit it as a `DemonstrativeUnfoldingSlice@Context`; in that narrower case `demonstrative walkthrough` names the public episteme and `mantra move` names one conditional `DemonstratedPatternUseRow@Context`. Repetition alone creates no method order, work order, authority, plan, or performed work.

This Preface explains why these practical uses belong to one framework. The Table of Contents supports search when the reader already knows the pattern family. The pattern body governs the actual project claim and carries the exact Solution, boundaries, and checks. README and ToC references point to those direct patterns and published term rows; they do not become alternate schema or finding stores.

This Preface is also a reader-facing rendering of FPF's first-principles architecture. It is written for people who need the whole-framework picture before entering exact patterns. It foregrounds holons, descriptions, architecture, evidence, publication, choice, improvement, source-publication and source-use currentness, and domain or local framework growth; it deliberately coarsens, omits, or defers individual pattern detail, source publications, source-use history, and many relation records. When a Preface claim becomes load-bearing, return to the governing pattern body.

Use the `readme` when a current project question needs a practical-use card and a direct pattern. Use this Preface when you need the whole-FPF picture. Use the Table of Contents when you already know the pattern family or need a search-oriented overview. Use the pattern body for the exact Solution and the claim it governs.

The large areas of the specification can be read as one conceptual architecture. You do not need every name in this list yet; it is a map for later lookup:

- Part A gives the kernel: holons, contexts, roles, capabilities, methods, work, time, scope, signatures, architecture, characteristics, measurement, comparison, and foundations for choosing from candidate sets.
- Part B gives transdisciplinary reasoning, emergence, evidence, assurance, trust, canonical reasoning, creativity, problem-side records and cues, and bridge discipline.
- Part C gives major extension patterns: characterization, measurement, mathematical modeling, architecture, temporality, causality, option portfolios, quality, problem shaping, and precision restoration in specialized domains.
- Part D keeps ethics, conflict, and multi-scale value questions visible where they are live.
- Part E gives the FPF constitution: pillars, guard rails, pattern form, lexical discipline, description and publication discipline, transformation-flow structures for carrying results through work, admission, review, and design-rationale discipline.
- Part F gives unification and naming: local meaning units, concept sets, bridges, term sheets, local-first naming, and technical prose repair.
- Part G gives state-of-the-art work, option portfolios, option selection, benchmarks, shipping, evidence, bridges, dashboards, and refresh disciplines for reusable domain work.
- Later publication units carry glossaries, expanded cases, annexes, or other supporting units when the compact pattern body is not enough.

That orientation list is only for lookup. The exact rules remain in the pattern bodies.

