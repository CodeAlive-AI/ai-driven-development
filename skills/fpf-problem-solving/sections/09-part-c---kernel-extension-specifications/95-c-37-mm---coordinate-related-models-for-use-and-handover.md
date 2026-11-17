## C.37.MM - Coordinate Related Models for Use and Handover

> **Type:** Method pattern
> **Status:** Stable

### C.37.MM:1 - Problem frame

**Use this when** a decision depends on what several models establish together, or a successor must be able to interpret, reproduce or revise their results. The models may concern a system, a method, a relation, or several connected entities. A colleague can understand every diagram and still be unable to answer the question for which they received the set.

Start with the work the recipient must do and the conclusion on which it depends. If a single understood model settles the question, use it directly. C.37:4.6 covers the simpler case in which a recipient needs several representations for one action and each keeps its own supported conclusion.

### C.37.MM:2 - Problem

One model can omit a condition another silently assumes. A recipient can also receive all the needed models and still lack the conventions for reading a blank entry, a shared designation or an estimate. Which models, relations and methods must remain available for the recipient's work?

### C.37.MM:3 - Forces

Adding material from more specialists can improve coverage while making a contradiction harder to locate. The author may know an interpretation that a successor has never encountered. Recording every possible connection imposes work and can hide the few connections that determine the answer.

### C.37.MM:4 - Solution

#### C.37.MM:4.1 - Establish what the models must support together

Name the intended inference, action or reproduction task and its possible outcomes. Identify which model supplies which premise. For each premise recover the modeled entity, conditions, interpretation and relevant edition. A local name for several models supplies a convenient reference. If the proposed **multimodel** is to be relied on as a coordinated set, establish the consequential connections that let the models support this use.

When several models concern the same entity, establish its identity across them. When they concern different entities, state the actual relation. A system, the work that produces it and a cost estimate for that work can all affect one design decision. The estimate's use depends on what work it covers. For an admitted holon, B.1 and the kind-specific method govern the inference from the constituents and their organization to a whole-level result. A modeled relation with independently identified participants needs no presumption of physical parts.

#### C.37.MM:4.2 - Test the joint conclusion

State how the claims from the models are to be read together. Align such matters as units, conditions, time, configuration and whether a value was stipulated, observed or predicted when the conclusion depends on them. Check whether the commitments can all hold in the same case. Pairwise compatibility can leave the whole set inconsistent. If no case satisfies all the commitments, trace the conflict to the models or their interpretation. If information is missing, identify the premise or correspondence needed to settle compatibility.

To establish that an outcome is possible under these models, exhibit one jointly admissible case with that outcome. To guarantee the outcome under the stated conditions, establish that at least one case is admissible and that every jointly admissible case has that outcome. One admissible exception defeats the guarantee.

A claim about a candidate is distinct from a claim about how an actual system performed. To use a test result from an observed system, state what was observed and which target claim it supports under which conditions. B.5.MR supplies the test for a further claim that joint use strictly refines the earlier model. A gain in interpretation can occur while the set of eligible candidates stays the same.

#### C.37.MM:4.3 - Make the receiving use reproducible

Ask what the successor will need to do. To **read** an existing result, they need the governing types, meanings, constraints, editions and consequential links. A **metamodel** can supply conventions that determine which models are admissible. A **megamodel**, in this handover use, makes the related models and the relevant links to their governing models recoverable. A reference to an accessible, identified edition suffices when it gives the recipient what they need. If the governing conventions may themselves change, preserve the grounds for the relevant higher-order choices.

To **repeat, adapt or examine the original derivation**, identify its production method and the inputs and assumptions on which it depends. To **check its conclusion independently**, establish the common target, conditions and meaning of the result. A missing premise leaves the original derivation incomplete. The conclusion can still be established by another sound method. For a claim about every admissible case, one counterexample that meets its conditions refutes the claim. A glossary can settle what an estimate means while leaving the successor unable to recompute it. When one source supplies a well-understood method, name the applicable edition and the values fixed locally.

