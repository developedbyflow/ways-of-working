# Design doc

- **Use it when:** a large feature (see the size table in `feature.md`), a change across several parts or teams, or anything that's hard to undo.
- **Not when:** the decision is small → `/wow-grill` and an ADR are enough.
- **Reads:** the grill output, the research, the spikes, the architecture.
- **Writes:** `docs/design/YYYY-MM-title.md`, the big choices as ADRs in `docs/adr/`, `docs/risks.md`.

```markdown
# Title
Status · Author · Reviewers · Date
## Context and problem (with the number)
## Goals / Non-goals
## Design: diagram, data, API contract, how it fails
## Alternatives considered, and why not
## Security and privacy: what we protect, what can go wrong, how we prevent it
## Rollout and rollback: flag, migration steps, how to undo
## Milestones and open questions
```

## Steps
1. **Grill first** → `/wow-grill`. The doc records decisions; the thinking happens before and while you write.
2. **Write it in 1–2 pages**, using the template. Prefer diagrams to paragraphs.
   - Skip the non-goals → the scope grows.
   - Skip the alternatives → reviewers propose them again in the meeting.
3. **Security and rollback are never empty.** If you write "none", say why.
4. **Review:**
   - 1–3 people who will be affected; comments go in the doc;
   - talk to the key people one-to-one beforehand;
   - a meeting only for the disagreements.
   - STOP: no open blocker before coding starts.
5. **Decide and record:** the decision and the date at the top. The big choices become ADRs.
6. **Keep it true:** if building changes the design, update the doc or mark the old part as outdated.
   - Skip it → the next person trusts a doc that lies.

## Done when
- [ ] reviewers have no open blockers
- [ ] the non-goals, alternatives, security and rollback sections are written

## Concepts if you get stuck
- Design in the real world → S17 Design in the Real World
- Staff work: docs, reviews, alignment → S19 Staff and Beyond
- Frontend system design → F18 Frontend system design
- System design → Backend 15 System design
- Leading technical decisions → F17 Technical leadership in frontend

## Next level
- `staff` An RFC process for the team, with a review checklist.

## Next
`/wow-plan`, `/wow-feature`, `/wow-comms`. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
