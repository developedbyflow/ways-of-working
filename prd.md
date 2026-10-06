# PRD (product requirements)

- **Use it when:** you define what to build for a product, a version, or a big area, after the brief.
- **What you get:** requirements with acceptance criteria, and a first version small enough to ship.
- **Run it:** `/wow-prd version 1 of the meal planner`
- **Not when:**
  - one feature → `/wow-feature`;
  - how to build it → `/wow-architecture`, `/wow-design-doc`.
- **Reads:** `docs/product/brief.md`, `docs/opportunities.md`, the research, the design system.
- **Writes:** `docs/product/prd.md`, or `prd-<area>.md` for one area.

```markdown
# <Product or area> PRD
Status · Owner · Date
## Goal and the number
## Users and their main jobs
## User journeys: the 3–5 main flows, step by step
## Requirements: must / should / later, each with acceptance criteria
## Non-functional: speed, availability, privacy, accessibility, languages
## Out of scope
## The first version
## Open questions
```

## Steps
1. **Start from the brief:** the goal, the number, the users.
   - Skip it → requirements that serve nobody in particular.
2. **Journeys:** the main flows from the user's side, step by step. Each step later becomes screens (`/wow-ui-design`).
3. **Requirements:** what the user can do, not how it's built.
   - each one has acceptance criteria: given / when / then;
   - each one is ranked must, should or later.
   - Skip it → everything is a "must".
4. **Non-functional, with numbers:** page load, uptime, how long data is kept, the WCAG level, the languages.
5. **Out of scope**, written down.
   - Skip it → the scope grows quietly.
6. **The first version:** the smallest set of musts that reaches the goal for the first users. Not a smaller copy of everything.
7. **Review.**
   - STOP: design and engineering read it. Their questions are answered, or listed as open with an owner.
8. **Ready to build:** the PRD, the UI design, the architecture and the plan agree; every must has criteria; every open question has an owner.
   - STOP: confirm before the first `/wow-feature`.
   - Skip it → the build stops halfway on a question nobody owned.

## Done when
- [ ] the journeys are written
- [ ] the requirements are ranked, each with acceptance criteria
- [ ] the non-functional numbers are set
- [ ] out of scope and the first version are written
- [ ] the ready-to-build check passed

## Concepts if you get stuck
- Requirements and trade-offs
- User journeys
- MVP: the smallest version that reaches the goal

## Next
`/wow-ui-design`, `/wow-architecture`, `/wow-roadmap`, `/wow-plan`. End with `/wow-retro`.

## Changelog
- 2026-10-06: v1
