# Retro

- **Use it when:** a task is done (task), at the end of the week (week), at the end of a quarter (quarter).
- **Not when:** an incident is still open. The postmortem comes first: `/wow-incident`.
- **Reads:** the page you used, the ticket with its estimate, `impact-log.md`.
- **Writes:** the page in `ways-of-working/` (with a changelog line), `CLAUDE.md`, `impact-log.md`; each quarter also CV bullets, STAR stories and Career Tracker evidence.

## Task (2 minutes)
1. **The page:** what helped, what was missing, and what you skipped without anything breaking.
   - A step skipped three times with nothing broken is a candidate for removal.
   - STOP: you approve every change to a page.
2. **The AI:** what did it get wrong that one rule would prevent? That rule becomes one line in `CLAUDE.md`.
3. **Estimate vs actual:** write both in the ticket, plus one line on why they differ.
   - Skip it → your estimates never get better.
4. **Impact log:** one entry.
   - Skip it → in six months you can't say what you did, and the CV gets vague bullets.
5. **New situation with no page?** Add a one-line row to README. It becomes a page the next time it happens.

```markdown
## <date> · <project> · <task title>
- What I did: <one sentence>
- What changed: <the number before → after, for users or the team>
- Proof: <PR, dashboard, report>
- Competence: <Career Tracker area · competence>
```

## Week (15 minutes)
1. **What moved:** this week's impact-log entries.
2. **What is stuck**, and why; the risks in `docs/risks.md` that changed.
3. **Work in progress:** how many things are open at once. Finish before you start something new.
4. **Next week:** the 1–3 things that matter, plus one "Next level" item to practice.

## Quarter (1 hour)
1. **Read the quarter's impact log.**
2. **CV bullets:** pick the 3–5 entries with the clearest number. Write each as "did X, which changed Y by Z".
3. **STAR stories:** turn two of them into stories (situation, task, action, result).
4. **Evidence:** add the links to the Career Tracker, on the competences they prove.
5. **Next level:** which items do you already do? Move them into the steps of their page.

No streaks and no scores. The loop records what changed, never how many days in a row.

## Done when
- [ ] task: the page, `CLAUDE.md` and the impact log are updated
- [ ] week: next week's 1–3 things are written
- [ ] quarter: CV bullets, two STAR stories and the evidence are added

## Concepts if you get stuck
- CV bullets, STAR stories, impact with numbers → F23 The product-minded engineer

## Next
Nothing. This closes the loop.

## Changelog
- 2026-10-05: v1
