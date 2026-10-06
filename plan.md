# Plan

- **Use it when:** before committing to work, for:
  - **one feature:** the slices and a time range;
  - **an initiative of several weeks:** milestones, decisions, risks.
- **What you get:** slices that ship one by one, a time range people believe, and the risks named early.
- **Run it:** `/wow-plan the shopping list feature`
- **Not when:** you're deciding how to build it → `/wow-design-doc` or `/wow-grill`.
- **Reads:** the ticket or the design doc, `docs/risks.md`, `docs/tech-debt.md` (debt that slows this work), past estimates and actuals (the tickets, the impact log).
- **Writes:**
  - the slices as tickets, each with what blocks it and its estimate;
  - `docs/risks.md`;
  - the status updates, through `/wow-comms`.

## One feature
1. **Slices:** thin pieces that each work end to end and can ship alone, behind a flag. Each slice names what blocks it.
   - Skip it → a three-week branch that merges at the very end.
2. **A range for each slice:** best, likely and worst case, with the assumptions written down. When the uncertainty is large, do a spike instead of padding the number.
   - Skip it → a single date nobody believes.
3. **Risks:** what could make it late → `docs/risks.md`, with an owner.
4. **Agree.**
   - STOP: agree on the order and the range with whoever asked.

## Initiative (several weeks)
1. **The goal**, and the number that tells you it's done.
2. **Milestones:** each one delivers something usable. The riskiest one comes first.
3. **Open decisions**, in the order they block each other. Each gets a `/wow-grill`.
4. **A weekly status** → `/wow-comms`: progress, risks, next, asks.
5. **Re-plan when reality changes.** Say it early, with options: cut scope, move the date, add people.
   - Skip it → the delay is announced on the deadline.

## Done when
- [ ] the slices are tickets, each with a range and its blockers
- [ ] every risk has an owner
- [ ] initiative: the milestones and the weekly status are set

## Concepts if you get stuck
- Prioritizing, RICE, cost of delay
- Trade-offs
- Leading initiatives

## Next level
- Compare estimates with actuals every month (at the weekly `/wow-retro`) and adjust how you estimate.
- `staff` A technical strategy: where the system should be in a year, and the initiatives that get it there.

## Next
`/wow-feature` for each slice; `/wow-comms`. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
