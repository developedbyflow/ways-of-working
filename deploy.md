# Release and deploy

- **Use it when:** you ship a change to production.
- **Not when:** servers, DNS, the database, or secrets change → `/wow-cloud`.
- **Reads:** `docs/runbook.md`, the risk section of the PR, the migration plan.
- **Writes:** release notes, runbook updates.

The skill gives you every command. You run them.

## Steps
1. **One build, everywhere:**
   - CI builds once and tags the build with the commit;
   - the same build goes to staging and to production;
   - configuration comes from the environment.
   - Skip it → "it worked on staging" proves nothing.
2. **Before you deploy:**
   - migrations are backward compatible (`/wow-migration`);
   - the flag can turn the feature off;
   - you know the rollback command and how long it takes.
   - STOP: a change that can't be undone gets a second look, and a time with low traffic.
3. **Deploy through the pipeline.** Traffic goes to the new version only after its health check passes. Roll it out gradually when the platform allows it.
4. **Watch for 15–30 minutes:** the error rate, latency, the key business event, and frontend errors for the new release.
   - Skip it → users report the problem before you notice it.
5. **Roll back fast** when the numbers go wrong. Don't debug in production. Fix forward only when the fix is tiny and clear.
6. **Release notes:** what changed for users, in their words, with links to the PRs.

**Rollback rehearsal:** once a quarter, practice the rollback on staging and time it.

## Done when
- [ ] deployed by the pipeline, with health checks green
- [ ] the numbers were watched after the release
- [ ] the release notes are written

## Frontend · Backend · Fullstack
- **Frontend:**
  - static files with hashed names and a long cache;
  - `index.html` without cache;
  - source maps uploaded to the error tracker.
- **Backend:** health checks, migrations as a separate step, a graceful shutdown.
- **Fullstack:** when the backend adds fields, it goes first and stays backward compatible; the frontend follows. Never the other way around.

## Concepts if you get stuck
- Pipelines, environments, health checks, rollback → [Backend 08 Infrastructure, deploy and observability](https://claude.ai/artifact/WqBR1zmfYkwSPwatLnhhjN)
- Frontend build and deploy → [F11 Tooling, build and deploy](https://claude.ai/artifact/7UCtfqHKtpNyvWsLx74xPx)
- Flags and releases in production → [F16 The frontend in production](https://claude.ai/artifact/46i2EYDtDsXGonv52HDA7C)
- Reliability → [S09 Reliability](https://claude.ai/artifact/93Z3DRAoAx7WTiRWgdUyZE)

## Next level
- Deploy on every merge, with risky changes behind flags.
- Track the four DORA numbers: how often you deploy, how long a change takes to reach production, how many deploys fail, how fast you recover.
- `staff` Progressive delivery across the team.

## Next
`/wow-incident` if it goes wrong; `/wow-experiment` to measure. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
