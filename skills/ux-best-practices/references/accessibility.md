# Accessibility and Inclusive UX

Sources verified 2026-10-21. Apply this section to web interfaces; for native apps, also check platform guidelines. Do not substitute iOS pt or Android dp for CSS px.

## Contents

- [Basis and limits](#basis-and-limits)
- [Controls and focus](#controls-and-focus)
- [Zoom and contrast](#zoom-and-contrast)
- [Forms and cognitive accessibility](#forms-and-cognitive-accessibility)
- [Verification and reporting results](#verification-and-reporting-results)

## Basis and limits

Use **WCAG 2.2 AA** as this skill's baseline target unless the project sets another. Do not treat this setting as a legal requirement. AA includes the applicable A and AA requirements. Apply AAA only as an explicitly labelled improvement or when the project requires it. This section is a selection of common UX checks, not a full audit or a conformance certification.

### A01. Normative basis

Source: W3C, [WCAG 2.2](https://www.w3.org/TR/WCAG22/); Recommendation of **2024-12-12**. Verified 2026-10-21. Normative standard.

- Check keyboard operation and the ability to leave components: **2.1.1 and 2.1.2, A**. The 2.1.1 exception covers a function that essentially depends on the path of movement, not merely a chosen input implementation.
- For dragging, provide a single-pointer action without dragging: **2.5.7, AA**. Exceptions: essential dragging, or unmodified browser behavior. A keyboard alternative alone does not satisfy this criterion.
- Auto-fill or let the user select information already entered earlier in the same process: **3.3.7, A**. Allow for the exceptions for necessity, security and information that is no longer valid.
- Also check text alternatives (**1.1.1, A**), structure and relationships (**1.3.1, A**), conveying meaning by more than color (**1.4.1, A**), visible focus (**2.4.7, AA**), accessible name/role/value (**4.1.2, A**) and status announcements without moving focus (**4.1.3, AA**).

### A02. Status of WCAG 3

Source: W3C WAI, [WCAG 3 Introduction](https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/); updated **2026-09-25**. Verified 2026-10-21. Official explanation of the status.

WCAG 3 remains an unfinished draft; do not use it as a conformance standard. Apply WCAG 2.2. Check the official status before changing versions.

## Controls and focus

### A03. Semantics and ARIA

Source: W3C WAI, [APG Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/); publication date not established; the guide describes ARIA 1.2. Verified 2026-10-21. Non-normative guidance.

Prefer the appropriate native element. For a custom control, implement keyboard handling, name, states and behavior separately: `role="button"` does not add key handling. Check semantics in the accessibility tree and check interaction in the target browsers and screen readers. An APG example does not guarantee support for every combination of browser, touch and assistive technology.

### A04. Target size

Source: W3C WAI, [Understanding 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html); WCAG 2.2, publication date not established. Verified 2026-10-21. Explanation of an **AA** criterion.

Check a hit area of **24 × 24 CSS px** or an applicable exception. For the spacing exception, a circle of 24 CSS px diameter centered on the bounding box of a small target must not intersect another target or the similar circle of another small target. This is not a requirement for a 24 px gap. The other exceptions: equivalent control, inline target, unmodified browser control, essential presentation. **44 × 44 CSS px** is the enhanced criterion **2.5.5 AAA**, with its own exceptions [A01]. Use larger targets as the context requires, without declaring them mandatory for AA.

### A05. Focus under overlapping elements

Source: W3C WAI, [Understanding 2.4.11](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html); WCAG 2.2, publication date not established. Verified 2026-10-21. Explanation of an **AA** criterion.

Walk the page with the keyboard while banners and sticky panels are open: a focused control must not be entirely hidden by author-created content. Full visibility is the preferred improvement and **2.4.12 AAA**. Check separately that the focus indicator is visible: a visible fragment of the control does not prove it. For user-initiated repositioning, evaluate the original position. For content the user has expanded, consider whether the focused control can be revealed without moving focus.

### A12. Modal dialog

Source: W3C WAI, [APG Dialog (Modal)](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/); publication date not established. Verified 2026-10-21. Recommended pattern.

On open, move focus inside, keep Tab/Shift+Tab within the dialog, support Escape and provide a visible close control. On close, return focus to the invoking element or to a logical next step. Provide an accessible name. Use `aria-modal` only when the background is actually inert. Choose the initial focus by content: the heading may suit long text; the least destructive button may suit a hard-to-reverse action. Do not automatically send focus to the first button without assessing the scenario.

## Zoom and contrast

### A06. Reflow

Source: W3C WAI, [Understanding 1.4.10](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html); WCAG 2.2, publication date not established. Verified 2026-10-21. Explanation of an **AA** criterion.

Check that information and functions are preserved without two-direction scrolling at a width of **320 CSS px** for vertical reading, and at a height of **256 CSS px** for horizontal reading. An equivalent check, for example: a 1280 CSS px viewport at 400% zoom. Exceptions for necessarily two-dimensional regions, such as maps and tables, do not exempt the surrounding page or the content of individual cells. Check that actions and navigation survive reflow: having a mobile layout does not by itself confirm the criterion is met.

### A07. Text contrast

Source: W3C WAI, [Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html); WCAG 2.2, publication date not established. Verified 2026-10-21. Explanation of an **AA** criterion.

Check a minimum of **4.5:1** for regular text and **3:1** for large text. Large text: **18 CSS pt** or larger, or **14 CSS pt bold**; that is 24 CSS px and about 18.67 CSS px respectively. Do not round borderline ratios up. Placeholder text also needs contrast. Allow for the exceptions for logos, decorative or incidental text and inactive controls. Take colors from the actual styles; screenshot antialiasing does not give a reliable contrast value.

### A08. Contrast of meaningful graphics

Source: W3C WAI, [Understanding 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html); WCAG 2.2, publication date not established. Verified 2026-10-21. Explanation of an **AA** criterion.

Check **3:1 against adjacent colors** for information required to identify an active control, its state, and meaningful graphics. This is not a requirement for contrast between two states that are not adjacent. Do not add a mandatory border: sufficiently contrasting text or an icon can identify a button. Allow for the exceptions for inactive and unmodified browser controls, and for essential presentation of graphics.

## Forms and cognitive accessibility

### A09. Forms

Source: W3C WAI, [Forms Tutorial](https://www.w3.org/WAI/tutorials/forms/); updated **2026-03-27**. Verified 2026-10-21. Practical guidance combining requirements of different levels.

Ask for the necessary information; associate fields with labels and groups with fieldset/legend. Give instructions, success and error notifications, and a way to correct. Split a long form into logical steps with progress when that helps the task. Avoid time limits; where needed, provide time controls, allowing for the exceptions provided.

### A10. Cognitive accessibility

Source: W3C, [Making Content Usable for People with Cognitive and Learning Disabilities](https://www.w3.org/TR/coga-usable/); Working Group Note **2021-04-29**. Verified 2026-10-21. Supplementary non-normative guidance.

Use familiar patterns, plain words, headings and short instructions. Preserve context; support error correction and getting help. Reduce the process's reliance on memory. Include people with cognitive differences in research and usability testing. Do not present these recommendations as mandatory WCAG criteria.

### A11. Authentication

Source: W3C WAI, [Understanding 3.3.8](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html); WCAG 2.2, publication date not established. Verified 2026-10-21. Explanation of an **AA** criterion.

Support password managers, autofill and paste. Do not make a cognitive test the only route without an acceptable alternative or help. Check sign-in, MFA and recovery. AA allows object recognition and personal non-text content; the enhanced **3.3.9 AAA** does not include these two exceptions. Do not present a permitted exception as preferred UX. The criterion concerns an existing user; offering the same conveniences at registration is a separate recommendation.

## Verification and reporting results

Use the following statuses as this skill's working procedure:

- **Confirmed:** state the observation, the method of verification and the affected scenario.
- **Likely risk:** describe the visual sign and what still needs to be checked.
- **Not verified:** list the unavailable data; do not turn the absence of errors in an image into a successful check.

From a screenshot, assess hierarchy, states and likely problems. Exact sizes and colors need measurements; semantics need the DOM or accessibility tree; focus, keyboard, reflow and screen reader behavior need interactive checks. State the states checked and the limitations. Do not derive a conformance percentage from this selection of rules.
