# Developer experience audit

- **Bar:** a new person runs the app on day one, CI is fast and green, and the docs say how.
- **Tools:**
  - time a fresh clone until the app runs;
  - CI timings per step;
  - count the manual steps.

## Checklist
- [ ] **README:** run, test and deploy in a few commands, tried on a fresh machine or container.
- [ ] **Dependencies:** one command starts them all (`docker compose up`).
- [ ] **CI:** you know how long it takes and where the time goes. Dependencies and builds are cached.
- [ ] **Lint and format** run by themselves: on save, before commit, or in CI.
- [ ] **Dependency updates** are automated and grouped (Renovate or Dependabot).
- [ ] **Common work starts from a template or generator**, such as a new feature or a new endpoint.
- [ ] **Local errors and logs** are readable.
- [ ] **Docs are current:** ADRs, `REPO-MAP.md`, the runbook.

## Concepts
- Tooling, build and deploy
- .NET project and tools
- Pipelines and environments

## Changelog
- 2026-10-05: v1
