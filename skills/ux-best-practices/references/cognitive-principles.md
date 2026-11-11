# Cognitive Principles and Laws of UX

Use these principles to explain a problem and to form design hypotheses. How many "laws" a finding cites says nothing about its severity. Sources verified **2026-10-21**; exact links, dates and evidence types are in [sources.md](sources.md).

Laws of UX is an external source by Jon Yablonski; consult the linked source registry for original pages.

## Contents

- [Laws by area](#laws-by-area)
- [Laws by task](#laws-by-task)
- [The eight articles](#the-eight-articles)
- [Four laws: rules and misuse](#four-laws-rules-and-misuse)
- [H01: heuristic inspection](#h01-heuristic-inspection)
- [Information architecture: skill synthesis](#information-architecture-skill-synthesis)
- [Inspiration and good faith](#inspiration-and-good-faith)

## Laws by area

Use the source registry to find the original material.

| Area | Law (slug) | Principle |
|------|------------|-----------|
| Decisions | Hick's Law (`hicks-law`) | Decision time grows with the number and complexity of choices. |
| Decisions | Choice Overload (`choice-overload`) | Too many options overwhelm and stall decisions. |
| Decisions | Cognitive Bias (`cognitive-bias`) | Systematic reasoning errors shape perception and choice. |
| Effort | Cognitive Load (`cognitive-load`) | Mental resources are limited; remove extraneous load. |
| Effort | Tesler's Law (`teslers-law`) | Complexity is constant; absorb it in the system, not the user. |
| Effort | Occam's Razor (`occams-razor`) | Prefer the design with the fewest assumptions and elements. |
| Effort | Pareto Principle (`pareto-principle`) | ~80% of effects come from ~20% of causes; focus there. |
| Effort | Postel's Law (`postels-law`) | Be liberal in what you accept from users, strict in what you output. |
| Memory | Miller's Law (`millers-law`) | Working memory is small (about 7±2 items); not a limit on menu length. |
| Memory | Working Memory (`working-memory`) | Holds information briefly; don't make users recall across screens. |
| Memory | Chunking (`chunking`) | Group information into meaningful units. |
| Memory | Serial Position Effect (`serial-position-effect`) | First and last items are remembered best. |
| Attention | Von Restorff Effect (`von-restorff-effect`) | The item that differs is the one remembered. |
| Attention | Selective Attention (`selective-attention`) | Users filter out what seems irrelevant (banner blindness). |
| Attention | Flow (`flow`) | Balance challenge and skill; avoid interruptions. |
| Expectations | Jakob's Law (`jakobs-law`) | Users expect your product to work like the ones they already know. |
| Expectations | Mental Model (`mental-model`) | Match how users believe the system works. |
| Expectations | Paradox of the Active User (`paradox-of-the-active-user`) | Users skip manuals and start using the product right away. |
| Expectations | Aesthetic-Usability Effect (`aesthetic-usability-effect`) | Attractive design is perceived as more usable; it does not prove usability. |
| Targets & time | Fitts's Law (`fittss-law`) | Larger, closer targets are faster to acquire. |
| Targets & time | Doherty Threshold (`doherty-threshold`) | Responses under ~400 ms keep users engaged; a historical finding, not an app SLA. |
| Targets & time | Parkinson's Law (`parkinsons-law`) | A task expands to fill the time available; shorten it. |
| Motivation | Goal-Gradient Effect (`goal-gradient-effect`) | Effort increases as the goal gets closer. |
| Motivation | Zeigarnik Effect (`zeigarnik-effect`) | Unfinished tasks are remembered; show progress. |
| Motivation | Peak-End Rule (`peak-end-rule`) | Experiences are judged by their peak and their end. |
| Gestalt | Law of Prägnanz (`law-of-pragnanz`) | People read complex shapes in their simplest form. |
| Gestalt | Law of Proximity (`law-of-proximity`) | Nearby elements read as a group. |
| Gestalt | Law of Similarity (`law-of-similarity`) | Similar-looking elements read as related. |
| Gestalt | Law of Common Region (`law-of-common-region`) | Elements in a shared boundary read as a group. |
| Gestalt | Law of Uniform Connectedness (`law-of-uniform-connectedness`) | Visually connected elements read as related. |

## Laws by task

- **Forms and checkout:** choice-overload, hicks-law, teslers-law, cognitive-load, postels-law.
- **Navigation:** serial-position-effect, millers-law, chunking, mental-model.
- **Buttons and CTAs:** fittss-law, von-restorff-effect, selective-attention.
- **Loading and waiting:** doherty-threshold, parkinsons-law; also `performance.md`.
- **Onboarding:** paradox-of-the-active-user, 2024-onboarding-for-active-users, goal-gradient-effect.
- **Conventions vs innovation:** jakobs-law, mental-model, 2024-familiar-vs-novel.
- **Visual design:** aesthetic-usability-effect, law-of-pragnanz, law-of-proximity, law-of-similarity.

## The eight articles

| ID and file | Action for the agent | Check and limits |
|---|---|---|
| L01 (see sources.md) | Keep expected names, placement and behavior for frequent tasks. Propose a novel interaction when it improves the task or is the goal of the experience. | Compare how clear the first action is and whether people finish. Familiarity does not forbid novelty; expressiveness does not prove benefit. |
| L02 (see sources.md) | Let people start a useful action; explain complex parts in context and keep help reachable later. | Check that the first useful result needs no long tour. Keep mandatory training when the task or safety requires it. |
| L03 (see sources.md) | Remove repeated entry and manual matching by using reliable data and editable assumptions. | Check that autofill can be corrected. Do not hide essential complexity in opaque automation. |
| L04 (see sources.md) | Make search input and results match intent. Consider suggestions, grouping and visual relationships. | The example describes an earlier version of Google; do not copy it as a current spec. Do not make autofocus a universal rule. |
| L05 (see sources.md) | Work on tense moments and the ending: confirmation, status, next step, recovery. | Judge the whole journey. A pleasant ending does not excuse friction or an artificially longer process. |
| L06 (see sources.md) | Organize information into meaningful groups and use familiar mental models. Support the user's goal when the interface changes. | Do not cap menus at seven; assess discoverability. Psychology does not justify manipulating attention. |
| L07 (see sources.md) | Remove elements and steps with no established useful role. Choose the simpler of equivalent solutions. | Check clarity, comparability of options and access to features. Fewer visible elements do not always mean less effort. |
| L08 (see sources.md) | Remove needless memorization; label ambiguous icons; present compared options in a clear structure. | Check language, readability and completeness of the choice. Do not hide important alternatives just to reduce the object count. |

These are Jon Yablonski's practical interpretations, not eight new controlled studies. Judge the age of an example separately from how durable the principle is.

## Four laws: rules and misuse

### L09: Fitts

Make frequent targets easy to reach and tell apart. Check the real hit area, neighboring targets, touch input and position relative to the related content. Confirm sizes against platform and accessibility requirements (`accessibility.md`). Do not place "Delete" next to a frequent confirmation just to shorten the distance: the cost of a mistaken tap matters too. The last point is skill synthesis.

### L10: Hick

Cut unnecessary decisions at the moment of action. Group options and reveal advanced settings when needed. In a catalog where people know their target, good labels, filters and search can beat removing options. Assess how hard the options are to understand, the person's experience and the navigation depth; do not derive an allowed number of options from a slogan.

### L11, H02: Miller and memory

Reduce the need to remember things between screens: show the selected conditions and actions, group related data. Do not set a 7 ± 2 limit for menus, cards or columns. NN/g explains separately that a visible menu relies on recognition, so the memory limit cannot be turned mechanically into a menu limit.

### L12: Postel

Accept unambiguous input variants and help people fix the format. Separate convenient formatting from whether a value is valid. Do not strip meaningful characters from names, and do not guess ambiguous dates, currencies or identifiers. Do not use input tolerance to weaken server-side validation; define security rules separately. Check the context against DS01 (`interaction-patterns.md`).

## H01: heuristic inspection

Check whether: status is visible; the language matches the task; the person has control and a way out; patterns are consistent; errors are prevented; no needless memorization is required; repeated work is efficient; every detail is useful; errors can be understood and fixed; help is available. These are NN/g inspection directions, not a quality certificate and not ten equally weighted metrics. Show the concrete observation and the affected task.

## Information architecture: skill synthesis

Name the main objects and tasks in the audience's language. Separate navigation between objects from actions on the current object. Test labels with findability tasks; use tree testing or card sorting to study the structure when needed. Preserve orientation: section, filters, selected object, predictable return. Do not impose a click count on a task.

For expert tools, weigh the cost of repeated actions, shortcuts and the density of useful information. Do not split a familiar working form into many screens only because that helps novices in another product.

## Inspiration and good faith

Use **H03, Growth.Design** as a visual catalog of ideas and hypotheses. Its format resembles Laws of UX, but it does not confirm that each effect replicates. For a contested causal claim, find a study or test the hypothesis in the product.

Use **H04, Deceptive Patterns** to spot hidden terms, hard cancellation, misleading defaults, and fake urgency or social proof. Propose a transparent alternative with a clear price, consequences and choice. Do not make a legal assessment from one taxonomy.
