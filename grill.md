# Grill: from problem to decision

- **Use it when:** a problem or a decision has no clear answer, or you want a plan stress-tested.
- **Not when:**
  - the docs can answer a single factual question → `/wow-research`;
  - only building something will answer it → `/wow-spike`.
- **Reads:** the ticket, the code, logs, data, docs, `GLOSSARY.md`, `docs/adr/`.
- **Writes:** an ADR in `docs/adr/`, `GLOSSARY.md`, `docs/risks.md`, questions for other people.

## Steps
1. **The problem in one sentence**, and what "solved" means: a number, or something you can observe.
   - STOP: confirm it.
   - Skip it → you solve a different problem.
2. **Facts first.** Look up whatever the code, logs, data or docs can answer, and note the source.
   - Skip it → decisions rest on guesses.
3. **Rounds of questions.**
   - Each question is numbered and comes with a recommended answer and the reason for it.
   - Ask only the questions you can answer now; the rest depend on these answers.
   - STOP after each round.
   - A question only someone else can answer → write it for them (who, what you need back, by when). That branch waits.
   - A concept you don't know → `/wow-explain-again`, then continue.
   - A new word → `GLOSSARY.md`.
   - Skip it → hidden assumptions surface in production.
4. **Options:** 2–3 of them, each with its cost, what breaks, and when it's the right one. Put numbers on it where you can: ms, KB, days, money. Add "do nothing" when that's a real option.
   - Skip it → you pick the first idea.
5. **Decide.**
   - STOP: you choose.
6. **Write it down as an ADR.** Risks go to `docs/risks.md`.
   - Skip it → in three months nobody knows why, and the debate starts again.
7. **Present it**, when someone else decides or must agree → `/wow-comms`, decision format. Include the objections, and when you'd agree with them.

It ends when no question is open and nothing is silently assumed.

```markdown
# 0007 Store prices in minor units
Status: proposed | accepted | replaced by 00NN
Context: what forces the decision, with numbers
Decision: what we do
Options not chosen: each one, and why not
Consequences: what gets better, what gets worse, what we watch
```

## Done when
- [ ] the problem and "solved" are confirmed
- [ ] every assumption is either a fact with a source or an open question with an owner
- [ ] the ADR is written

## Frontend · Backend · Fullstack
Questions that usually come up:
- **Frontend:** who sees it, on which devices, which states; what lives in the URL and what lives in state.
- **Backend:** the data; two requests at once; a dependency that's down; the scale.
- **Fullstack:** where the logic lives, the shape of the contract, who validates what.

## Concepts if you get stuck
- Requirements and trade-offs → S01 Requirements and Trade-offs
- Leading technical decisions → F17 Technical leadership in frontend
- Design principles → Backend 09 Principles and design patterns

## Next level
- Name things in the code with the words from `GLOSSARY.md`.
- `staff` Run a grill for someone else's decision: you ask the questions, they decide.

## Next
`/wow-design-doc` for big decisions, `/wow-architecture`, `/wow-feature`. `/wow-comms` when someone else decides. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
