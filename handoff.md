# Leaving a project (handoff)

- **Use it when:** you leave a project, or hand an area to someone else: a new job, a move to another team, a long absence.
- **What you get:** a project the next person can run, deploy and roll back without you.
- **Run it:** `/wow-handoff the payments service`
- **Not when:** you're the one arriving → `/wow-join`.
- **Reads:** `REPO-MAP.md`, `docs/adr/`, `docs/risks.md`, `docs/tech-debt.md`, the runbook, `docs/postmortems/`, `docs/audits/`, open tickets and PRs.
- **Writes:** `HANDOFF.md`, an updated `REPO-MAP.md` (through `/wow-repo-tour`), the list of access transfers.

```markdown
# Handoff: <project or area> · <date>
## State: what works, what's in progress (links), what's broken
## Decisions: the ADRs that matter most, and the decisions still open
## Risks and debt: the top 5, and what to do about each
## Run, deploy, roll back: links to README and the runbook
## Access: accounts, keys, domains, billing, and who owns each one now
## People: who knows what, who to ask
## The first two weeks: what I would do first if I stayed
```

## Steps
1. **Start early:** at least two weeks before you leave.
   - Skip it → the handoff is a rushed call on your last day.
2. **Update `REPO-MAP.md`** (`/wow-repo-tour`) and the runbook.
3. **Write `HANDOFF.md`** using the template.
4. **Transfer access:** domains, billing, cloud, repos and secrets go to a named person. Rotate the secrets you knew.
   - STOP: confirm each transfer.
   - Skip it → a domain expires on your card, or a key only you had stops working.
5. **Walkthrough:** the next person runs, deploys and rolls back while you watch.
   - STOP: they did it without your hands on the keyboard.
6. **Remove your own access.**

## Done when
- [ ] the next person deployed and rolled back alone
- [ ] every access has a new owner
- [ ] `HANDOFF.md` exists

## Concepts if you get stuck
- Runbooks, environments, access

## Next level
- `staff` A "bus factor" check: every critical area has two people who can run it.

## Next
`/wow-retro`: add the project to your impact log.

## Changelog
- 2026-10-05: v1
