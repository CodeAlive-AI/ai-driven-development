## CMP.16 - Construct Computational Units and Operations for a Required Whole

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### CMP.16:1 - Problem frame

**Use this when** you can state behavior that a computation must obtain, but the available units and operations do not yet give a workable way to obtain it. The difficulty can appear before implementation or after a change: separately sensible steps do not compose, a small unit discards information the join needs, or every client must repair the same invalid intermediate arrangement.

The useful move is to design the units and their permitted operations together. Try constructing the required whole, recover what a failed join needs, and change the unit, the operation or the conditions of assembly. Then connect that computational abstraction to an obtainable implementation. The result is a usable level of operations with grounds for its whole behavior.

For example, deciding whether each text fragment is locally balanced loses information needed to decide whether their concatenation is balanced. A richer fragment meaning can make the join both simple and general. In a continuing service, exposing separate count reads and writes can invite invalid combinations; a state-changing operation with an explicit admission rule can make a capacity condition maintainable. Neither remedy is selected by choosing a storage format alone.

The reader can follow operations on a state and an elementary invariant argument. C.29.2 supplies the computational question and the available model. MATH.17 supplies composition and its closure conditions; MATH.18 supplies interpretation between levels. CMP.2, CMP.10, CMP.12 and CMP.14 develop particular recursive, storage, interpretation and interaction contributions when the construction below needs them.

Keep known adequate units and operations when they already serve the work. Use CMP.10 directly when the operations are sufficiently known and only their representation needs improvement. Use CMP.13 when the question is how to obtain a cheaper sound analysis of a computation. This method instead constructs the units and operations used to obtain the behavior itself. It does not replace the subject inquiry that determines what behavior is useful.

### CMP.16:2 - Problem

How can units, operations and their assembly be constructed together so that the required computational whole can be obtained, understood and changed without inventing a missing connection at every use?

Starting only from small familiar operations can make the whole unnecessarily difficult. Starting only from an elegant abstract interface can hide an unimplementable operation or an excluded case. The construction must work in both directions: from the whole's requirements to the contributions it needs, and from available contributions to a whole that actually meets those requirements.

### CMP.16:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Small units and sufficient meaning | A simpler unit can make composition cheaper or discard the distinction needed to compose correctly. |
| Valid construction and required coverage | Restricting constructors can preserve an invariant while excluding a case the work still needs. |
| A useful level and an obtainable implementation | Hiding detail helps a client only when the promised operations can be supplied below that boundary. |
| Local guarantees and shared behavior | Individually valid transitions can interfere or fail to make progress when combined. |
| Generality and cost | A universal interface can impose more work than a restricted one suited to the receiving use. |
| Preservation and deliberate change | Another representation can preserve behavior; another observation or operation can require a new abstraction. |

### CMP.16:4 - Solution

Construct a provisional whole with proposed units and operations, use its first consequential failure to revise them together, and justify the resulting level against both its clients and its implementation. The moves below can return to one another. An already sufficient interface needs neither reinvention nor an exhaustive search for alternatives.

#### CMP.16:4.1 - Recover the behavior and the freedom to change its construction

State what a recipient must observe or do with the result. Include consequential continuations: a value may later be updated, an object traversed, a description interpreted, or an event acknowledged. Distinguish a finite answer from continuing behavior. For a continuing computation, state what must always hold and what response must eventually occur under which environmental assumptions.

Recover the admitted cases and the available operations through C.29.2. Separate required behavior from an inherited implementation choice. A requirement to preserve order does not require an array; a capacity limit does not necessarily require exposing a mutable counter. Conversely, a physical coupling, a particular external format or an existing client's observation can be binding. Do not change those requirements merely to make the preferred construction easier.

Choose one whole use that exposes the difficulty and a consequential variation. These are design probes, not the scope of the method. If the proposed change would answer a different question, make that difference explicit and return it to the receiver instead of presenting the changed answer as preservation.

#### CMP.16:4.2 - Try the whole before fixing the units

Sketch the computation at a level where its intended effect can be followed. Treat a proposed higher operation as a temporary obligation: say what it receives, what it must return or change, and why the rest of the construction needs it. Do not yet assume that the operation exists or costs one step.

Suppose each proposed part has supplied exactly its promised result. Attempt the next join or continuation. At the first missing contribution, identify the distinction or action that would make the join possible. Typical remedies have different grounds:

