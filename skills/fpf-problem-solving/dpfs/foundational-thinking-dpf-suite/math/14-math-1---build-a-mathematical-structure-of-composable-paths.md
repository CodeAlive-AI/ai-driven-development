## MATH.1 - Build a Mathematical Structure of Composable Paths

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### MATH.1:1 - Problem frame

Use this pattern when you know elementary steps and their permitted connections, but still need mathematical objects for their finite combinations. Typical questions are: which steps form a permitted sequence, how can two sequences be joined, and which distinctions must remain available for a later operation?

The construction below makes paths from generating arrows. An arrow has a starting object and an ending object; these can be states, types or mathematical objects. A path is a finite ordered list of arrows whose adjacent endpoints agree. The resulting structure can describe formal words as well as possible routes through a process. Its mathematical laws come from the construction.

Start by writing two steps you want to join and their endpoints. If the first ends where the second starts, their ordered pair is already a useful first path. If the written endpoint hides a condition that changes whether the second step is available, refine the endpoint before joining them.

You need elementary sets, ordered lists and equality. If an existing structure already supplies the combinations and distinctions your question needs, use its operations directly. This pattern is useful when constructing or changing those operations is itself the difficulty.

### MATH.1:2 - Problem

A list of elementary steps leaves the composite objects and their operations undecided. Joining names that merely look compatible can produce a combination that the generating rules do not permit. Collapsing two paths to the same endpoint can also erase their different steps, costs or available continuations.

The mathematical task is to construct the combinations, define when composition is possible, and establish the laws that follow. The result should let another person or computational agent reproduce a path and reason about a longer combination from its parts.

### MATH.1:3 - Forces

| Force | Tension |
| --- | --- |
| Finite description and unbounded reuse | A few generators can produce arbitrarily long paths; listing all paths is usually impossible. |
| Keeping distinctions and economical reasoning | Remembering the generators preserves information, while a later question may need only a quotient or a numerical value. |
| Local compatibility and later use | An endpoint sufficient for today's composition may hide a condition needed by a changed continuation. |
| Composition and interpretation | Concatenation has laws by construction; a physical or computational interpretation has further conditions of its own. |

### MATH.1:4 - Solution

**Local mantra:** name the endpoints; form paths; join matching paths; use the composition laws; retain the distinction needed by the next operation.

#### MATH.1:4.1 - Choose objects and generating arrows

Write the objects at which the elementary steps start and end. For each generator `a`, give a source `s(a)` and a target `t(a)`. Several generators may have the same source and target.

Include conditions that determine the availability of the selected continuations. A location may be enough for one problem; another may require a pair such as `(location, permission)`. Use a failed attempted continuation to find the needed distinction. There is no requirement to anticipate every possible future operation.

The generating arrows and endpoints form a directed graph in the mathematical sense. A drawing can display it, but the vertices, arrows and endpoint functions define the structure. A physical network or an organization's work may be interpreted through this graph; that application supplies its own claims about what the arrows can represent.

#### MATH.1:4.2 - Form finite paths

A path of length `n>0` is a list `[a1,…,an]` with `t(ai)=s(a(i+1))` for every adjacent pair. Its source is `s(a1)` and its target is `t(an)`.

At each object `x`, add an empty path `id_x`. It starts and ends at `x` and contains no generator. Keeping its object matters: the empty path at one object cannot serve as the identity at another.

Initially, two nonempty paths are equal when their lists contain the same generators in the same order. The empty paths are equal only at the same object. This choice retains the sequence used to construct the path. A later identification can deliberately forget part of it, using MATH.2.

Construct only the paths needed for the immediate question, or describe a family by its formation rule. Cycles make infinitely many paths possible, but each path remains finite.

#### MATH.1:4.3 - Define composition by concatenation

For paths `p:x→y` and `q:y→z`, write `p;q` for the path obtained by putting the list of `q` after the list of `p`. Here the semicolon is read in execution order: first `p`, then `q`.

Composition is defined when the full intermediate object agrees. Its source is `x` and its target is `z`. If the endpoints disagree, repair the proposed sequence, supply a connecting arrow that is actually permitted, or return the failed connection.

Concatenation gives two laws:

- `id_x;p=p=p;id_y` for `p:x→y`, because an empty list adds no generator.
- `(p;q);r=p;(q;r)` for three consecutively composable paths, because both sides contain the same three lists in the same order.

These arguments establish identity and associativity for this construction. They can be reused while the definitions stay unchanged. They leave the order of the generators intact: `p;q` and `q;p` can differ or one can be undefined. A structure with objects, arrows and these laws is a category; the path construction gives the free category on the generating graph.

