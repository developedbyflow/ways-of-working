# Incident

- **Use it when:**
  - production is broken or slow for users, right now;
  - a security event: a leaked secret, suspicious access, exposed data.
- **What you get:** the damage stopped first, people kept informed, and a postmortem so it doesn't happen again.
- **Run it:** `/wow-incident checkout returns 500`
- **Not when:** a bug that has a workaround and blocks nobody → `/wow-bug`.
- **Reads:** `docs/runbook.md`, dashboards, logs, recent deploys.
- **Writes:** the incident notes with a timeline, the status updates (`/wow-comms`), `docs/postmortems/YYYY-MM-DD-title.md`, the actions, `docs/risks.md`.

## Steps
1. **Declare it, and lead it:** say it in the channel; one person leads (when you're alone, that's you); note the start time.
   - Skip it → two people fix the same thing, or nobody does.
2. **Stop the damage first:** roll back the last deploy, turn off the flag, scale up, block the bad input. Understanding comes after.
   - STOP: choose how you stop the damage.
   - Skip it → users suffer while you debug.
3. **Communicate** → `/wow-comms`, incident format: who is affected, what you know, and when the next update comes. Keep the timeline as you go.
4. **Confirm the recovery** with the numbers, not by feel.
5. **Fix the cause** with `/wow-bug`, once things are stable.
6. **Postmortem, within a few days, without blame.**
   - Skip it → it happens again.

## Security incident: also
- **Contain it:** revoke and rotate the leaked secret, block the access, keep the logs as evidence.
- **Check what was accessed.**
- **Personal data exposed?** Under GDPR the company must notify the supervisory authority within 72 hours of finding out, unless the risk to people is unlikely. When the risk is high, it must also tell the people affected. Bring in whoever is responsible for that: the DPO, or legal.

```markdown
# <date> <title>
Impact: who, how many, how long, what data
Timeline: detected → mitigated → resolved, with times
Cause: what happened, and why it was possible (ask "why" until you reach something you can change)
What went well
Actions: each with an owner and a date
```

## Done when
- [ ] users are no longer affected
- [ ] the postmortem is written
- [ ] every action has an owner and a date

## Frontend · Backend · Fullstack
- **Frontend:** errors by release in the error tracker, flags that switch features off, a static fallback page.
- **Backend:** logs by request id, dashboards, rollback.
- **Fullstack:** check whether the frontend's retries are making it worse.

## Concepts if you get stuck
- Logs, alerts, rollback, runbooks
- The frontend in production
- Reliability, SLOs, postmortems
- Security

## Next level
- SLOs, with alerts on what users feel.
- `staff` Postmortem reviews across teams, and checking that the actions get done.

## Next
`/wow-bug`, `/wow-comms`, `/wow-audit production-readiness`. End with `/wow-retro`, after the postmortem.

## Changelog
- 2026-10-05: v1
