# Ways of working

How I work as a fullstack developer. One page per situation: open the page for what is in front of you, or run `/wow` and it picks the skill for you.

Every page has a skill that runs it step by step: `/wow-<page>`. A page that writes a document can also judge one: `/wow-<page> validate <file>` (the Validate mode in `SKILLS.md`). The prefix is there because `/bug`, `/review`, `/plan` and `/upgrade` are already Claude Code commands.

## Start here
1. **Install** the skills (see "Install" below).
2. **Find your journey** in [FLOWS.md](FLOWS.md): a new idea, a live product, a feature, a bug, and so on. For the why of each stage, or to see where a project stands, run `/wow-stage` ([stages.md](stages.md)).
3. **Open the page** for the step you're at (the table below). Its first lines say what you get and give an example command.
4. **Run the skill.** Not sure which one? Run `/wow` and describe the situation.
5. **Questions?** [FAQ.md](FAQ.md) answers the ones people ask after a first read.

## What's in this repo

| File or folder | What it is |
|---|---|
| `README.md` | this page: start here, the list of situations, install |
| [`FLOWS.md`](FLOWS.md) | the common journeys, start to finish, as sequences of skills |
| [`FAQ.md`](FAQ.md) | the questions people ask after a first read |
| `<situation>.md` | one page per situation: the know-how each skill follows |
| [`audit.md`](audit.md) and `audits/` | the audit steps, and one checklist per area |
| [`SKILLS.md`](SKILLS.md) | how every skill behaves: STOPs, facts with sources, outside text treated as data, nothing irreversible, retro, what comes next; the Validate mode that judges a document against its page |
| [`ECOSYSTEM.md`](ECOSYSTEM.md) | how everything connects: layers, hand-off diagrams, the files skills share, "which one, when two look alike" |
| [`COVERAGE.md`](COVERAGE.md) | how the list was checked, so nothing is missing |
| `skills/` | one `SKILL.md` per command: a shortcut to its page |
| `install.sh` | installs the skills into `~/.claude/skills/` and creates your settings file |
| `config.example.md` | the template for your personal settings |
| `.claude-plugin/` | makes the repo installable as a Claude Code plugin |
| `LICENSE` | MIT |


