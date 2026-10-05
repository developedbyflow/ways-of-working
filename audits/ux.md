# UX audit

- **Bar:**
  - Nielsen's 10 usability heuristics;
  - a new user completes the main flows without help.
- **Tools:**
  - walk the main flows as a new user;
  - the funnel in analytics, to see where users drop off;
  - session recordings, with consent, if you have them;
  - a five-user test.

## Checklist
- [ ] **States:** every screen has empty, loading, error and success states.
- [ ] **Errors:** say what happened and how to fix it, next to the field, and keep what the user typed.
- [ ] **Forms:** only the fields you need, the right input types, validation when the user leaves a field.
- [ ] **Destructive actions** offer undo instead of "Are you sure?" where possible.
- [ ] **Response time:**
  - under 0.1 s feels instant;
  - over 1 s, show progress;
  - over 10 s, let the user do something else meanwhile.
- [ ] **Consistency:** the same words and the same components for the same things.
- [ ] **Small screens:** tap targets, thumb reach, no action that needs hover.
- [ ] **Speed users can feel:** skeletons for content; optimistic updates when the action can be undone.

## Language and formats
- [ ] Dates, numbers and currency are formatted for the user's language and region (`Intl`). Time zones are explicit.
- [ ] No hard-coded text; plurals handled; room for longer translations.
- [ ] CSS uses logical properties (`margin-inline-start`), so a right-to-left language would work.

## Concepts
- UX for developers → F21 UX for developers
- The product-minded engineer → F23 The product-minded engineer
- Accessibility → F04 Accessibility

## Changelog
- 2026-10-05: v1
