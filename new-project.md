# New project

- **Use it when:** you start an app or a service from zero.
- **Not when:** the project already exists → `/wow-join`.
- **Reads:** the problem: who uses it, how many people, what must never break; `docs/product/brief.md` and `docs/product/prd.md` if they exist.
- **Writes:** `CLAUDE.md`, README, `docs/adr/`, `docs/definition-of-done.md`, `docs/runbook.md`, the CI config, the PR template.

## Steps
1. **Problem, users, numbers:** who, how many, and what must never break (data, money, privacy). If it's unclear → `/wow-grill`.
   - Skip it → you pick a stack for the wrong scale.
2. **Architecture** → `/wow-architecture`. Start with one deployable app split into clear modules, unless a number says otherwise.
   - STOP: approve the first ADRs.
   - Skip it → the first shortcuts become the architecture.
3. **Repo and workflow:**
   - one main branch, short-lived branches, small PRs;
   - the PR template, `type(scope):` commit messages, the lockfile committed;
   - the folder convention for a feature (UI, API client, tests).
   - Skip it → every change starts a debate about where things go.
4. **Quality gates in CI:** lint, format check, typecheck, tests and build are required to merge. Add a dependency scan and a secret scan.
   - Skip it → broken code reaches main.
5. **Test strategy:** what each level tests.
   - unit tests for logic;
   - integration tests with a real database in a container;
   - component tests with the API mocked from the contract;
   - 1–3 end-to-end golden paths;
   - test data built with factories.
   - Skip it → many slow tests in the wrong place, and none where it matters.
6. **A small design system** → `/wow-design-system`: tokens and 4–5 base components.
   - Skip it → every screen invents its own buttons.
7. **Environments and the first deploy** → `/wow-cloud`, `/wow-deploy`.
   - The same build goes through every environment, and secrets live outside the code.
   - Deploy a "hello" page on day one or two.
   - Skip it → deploy problems show up the week you launch.
8. **Observability from day one:**
   - logs with a request id;
   - error tracking on the frontend and the backend;
   - a health check;
   - one alert on the error rate;
   - the runbook started.
   - Skip it → the first incident is debugged blind.
9. **Definition of ready and done**, written once. The PR template links to it.
   - STOP: approve it.
10. **`CLAUDE.md`:** stack, commands, conventions, and what the AI must never do.

## Done when
- [ ] a merged PR reaches production through the pipeline, with every gate green
- [ ] logs, error tracking and one alert work
- [ ] README says how to run and test it in a few commands
- [ ] the first ADRs and the definition of done are written

## Frontend · Backend · Fullstack
- **Frontend:**
  - Vite or Next.js, chosen by the rendering need (written as an ADR);
  - strict TypeScript, ESLint and Prettier.
- **Backend:**
  - ASP.NET Core with health checks and Problem Details for errors;
  - EF Core migrations;
  - Postgres in Docker for local work and for tests.
- **Fullstack:** the backend generates the OpenAPI document, and CI generates the TypeScript types from it.

## Concepts if you get stuck
- Project setup and tooling
- Architecture choices
- Tests at each level
- Pipeline, environments, logs
- Design system

## Next level
- A feature template (folders, tests, telemetry), so every feature starts the same way.
- `staff` Review the ADRs every quarter: which ones are no longer true?

## Next
`/wow-architecture`, `/wow-design-system`, `/wow-cloud`, `/wow-deploy`, then the first `/wow-feature`. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