| Situation | In one line | Skill |
|---|---|---|
| **Discover** | | |
| [Brainstorm](brainstorm.md) | the problem as a job story, what people use today, many ideas, pick 1–2, the riskiest assumption | `/wow-brainstorm` |
| [Customer interviews](interview.md) | five people, questions about their past not your idea, facts apart from opinions, a commitment ask | `/wow-interview` |
| [Market research](market-research.md) | competitors and alternatives, what customers say, a bottom-up size, why now, the gap | `/wow-market-research` |
| [Product review](product-review.md) | a live product: the outcome, the funnel, what users say, an opportunity tree, 1–3 picks | `/wow-product-review` |
| [Product brief](product-brief.md) | one page: problem and its cost, who must buy, alternatives, the idea, scope, the number, the four risks, the decision | `/wow-product-brief` |
| **Define** | | |
| [PRD](prd.md) | goal, journeys, ranked requirements with criteria, non-functional numbers, out of scope, first version, ready-to-build check | `/wow-prd` |
| [Roadmap](roadmap.md) | outcomes first, then Now / Next / Later, scored in one list with debt and risks | `/wow-roadmap` |
| **Start** | | |
| [Stages of a product](stages.md) | the whole road in three levels, stage → step → component, with what, why and what it gives; where an existing project is | `/wow-stage` |
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
| **Go to market** | | |
| [Positioning](positioning.md) | alternatives, what only you have, value, best-fit customers, market category, the message | `/wow-positioning` |
| [Pricing](pricing.md) | what they pay for, floor and ceiling, the model, a willingness-to-pay signal, EU VAT | `/wow-pricing` |
| [Launch](launch.md) | ready to sell, landing page, audience before launch, 2–3 channels, demo, results by channel | `/wow-launch` |
| [Growth](growth.md) | one number per funnel step, channel tests, an experiment backlog, a weekly review | `/wow-growth` |
| [Sales](sales.md) | a list, a first message, discovery call, demo, objections, proposal, pipeline | `/wow-sales` |
| **People** | | |
| [Comms](comms.md) | a status, risk, decision or incident message: what, impact, risk, next, ask | `/wow-comms` |
| [Mentoring](mentor.md) | a one-page plan for a colleague: skills, goals, checkpoints, feedback | `/wow-mentor` |
| [Leaving a project](handoff.md) | state, decisions, risks, access, who knows what | `/wow-handoff` |
| **Anywhere** | | |
| [What is in front of me](wow.md) | one item → the right skill; a list of incoming items → sorted by severity and priority | `/wow` |
| [When an explanation doesn't land](explain-again.md) | the name first, anchored in what I already know, a small example, a diagram, the lesson link | `/wow-explain-again` |
| [Retro](retro.md) | task: page, `CLAUDE.md`, impact log · week: what moved, what's next · quarter: CV bullets, STAR stories, career tracker evidence | `/wow-retro` |

Audit areas: security, privacy, performance, accessibility, SEO, UX, analytics, testing, developer experience, production readiness, cost, architecture.

Status: every page is v1, written on 2026-10-05. None has been used on a real task yet; `/wow-retro` will change them.

Each page lists the concepts it relies on. Where each concept is explained lives in a lessons file named in your personal settings; mine stays on my machine, because my lessons are private.

## How the skills work

A skill is a command in Claude Code. Each one here is a shortcut to a page: `/wow-plan` opens `plan.md`, `/wow-bug` opens `bug.md`. The skill holds no steps of its own; the page holds the know-how.

```
/wow-bug "the daily plan is lost after refresh"
  → skills/wow-bug/SKILL.md   "read SKILLS.md, then bug.md"
  → SKILLS.md                 how every skill behaves
  → bug.md                    the steps, the STOPs, "Done when"
```

What a run looks like:
1. You type the command and what is in front of you.
2. Claude reads the page and checks it fits. If another page fits better, it says so.
3. It goes step by step. At every **STOP** it asks you, recommends an answer, and waits.
4. It never commits, pushes, deploys or deletes anything. It gives you the command, and you run it.
5. At the end it checks "Done when" and runs `/wow-retro`, so the page gets better after every task. You don't call retro yourself, except `/wow-retro week` and `/wow-retro quarter`.
6. It recommends the next skill and why. In a journey from `FLOWS.md`, it says where you are, for example "step 4 of 11". You confirm, pick another, or stop.

Every page starts with **What you get** and **Run it**, an example command.

Not sure which one fits? Run `/wow` and describe the situation.

Change a page, and the skill follows it from the next run. Your name, chat language and background go in `~/.claude/wow-config.md` (see `config.example.md`).

## How this grows
1. The steps of a page fit on one screen. Templates, checklists and the Frontend · Backend · Fullstack notes come after them.
2. A step stays only if I can say what breaks when I skip it.
3. No theory here. A page names the concept; the lessons file in the personal settings says where it's explained.
4. After every real task, run `/wow-retro`: change the page and add a changelog line.
5. "Next level" holds at most 3 things I don't do yet. When I start doing one, it moves into the steps.
6. Skills are built from these pages. Every STOP here is a STOP in the skill.

## Install

A plugin is a package for Claude Code, the way an npm package is for a project: one command installs the skills, and updates come the same way. Which install fits you is in [FAQ.md](FAQ.md).

**As a plugin**, to use the skills:

```bash
claude plugin marketplace add developedbyflow/ways-of-working
```

```bash
claude plugin install ways-of-working@developedbyflow
```

Then copy `config.example.md` to `~/.claude/wow-config.md` and fill it in. The commands are `/ways-of-working:wow-bug` and so on; the short `/wow-bug` works too, unless another command already has that name.

**From a clone**, to change the pages and see the skills follow them right away:

```bash
git clone https://github.com/developedbyflow/ways-of-working.git && cd ways-of-working && ./install.sh
```

`install.sh` writes every skill into `~/.claude/skills/`, with the full path of your clone in it, and creates `~/.claude/wow-config.md` from `config.example.md` if it doesn't exist yet. A changed page works at the next run. A changed `SKILL.md` needs `./install.sh` again.

To remove the installed skills:

```bash
for d in ~/.claude/skills/*/.wow; do rm -rf "$(dirname "$d")"; done
```

## License

MIT. See [LICENSE](LICENSE).