- Enrich a returned summary when the join needs information the part discarded. CMP.2 develops this for recursive construction.
- Introduce a compound unit when a relation between smaller items must be preserved by every permitted assembly. Check that the new constructor still covers the required cases.
- Change the operation boundary when separately exposed updates permit invalid states or repeated repair. Include the boundary's interruption and visibility assumptions.
- Pass context or postpone a choice when a part cannot correctly decide without information available at the join.
- Change the decomposition when obtaining the missing contribution would repeat the original difficulty or exceed the resource limit.

Try a simple alternative alongside the favored design. Keeping the original units and checking the final result can be cheaper when invalid assemblies are rare and harmless. A stronger constructor is useful when it makes repeated use or reasoning materially easier.

#### CMP.16:4.3 - Give the proposed unit a meaning through its uses

Describe what a unit represents and which operations clients may perform. Include constructors, observations, transformations and combinations needed by the whole. State conditions of use: an operation can be partial, require ownership of a token, depend on an environment, or report failure. Such conditions must be obtainable and respected by the client, not hidden in a proof that the client cannot satisfy.

Decide which distinctions can be hidden. If two lower-level states represent the same unit, the permitted observations and continuations must respect that identification on the promised scope. A summary that forgets the order of items cannot support an arbitrary future order query. A mutable object and an independent copy may have the same current values but differ after a change. MATH.2 and MATH.18 supply the mathematical identification and interpretation questions; the construction here chooses what the computational client needs them to preserve.

For pure composition, state the operations and the laws the intended assembly uses. Associativity permits regrouping, not reordering. An identity supplies an empty case; an inverse is needed only if the proposed operation undoes a contribution. For stateful behavior, state admissible transitions and observations instead of forcing it into a pure algebra. For a language of descriptions, specify constructors and meanings; CMP.12 develops the corresponding interpreter or translation.

This is an abstraction boundary only when clients can use the stated operations without depending on hidden detail. If a client bypasses it by editing internal state or inspecting an undocumented encoding, either include that behavior in the agreement or remove the bypass.

#### CMP.16:4.4 - Obtain the operations and establish usable composition

Construct each required operation from available steps, or obtain a sufficiently qualified supplier. For a constructor, show how it produces a valid unit from admitted input, or how it detects and reports an unsupported input before the client relies on validity. For an update, derive the changed state from the invariant rather than assuming that a familiar assignment preserves it.

Then establish the whole-forming claim. For a pure assembly, show that the join of admissible contributions has the required meaning and remains usable in the next join. Account for base and empty cases. For a transition system, show that initialization establishes the state condition and every permitted transition maintains it; include the environmental actions that can affect that condition. Induction can then cover arbitrary finite assemblies or execution prefixes under those premises. It does not by itself prove eventual response or cover an omitted operation.

Check coverage separately. Can every required input or behavior be obtained with these constructors and operations? Restricting a unit to internally balanced fragments, for example, would exclude valid whole texts split inside a nested expression. An invariant can be perfectly preserved while that restriction makes the construction unsuitable. Broaden the unit, change the assembly or report the actual limitation.

The construction may depend on a supplied primitive. Keep that dependency visible and return to C.29.3 when its realization is unsettled. CMP.14 establishes the permitted interference and progress when an operation must remain indivisible or coordinate participants. An abstract operation is a useful design result before that realization is available, but it is not yet an executable promise in that environment.

#### CMP.16:4.5 - Relate the new level to its implementation

For a deterministic state abstraction, let `I(c)` state that a concrete state `c` is valid, and let `alpha(c)` give its abstract meaning. Explain how initialization obtains a state satisfying `I`. For each abstract operation, begin with a related state and an admitted argument, follow its concrete implementation, and show that the resulting state remains valid and represents a permitted abstract result. Include the observation returned to the caller. This argument can be ordinary prose and equations; a formal notation or proof assistant is chosen when it earns its cost.

For a pure summary `h` and a source composition `*`, a useful obligation is:

`h(x * y) = combine(h(x), h(y))`.

This equation explains why independently obtained summaries can replace the source parts at that join. It is a claim to derive from their meanings, not an instruction to assume a homomorphism. If it fails, identify the lost distinction, strengthen the summary or restrict the proposed use. A relation rather than a single function can be needed for nondeterminism or multiple acceptable implementations; CMP.12 develops behavior preservation and CMP.14 supplies the interaction conditions.

Also connect progress and resource claims. A lower-level operation can preserve every completed observation while looping forever before producing one. A correct response can miss the required deadline. A finite sequence of abstract operations can expand into unaffordable work. Do not transfer termination, responsiveness or unit cost merely because a value correspondence holds.