#### MATH.1:4.4 - Use the path at the needed level

Return the path that answers the immediate composition question, or the formation and composition rules when the receiving work needs a reusable family.

If each generator has a supplied additive cost, obtain a path's cost by adding the costs of its generators; the empty path has cost zero. Keep the path as well when the receiver needs to execute it or inspect why it is available. Two paths with the same cost can contain different generators.

If a representation hides an intermediate object, test the attempted composition that made the distinction matter. Refine the objects or retain the paths until the subsequent operation is well defined. MATH.2 constructs an identification that preserves selected operations; it can later reduce the structure deliberately.

An interpretation can associate generators with transformations in another setting. The mathematical path then specifies their composition. Whether those transformations are available and adequate in that setting is the application's question, using such common methods as FPF C.29 and B.5.MPC.

Stop when the receiving question has a permitted path, a reusable construction, or a specific failed connection. Constructing every possible path or proving an unchanged concatenation law again adds no result to that use.

### MATH.1:5 - Archetypal Grounding

#### MATH.1:5.1 - A continuation that needs a permission

Two routes `p` and `q` start at `S` and reach location `V`; their costs are 1 and 4. A final step `r` costs 2. Under the first rule, `r` is available after either route, so `p;r` and `q;r` are paths and their costs are 3 and 6.

Now change the rule: only `q` grants the permission needed for `r`. Keeping a single endpoint `V` would still make `p;r` appear composable.

Construct two intermediate objects, `V0=(V,0)` and `V1=(V,1)`. Set:

| Generator | Source | Target | Cost |
| --- | --- | --- | ---: |
| `p` | `S` | `V0` | 1 |
| `q` | `S` | `V1` | 4 |
| `r` | `V1` | `T` | 2 |

The path `q;r` exists and costs 6. The expression `p;r` fails the endpoint test. Selecting the cheaper prefix first would therefore lose the available completion. The useful result is the permitted path and its cost; the refined endpoint explains why it is permitted.

If a further generator `a:V0→V1` grants permission at cost 1, a new path `p;a;r` becomes available at cost 4. The former failure has opened a construction question: what additional arrow would connect the available prefix to the required continuation?

#### MATH.1:5.2 - Natural numbers from repetition

Take one object `X` and one generating loop `a:X→X`. The paths are the empty word, `a`, `a;a`, and longer repetitions. Write `a^n` for the list containing `n` copies, with `a^0=id_X`.

Concatenating `a^m` and `a^n` gives `a^(m+n)`. Thus lengths supply an arithmetic account of this structure: the identity corresponds to 0 and composition corresponds to addition. Every path is determined by its length in this one-generator case.

Adding a second loop `b` changes the situation. The paths `a;b` and `b;a` both have length 2 but are different lists. Counting generators now loses their order. It still answers a length question; a question about which generator acts first requires the path.

#### MATH.1:5.3 - Order matters under interpretation

On integers let `f(x)=x+1` and `g(x)=2*x`. Both generators start and end in the integer type, so both orders are composable. Starting from 0, `f;g` returns 2, while `g;f` returns 1.

The associativity argument allows regrouping a longer list. It does not authorize exchanging `f` and `g`. The differing results make that boundary consequential.

#### MATH.1:5.4 - Keep the intermediate states of interacting updates

Two updates to a counter each read its current value, retain that reading and later write the reading plus one. From zero, finishing one update before the other gives two. If both read zero before either writes, the final value is one.

To represent the difference, a state retains the counter, each update's saved reading and whether its read and write have occurred. A read copies the counter into that update's saved value; its later write replaces the counter by that saved value plus one. Form paths in which each read precedes its own write. The paths read-A, write-A, read-B, write-B and read-A, read-B, write-A, write-B return two and one respectively.

Treating each update as one indivisible arrow would lose the second path. If the work can require one complete update to finish before the other, the restricted paths preserve both increments. FPF C.29 establishes how these transitions describe the implemented work; Method Engineering B.1.5.CM helps change its composition. Choosing an implementation also depends on how it handles waiting, interruption and failure.

### MATH.1:6 - Bias-Annotation

A familiar drawing can make location seem like the whole state. The permission case exposes the omitted condition through a failed continuation, then repairs the mathematical object.

The construction also favors retaining history. This is useful while the role of the generators is unsettled, but it can be unnecessarily expensive when only a value or an equivalence class is needed. Use the subsequent quotient or evaluation deliberately, stating the operation or question it preserves.

