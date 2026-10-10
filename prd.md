# PRD (product requirements)

- **Use it when:** you define what to build for a product, a version, or a big area, after the brief.
- **What you get:** the first version (MVP) with acceptance criteria for every feature, the success metrics, and non-functional numbers that don't contradict each other.
- **Run it:** `/wow-prd version 1 of the meal planner`
- **Not when:**
  - one feature → `/wow-feature`;
  - how to build it → `/wow-architecture`, `/wow-design-doc`.
- **Reads:** `docs/product/problem.md`, `docs/product/brief.md`, `docs/product/ideas.md`, the research.
- **Writes:** `docs/product/prd.md`, or `prd-<area>.md` for one area; `docs/product/ideas.md` sorted.

```markdown
# <Product or area> PRD
## Goal
## Success metrics: problem today | target | how I measure it
## User journeys: the 3–5 main flows, step by step
## MVP scope: the feature IDs from ideas.md
## Done when: per feature, checkable criteria
## Non-functional: speed, privacy, devices, languages, availability, backups, accessibility
## Out of scope: everything after the MVP in ideas.md
## Open decisions: what each blocks, who answers, by when
## Journal: dated decisions
```

## Steps
1. **Success metrics from the cost of the problem.** Each cost in `problem.md` becomes a target: "~30 minutes a day" → "a full day logged in under 5 minutes". Each target says how it's measured; targets measured in the app become events in `docs/tracking-plan.md`, each with its target and date (template in `experiment.md`).
   - Skip it → "done" means the code is written, not that the problem is solved.
2. **Sort the ideas.** Take every idea from `docs/product/ideas.md` (stable IDs, never renumbered): MVP first, ordered by what the others depend on, then what solves the problem, then the rest; after the MVP, High / Medium / Low. Check dependencies: a weight chart needs a weight log; a scanner needs a data source.
   - Skip it → everything is a must, or a must depends on something left for later.
3. **The checks no list of features makes on its own:**
   - **payment:** if the goal is revenue, is there a feature through which people pay?
   - **both sides:** every admin queue has the user action that fills it (admins see reported mistakes → users can report one), and the other way round;
   - **AI cost:** for every AI feature, the cost per call and a budget per user (around 10–20% of the price), with what happens when it runs out.
   - Skip it → an MVP nobody can pay for, or an AI feature that loses money on heavy users.
4. **Journeys:** the main flows from the user's side, step by step. Each step later becomes screens (`/wow-ui-design`).
5. **Done when, per feature:** criteria you can tick yes or no ("I can reset my password from the email", not "the account works well"). Use given / when / then only where the flow is complex. Write data rules where they matter:
   - a missing value is not zero (an unknown nutrient, a day not logged);
   - store raw data, calculate what derives from it (a grade, a total);
   - when an item changes, past records keep their values (snapshot).
6. **Non-functional, with numbers:** speed (0.1 s feels instant, 1 s keeps the flow, 10 s is the limit), personal and health data (consent, hosting region, export, deletion), devices, languages, availability, backups (RPO, RTO), accessibility (WCAG level, tap targets). Third-party providers appear as requirements (region, DPA, no training on our data), never by name; the name is decided in an ADR.
   - Check that the numbers agree: an RTO of 4 h doesn't fit in 99.5% availability (3.6 h per month).
7. **Out of scope:** everything after the MVP, by reference to `ideas.md`.
   - Skip it → the scope grows quietly.
8. **Review.**
   - STOP: design and engineering read it. Their questions are answered, or listed as open with an owner.
9. **Ready to build:** the PRD, the UI design, the architecture and the plan agree; every MVP feature has criteria; every open decision has an owner. The ones that are the user's are asked now, with a recommendation, not left in the file.
   - STOP: confirm before the first `/wow-feature`.
   - Skip it → the build stops halfway on a question nobody owned.

## Done when
- [ ] success metrics come from the cost of the problem
- [ ] ideas are sorted, dependencies checked
- [ ] payment, both sides and AI cost are checked
- [ ] the journeys are written
- [ ] every MVP feature has checkable criteria
- [ ] the non-functional numbers are set and agree with each other
- [ ] out of scope is written
- [ ] the ready-to-build check passed

## Concepts if you get stuck
- MVP: the smallest version that solves the problem
- Acceptance criteria
- User journeys
- Unit economics
- RPO and RTO

## Next
`/wow-ui-design`, `/wow-architecture`, `/wow-roadmap`, `/wow-plan`. End with `/wow-retro`.

## Changelog
- 2026-10-10: v3. Success metrics from the cost of the problem; ideas sorted with stable IDs and dependencies; checks for payment, both sides and AI cost; criteria you tick yes or no; data rules (missing ≠ zero, store raw, snapshots); providers as requirements; non-functional numbers that agree. From the MacroMate rebuild: the MVP had no payment feature until the AI-cost discussion, admins had a reported-mistakes list with no report button, and an RTO of 4 h broke a 99.5% availability target.
- 2026-10-07: v2. Open questions carry what they block and by when; the user's blocking ones are asked on the spot. The number becomes events with targets. A dated journal closes the file. From the ProjectX MVP PRD.
- 2026-10-06: v1
