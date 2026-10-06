# Design system

- **Use it when:** a component or tokens that many screens reuse: new, changed, or removed.
- **What you get:** a shared component that is accessible, documented and safe to change.
- **Run it:** `/wow-design-system a Combobox component`
- **Not when:** a single screen → `/wow-ui-design`.
- **Reads:** the design (Figma or a sketch), the existing components, the tokens.
- **Writes:** the component (code, tests, stories), the tokens, the design system changelog.

## Steps
1. **Is it shared?** It's used in three places, or soon will be. Otherwise, keep it next to the screen that uses it.
   - Skip it → a design system full of components nobody reuses.
2. **The API:**
   - props named after what they mean, not how they look (`variant="danger"`, not `color="red"`);
   - clear rules for controlled and uncontrolled use;
   - composition (`children`, slots) instead of many boolean props.
   - Skip it → 25 props, and every screen uses a different combination.
3. **States and variants:** hover, focus, active, disabled, loading, error, sizes, and dark mode through tokens.
4. **Accessible by default:**
   - the right element (`button`, not a clickable `div`);
   - keyboard support and a visible focus;
   - ARIA only where HTML can't do it. Complex widgets (dialog, combobox, tabs) follow the WAI-ARIA Authoring Practices pattern.
5. **Tokens, not values:** color, spacing, type and radius come from tokens. No hard-coded values.
6. **Docs and tests:** one story per state, a test for behavior and keyboard use, an axe check.
   - STOP: one team that will use it reviews the API before merge.
7. **Release:**
   - follow semver: a breaking change is a major version;
   - before removing anything, deprecate it with a warning, a migration note and a date;
   - provide a codemod when there are many usages.
   - Skip it → an update silently breaks screens you don't own.

## Done when
- [ ] a story for every state
- [ ] the keyboard test passes and axe is clean
- [ ] a changelog entry

## Concepts if you get stuck
- Tokens, component API, versioning, governance
- Accessible components
- Components and hooks
- CSS

## Next level
- Adoption: move the screens to the component, and count how many have moved.
- `staff` A contribution model: owners, review, and who can add a component.

## Next
`/wow-ui-design`, `/wow-pr`. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