To **act on the result**, the recipient may additionally need the resources, capability and authority for the work. An assignment, where relied on, is a relation with a system as its holder under A.2.1. Handing over an account does not establish that anyone has performed the work.

#### C.37.MM:4.4 - Reopen only the dependent conclusions

When an observation, model edition or interpretation changes, follow the consequential relations to the conclusions and actions that used it. Tell their users what changed and which use must be reconsidered. Test the revised result under the conditions that made the change relevant. If an earlier model is retained as evidence of a past decision, keep its effective edition identifiable.

### C.37.MM:5 - Archetypal Grounding

Two accounts bear on the same stipulated preference relation over three alternatives. The first reports that A is preferred to B, the second that B and C are tied. With a shared population, comparison conditions and the premise that these judgments are readings of one complete and transitive weak order, the two claims imply that A is preferred to C. If a blank in the second table means “uncompared”, the tie is missing and the conclusion is open. The two files can remain as they are. A recipient needs the applicable interpretation of that entry and the grounds for the common relation. Observed human choices require evidence for any claim that this weak-order interpretation fits them.

An engineering team receives a design and a table of life-cycle cost estimates. It can read the units and still be unable to adapt the estimate to a new maintenance interval. Field observations of failures and a fixed catalogue replacement schedule can yield the same sum for the original interval. Ask which method produced the estimate and recover its inputs before revising it. Under SYSE.7 a narrowly defined decision may need just one of these descriptions. A commission for a whole-system account can require additional engineering coverage.

### C.37.MM:6 - Bias-Annotation

Readers commonly give precedence to the most precise-looking model. A model precise about functional behavior can omit a cost, construction or usage premise on which the recipient's decision turns. Recover the missing premise before preferring a format.

### C.37.MM:7 - Conformance Checklist

- The intended result, the modeled entities, each model's contribution and the indispensable relations are recoverable.
- The joint inference has the support its conclusion needs. A claim of possibility has a jointly admissible case with that outcome. A guarantee covers every jointly admissible case and the models admit at least one. A conflict or gap leads back to the affected premise.
- Material supplied at handover is sufficient for the recipient's actual use, including the production method for repeating, adapting or checking its derivation, and the grounds of comparison for an independent check.

### C.37.MM:8 - Common Anti-Patterns and How to Avoid Them

A common title, shared file or new graph can hide a missing relation. Read its consequential links in ordinary terms and test the conclusion they are claimed to support. A publisher can also provide every governing convention while omitting an entire aspect the decision needs. Check coverage against the original assignment.

### C.37.MM:9 - Consequences

A recipient can identify why a joint conclusion holds, which question remains open and which work must be repeated when a premise changes. One usable edition reference can support several models.

### C.37.MM:10 - Architectural Rationale

The needed method concerns the relations required by the receiving use. C.13 governs a separate claim of collection or composition, and A.22 governs identity for a selected structure. The same work can be carried through in ordinary prose, a project account or a maintained registry.

### C.37.MM:11 - SoTA-Echoing

Megamodeling in model-driven engineering makes models and typed relations, including conformance, available for navigation. Architecture-description practice uses stakeholder concerns to select views and viewpoints to interpret them. A model register can serve a successor who needs to retrieve the governing edition. For a decision that depends on several views, even a complete register leaves open which conclusions their commitments support together. Section 4.2 tests the joint inference. Section 4.3 distinguishes the inputs needed to repeat its derivation from the grounds for checking the conclusion independently. Revisit the selected views and links when a new decision needs a different premise or when a change of convention alters a premise already in use. [Bézivin, Jouault and Valduriez, *On the Need for Megamodels*](https://s23m.com/oopsla2004/bezivin-megamodel.pdf) · [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html)

### C.37.MM:12 - Relations

C.37 governs co-use for one action. C.37.MP governs several actions that depend on one method representation. C.2.1 supplies the identity of each model episteme, E.17.0 governs viewpoint and view when asserted, B.5.MR compares model commitments, and SYSE.7 applies this method in engineering.

### C.37.MM:End
