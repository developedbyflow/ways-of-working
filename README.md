# Ways of Working

Claude Code skills that take a product from an idea to production, one step at a time.

## Who it's for

Me first. Written so anyone can use it, because I want to share it on YouTube.

## Why

- **Not skipping steps.** With AI it's easy to jump straight to code and forget the problem, the market and the architecture.
- **Learning the whole process**, so I can apply it at my job.
- **Growing from frontend to architect.** Every step explains the principle behind it, not just what to do.
- **Sharing it** on YouTube.

Two skills to get good at: **finding ideas with potential, then marketing and selling them**, and **fullstack development**.

Each skill is one step of the road, in order. It explains why the step matters and leaves a document behind.

## The bar

Everything here is what a senior engineer or a C-level at a well-run company would do, never the amateur shortcut, because the point is to grow. Each step is held to the bar of the role that owns it:

| Role | Owns |
|---|---|
| **CEO** | the whole: which problem, go or stop, the vision |
| **CPO** | the product: the problem, the users, what goes in the first version |
| **CTO** / senior engineer | the architecture, the code, the quality, the security |
| **CFO** | the money: price, cost per user, margin, runway |
| **CMO** | reaching people: positioning, channels, the funnel, sales |
| **COO** | running it day to day: support, backups, incidents, vendors, legal |

And always in the simplest form that meets that bar: senior means knowing what to leave out.

The skills also watch for risky assumptions: when a decision rests on something unchecked and being wrong would cost a lot, they stop and propose a test (see `risk-tests` in [FLOWS.md](FLOWS.md)). You only say yes or no.

## How a skill is written

One folder per skill in `skills/`, with one `SKILL.md` that holds everything. A skill is named after what it does (`problem`, `prd`, `risk-tests`), with no phase, context or number in the name, because the same skill can serve several situations: a code review works on your own product and at a job.

The grouping lives in [FLOWS.md](FLOWS.md) as **recipes**: one per situation (a new SaaS product, an existing codebase at work), with the skills to run, their order and their phase.

Every skill has the same sections:

- **When to use it**
- **The problem it solves**
- **Steps**
- **The bad version and why not**
- **What breaks if you skip it**
- **The principle behind it**
- **How to apply it at work**
- **Done when**
- **Next**

## Install

```bash
git clone https://github.com/developedbyflow/ways-of-working.git
./ways-of-working/install.sh
```

It links each skill into `~/.claude/skills`, so an edit or a `git pull` applies right away. Run it again after a pull that adds, renames or removes a skill; `./install.sh --remove` takes them all out. Start a new Claude Code session to see them.

## How to use it

[FLOWS.md](FLOWS.md) says which skill to run, in what order, and what each one reads and writes. Starting a new product: run `/docs-setup`, write every idea into `docs/ideas.md`, then run `/brainstorm`.
