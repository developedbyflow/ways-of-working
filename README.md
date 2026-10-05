# Ways of working

How I work as a fullstack developer. One page per situation: open the page for what is in front of you, or run `/wow` and it picks the skill for you.

Every page has a skill that runs it step by step: `/wow-<page>`. The prefix is there because `/bug`, `/review`, `/plan` and `/upgrade` are already Claude Code commands.

- How the pages, the skills and the project files connect: [ECOSYSTEM.md](ECOSYSTEM.md).
- How I checked that nothing is missing: [COVERAGE.md](COVERAGE.md).
- How every skill behaves: [SKILLS.md](SKILLS.md).

| Situation | In one line | Skill |
|---|---|---|
| **Start** | | |
| [New project](new-project.md) | architecture, small design system, CI/CD and quality gates, environments, test strategy, logs and alerts, definition of done, first ADRs | `/wow-new-project` |
| [Joining a project](join.md) | access, people, how the team works, run it locally, a first small PR | `/wow-join` |
| [Understanding a codebase](repo-tour.md) | what it does, folder map, one request traced end to end, data model, risky areas, glossary | `/wow-repo-tour` |
| **Decide** | | |
| [Grill](grill.md) | from a problem to a decision, in rounds of questions; ends with an ADR | `/wow-grill` |
| [Research](research.md) | answer a question from primary sources; choosing a library or vendor; build vs buy | `/wow-research` |
| [Spike](spike.md) | a throwaway prototype that answers one question | `/wow-spike` |
| **Design** | | |
| [Architecture](architecture.md) | requirements and numbers → components and data flow → failure modes, scale, threats → the 2–3 big decisions as ADRs | `/wow-architecture` |
| [Data model](data-model.md) | entities from the glossary → tables, keys, constraints → the queries the app runs → indexes → how it migrates | `/wow-data-model` |
| [API design](api-design.md) | what the client needs → the contract first: requests, responses, errors, pagination, versioning, who is allowed | `/wow-api-design` |
| [UI design](ui-design.md) | the user's steps → screens and their states → components from the design system, accessible from the start | `/wow-ui-design` |
| [Design system](design-system.md) | a reusable component or tokens: API, accessibility, states, docs, tests, versioning, deprecation | `/wow-design-system` |
| [Integration](integration.md) | a service I don't own: contract, auth, timeouts, retries, idempotency, webhooks, fallback, test mode, cost | `/wow-integration` |
| [AI feature](ai-feature.md) | a feature that calls an LLM: is it worth it, context, structured output, examples to test against, guardrails, cost, fallback, privacy | `/wow-ai-feature` |
| [Design doc](design-doc.md) | goals, non-goals, design, alternatives, threats, rollout and rollback; read by others before coding | `/wow-design-doc` |
| **Plan** | | |
| [Plan](plan.md) | one feature (slices, a range) or an initiative (milestones, decisions, risks); the estimate is compared with the actual at retro | `/wow-plan` |
| **Build** | | |
| [Feature](feature.md) | problem → criteria → UI design → technical design → tests → thin slice → ship and measure; also removing a feature | `/wow-feature` |
| [Bug](bug.md) | reproduce → failing test → fix → cause; hard bugs and flaky tests | `/wow-bug` |
| [Refactor and tech debt](refactor.md) | tests as a safety net first, then small steps; behavior stays the same | `/wow-refactor` |
| [TDD](tdd.md) | one failing test → make it pass → clean up → commit | `/wow-tdd` |
| [Working with AI](brief.md) | I decide the design, the AI types: context, small asks, tests it can't change | `/wow-brief` |
| [Code review](review.md) | does it do what was asked, does it follow the standards (two separate passes); extra checks for AI code | `/wow-review` |
| [Pull request](pr.md) | review my own diff, then a description with a picture, proof and risk | `/wow-pr` |
| **Ship** | | |
| [Release and deploy](deploy.md) | pipeline, the same build through every environment, release notes, a rehearsed rollback | `/wow-deploy` |
| [Cloud and infrastructure](cloud.md) | servers, database, domain, TLS, secrets, written as code | `/wow-cloud` |
| [Migration](migration.md) | schema, data, API, or a move to a new library: add the new next to the old → move → remove the old; one-off data fixes | `/wow-migration` |
| [Dependency upgrade](upgrade.md) | read the changes, one upgrade per PR, a way back | `/wow-upgrade` |
| [Experiment](experiment.md) | hypothesis, metric, guardrails, sample size, duration, stop rule → result written down | `/wow-experiment` |
| **Run** | | |
| [Incident](incident.md) | stop the damage → communicate → fix → postmortem without blame; security incidents | `/wow-incident` |
| [Audit](audit.md) | measure → findings with what breaks → I choose → fix → measure again; 12 areas | `/wow-audit <area>` |
| **People** | | |
| [Comms](comms.md) | a status, risk, decision or incident message: what, impact, risk, next, ask | `/wow-comms` |
| [Mentoring](mentor.md) | a one-page plan for a colleague: skills, goals, checkpoints, feedback | `/wow-mentor` |
| [Leaving a project](handoff.md) | state, decisions, risks, access, who knows what | `/wow-handoff` |
| **Anywhere** | | |
| [What is in front of me](wow.md) | one item → the right skill; a list of incoming items → sorted by severity and priority | `/wow` |
| [When an explanation doesn't land](explain-again.md) | the name first, anchored in what I already know, a small example, a diagram, the lesson link | `/wow-explain-again` |
| [Retro](retro.md) | task: page, `CLAUDE.md`, impact log · week: what moved, what's next · quarter: CV bullets, STAR stories, Career Tracker evidence | `/wow-retro` |

Audit areas: security, privacy, performance, accessibility, SEO, UX, analytics, testing, developer experience, production readiness, cost, architecture.

Status: every page is v1, written on 2026-10-05. None has been used on a real task yet; `/wow-retro` will change them.

The links to the lessons live in `LESSONS.md`, which stays on my machine and out of git: the lessons are private, so the links wouldn't open for anyone else.

## How this grows
1. The steps of a page fit on one screen. Templates, checklists and the Frontend · Backend · Fullstack notes come after them.
2. A step stays only if I can say what breaks when I skip it.
3. No theory here. A concept gets its name and the name of its lesson; the skills look up the link in `LESSONS.md`.
4. After every real task, run `/wow-retro`: change the page and add a changelog line.
5. "Next level" holds at most 3 things I don't do yet. When I start doing one, it moves into the steps.
6. Skills are built from these pages. Every STOP here is a STOP in the skill.

## Install the skills
The skills live in `skills/`. `install.sh` links each one into `~/.claude/skills/`, so a change in this repo reaches Claude Code right away.

```bash
./install.sh
```

To remove them:

```bash
find ~/.claude/skills -maxdepth 1 -type l -name 'wow*' -delete
```