At the physical boundary, preparation, actual evolution and readout must supply the relation assumed here. A new physical unit may require an engineering change. Use C.29.3 to obtain that connection and carry any unresolved condition back to the promised whole.

#### CMP.16:4.6 - Compare the complete work and preserve the useful level

Count constructing and converting units, performing their operations, maintaining their invariants, communicating and obtaining the final observations. Include the information retained for later operations. CMP.10 compares concrete storage and access choices; CMP.3 handles shared subcomputations. A cheap abstract join can still require large construction or output work.

Choose a sufficient implementation without unnecessarily exposing it above the boundary. This permits a later replacement when it preserves the operations and observations on which clients rely. A change from a list to a tree can preserve a sequence interface while changing costs. A change from ordered delivery to unordered delivery does not preserve a client that observes order.

When no arrangement satisfies all demands, return the precise conflict: a missing observation, an unsupported operation, an unaffordable construction or an unavailable realization. CMP.1 and CMP.11 can establish relevant impossibility or lower-bound claims; a failed design alone does not establish them. A qualified weaker result is useful only when its receiver accepts the difference.

#### CMP.16:4.7 - Change a condition and reconstruct the affected whole

Vary an input family, required observation, operation, interaction or resource limit that could alter the design. Follow its effect through the abstraction and back to the whole. Ask whether the old unit still retains enough information, whether the allowed operations still preserve its meaning, and whether their implementation still meets the conditions of use.

Preserve unaffected constructions. A new query can require another summary while leaving the source composition intact. A concurrency requirement can preserve abstract operations while invalidating a sequential implementation. A changed subject interpretation can leave an algorithm correct for its earlier mathematical question but unsuitable for the receiving work. These are different returns.

Finish with the usable units and operations, their construction, the reason their permitted assembly obtains the required behavior, and the implementation and resource conditions on which that use depends. It must let the recipient perform the intended whole without privately inventing its missing join.

### CMP.16:5 - Archetypal Grounding

#### CMP.16:5.1 - Construct a fragment meaning that makes concatenation usable

A text is a finite sequence of opening and closing parentheses. The required answer is whether its parentheses are balanced: every prefix has at least as many openings as closings, and the totals agree at the end. The text arrives as independently obtained fragments, which must be combined in their original order.

The first proposal records only whether each fragment is balanced. It fails on the fragments `(()` and `())`: neither is balanced alone, while their concatenation `(()())` is balanced. Requiring every fragment to be balanced would change the admitted splits rather than solve the original problem.

Recover what the whole needs from a fragment. Treat an opening as `+1` and a closing as `-1`. Let `d` be the total change in balance and `m` the minimum of all prefix balances, including the empty prefix with balance zero. The pair says both where the fragment leaves a caller's balance and how far below that starting balance it can go. For a caller entering with balance `b`, the fragment never becomes negative exactly when `b + m >= 0`; its ending balance is `b + d`.

If fragment `A` is followed by `B`, each prefix lies inside `A` or consists of all of `A` followed by a prefix of `B`. Therefore:

```text
combine((dA,mA),(dB,mB)) = (dA+dB, min(mA, dA+mB))
empty = (0,0)
open  = (1,0)
close = (-1,-1)
```

The formula is obtained from the required prefix observation, not guessed from a convenient tuple. It gives the summary of concatenation. Consequently it is associative on summaries of fragments: either grouping describes the same ordered text and the same prefix minimum. It is not commutative. Combining `open` with `close` gives `(0,0)`; reversing them gives `(0,-1)`. The identity `empty` follows from including the empty prefix.

For `(()`, the summary is `(1,0)`; for `())`, it is `(-1,-1)`. Their join is `(0,0)`, so the whole is balanced. A whole summary is balanced exactly when its total is zero and its prefix minimum is nonnegative. A possible implementation is:

```python
def combine(left, right):
    dl, ml = left
    dr, mr = right
    return dl + dr, min(ml, dl + mr)

def summarize(text):
    result = (0, 0)
    for char in text:
        if char == "(":
            piece = (1, 0)
        elif char == ")":
            piece = (-1, -1)
        else:
            raise ValueError("unsupported character")
        result = combine(result, piece)
    return result

def is_balanced(summary):
    total, minimum = summary
    return total == 0 and minimum >= 0
```