### MATH.1:7 - Conformance Checklist

- Can the reader identify each generator's source and target?
- Does each constructed path satisfy the adjacent-endpoint condition, including any action-changing refinement such as permission?
- Are empty paths attached to their objects and composition defined in one stated order?
- Are the claimed identity and associativity laws supported by the construction used?
- Does the returned path retain the detail required by its next use? If only a cost, length or class is returned, is that sufficient for the receiving question?
- When a connection fails, is the missing or incompatible endpoint recoverable without inventing an available generator?


### MATH.1:8 - Common Anti-Patterns and How to Avoid Them

**Join by location while losing an enabling condition.** In :5.1, replacing `V0` and `V1` by `V` creates an apparent connection that the permission rule excludes. Restore the condition in the intermediate object and try the composition again.

**Use a path value as a substitute for a path.** The same length can describe `a;b` and `b;a`. Return the list when order matters; return the value when the question only consumes that value.

**Read associativity as permission to reorder.** Parentheses choose grouping. They leave generator order unchanged, as the `f;g` example shows.

### MATH.1:9 - Consequences

The construction turns elementary connections into reusable mathematical objects and an operation on them. It provides a witness for a permitted combination and a precise location for a failed one. Different contributors can prepare subpaths and compose them at shared endpoints.

Retaining all generator lists can produce a much larger structure than the final question needs. A quotient can remove selected distinctions; a cost calculation can compare alternatives. Each reduction has to preserve what its receiving use consumes.

A new continuation may reveal an inadequate object description. The repair then changes the endpoint distinction and the affected paths, while unchanged generating rules and concatenation arguments remain reusable.

### MATH.1:10 - Architectural Rationale

Generating first and identifying later separates two mathematical decisions: which composites exist and which of them count as the same. It gives a small constructive starting point when an application or theory has elementary steps but no satisfactory account of their combinations.

The empty path and endpoint conditions make composition uniform. An already completed segment can be treated like an elementary arrow in a larger composition. This is why the same construction supports words, typed transformations and possible routes through a process.

A concrete transformation structure can be more economical when only its resulting transformations matter. Paths earn their additional detail when the sequence, its formation conditions or its later reinterpretation affects the answer. The examples expose both uses: with one object and one generating loop, length determines the path; adding a second loop permits paths of equal length with different orders.

This method constructs a particular mathematical structure. FPF B.5.RC helps recover a construction already described, and C.29 helps relate a mathematical structure to another subject. Their results can be used before or after this construction.

### MATH.1:11 - SoTA-Echoing

**Question:** how can permitted elementary connections generate reusable composites while retaining their order and formation conditions?

**Adopt** the free-path construction in Fong and Spivak's [*Seven Sketches in Compositionality*](https://arxiv.org/pdf/1803.05316), §3.2.1, pp.82-83, 2018 manuscript: arrows generate finite paths, with empty paths and concatenation. It supplies the constructive definitions used in :4.2-:4.3.

An alternative is to compose the interpreted transformations directly. Retaining permission in the state can make the required continuation's availability explicit; the functions in :5.3 already distinguish the two orders. By comparison, a location-only summary in :5.1 loses permission, and length alone in :5.2 loses order.

**Adapt** the construction by retaining generator history when the receiving question needs it. On the integers let `f(x)=x+1` and `h(x)=x-1`. The path `f;h` and the empty path induce the same identity function. With unit cost for each generator their costs are 2 and 0. Direct function composition answers the transformation question; the paths retain the steps for inspection or replacement, while a cost-only question can use their calculated costs. The trade-off is the larger space of paths in exchange for recoverable history.

Section 3.2.2, pp.84-85, supplies the later option of imposing path equations; MATH.2 develops operation-preserving identification. The route and permission cases here are authored applications of the mathematics. Reconsider this choice if a quotient or an interpreted structure supports the same required continuations with less retained detail, or if the problem's compositions are not finite sequential paths.

### MATH.1:12 - Relations

- **Uses FPF B.5.RC when needed:** recover an unfamiliar source's objects and construction rules before choosing generators.
- **Supplies MATH.2:** paths and composition can be the objects and operation whose identification is tested.
- **Connects with FPF C.29 and B.5.MPC:** carry a mathematical path or obstruction to an interpreted subject, and revisit the subject formulation when the correspondence fails.
- **Connects with FPF B.5.QD and C.39.RO:** a missing connection can motivate a new generating operation or a new mathematical question.

### MATH.1:End
