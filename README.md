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

Everything here is what a senior engineer, a CTO, a CEO, a CFO or a CMO at a well-run company would do, never the amateur shortcut, because the point is to grow. And always in the simplest form that meets that bar: senior means knowing what to leave out.

## When a skill gets added

Only after I've done that step on a real project (MacroMate). No skill is written ahead of the experience.

## How a skill is written

One folder per step in `skills/`, named `phase-step` (for example `discovery-problem`), with one `SKILL.md` that holds everything. No numbers in names: the order lives here, so a new step never renames the others. Every skill has the same sections:

- **When to use it**
- **The problem it solves**
- **Steps**
- **The bad version and why not**
- **What breaks if you skip it**
- **The principle behind it**
- **How to apply it at work**
- **Done when**
- **Next**

## Start a new project

1. Write everything in your head into `docs/ideas.md`, in any form.
2. Run `/discovery-brainstorm`. It shapes the ideas, finds the problems behind them, and picks one.
3. Follow the road below.

## Where the documents go

One folder per phase in the project's `docs/`, numbered in the order of the road; each step's file is numbered inside it:

```
docs/
  ideas.md               your raw ideas, shaped in 00 Brainstorm, sorted in 04 PRD
  01-discovery/
    00-brainstorm.md
    01-problem.md
    02-market-research.md
    03-product-brief.md
```

## The road

### Discovery: what to build, for whom and why
0. [Brainstorm](skills/discovery-brainstorm/SKILL.md) · `/discovery-brainstorm` (not yet tried on a project)
1. [Problem](skills/discovery-problem/SKILL.md) · `/discovery-problem`
2. [Market research](skills/discovery-market-research/SKILL.md) · `/discovery-market-research`
3. [Product brief](skills/discovery-product-brief/SKILL.md) · `/discovery-product-brief`
