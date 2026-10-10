---
name: saas-prototype
description: "Discovery, step 05, optional: test whether people can use the main flow before any code. A throwaway clickable prototype of 2–3 journeys from the PRD, 3–5 tasks written as goals, a pass mark set in advance, 5 people from the segment thinking aloud, results per task and problems by severity, then fix and retest or move on. Use after the PRD when the main flow is new to people or the usability risk in the brief is high. Also judges an existing test: /saas-prototype validate <file>."
argument-hint: "[the journeys to test] or validate <file>"
---

# Discovery · 05 Prototype (optional)

## When to use it
Optional, after the PRD (04), before architecture and code.
- **Do it** when the main flow is new to people (for example scanning a plate, recipe variants), when users aren't technical, or when the brief rates the usability risk high.
- **Skip it** when the flow follows a pattern people already know (login, a list, a form), for an internal tool, or when a mistake is cheap to fix after launch. Write in the brief's journal that you skipped it and why.

## The problem it solves
You find out whether people can use the product before writing code (Marty Cagan's usability risk). A change to a drawing costs minutes; in code, days.

## How to run it
- **The bar:** do what a senior engineer or the C-level who owns this area (CEO, CPO, CTO, CFO, CMO, COO) at a well-run company would accept, in the simplest form that meets it. Use the real industry method and name it, so the user learns it. Senior also means knowing what to leave out: say what you skip and why.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Every `docs/…` path below means that folder.
- **Spot risky assumptions for the user:** when a decision here rests on something nobody has checked ("I think people will…", "the AI can probably…") and being wrong would cost a lot, stop and propose a risk test: what to check, how long it takes, the pass mark, and when it must be done. The user only says yes or no; run it with `/risk-tests`. Don't propose one for cheap, easy-to-undo choices.
- **Read first:** `docs/01-discovery/04-prd.md` (journeys, glossary, criteria) and the usability risk in `docs/01-discovery/03-product-brief.md`.
- **The user runs the sessions.** You prepare the script, the tasks and the results table, and help read the results.
- **Behaviour over opinion:** count what people did, not what they said they liked.

## Steps

### 1. What to test
The 2–3 journeys from the PRD that lead to the moment value lands. Not the whole app.

### 2. The screens
Only the screens of those journeys:
- **real content:** real names and values, a long name, zero items, many items; never lorem ipsum;
- **the states that matter:** empty, loading, error;
- **the words from the glossary,** so the test also checks the language.

### 3. The prototype
Clickable, as low-fidelity as possible while still feeling real: Figma, or plain HTML. It is not production code and gets thrown away. Building it in the real stack makes you attached to it and slow to change it.

### 4. The tasks
3–5 tasks, written as goals, not instructions:
- "You just ate a yogurt and a banana. Log them." not "Tap + and search for yogurt."
- Each one has a clear end the person can recognise.
- Start with an easy one.

### 5. The pass mark, set now
For example: 4 of 5 people finish each task without help, in under 2 minutes, with an ease score of at least 5 of 7. Write it before the first session.

### 6. The people
5 people from the segment in 01 (Jakob Nielsen: 5 users find about 85% of the problems). Not developer friends: they already know how apps work. Ask before recording; no real names in the notes.

### 7. The sessions, 20–30 minutes each
- Say it's the app being tested, not them, and nothing they do is wrong.
- Ask them to think aloud.
- Don't help, don't explain, don't defend. When they're stuck, ask "what do you expect to happen?" After 3 minutes stuck, mark it failed and move on.
- Note where they stop, what they look for, what they say, how long each task takes.
- **After each task:** "How easy was that, from 1 to 7?" (SEQ, Single Ease Question).
- **At the end:** "What was the most confusing part?" and "What did you expect that wasn't there?"

### 8. The results
- A table, task × person: done / with help / failed, the time, the ease score.
- The problems, grouped and rated:
  - **blocks:** they couldn't finish the task;
  - **slows:** they finished, but got lost or hesitated;
  - **cosmetic:** they noticed it, it didn't stop them.
- Each problem with how many of the 5 hit it and one quote.

### 9. The decision
- **Below the pass mark, or any "blocks":** fix it in the prototype, retest with 2–3 new people.
- **Above it:** move on to architecture.
- Write the result as the usability risk's status in the brief, with a journal line. What changes in the flow goes into the PRD (journeys, criteria), with a journal line there too.

Then write `docs/01-discovery/05-prototype.md`:

```markdown
# 05 – Prototype
**Journeys tested:** UJ-…
**Prototype:** [link]
**Pass mark:** …
## Tasks
1. …
## Results
| Task | P1 | P2 | P3 | P4 | P5 | Done without help | Avg time | Avg ease (1–7) |
## Problems
| Problem | Severity | How many of 5 | Quote | Fix |
## Decision
[pass / fix and retest], because …; brief and PRD updated on [date]
```

## Validate mode
`/saas-prototype validate <file>`: judge an existing usability test, change nothing.
1. Read the file, the PRD and the brief.
2. Check the template and "Done when" item by item, citing the lines.
3. Then ask: were the tasks goals or instructions? Was the pass mark written before the sessions? Were the people from the segment? Did anyone help during a task? Are the results what people did, or what they said? Did every "blocks" problem get fixed and retested? Did the PRD change where the flow changed?
4. Report: findings by severity, each with the line, what's wrong and what to change; then what the test does well; then what you couldn't evaluate. The user picks what to apply.

## The bad version and why not
- Testing on developer friends → they know how apps work; they aren't your users.
- Telling them what to do → you test your instructions, not the app.
- Asking "did you like it?" → what they managed to do counts, not what they say.
- Building the prototype in production code → you get attached to it and stop changing it.
- Prototyping the whole app → weeks on screens nobody tests.

## What breaks if you skip it
You learn after launch, from people who leave without saying why, that the main flow isn't clear. Then the fix costs code, not a drawing.

## The principle behind it
Behaviour beats opinion: measure what people do, not what they say. The cheapest mistake is the one caught on paper.

## How to apply it at work
Before a big new flow, ask for a prototype tested with 5 users. In refinement, ask: "has anyone tried this flow?"

## Done when
- [ ] 2–3 journeys picked from the PRD, the screens with real content and states
- [ ] 3–5 tasks written as goals
- [ ] the pass mark written before the first session
- [ ] 5 sessions with people from the segment
- [ ] a results table and the problems rated by severity
- [ ] a decision; the brief's usability risk and the PRD updated, each with a journal line

## Next
Delivery: the architecture.