Character summaries provide the constructors; `combine` supplies the effective join. Its arguments must be summaries of admitted fragments; an arbitrary supplied pair has not acquired that meaning merely by having two integer fields. The semantic equation connects this small computational algebra to arbitrary finite texts. CMP.2 can organize recursive construction, and CMP.10 can choose an aggregate tree when later edits matter. In a word model with sufficiently wide counters, scanning takes linear work and a join takes constant work. Unbounded text length needs a corresponding account of growing counters; the pair is not literally constant storage in every bit model.

**Changed observation.** Now return the position of the first negative prefix, if one exists. The two texts `)()(` and `())(` have the same length four and the same summary `(0,-1)`, but their first negative positions are one and three. The existing pair cannot answer this query. No faster decoding of the pair recovers the lost distinction.

One remedy retains the composition tree, each child's length and pair, and the leaf characters. Enter the root with balance zero. If a left child's minimum plus the incoming balance is negative, descend left. Otherwise add its total to the balance, skip its length and descend right. At a negative leaf, the accumulated position identifies the first offending character. If the root minimum is nonnegative, there is no negative prefix; a positive final total instead reports unmatched openings. A balanced tree gives a descent proportional to its height after the summaries have been maintained. The storage and update obligations belong to the remedy, not to the old two-number claim.

The original balance decision remains valid. The stronger observation changes the retained unit and its operations. This distinguishes generality over all finite admitted fragments from adequacy for every possible later query.

#### CMP.16:5.2 - Construct an operation boundary for a continuing capacity condition

A service grants permission to use at most `K` resource slots at once, where `K` is a fixed nonnegative integer. Its computational responsibility is to track outstanding grants and refuse another when `K` are active. The relation between a grant and actual resource use is a further requirement: cooperating clients begin use under their own grant and release it only after use ends. Authentication against a caller trying to release another caller's grant is a separate requirement. The computation alone cannot prevent an uncooperative client from using a physical resource.

Exposing `read_count` and `write_count` leaves each client to reconstruct admission and release. A more useful unit is the grant service itself, with `acquire` and `release(ticket)` operations. In an initially sequential model, retain a set `active` and a monotonically increasing ticket number. `acquire` returns `Busy` if `len(active) == K`; otherwise it obtains a fresh ticket, adds it to `active` and returns it. `release` removes a ticket only if it is active, otherwise reports that no active grant matches it. The ticket, rather than an unqualified decrement, identifies what can be released.

Initialization establishes `active = {}`. An admitted acquisition changes its size from a number below `K` to at most `K`; release cannot increase it. Thus every permitted sequence preserves `0 <= len(active) <= K`. Fresh tickets ensure that a delayed second release of an old grant cannot release a later grant. The sequence `acquire -> 0`, `release(0)`, `acquire -> 1`, `release(0)` leaves ticket 1 active: the final release reports no matching active grant.

This is a safety argument for the stated operations. It does not establish that a waiting caller eventually receives permission; that requires available releases and a selection policy. Nor does it settle retry after a lost acquisition reply. If the required behavior gives one grant per logical request, request identity and the retry protocol must be added through CMP.14. The old operations still explain their narrower behavior but not that stronger service.

**Changed execution condition.** Two callers now execute the acquisition body concurrently. With `K = 1`, both can observe an empty set before either inserts a ticket, then insert different tickets. The abstract invariant was not wrong; the implementation no longer supplies the atomic transition it assumed. One remedy serializes the check and insertion through an available exclusive mechanism. CMP.14 develops its permitted histories and progress conditions; C.29.3 establishes whether the chosen executor supplies the required operation.

The ticket implementation also has conditions. A bounded counter can wrap, and a restart can forget active grants. Restricting the lifetime, preserving state or changing the ticket construction needs an argument covering the actual use. Those conditions can select another representation without changing the abstract service, or reveal that its former promise cannot be maintained. This is a continuing computational abstraction, not a terminating calculation whose final count alone defines success.

### CMP.16:6 - Bias-Annotation

Familiar abstractions can bias the designer toward a representation before the required observations are understood. A successful small assembly can conceal an excluded case or an expensive constructor. Conversely, fascination with general interfaces can replace a sufficient direct computation with unnecessary machinery. Use a consequential changed condition and a simple alternative to expose these biases.

An implementation specialist may privately supply an atomic operation, a stable identity or an invariant repair that the description omitted. Keep that contribution explicit. A mathematically convenient model and a physical or organizational arrangement can differ at precisely the step the abstraction hides.

### CMP.16:7 - Conformance Checklist

Recognition asks whether the units and operations themselves need construction for the required whole. An existing adequate interface or a pure storage choice can end that question without this method.

For assurance of the selected construction, establish the consequential claims:

