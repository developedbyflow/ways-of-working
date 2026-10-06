# Audit

- **Use it when:** you check one area of something that already exists: before a launch, after a big change, every few months, or when a number gets worse.
- **What you get:** a report with numbers before and after, and checks in CI so the problems don't come back.
- **Run it:** `/wow-audit accessibility`
- **Not when:**
  - one problem → `/wow-bug`;
  - one diff → `/wow-review`.
- **Reads:** the area's checklist in `audits/`, the last report in `docs/audits/`, the project docs the area needs (`docs/tracking-plan.md`, `docs/postmortems/`), the app.
- **Writes:**
  - the report, `docs/audits/YYYY-MM-area.md`;
  - the findings, as tickets;
  - `docs/tech-debt.md`, `docs/risks.md`.

## Steps
1. **Scope:** the area, the part of the app, and the bar to meet (for example WCAG 2.2 AA, or the "good" Core Web Vitals).
   - STOP: confirm it.
   - Skip it → you audit everything a little and nothing well.
2. **Tools first:** run the tools the checklist names, and save their output.
3. **Manual checks:** what the tools can't see. Each checklist lists them.
4. **Findings:** for each one, write down:
   - where it is;
   - what breaks, and for whom;
   - how severe it is (critical, high, medium, low);
   - the evidence (a screenshot, a number, a request);
   - the fix.
   - Skip "what breaks" → nobody prioritizes it.
5. **Choose.**
   - STOP: for each finding, you choose: fix it now, ticket it for later, or accept it with the reason written down.
6. **Fix it** with `/wow-bug`, `/wow-feature` or `/wow-refactor`, then measure again with the same tool. The numbers before and after go in the report.
7. **Keep it from coming back:** add a CI check where you can (axe, Lighthouse CI, a dependency scan, a bundle budget).
   - Skip it → the next audit finds the same things.

## Areas

| Area | Checklist |
|---|---|
| Security | [audits/security.md](audits/security.md) |
| Privacy | [audits/privacy.md](audits/privacy.md) |
| Performance | [audits/performance.md](audits/performance.md) |
| Accessibility | [audits/accessibility.md](audits/accessibility.md) |
| SEO | [audits/seo.md](audits/seo.md) |
| UX | [audits/ux.md](audits/ux.md) |
| Analytics | [audits/analytics.md](audits/analytics.md) |
| Testing | [audits/testing.md](audits/testing.md) |
| Developer experience | [audits/dx.md](audits/dx.md) |
| Production readiness | [audits/production-readiness.md](audits/production-readiness.md) |
| Cost | [audits/cost.md](audits/cost.md) |
| Architecture | [audits/architecture.md](audits/architecture.md) |

```markdown
# <Area> audit · <date>
Scope and bar:
Tools and their output:
Findings: where · what breaks, for whom · severity · evidence · fix · decision
Before → after:
Checks added to CI:
```

## Done when
- [ ] the report has the numbers before and after
- [ ] every finding is fixed, ticketed, or accepted with a reason
- [ ] a CI check is added where possible

## Next level
- An audit calendar: security and dependencies every month, accessibility and performance every quarter.
- `staff` One quality dashboard for the team.

## Next
`/wow-feature`, `/wow-bug`, `/wow-refactor` for the fixes. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
