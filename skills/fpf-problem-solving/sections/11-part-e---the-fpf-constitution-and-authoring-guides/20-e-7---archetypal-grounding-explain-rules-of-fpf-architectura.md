## E.7 - Archetypal Grounding: Explain Rules of FPF Architectural Patterns through Cases

> **Status:** Stable

### E.7:1 - Problem frame

Use this pattern when writing or reviewing an architectural rule that somebody must apply. Identify the question the practitioner brings and the decision the rule lets them make. Choose a demonstration in which the reader can see what makes that decision warranted. A reader who came for a fact about one occurrence can use the fact directly.

### E.7:2 - Problem

An author can explain a related subject accurately while leaving the reader's question unanswered. The mistake can run either way. “Identify the objects and relations” omits which participants and relations matter to this decision. A fully worked instance can prescribe a particular kind of participant, arrangement or model where the reader was meant to choose one. More detail about that instance can leave the original choice just as obscure.

### E.7:3 - Forces

| Force | Question for the author |
|---|---|
| Generality and grounding | Which relation warrants the conclusion throughout its stated application, and where can the reader see it at work? |
| Scope and attention | Which wholes, constituents or interactions must the reader consider? At each relevant scale, which alternatives must the model distinguish? |
| Brevity and explanation | Does the reader already have the grounds for the answer? What would a further illustration let them decide? |

### E.7:4 - Solution — mandatory *Archetypal Grounding* subsection

Every architectural pattern **SHALL** include a section headed **Archetypal Grounding**. Derive its content from the work promised in Solution. State the question, who must make the choice, which kinds of things the claim is about, and which relation supports the answer. A method can organize several constituent methods. A system can perform work by a method, and an episteme can report what happened. A fact about one of these can help answer a question about another when the connection is established.

Choose a fitting passage, case, comparison, or usable boundary of the rule. Show what the practitioner starts with, which decision they make and why it follows. When a passage changes the kind of holon, its scale of composition, or the level of abstraction of its model, identify the correspondence at the point the reader needs it. On returning to the commissioned question, use the part of the argument that survives this move. A demonstration can contain the entire general argument when its reasoning covers the permitted variations. A finding confined to one case carries that reach.

When `U.System` and `U.Episteme` disclose different conditions of the rule, show the difference. Rules about methods, work, disciplines or relationships across kinds need grounding in those subjects. For a range, explain what holds at each relevant scale or level, what transfers between them, or what they support only together, according to the claim. C.39.SA helps to select the range. C.37.MM connects findings from several models. F.19 returns to C.39.QR when a clear passage answers a different question, and to C.39.GA when the reader needs the omitted general argument.

### E.7:5 - Archetypal Grounding for E.7

An author explaining B.1 wants a practitioner to decide whether several constituents make the claimed whole. The author first identifies what would warrant that decision for the kind of whole in question. In B.1:5.1 the arrangement of physical components supports a claim about an assembly. In B.1:5.2 a collection of sources can exist while their claims still lack the integration required of the proposed episteme. The author chooses the contrast because it exposes a consequential assumption: the way constituents make a whole must be established for its kind. Merely naming a system and an episteme would leave that decision to the reader.

Now change the commission: the reader of A.15.1:5.1 must establish which executions constituted a particular completed work. The same team and plan are compatible with an operation performed during that work and with an operation performed earlier whose result the team used. The author therefore grounds the rule in what was actually performed and how that execution belonged to the work. The plan and prior result have a supporting role. This choice follows from the question about performed work and can be used in another organization with other performers and records.

### E.7:6 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑AG.1** | Every architectural pattern **SHALL** contain an *Archetypal Grounding* section under E.8's heading rules. | Readers can find the application beside its rule. |
| **CC‑AG.2** | The grounding **MUST** show what allows the reader to answer the commissioned question for the kinds and relations it concerns. Use a contrast when it reveals an otherwise unresolved choice or limit. | A related, intelligible example can leave the main decision open. |
| **CC‑AG.3** | For a claim confined to particular conditions, identify what the operation requires. For a wider claim, give grounds that reach its stated uses. E.5.4's lenses can expose an assumption worth testing. | Readers can distinguish a boundary of the rule from the reach of evidence shown. |
| **CC‑AG.4** | Admission of an architectural pattern requires a grounding section satisfying CC‑AG.1–3. | Keeps grounding a condition of acceptance. |

### E.7:7 - Consequences

A practitioner can see which choices the rule supplies and which they must make for their own work. The author can keep a short direct demonstration, or add a contrast where the first application leaves a consequential alternative unresolved.

### E.7:8 - Rationale

**P‑2 Didactic Primacy** requires the explanation to support the practitioner's work. **P‑1 Cognitive Elegance** favours the smallest demonstration that carries the needed reasoning. Change an assumption of the example while keeping the commission fixed. If the reader's justified answer changes, make the dependency visible. If a claim is universal over a stated domain, a counterexample inside that domain can settle the question against it. A successful instance supports the general claim only to the extent that its argument applies throughout that domain.

### E.7:9 - Relations

* **Implements macro flow:** `pat:authoring/didactic‑architecture` (E.6).
* **Selects relevant kinds and relations:** `pat:kernel/holon` (A.1), C.39.SA and C.37.MM.
* **Exposes assumptions:** `pat:guard/bias‑audit` (E.5.4) via CC‑AG.3.
* **Governs the grounding section:** `pat:authoring/pattern‑template` (E.8).

### E.7:End
