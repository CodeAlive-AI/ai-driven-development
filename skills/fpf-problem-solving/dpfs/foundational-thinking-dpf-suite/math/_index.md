# Mathematical Thinking DPF

**DocID:** `MATH` within **FPF Library**.

> A pattern language for constructing mathematical objects, operations and arguments, using their results, and developing the next useful question.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 24 October 2026
- **Status:** Eternal alpha: a growing repertoire of methods for mathematical work.
- **License:** © 2026 Anatoly Levenchuk. Original framework text: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Cited sources retain their own terms.
- **Publication:** [FPF Library repository](https://github.com/ailev/FPF)

Begin with the working question. If you have not yet identified its mathematical contribution, use Readme entry MP-FRAME. Use the Table of Contents to find a relevant pattern, then open its Problem frame, Solution, worked cases and checklist. Readme follows connected mathematical work; Architectural Reference explains the methods and when to revise a construction.

The reference code **MATH** names this DPF. Its numbers are stable pattern addresses; § shows position in this edition. References such as B.5.RA and C.29.1 name patterns in [FPF](../../../sections/03-first-principles-framework-readme/_index.md). Use those patterns when the cited question arises.

When a mathematical result changes a working method, FPF Core provides two further methods: [FPF B.1.5.CM](../../../sections/08-part-b---trans-disciplinary-reasoning-cluster/09-b-1-5-cm---construct-and-qualify-a-composite-method.md) helps resolve a proposed composition of methods; [FPF A.3.1.CC](../../../sections/05-part-a---kernel-architecture-cluster/25-a-3-1-cc---check-the-coherence-of-a-method-claim.md) helps locate an inconsistency between a method, its descriptions, the work performed and its supporting means.

Open the cited publications for those pattern bodies. When using another edition, revisit your conclusion if a cited operation or condition has changed.

To cite this edition: Anatoly Levenchuk, *Mathematical Thinking DPF*, [FPF Library repository](https://github.com/ailev/FPF). Include the version date shown above.

# Table of Contents

## Public units

| Unit | Title | Use |
| --- | --- | --- |
| Readme | [Mathematical Thinking - Readme](_index.md#mathematical-thinking---readme) | Follow connected mathematical work. |
| Architectural Reference | [Mathematical Thinking DPF Architectural Reference](_index.md#mathematical-thinking-dpf-architectural-reference) | Understand the connected methods, their rationale, sources and limits. |
| MATH.Reference:1 | [Problem frame - Construct mathematics for the question](01-math-reference-1---problem-frame---construct-mathematics-for.md) |  |
| MATH.Reference:2 | [Problem and forces - Make a usable construction](02-math-reference-2---problem-and-forces---make-a-usable-constr.md) |  |
| MATH.Reference:3 | [Solution - Connect constructions through what they supply](03-math-reference-3---solution---connect-constructions-through.md) |  |
| MATH.Reference:3.1 | [Form objects, operations and representations](03-math-reference-3---solution---connect-constructions-through.md#mathreference31---form-objects-operations-and-representations) |  |
| MATH.Reference:3.2 | [Obtain an argument and the object it supports](03-math-reference-3---solution---connect-constructions-through.md#mathreference32---obtain-an-argument-and-the-object-it-supports) |  |
| MATH.Reference:3.3 | [Change a construction and develop its theory](03-math-reference-3---solution---connect-constructions-through.md#mathreference33---change-a-construction-and-develop-its-theory) |  |
| MATH.Reference:3.4 | [Return a construction to further work](03-math-reference-3---solution---connect-constructions-through.md#mathreference34---return-a-construction-to-further-work) |  |
| MATH.Reference:3.5 | [Use this contribution within the wider repertoire](03-math-reference-3---solution---connect-constructions-through.md#mathreference35---use-this-contribution-within-the-wider-repertoire) |  |
| MATH.Reference:3.6 | [Constituent actions in ongoing work](03-math-reference-3---solution---connect-constructions-through.md#mathreference36---constituent-actions-in-ongoing-work) |  |
| MATH.Reference:4 | [Worked use - Choose a representation after the question changes](04-math-reference-4---worked-use---choose-a-representation-afte.md) |  |
| MATH.Reference:5 | [Worked use - Construct a choice after finding an obstruction](05-math-reference-5---worked-use---construct-a-choice-after-fin.md) |  |
| MATH.Reference:6 | [Checks and common failures - Preserve what the next construction needs](06-math-reference-6---checks-and-common-failures---preserve-wha.md) |  |
| MATH.Reference:7 | [Consequences, biases and limits](07-math-reference-7---consequences-biases-and-limits.md) |  |
| MATH.Reference:8 | [Architectural Rationale - Organize by reusable constructions](08-math-reference-8---architectural-rationale---organize-by-reu.md) |  |
| MATH.Reference:9 | [Source use and currentness](09-math-reference-9---source-use-and-currentness.md) |  |
| MATH.Reference:10 | [Relations to further reasoning and work](10-math-reference-10---relations-to-further-reasoning-and-work.md) |  |

## Part A - Choose and relate constructions

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [MATH.16 - Choose a Mathematical Construction from Its Required Maps (Universal Property)](12-math-16---choose-a-mathematical-construction-from-its-requir.md) | Stable | universal property; product; coproduct; pullback; function object; currying. What maps should a new object support, and how can that requirement select a construction? | MATH.2 for quotients; MATH.5 for generator extensions; MATH.7 for reversible representations; C.29 for interpretation in another subject. |
| 2 | [MATH.17 - Construct Mathematical Spaces of Operations and Operations on Them](13-math-17---construct-mathematical-spaces-of-operations-and-op.md) | Stable | operations as objects; admissible functions; closure; higher-order operation; transformation law. How can a rule be constructed, combined or changed while retaining the consequence its use needs? | MATH.16 for function objects; MATH.1/.2 for retained steps or identification; MATH.18 for interpretation between accounts; C.29 for a working-method application. |
| 3 | [MATH.1 - Build a Mathematical Structure of Composable Paths](14-math-1---build-a-mathematical-structure-of-composable-paths.md) | Stable | generators; paths; endpoints; identity; associativity. Which elementary steps can be composed? When do different sequences need to remain distinct? | MATH.2 when paths will be identified; C.29 when the construction represents another subject. |
| 4 | [MATH.2 - Treat Objects as the Same While Preserving Operations (Quotient)](15-math-2---treat-objects-as-the-same-while-preserving-operatio.md) | Stable | quotient; congruence; equivalence; partial operation; refinement. Can these objects be treated as the same without losing a later operation or result? | MATH.1 when paths first need construction; MATH.6 for a counterexample to the proposed identification. |
| 5 | [MATH.5 - Extend a Generator Assignment While Preserving Operations (Homomorphism)](16-math-5---extend-a-generator-assignment-while-preserving-oper.md) | Stable | generators; relations; homomorphism; free structure; extension. How can a choice on generators determine an operation-preserving map on everything they generate? | MATH.1 for paths; MATH.2 when an extension must descend to a quotient. |
| 6 | [MATH.7 - Transport a Mathematical Structure Through a Bijection](17-math-7---transport-a-mathematical-structure-through-a-biject.md) | Stable | bijection; transport; inverse map; isomorphism; domain of operation. How can a useful operation, law and answer be carried through a change of representation? | MATH.2 when identification is proposed instead of a bijection; C.29 for interpretation in another subject. |
| 7 | [MATH.18 - Compare Mathematical Accounts through Interpretations](18-math-18---compare-mathematical-accounts-through-interpretati.md) | Stable | interpretation; primitive operation; preservation; reflection; round trip; equivalence. Which constructions, equations and maps transfer between two mathematical descriptions, and what can be recovered? | MATH.5 for generated interpretations; MATH.7 for bijective transport; MATH.2 for quotients; MATH.17 for transformations of operations. |

## Part B - Construct and criticize arguments

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [MATH.19 - Construct a Proof through Intermediate Claims](19-math-19---construct-a-proof-through-intermediate-claims.md) | Stable | lemma; backward and forward reasoning; generalization; proof dependency. Which intermediate claim connects the available premises to the desired conclusion? | B.5.RA for recovery of a supplied argument; MATH.4 for induction; MATH.6 for a separating case; MATH.12 for obtaining an object from the proof. |
| 2 | [MATH.4 - Construct a Witness by Induction](20-math-4---construct-a-witness-by-induction.md) | Stable | induction; recursive witness; base and step; representation. How can a proof supply an object for every finite input? Does the construction respect equivalent representations? | MATH.2 when a recursive construction must respect identification; MATH.12 for extracting constructions from other proof rules. |
| 3 | [MATH.12 - Extract a Construction from a Proof](21-math-12---extract-a-construction-from-a-proof.md) | Stable | constructive proof; witness; function; pair; branch; finite search; computation. Which data-producing operation does a proof supply, and what is needed to execute it? | B.5.RA for an unfamiliar argument; MATH.4 for induction; C.29.2/.3 for formulation or execution questions. |
| 4 | [MATH.6 - Refute a Mathematical Claim with a Countermodel](22-math-6---refute-a-mathematical-claim-with-a-countermodel.md) | Stable | counterexample; countermodel; quantifiers; finite scope; encoding. What concrete structure refutes the claim? What does an unsuccessful bounded search leave unresolved? | B.5.RA if the claim's argument needs recovery; MATH.2 when the counterexample defeats an identification. |
| 5 | [MATH.20 - Bound a Mathematical Unknown by Comparable Constructions](23-math-20---bound-a-mathematical-unknown-by-comparable-constru.md) | Stable | bound; inequality; enclosure; relaxation; attainability; residual and error. Which comparison can answer the question before the whole unknown is obtained? | MATH.19 for an intermediate inequality; MATH.6 for a failed bound; MATH.21 for convergent approximation; FPF for choosing further work. |

## Part C - Change a construction and develop its theory

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [MATH.11 - Construct an Invariant from Transformation Rules](24-math-11---construct-an-invariant-from-transformation-rules.md) | Stable | invariant; transformation rule; preservation equation; coefficient; reachability. How can a preserved expression be constructed and used to obtain a formula or exclude a target? | MATH.2 for identification; MATH.7 for transport; C.29 for a consequence about the modeled subject. |
| 2 | [MATH.13 - Derive a Consequence from a Symmetry](25-math-13---derive-a-consequence-from-a-symmetry.md) | Stable | symmetry; uniqueness; fixed point; orbit; conservation; numerical update. What does a transformation preserve, and which conclusion actually follows from that symmetry? | MATH.8 for the full orbit construction; MATH.9 for compatible choice; MATH.10 for admissible variation. |
| 3 | [MATH.8 - Generate a Solution Family by Symmetry](26-math-8---generate-a-solution-family-by-symmetry.md) | Stable | group action; solution orbit; stabilizer; repetitions; representatives. Which solutions can be generated from one solution, and how much of the solution set does this cover? | MATH.13 for an unresolved symmetry consequence; MATH.9 when one compatible representative is required. |
| 4 | [MATH.9 - Determine Whether and How a Choice Rule Can Respect Symmetry](27-math-9---determine-whether-and-how-a-choice-rule-can-respect.md) | Stable | equivariant choice; stabilizer; symmetry obstruction; additional data. Can one allowed answer be chosen consistently with symmetry? What can replace an impossible choice? | MATH.8 for solution orbits; MATH.13 for an earlier consequence or uniqueness question. |
| 5 | [MATH.10 - Improve a Mathematical Candidate or Derive a Necessary Condition by Admissible Variation](28-math-10---improve-a-mathematical-candidate-or-derive-a-neces.md) | Stable | admissible variation; improving change; stationary point; boundary minimum; constraint; first variation. Which change is allowed, can it improve the candidate, and what condition follows? Does that condition establish an optimum? | B.5.RA if the variational argument needs recovery; C.29 when a mathematical variation represents a subject change. |
| 6 | [MATH.21 - Construct an Object through Convergent Approximations](29-math-21---construct-an-object-through-convergent-approximati.md) | Stable | limit; completeness; compatible approximation; uniform convergence; error control. How can finite approximations construct an object while retaining the next operation? | MATH.20 for bounds; MATH.19 for convergence and interchange arguments; MATH.2 for classes of representations; computational methods for effective obtaining. |
| 7 | [MATH.22 - Change Axioms and Trace Their Consequences](30-math-22---change-axioms-and-trace-their-consequences.md) | Stable | axiom change; theory; interpretation; model; independence; proof repair. Which constructions and consequences survive when assumptions change? | MATH.18 for interpretations; MATH.19 for replacement proofs; MATH.6 for countermodels; MATH.23 for a further conjecture. |
| 8 | [MATH.23 - Develop a Conjecture by Changing a Construction](31-math-23---develop-a-conjecture-by-changing-a-construction.md) | Stable | conjecture; construction variation; proof and refutation; generalization; next problem. How can a change or obstruction yield a precise useful claim and an attainable next operation? | MATH.19 for proof construction; MATH.6 for refutation; MATH.22 for theory change; B.5.QD/C.40.CD for continued inquiry. |

# Mathematical Thinking - Readme

## Practical entries

A mathematical result often becomes an input to further work: a construction supplies the objects for a proof, a failed implication changes the question, and a changed rule requires an argument that its useful properties survive. The patterns in this language help make and connect those contributions.

The two worked connections below start at different places. The first turns a working difficulty into a mathematical question and returns the answer to its subject. The second changes a rule so that independently obtained results can be combined, proves the new rule and revisits it when the requested answer changes. Enter with the results already available; a settled contribution need not be reconstructed.

Use the Table of Contents to find other questions and the actual pattern titles. Each body states its prerequisites, method, examples and limits. A construction can serve mathematics itself or describe another subject; FPF C.29 helps establish what its result says about that subject.

You can ask an assisting agent: “Explain this and comment on my proposal without FPF jargon; use the language of my work.”

### MP-FRAME - Find the mathematical contribution in an unfamiliar problem

- **Situation:** Something in the work is unexplained or fails, and you do not yet know whether another observation, a new model, a mathematical construction or a different computation is needed.
- **Question:** What must become distinguishable or possible for the next answer to be useful?
- **First useful result or blocker:** A mathematical task with a stated use. For example, a cart's travel log gives total distance, but that total cannot tell whether the cart returned to its start. Identify the position question first. With straight-line motion and known displacements, a sequence of signed displacements supplies an account that can answer it. MATH.1 constructs the sequences and their composition; MATH.5 derives the accumulated displacement from the elementary displacements. A sensor report must first be interpreted as the movement it measures.
- **Start with:** FPF B.5.FM. State the working question, identify the participants and relations that may change its answer, and build a small account that yields a consequence. If an unfamiliar theory supplies the account, B.5.TU helps construct its application. B.5.MPC connects the physical, mathematical and computational contributions when the difficulty lies between them. Their bodies are in the FPF publication linked above. If the problem is deciding what an object must let you form or recover, use MATH.16. If it is deciding which distinctions can be forgotten, use MATH.2. If an implication is doubtful, use MATH.6. The question determines the construction; an available formula may settle only part of it. C.29 supplies the interpretation through which a mathematical result answers the original question. C.29.2/.3 develop a needed procedure and its execution.
- **Stop or return:** After the question changes, test whether the summary still determines the answer. If two runs have the same final position but differ in a requested visit, recover the information that separates them. MATH.2 helps locate the failed identification; B.5.QD develops the next useful question. For a working method changed by the result, B.1.5.CM helps describe the proposed operations and their relations; A.3.1.CC checks the claims in that account and its description. The Architectural Reference's worked use follows these choices in detail.

### MP-COMBINE-RESULTS - Change a rule so that separately obtained results can be combined

- **Situation:** A rule works for one input, but splitting the work or combining its results changes the answer.
- **Question:** What must each contribution retain, how should contributions combine, and why will the result still answer the original question?
- **First useful result or blocker:** A composable summary with a stated use. For an arithmetic mean of finitely many real values, return each group's sum and count; add these pairs and divide the total sum by the total count.
- **Start with:** [MATH.23](31-math-23---develop-a-conjecture-by-changing-a-construction.md) to develop the question; [MATH.2](15-math-2---treat-objects-as-the-same-while-preserving-operatio.md) to choose compatible identification; [MATH.17](13-math-17---construct-mathematical-spaces-of-operations-and-op.md) to work on the combining operation; [MATH.19](19-math-19---construct-a-proof-through-intermediate-claims.md) for the argument.
- **Stop or return:** Use the proved rule within its assumptions. A new statistic, allowed transformation or arithmetic implementation can invalidate a retained-information or proof step; return to that step.

#### Worked connection for MP-COMBINE-RESULTS


**1. Recover the failure and intended result.** Averaging the means of [0] and [2,4] gives 1.5, while the mean of the combined list is 2. MATH.23 turns this difference into a question: which summary recovers the mean of every nonempty combined finite list, for every partition into nonempty groups? The result is a claim and its range of cases for the identification step.

**2. Decide what may be forgotten.** MATH.2 tests identification against the operations still needed. Equal means are insufficient: [0] and [0,0] both have mean 0, but adjoining [2] gives means 1 and 2/3. Instead identify lists with equal sum and count. Concatenation respects that identification because both components add. Empty lists can have summary (0,0); division is defined only after the combined count is positive.

**3. Make the rule itself available for work.** Combine (s,n) and (t,m) as (s+t,n+m). MATH.17 asks whether the operation stays within the chosen space and which laws the use needs. The pair summarizes an input; the binary operation is another mathematical object, which can be compared with a replacement. Associativity permits regrouping; commutativity permits reordering. These laws become premises needed by the proof.

**4. Connect the local calculation to all allowed combinations.** MATH.19 separates two claims: summarizing a concatenation equals combining its summaries, and extracting s/n at positive n returns the list's arithmetic mean. The first follows from addition of sums and lengths. Repeated combination follows by induction over the finite grouping, using [MATH.4](20-math-4---construct-a-witness-by-induction.md) if that induction needs construction. The argument thus covers every stated partition.

**5. Use the result with its conditions.** Contributors can now return pairs to combine. FPF C.29 connects the mathematics to actual records: which values belong to the population and whether any are duplicated remain subject questions. Real addition supplies the laws above; floating-point regrouping needs its numerical account when rounding can change the use.

**6. Develop the next question.** If the answer becomes a median, sum and count no longer suffice: [0,0,6] and [0,3,3] share both but have medians 0 and 3. Return to step 2 and use MATH.23 to construct the new question. A quantile method or a different summary can supply the next contribution.

---

## Files of this publication

Generated by the skill's splitter: one file per section, in reading order.


### Mathematical Thinking DPF Architectural Reference

- [MATH.Reference:1 - Problem frame - Construct mathematics for the question](01-math-reference-1---problem-frame---construct-mathematics-for.md) (12 lines)
- [MATH.Reference:2 - Problem and forces - Make a usable construction](02-math-reference-2---problem-and-forces---make-a-usable-constr.md) (17 lines)
- [MATH.Reference:3 - Solution - Connect constructions through what they supply](03-math-reference-3---solution---connect-constructions-through.md) (66 lines)
- [MATH.Reference:4 - Worked use - Choose a representation after the question changes](04-math-reference-4---worked-use---choose-a-representation-afte.md) (18 lines)
- [MATH.Reference:5 - Worked use - Construct a choice after finding an obstruction](05-math-reference-5---worked-use---construct-a-choice-after-fin.md) (14 lines)
- [MATH.Reference:6 - Checks and common failures - Preserve what the next construction needs](06-math-reference-6---checks-and-common-failures---preserve-wha.md) (17 lines)
- [MATH.Reference:7 - Consequences, biases and limits](07-math-reference-7---consequences-biases-and-limits.md) (12 lines)
- [MATH.Reference:8 - Architectural Rationale - Organize by reusable constructions](08-math-reference-8---architectural-rationale---organize-by-reu.md) (18 lines)
- [MATH.Reference:9 - Source use and currentness](09-math-reference-9---source-use-and-currentness.md) (25 lines)
- [MATH.Reference:10 - Relations to further reasoning and work](10-math-reference-10---relations-to-further-reasoning-and-work.md) (10 lines)
- [MATH.Reference:End](11-math-reference-end.md) (2 lines)

### Part A - Choose and relate constructions

- [MATH.16 - Choose a Mathematical Construction from Its Required Maps (Universal Property)](12-math-16---choose-a-mathematical-construction-from-its-requir.md) (252 lines)
- [MATH.17 - Construct Mathematical Spaces of Operations and Operations on Them](13-math-17---construct-mathematical-spaces-of-operations-and-op.md) (203 lines)
- [MATH.1 - Build a Mathematical Structure of Composable Paths](14-math-1---build-a-mathematical-structure-of-composable-paths.md) (183 lines)
- [MATH.2 - Treat Objects as the Same While Preserving Operations (Quotient)](15-math-2---treat-objects-as-the-same-while-preserving-operatio.md) (203 lines)
- [MATH.5 - Extend a Generator Assignment While Preserving Operations (Homomorphism)](16-math-5---extend-a-generator-assignment-while-preserving-oper.md) (232 lines)
- [MATH.7 - Transport a Mathematical Structure Through a Bijection](17-math-7---transport-a-mathematical-structure-through-a-biject.md) (210 lines)
- [MATH.18 - Compare Mathematical Accounts through Interpretations](18-math-18---compare-mathematical-accounts-through-interpretati.md) (211 lines)

### Part B - Construct and criticize arguments

- [MATH.19 - Construct a Proof through Intermediate Claims](19-math-19---construct-a-proof-through-intermediate-claims.md) (241 lines)
- [MATH.4 - Construct a Witness by Induction](20-math-4---construct-a-witness-by-induction.md) (213 lines)
- [MATH.12 - Extract a Construction from a Proof](21-math-12---extract-a-construction-from-a-proof.md) (243 lines)
- [MATH.6 - Refute a Mathematical Claim with a Countermodel](22-math-6---refute-a-mathematical-claim-with-a-countermodel.md) (195 lines)
- [MATH.20 - Bound a Mathematical Unknown by Comparable Constructions](23-math-20---bound-a-mathematical-unknown-by-comparable-constru.md) (238 lines)

### Part C - Change a construction and develop its theory

- [MATH.11 - Construct an Invariant from Transformation Rules](24-math-11---construct-an-invariant-from-transformation-rules.md) (239 lines)
- [MATH.13 - Derive a Consequence from a Symmetry](25-math-13---derive-a-consequence-from-a-symmetry.md) (211 lines)
- [MATH.8 - Generate a Solution Family by Symmetry](26-math-8---generate-a-solution-family-by-symmetry.md) (205 lines)
- [MATH.9 - Determine Whether and How a Choice Rule Can Respect Symmetry](27-math-9---determine-whether-and-how-a-choice-rule-can-respect.md) (254 lines)
- [MATH.10 - Improve a Mathematical Candidate or Derive a Necessary Condition by Admissible Variation](28-math-10---improve-a-mathematical-candidate-or-derive-a-neces.md) (224 lines)
- [MATH.21 - Construct an Object through Convergent Approximations](29-math-21---construct-an-object-through-convergent-approximati.md) (205 lines)
- [MATH.22 - Change Axioms and Trace Their Consequences](30-math-22---change-axioms-and-trace-their-consequences.md) (208 lines)
- [MATH.23 - Develop a Conjecture by Changing a Construction](31-math-23---develop-a-conjecture-by-changing-a-construction.md) (240 lines)
