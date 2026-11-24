# Sources

What each rule of the skill rests on. These are design arguments, engineering reports, formal
results under stated assumptions, and studies of selected failures. They are different kinds of
grounds and do not add up to one measure. None of them measures the effect of this method, and
counts from the failure studies describe their samples, not software in general.

## Contents

- [Change and simplicity](#change-and-simplicity)
- [Models, boundaries and interfaces](#models-boundaries-and-interfaces)
- [Comparing designs](#comparing-designs)
- [Guarantees under failure](#guarantees-under-failure)
- [Studies of how systems break](#studies-of-how-systems-break)
- [Evidence and its limits](#evidence-and-its-limits)
- [Sources of the moves](#sources-of-the-moves)

## Change and simplicity

| Source | What the skill takes |
|---|---|
| Kent Beck, 2012: "for each desired change, make the change easy (warning: this may be hard), then make the easy change" | The core rule |
| Kent Beck, *Tidy First?* (2023) | Structure changes apart from behaviour changes; tidy first, after, later or never; coupling as the cost of change; gathering code into one pile |
| Michael Feathers, *Working Effectively with Legacy Code* (2004) | Seams; characterization tests |
| Ola Ellnestam, Daniel Brolund, *The Mikado Method* (2014) | Try, note, revert, do the prerequisites |
| Danilo Sato, "Parallel Change" | Expand, migrate, contract |
| Sandi Metz, "The Wrong Abstraction" (2016) | Duplication is cheaper than a wrong abstraction |
| Carson Gross, [The Grug Brained Developer](https://grugbrain.dev/) | Saying no to scope; waiting for the shape before abstracting; locality of behaviour; knowing why a fence is there before removing it (Chesterton's fence) |

## Models, boundaries and interfaces

| Source | What the skill takes |
|---|---|
| David Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules" (1972) | A boundary hides a decision likely to change, not a step of processing |
| John Ousterhout, *A Philosophy of Software Design*, 2nd ed. (2021) | Deep modules; complexity as what a reader must hold in mind; design it twice; define errors out of existence |
| Eric Evans, *Domain-Driven Design* (2003) | A model in the language of the domain; contexts with their own meaning of a term |
| Scott Wlaschin, *Domain Modeling Made Functional* (2018) | States and transitions as types; unvalidated input apart from valid domain values |
| Yaron Minsky, "Effective ML"; Alexis King, "Parse, don't validate" (2019) | Illegal states that cannot be represented; convert once at the edge |
| Hyrum Wright, "Hyrum's Law" | Every observable behaviour will be depended on |

## Comparing designs

| Source | What the skill takes |
|---|---|
| Len Bass, Paul Clements, Rick Kazman, *Software Architecture in Practice*, 4th ed. (2021) | Quality scenarios: event, conditions, response, measure; comparing designs on the same scenarios; trade-off points |

## Guarantees under failure

| Source | What the skill takes |
|---|---|
| Martin Kleppmann, Chris Riccomini, *Designing Data-Intensive Applications*, 2nd ed. (2026) | What another participant can observe between the steps of an operation and after its repeat; isolation, durability, ordering |
| Michael Nygard, *Release It!*, 2nd ed. (2018) | How a local problem spreads through healthy components; limits on waiting and resources; protections chosen by failure mechanism |
| Heather Adkins et al., *Building Secure and Reliable Systems* (2020), chapters 6-9 | Understandable structure as the basis for reasoning about invariants; design for change and recovery |
| Loren Kohnfelder, Praerit Garg, "The Threats to Our Products" (Microsoft, 1999); Adam Shostack, *Threat Modeling: Designing for Security* (2014) | STRIDE as six questions about what a caller can force on purpose; the threat model made at design time and sized to the change |
| Nancy Leveson, *Engineering a Safer World* (2012) | Start from unacceptable losses; harm that arises from the interaction of working parts |
| Leslie Lamport, *Specifying Systems* (2002) | States and transitions as the language of a promise; safety apart from progress |
| J. Saltzer, D. Reed, D. Clark, "End-to-End Arguments in System Design" (1984) | Some guarantees can only be completed where their meaning is known |
| Marc Brooker, "Timeouts, retries, and backoff with jitter" (Amazon Builders' Library) | A timeout leaves the outcome unknown; retries amplify load; budgets |
| Becky Weiss and Mike Furr, "Static stability using Availability Zones" (Amazon Builders' Library) | Normal work and recovery have different dependencies |
| Mike Ulrich, "Addressing Cascading Failures" (Google SRE book) | Queues, shared resources, early refusal, deadline propagation |

## Studies of how systems break

Each entry gives the mechanism the study explains.

| Study | Mechanism |
|---|---|
| Yuan et al., "Simple Testing Can Prevent Most Critical Failures" (OSDI 2014) | An error handler is part of the state protocol; wrong handling of a reported error escalates |
| Leesatapornwongsa et al., "TaxDC" (ASPLOS 2016) | Whole protocols race: a user operation, recovery, change of ownership, background cleanup |
| Alquraan et al., "An Analysis of Network-Partitioning Failures in Cloud Systems" (OSDI 2018) | Participants see different reachability; ownership rules must cover partial partitions and healing |
| Huang et al., "Gray Failure" (HotOS 2017) | The detector reports healthy while clients fail |
| Pillai et al., "All File Systems Are Not Created Equal" (OSDI 2014) | A storage contract is weaker than the application assumed |
| Bronson et al., "Metastable Failures in Distributed Systems" (HotOS 2021); Huang et al., "Metastable Failures in the Wild" (OSDI 2022) | A failure sustains itself after its trigger is gone |
| Oppenheimer et al., "Why Do Internet Services Fail, and What Can Be Done About It?" (USITS 2003) | A configuration change reaches the whole service at once; redundancy does not mask it |

## Evidence and its limits

| Source | What the skill takes |
|---|---|
| Newcombe et al., "How Amazon Web Services Uses Formal Methods" (CACM 2015) | A small model of the critical transitions finds sequences review does not |
| Zhou et al., "FoundationDB" (SIGMOD 2021) | Testability designed in; lifecycle and recovery as architectural dependencies |
| Hawblitzel et al., "IronFleet" (SOSP 2015) | Always say what was checked, against which specification, under which assumptions |
| Alvaro et al., "Lineage-driven Fault Injection" (SIGMOD 2015) | Start from a successful outcome and search for the failures that remove it; several paths are not proof of independence |
| Wang et al., "Are 'Solved Issues' in SWE-bench Really Solved Correctly?" (ICSE 2026); Yu et al., "UTBoost" (ACL 2025) | An accepted agent patch can still be wrong; the acceptance procedure itself needs checking |

## Sources of the moves

| Move | Source |
|---|---|
| Verifiable hint | Butler Lampson, "Hints for Computer System Design" (1983) |
| Single writer | Martin Thompson, "Single Writer Principle" (2011) |
| Order-insensitive operations | Joseph Hellerstein, Peter Alvaro, "Keeping CALM" (CACM 2020) |
| Escrow | Patrick O'Neil, "The Escrow Transactional Method" (1986) |
| Structured concurrency | Martin Sústrik; Nathaniel J. Smith, "Notes on structured concurrency" (2018) |
| Remove the dangerous fallback | Jacob Gabrielson, "Avoiding fallback in distributed systems" (Amazon Builders' Library) |
| Shed load early | David Yanacek, "Using load shedding to avoid overload" (Amazon Builders' Library) |
| Deterministic simulation | FoundationDB (above) |
| Deletion test | tef, "Write code that is easy to delete, not easy to extend" (2016) |
| Design with a time limit | Martin Fowler, "SacrificialArchitecture" (2014) |
| Idempotent operations and identity | Pat Helland, "Life beyond Distributed Transactions" (2007) and "Idempotence Is Not a Medical Condition" (2012) |
