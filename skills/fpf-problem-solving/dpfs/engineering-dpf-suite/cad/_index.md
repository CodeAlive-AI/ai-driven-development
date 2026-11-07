# Control Architecture Design Principles Framework

**Edition:** [CAD, 23 October 2026](08-cad-reference-8---names-and-continuing-references.md).

Use this framework when a control design must reconcile what can be observed in time, what the controller must remember, how decisions are divided, which commands remain feasible, and what the implementation can execute. It helps construct and compare those arrangements for an engineered dynamical system, including the choice to keep one sufficient controller.

The quantitative methods principally cover sampled linear models with bounded uncertainty and specified feedback-law candidates. The planning-and-feedback branch also states a separate conditional continuous-time error-bound construction. This is a bounded practice within control engineering; identification, unrestricted controller synthesis and physical qualification require their own methods.

# Table of Contents

- [Readme](_index.md#control-architecture-design-principles-framework-readme)
- [Control Architecture Design Architectural Reference](_index.md#control-architecture-design-architectural-reference)
  - [CAD.Reference:1 - What the language helps obtain](01-cad-reference-1---what-the-language-helps-obtain.md)
  - [CAD.Reference:2 - The objects and independently useful contributions](02-cad-reference-2---the-objects-and-independently-useful-contr.md)
  - [CAD.Reference:3 - Information, tracking and execution must describe the same loop](03-cad-reference-3---information-tracking-and-execution-must-de.md)
    - [CAD.Reference:3.1 - How information changes a command margin](03-cad-reference-3---information-tracking-and-execution-must-de.md#cadreference31---how-information-changes-a-command-margin)
    - [CAD.Reference:3.2 - A complete joint design and a changed delay](03-cad-reference-3---information-tracking-and-execution-must-de.md#cadreference32---a-complete-joint-design-and-a-changed-delay)
  - [CAD.Reference:4 - The layered planning-and-feedback branch](04-cad-reference-4---the-layered-planning-and-feedback-branch.md)
    - [CAD.Reference:4.1 - The recurring whole problem](04-cad-reference-4---the-layered-planning-and-feedback-branch.md#cadreference41---the-recurring-whole-problem)
    - [CAD.Reference:4.2 - Why these four contributions belong together](04-cad-reference-4---the-layered-planning-and-feedback-branch.md#cadreference42---why-these-four-contributions-belong-together)
    - [CAD.Reference:4.3 - Connect dynamics, decisions and computation by their actual quantities](04-cad-reference-4---the-layered-planning-and-feedback-branch.md#cadreference43---connect-dynamics-decisions-and-computation-by-their-actual-quantities)
    - [CAD.Reference:4.4 - Reuse the external foundations without losing the subject transition](04-cad-reference-4---the-layered-planning-and-feedback-branch.md#cadreference44---reuse-the-external-foundations-without-losing-the-subject-transition)
    - [CAD.Reference:4.5 - Several legitimate entries and their returns](04-cad-reference-4---the-layered-planning-and-feedback-branch.md#cadreference45---several-legitimate-entries-and-their-returns)
      - [CAD.Reference:4.5.1 - Keep a qualified loop and govern its commands](04-cad-reference-4---the-layered-planning-and-feedback-branch.md#cadreference451---keep-a-qualified-loop-and-govern-its-commands)
    - [CAD.Reference:4.6 - Worked joint revision](04-cad-reference-4---the-layered-planning-and-feedback-branch.md#cadreference46---worked-joint-revision)
    - [CAD.Reference:4.7 - Recognition, assurance and the cost of the arrangement](04-cad-reference-4---the-layered-planning-and-feedback-branch.md#cadreference47---recognition-assurance-and-the-cost-of-the-arrangement)
    - [CAD.Reference:4.8 - Source boundaries, bias and future change](04-cad-reference-4---the-layered-planning-and-feedback-branch.md#cadreference48---source-boundaries-bias-and-future-change)
  - [CAD.Reference:5 - What is covered and what must be supplied](05-cad-reference-5---what-is-covered-and-what-must-be-supplied.md)
  - [CAD.Reference:6 - Why one language, with independent uses](06-cad-reference-6---why-one-language-with-independent-uses.md)
  - [CAD.Reference:7 - Sources, external suppliers and consequential change](07-cad-reference-7---sources-external-suppliers-and-consequenti.md)
  - [CAD.Reference:8 - Names and continuing references](08-cad-reference-8---names-and-continuing-references.md)

## A. Choose the information available to control

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| --- | --- | --- | --- | --- |
| A.1 | [CAD.5 - Choose Observations and Internal State for Control](10-cad-5---choose-observations-and-internal-state-for-control.md) | Stable | Delayed observation; partial sensing; action history; information state; set estimation. “Which sensors and memory let this controller act within its limits?” “Can any action work with these observations?” | Uses A.3.3.PI and C.32.LCA; the main use is self-contained. CAD.2–CAD.4 are conditional receivers of :4.7. |

## B. Design a planning-and-feedback architecture

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| --- | --- | --- | --- | --- |
| B.1 | [CAD.1 - Derive a Control Decomposition from the Whole Problem](11-cad-1---derive-a-control-decomposition-from-the-whole-proble.md) | Stable | Control decomposition; information; horizon; computational burden. “Should these decisions be separated?” | Uses C.39 and MMP.9; CAD.2 develops the selected exchange; CAD.4 compares whole candidates. |
| B.2 | [CAD.2 - Construct the Planning and Feedback Interface](12-cad-2---construct-the-planning-and-feedback-interface.md) | Stable | Reference meaning; state reconstruction; sample-and-hold; reset; tracking dynamics. “What does the lower loop actually receive?” | Uses the selected decomposition and MMP.18; CAD.5:4.7 supplies the estimate-based branch. |
| B.3 | [CAD.3 - Construct a Jointly Admissible Command Domain](13-cad-3---construct-a-jointly-admissible-command-domain.md) | Stable | Invariant error; input reserve; constraint tightening; continuation. “Which commands can remain feasible?” | Uses CAD.2's connected dynamics; CAD.5:4.7 when state is estimated; returns to CAD.1 or CAD.2 on incompatibility. |
| B.4 | [CAD.4 - Co-design and Realize the Whole Control Architecture](14-cad-4---co-design-and-realize-the-whole-control-architecture.md) | Stable | Model order; gains; rates; deadlines; whole-candidate comparison. “Which feasible arrangement should be realized?” | Receives applicable CAD.1–CAD.3 and CAD.5 results; uses MMP.22; supplies the broader SYSE.6 decision. |

# Control Architecture Design Principles Framework Readme

Within FPF Library, **CAD** is the reference code and document identifier for the **Control Architecture Design Principles Framework**. A reference such as `CAD.5:4.5` identifies a pattern section; `CAD.Reference:3.2` identifies the Architectural Reference's joint example. The local pattern numbers are addresses, not an execution order.

**Suite:** [Engineering DPF Suite](../suite-reference/02-engineering-reference-0---engineering-specialization-and-mai.md) — control knowledge and design Methods for constructing, changing and sustaining engineered dynamical systems.

## Enter from the control question

| Your working difficulty | Obtain first | Direct entry |
| --- | --- | --- |
| A useful observation arrives after the action deadline, or different channels reveal different parts | An observation and memory arrangement, its error bound and the actions it permits; or a precise information limitation | [CAD.5](10-cad-5---choose-observations-and-internal-state-for-control.md) |
| One calculation cannot use the needed horizon, information and execution time together | Competing decompositions and the couplings each would remove | [CAD.1](11-cad-1---derive-a-control-decomposition-from-the-whole-proble.md) |
| Planner and feedback code use a “reference” with different timing or meaning | The actual exchange and its derived error dynamics | [CAD.2](12-cad-2---construct-the-planning-and-feedback-interface.md) |
| A stable controller cannot follow the requested command within state or actuator limits | A jointly admissible command/error domain with continuation, or a specific incompatibility | [CAD.3](13-cad-3---construct-a-jointly-admissible-command-domain.md) |
| A more accurate model, faster planner or extra sensor competes for limited resources | A comparison of complete feasible arrangements and the conditions of their realization | [CAD.4](14-cad-4---co-design-and-realize-the-whole-control-architecture.md) |

An engineer can use CAD.5 without introducing a planner or multiple layers. An engineer with a qualified lower loop can retain it and change command admission. If a current complete observation and a simple controller already meet the task, they remain a serious stopping alternative. Read the [Architectural Reference](_index.md#control-architecture-design-architectural-reference) when several results must fit together or a change reopens their conditions.

The intended reader can work with state-space models, feedback laws, bounded sets and elementary optimization. A reader who lacks those means needs instruction or a qualified control-engineering contributor. The examples are mathematical constructions. Before relying on a physical installation, establish its model, uncertainty and execution premises.

---

## Files of this publication

Generated by the skill's splitter: one file per section, in reading order.


### Control Architecture Design Architectural Reference

- [CAD.Reference:1 - What the language helps obtain](01-cad-reference-1---what-the-language-helps-obtain.md) (14 lines)
- [CAD.Reference:2 - The objects and independently useful contributions](02-cad-reference-2---the-objects-and-independently-useful-contr.md) (18 lines)
- [CAD.Reference:3 - Information, tracking and execution must describe the same loop](03-cad-reference-3---information-tracking-and-execution-must-de.md) (67 lines)
- [CAD.Reference:4 - The layered planning-and-feedback branch](04-cad-reference-4---the-layered-planning-and-feedback-branch.md) (94 lines)
- [CAD.Reference:5 - What is covered and what must be supplied](05-cad-reference-5---what-is-covered-and-what-must-be-supplied.md) (10 lines)
- [CAD.Reference:6 - Why one language, with independent uses](06-cad-reference-6---why-one-language-with-independent-uses.md) (10 lines)
- [CAD.Reference:7 - Sources, external suppliers and consequential change](07-cad-reference-7---sources-external-suppliers-and-consequenti.md) (19 lines)
- [CAD.Reference:8 - Names and continuing references](08-cad-reference-8---names-and-continuing-references.md) (8 lines)
- [CAD.Reference:End](09-cad-reference-end.md) (2 lines)

### A. Choose the information available to control

- [CAD.5 - Choose Observations and Internal State for Control](10-cad-5---choose-observations-and-internal-state-for-control.md) (479 lines)

### B. Design a planning-and-feedback architecture

- [CAD.1 - Derive a Control Decomposition from the Whole Problem](11-cad-1---derive-a-control-decomposition-from-the-whole-proble.md) (130 lines)
- [CAD.2 - Construct the Planning and Feedback Interface](12-cad-2---construct-the-planning-and-feedback-interface.md) (177 lines)
- [CAD.3 - Construct a Jointly Admissible Command Domain](13-cad-3---construct-a-jointly-admissible-command-domain.md) (204 lines)
- [CAD.4 - Co-design and Realize the Whole Control Architecture](14-cad-4---co-design-and-realize-the-whole-control-architecture.md) (154 lines)

### License

- [License](15-license.md) (3 lines)