- the required observations, admitted continuations and coverage conditions;
- obtainable constructors and operations, including any required external primitive;
- the reason their permitted assembly preserves meaning and any claimed invariant;
- progress and resource conditions distinct from value correspondence;
- the first changed action or representation under a consequential variation.

Use evidence suited to the conclusion. A trace can refute a claim; a general preservation claim needs its applicable argument; an actual realization needs its implementation basis.

### CMP.16:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Divide the task and assume the parts reconstruct it | Attempt the join and supply its missing information or operation. |
| Preserve an invariant by excluding required inputs | Check coverage separately and revise the unit or the receiving promise. |
| Call a complex operation primitive and count it as free | Obtain its implementation and include its relevant cost and progress conditions. |
| Hide a state distinction that a later continuation observes | Strengthen the abstraction or explicitly restrict that continuation. |
| Treat separate correctness as a joint guarantee | Establish the permitted composition and interference through the actual whole. |
| Treat a new encoding as a new physical arrangement | Obtain the preparation and realization that the proposed operation requires. |

### CMP.16:9 - Consequences

The construction can make a whole easier to obtain, explain and change by moving a repeated obligation into suitable units and operations. A client can then reason at that level while implementations vary within the established correspondence. It can also expose that a proposed abstraction loses coverage, needs unavailable support or costs more than direct work.

The burden is designing and maintaining the boundary, its operations and their grounds. Its useful result can be one sufficient construction or a precise unresolved join; a local failure does not prove that no computational way exists.

### CMP.16:10 - Architectural Rationale

The intended whole constrains the units, and attempted composition tests that choice. This makes synthesis and abstraction mutually informative without identifying them. The fragment example constructs a new summary from the observation needed at the join; the grant example constructs an operation boundary from a continuing state condition. A general claim follows only after the allowed constructions and their preservation grounds have been established.

Choosing a data structure is a serious alternative when the operations are already adequate; CMP.10 supplies it. Recursive decomposition is useful when subproblems and sufficient returns yield a finite answer; CMP.2 supplies that construction. Direct validation of a complete candidate can be cheaper than restricting every intermediate state. The present method is needed when units and operations must change together to make the whole obtainable or its repeated use tractable. CMP.13's approximate analysis can help establish a property, but it has a different result from the computational interface being designed.

The method permits several levels and several implementations. Reveal the detail that the receiving observation or resource argument needs; keep a boundary only where its promised independence is justified.

### CMP.16:11 - SoTA-Echoing

[Dijkstra's Notes on Structured Programming, EWD249](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html) provide a historical argument for developing data organization and operations together and for reasoning across levels while constructing a program. This method retains that constructive coupling without making one sequential programming style the boundary of computational organization.

[SICP's abstraction barriers](https://sicp.sourceacademy.org/chapters/2.1.2.html) give a historical worked account of clients using operations independently of a selected lower representation. Here the boundary is selected from the required whole and includes consequential continuing behavior. A simpler direct representation remains preferable when the boundary adds no useful independence.

The maintained [Verified Functional Algorithms chapter on abstract data types](https://softwarefoundations.cis.upenn.edu/vfa-current/ADT.html) makes interfaces, operation specifications and implementation proof obligations explicit through executable formal examples. It supplies a stronger checking option when those obligations warrant mechanization. A module signature can enforce the exposed structure; the stated behavioral laws still need their proofs.

MATH.17 and MATH.18 supply the composition and interpretation grounds used here. CMP.12 and CMP.14 carry the developed alternatives needed when control, effects or interaction change those grounds. Reopen a design when a new required observation, affordable implementation, admissible operation or execution condition changes the balance among these alternatives.

### CMP.16:12 - Relations

- **C.29.2** obtains the computational question and model; a changed primitive or observation returns to that formulation.
- **MATH.2, MATH.17 and MATH.18** supply identification under operations, composition and interpretation. Their applicable premises govern the computational construction.
- **CMP.2 and CMP.3** construct recursive joins and shared work when these supply operations of the proposed level.
- **CMP.10** chooses representations and accounts for their reads, updates and retention once the needed operations are known.
- **CMP.12** supplies interpretation and preservation when units are descriptions or implementations cross execution levels; **CMP.13** supplies approximate analysis for a selected property.
- **CMP.14 and CMP.15** establish interacting behavior and independently extensible combinations under their respective conditions.
- **C.29.3** connects operations to an actual prepared executor and interpreted readout. **C.39** supplies the broader construction and change of a way of working when the computational result is only one contribution.

### CMP.16:End
