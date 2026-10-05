# Joining a project

- **Use it when:** you start on a project that already exists: a new job, a new team, a client's repo.
- **Not when:** you only need to understand some code → `/wow-repo-tour`.
- **Reads:** README, `CLAUDE.md`, the ADRs in `docs/adr/`, the runbook and postmortems in `docs/`, `HANDOFF.md` if the last person left one, the team's onboarding doc.
- **Writes:** `REPO-MAP.md` and `GLOSSARY.md` (through `/wow-repo-tour`), `CLAUDE.md` if it's missing, your list of questions.

## Steps
1. **Access:** repo, CI, cloud console (read-only first), logs and error tracker, ticket tracker, chat channels.
   - Skip it → you lose days waiting for access.
2. **People and process**, on one page:
   - who decides product, who reviews, who knows which part;
   - how work flows from ticket to PR to deploy.
3. **Run it locally**, following README. Every step that was missing or wrong gets fixed in your first PR.
   - Skip it → the next person loses the same day.
4. **The code** → `/wow-repo-tour`.
5. **The production picture:** dashboards, the top issues in the error tracker, the last postmortems, how often it ships.
   - Skip it → you don't know what hurts.
6. **A first small PR** in the first days: a README fix, a small bug, a missing test.
   - STOP: pick it together with your lead.
   - Skip it → you learn the review and deploy process on something big and risky.
7. **The "looks odd" list:** for the first month, write it down and ask why. Don't fix it yet; there may be a reason. Then propose 1–2 improvements, with evidence.

## Done when
- [ ] it runs locally, and your first PR reached production
- [ ] `REPO-MAP.md` exists
- [ ] you know who to ask about each area

## Frontend · Backend · Fullstack
- **Frontend:** the design system, the route list, how data is fetched and cached.
- **Backend:** the request pipeline, the data model, background jobs.
- **Fullstack:** where validation lives on each side, and how the contract and the types are shared.

## Concepts if you get stuck
- How a backend handles a request → [Backend 02 Anatomy of a backend](https://claude.ai/artifact/NpS3aqhk6FmDNkUNej6nP1)
- How a large frontend is organized → [F14 Frontend architecture at scale](https://claude.ai/artifact/Gur1WgSsBwhrSBQMNmHBNS)

## Next level
- `staff` Write the onboarding doc you wished you had.
- `staff` In the first month, meet the people on the teams next to yours.

## Next
`/wow-repo-tour` (inside), then `/wow-bug` or `/wow-feature` for the first PR. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
