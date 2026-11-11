# Interaction Patterns

All sources listed here were verified on **2026-10-21**. The dates below refer to explicitly stated updates; where no date is given, do not substitute the verification date. Treat design-system recommendations as contextual patterns. Do not call them WCAG requirements without a separate reference to a normative criterion.

## Contents

- [Forms and data validation](#forms-and-data-validation)
- [Errors and recovery](#errors-and-recovery)
- [Interface states](#interface-states)
- [Modal dialogs](#modal-dialogs)
- [Tables and bulk actions](#tables-and-bulk-actions)
- [Responsiveness and units](#responsiveness-and-units)
- [Microcopy and messages](#microcopy-and-messages)

## Forms and data validation

**Action.** For a guided flow, start with one main question or one related task per step. Make the question a clear heading associated with a `label` or `legend`. First shorten and order the questions, then decide whether a progress indicator is needed.

**Check.** Walk through the form without the author's explanations. Check whether the required information, the current step and the next outcome are clear. With conditional branches, check that the overall length of the process is credible.

**Context.** This is a starting point for transactional services. Frequent expert work may need several fields on one screen; test this on a typical task.

Source: [DS03 — GOV.UK Question pages](https://design-system.service.gov.uk/patterns/question-pages/); no update date given.

**Action.** Accept unambiguous valid input variants. In the GOV.UK flow, validate by default on Continue/Submit; do not declare unfinished input an error. Keep values after an unsuccessful submission. Run server-side validation independently of client-side validation.

**Check.** Try slow typing, pasting, permitted separators and correcting an erroneous value. Make sure the person does not re-enter the other answers.

**Context.** Add earlier feedback where it has a justified benefit, for example for a length limit. Do not turn this pattern into a universal ban on validation on leaving a field.

Source: [DS01 — GOV.UK Recover from validation errors](https://design-system.service.gov.uk/patterns/validation/); no update date given.

**Action.** Before a significant final submission, let the person review the answers and change an individual section. Name the button after the result of the submission.

**Check.** Change an early answer and return to the review: the values must be preserved, and the person must not have to redo unrelated steps.

**Context.** In a large process, check whether intermediate review screens are useful; do not add a separate confirmation to every ordinary edit.

Source: [DS04 — GOV.UK Check answers](https://design-system.service.gov.uk/patterns/check-answers/); no update date given.

## Errors and recovery

**Action.** For an unsuccessful form submission, use messages next to the fields and a related summary. In the GOV.UK pattern, move focus to the summary; make its items links to the corresponding answers, with the same error text.

**Check.** Submit a form with several errors using only the keyboard. Check that the summary is announced, that links move to the fields, and that the remaining problems are discoverable after one is fixed.

**Context.** A summary even for a single error is a GOV.UK convention. Do not present it as a standalone WCAG requirement for every interface.

Source: [DS02 — GOV.UK Error summary](https://design-system.service.gov.uk/components/error-summary/); component changes: June 2026, Frontend v6.2.0; focus clarification: February 2025.

**Action.** Describe what went wrong, the consequences and the available fix. If the cause is unknown, say honestly that something failed and suggest a next step.

**Check.** From a single message it must be clear what action is possible now. Remove any invented cause, blaming of the user and irrelevant technical detail.

**Context.** Distinguish an input error, a refusal under service rules, missing permissions and a service malfunction; do not suggest fixing a field when the problem lies outside it.

Sources: [DS14 — Atlassian Error messages](https://atlassian.design/foundations/content/designing-messages/error-messages), [DS01 — GOV.UK Validation](https://design-system.service.gov.uk/patterns/validation/); no update dates given.

## Interface states

**Action.** Distinguish first launch with no data, no search results, a completed clear-out, restricted permissions and a system failure. For an empty state, explain the reason and a useful next step.

**Check.** Open each applicable variant separately. Check that the UI does not offer to create data instead of fixing a filter, or to request access instead of retrying the load.

**Context.** An illustration is optional; a decorative image must not carry the only explanation of the situation.

Source: [DS07 — Carbon Empty states](https://www.carbondesignsystem.com/building-blocks/core/patterns/empty-states); updated 2026-08-11.

**Action.** Show loading at the scale of the area it occupies. Use a skeleton for an expected content structure and a local indicator for a single action. Make a long wait informative.

**Check.** Slow down the service response. Make sure it is visible which operation is running and that independent areas remain clear.

**Context.** Do not turn buttons, menus, toasts or the dialog shell themselves into a skeleton. Do not show an invented completion percentage.

Source: [DS08 — Carbon Loading](https://www.carbondesignsystem.com/building-blocks/core/patterns/loading); updated 2026-08-11. The rule on credible progress is a practical skill synthesis.

For network and distributed scenarios, additionally use the following **skill-synthesis check**, without attributing it verbatim to Carbon:

| State | Action | Check and context |
|---|---|---|
| Offline | Explain the limitation; keep a draft if the product provides for it | Disconnect the network; check recovery without a false success message |
| Stale | Show how current the data is and how to refresh it | Change the data outside the current screen; check that the user's in-progress edit is not lost |
| Partial | Separate the available result from the part that failed | Fail one block; check a local retry |
| Unknown submission result | First find out the state of the operation | Test a dropped response after submission; do not suggest unconditionally retrying an irreversible action |

## Modal dialogs

**Action.** Justify the need for a separate decision. For an ordinary field error, use local feedback; move a complex multi-step process to a suitable screen. Make the heading and actions unambiguous.

**Check.** Check opening, initial focus, Tab/Shift+Tab, accessible closing, focus return and restoring accessibility of the page behind the dialog.

**Context.** Keeping focus inside an open modal must come with an accessible exit. If the originating element has disappeared, choose a logical point to continue from. A library component's accessibility status does not confirm that the integration is correct.

Sources: [DS05 — USWDS Modal](https://designsystem.digital.gov/components/modal/); changes 2026-08-18, v3.14.0. [DS06 — Modal accessibility tests](https://designsystem.digital.gov/components/modal/accessibility-tests/); page added 2025-02-14, the tests cited are marked v3.8.2.

## Tables and bulk actions

**Action.** Separate actions on the whole table, on selected rows and on a single record. Indicate sorting and bulk-selection mode; provide a clear way out of it. Reveal additional information as needed.

**Check.** Select several rows, change the sort order, and use the keyboard and touch. Check that actions are discoverable and that their scope is unambiguous. If there is pagination, explicitly check what "select all" means.

**Context.** Do not hide critical actions in hover alone. Choose density to suit the task and input; Carbon row sizes are not universal minimums. The check of selection across pages is skill synthesis.

Source: [DS09 — Carbon Data table](https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines); updated 2026-09-30, Stable.

## Responsiveness and units

**Action.** Change the composition according to the available window and text scale. Preserve the selected object and the task state. For large windows, consider related panels; adapt the primary navigation to the available space.

**Check.** Resize the window, change orientation and text size during a task. Check that work can continue and that keyboard control works alongside touch.

**Context.** Bottom navigation in a compact window and a side rail in a large one are Android/Material templates, not a required structure for a mobile website.

Sources: [DS10 — Android Adaptive apps](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps), updated 2026-10-08; [DS11 — Adaptive navigation](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation), updated 2026-09-22.

**Action.** For Apple touch controls, use the recommended hit area of at least **44 × 44 pt**. Always give the unit with the number.

**Check.** Measure the actual interactive area, not the size of the icon.

**Context.** Apple `pt`, Android `dp` and web `CSS px` are not interchangeable. Check web accessibility requirements separately; do not use numeric M3 recommendations from search snippets.

Source: [DS12 — Apple UI Design Dos and Don’ts](https://developer.apple.com/design/tips/); no update date given.

## Microcopy and messages

**Action.** Distinguish information, success, a warning about a future risk and an error that has already occurred. Place the message at the level of the affected area. Name the button after the action and its result.

**Check.** Read the heading, the message and the button separately. Make sure they are clear without color, do not contradict each other, and do not require guessing what "OK" means.

**Context.** Do not escalate every notification to a system banner. Adapt brand limits on word count and politeness forms to the language, the situation and the product.

Sources: [DS13 — Atlassian Designing messages](https://atlassian.design/foundations/content/designing-messages/), [DS14 — Error messages](https://atlassian.design/foundations/content/designing-messages/error-messages); no update dates given. The check of a message without color is skill synthesis, to be supplemented by a normative accessibility check.
