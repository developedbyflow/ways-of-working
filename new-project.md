# New project

- **Use it when:** you start an app or a service from zero.
- **What you get:** a skeleton that deploys from day one, with CI gates, tests, logs and alerts, and the first decisions written down.
- **Run it:** `/wow-new-project a meal-planning app for gym beginners`
- **Not when:** the project already exists → `/wow-join`.
- **Reads:** the problem: who uses it, how many people, what must never break; `docs/product/brief.md` and `docs/product/prd.md` if they exist.
- **Writes:** `CLAUDE.md`, README, `docs/adr/`, `docs/tech-stack.md`, `docs/definition-of-done.md`, `docs/runbook.md`, the CI config, the PR template. The documents go where the user says: the code repo's `docs/`, or a separate docs repository with folder names the user picks. Ask before writing.

## Steps
1. **Problem, users, numbers:** who, how many, and what must never break (data, money, privacy). If it's unclear → `/wow-grill`.
   - First look at the repository: its files, its history, and the reflog. Decisions left from an earlier start are offered as proposals or set aside; the user picks.
   - Skip it → you pick a stack for the wrong scale.
2. **Architecture** → `/wow-architecture`. Start with one deployable app split into clear modules, unless a number says otherwise.
   - STOP: approve the first ADRs.
   - Start `docs/tech-stack.md` (template below): every technology decided so far, and the ones still to decide, each with the step that decides it.
   - Skip it → the first shortcuts become the architecture, and in six months nobody knows why a package is there.
3. **Repo and workflow:**
   - one main branch, short-lived branches, small PRs;
   - the PR template, `type(scope):` commit messages, the lockfile committed;
   - the PR template asks: a new dependency has its row in `docs/tech-stack.md`;
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
- [ ] `docs/tech-stack.md` lists every technology, with why, or the step that decides it
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

## Tech stack template (`docs/tech-stack.md`)

One row per language, framework, library and tool the project depends on, grouped (languages, backend, database, frontend, tooling, infrastructure, observability). Big choices link to their ADR; small ones carry their reason in the row.

```markdown
| Technology | Version | What it is | What it does here | Why it | Not chosen | Cost: license, size, learning | Revisit when | Source |
|---|---|---|---|---|---|---|---|---|
| TanStack Router | 1.x (lockfile) | routing for React with validated params | the editor's URL: operator, group, week, day | typed params; a broken link is a type error | React Router | MIT; small; new API | breaking changes cost more than typed URLs save | ADR 0004, official docs |
| (to decide) | | | styling | | | | | new-project step 6 |
```

- A technology not decided yet gets a row "to decide", with the step that decides it.
- The version is the one in the lockfile; the row says the major version.
- A new dependency adds its row in the same change that adds it to the code.
- "Why it" must survive a colleague asking "why not the other one?". A big choice gets an ADR with the full argument: the need, the options, the trade-off said plainly, why it wins here, and when to revisit it.

## Changelog
- 2026-10-05: v1
- 2026-10-08: step 1 checks the repository and its history; ask where the documents live (Sated: a reset repo, then docs moved to a separate repository by the user).
- 2026-10-08: `docs/tech-stack.md`, a register of every technology with why, started after the architecture and kept current by the PR template (Sated; Florin wants the same at work).
- 2026-10-08: "Revisit when" in the tech stack template; a "why" that survives a challenge; the full argument in the ADR.
