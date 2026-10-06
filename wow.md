# What is in front of me (wow)

- **Use it when:** you're not sure which page fits, or you have a list of incoming things: bug reports, requests, alerts, user feedback.
- **What you get:** the right skill after one or two questions, or a sorted list when many things come in at once.
- **Run it:** `/wow users say the plan isn't saved after refresh`
- **Not when:** you already know the situation. Run that skill directly.
- **Reads:** README.md, the "Which one, when two look alike" table in ECOSYSTEM.md, FLOWS.md.
- **Writes:** nothing for one item; for a list, the sorted list with a skill and an owner per item.

## One item
1. **Say it in your own words.**
2. **At most two questions**, only the ones that separate two skills. Example: "Are users affected right now?" separates incident from bug.
   - Skip it → you start the wrong flow, for example debugging while users are down instead of rolling back.
3. **The skill and why**, in one sentence. If the item starts a longer journey (a new idea, a live product to improve), show the matching flow from FLOWS.md, so the user sees what comes after.
   - STOP: you confirm, then the skill starts.

## A list (triage)
1. **Merge duplicates.**
   - Skip it → the same problem gets fixed twice, by two people.
2. **One line per item:** what it is (bug, request, question, incident).
3. **Severity**, for bugs:
   - critical: data loss, security, or the main flow is unusable;
   - high: the main flow is broken for some users;
   - medium: there is a workaround;
   - low: cosmetic.
4. **Priority:** severity, how many users are hit, and what waiting costs. For product requests, use RICE.
   - Skip it → the loudest item wins, not the most important one.
5. **A skill and an owner per item**, or "won't do" with the reason, told to whoever asked.
   - STOP: you approve the order.

## Done when
- [ ] every item has a skill and an owner, or a written "won't do"

## Concepts if you get stuck
- Prioritizing requests, RICE, cost of delay
- How bad an outage is

## Next level
- `staff` A triage rotation and a response time per severity for the team.

## Next
The skill you chose. Its retro covers this step.

## Changelog
- 2026-10-05: v1
