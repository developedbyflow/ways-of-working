# Accessibility audit

- **Bar:** WCAG 2.2 level AA. In the EU, the European Accessibility Act has applied to many consumer services, e-commerce included, since 28 June 2025.
- **Tools:**
  - axe DevTools;
  - axe in the tests (`jest-axe`, `@axe-core/playwright`);
  - Lighthouse accessibility.

Automated tools find only part of the problems. The manual checks are required.

## Manual checks
- [ ] **Keyboard only:**
  - everything can be reached;
  - focus is visible and moves in a logical order;
  - no focus traps;
  - Esc closes dialogs, and focus returns to where it was.
- [ ] **Screen reader** (VoiceOver on a Mac, NVDA on Windows): the page title, headings, landmarks, labels and button names make sense; errors and status messages are announced.
- [ ] **Zoom:** usable at 200%, and readable at 320 CSS px wide without scrolling sideways.
- [ ] **Contrast:** 4.5:1 for normal text; 3:1 for large text and for UI parts like borders and icons.
- [ ] **Forms:** every field has a label; errors are linked to their field and don't rely on color alone; long forms have an error summary.
- [ ] **Images:** meaningful alt text; empty alt for decoration.
- [ ] **Motion:** respects `prefers-reduced-motion`.
- [ ] **Target size:** at least 24 × 24 CSS px.
- [ ] **Route changes** in a single-page app move the focus and update the title.

## Concepts
- Accessibility → F04 Accessibility
- Accessible components → F15 Design system
- Forms and states → F21 UX for developers

## Changelog
- 2026-10-05: v1
