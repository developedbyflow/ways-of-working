# Working with AI (brief)

- **Use it when:** you hand coding work to an AI, such as Claude Code.
- **Not when:** the product itself calls an LLM → `/wow-ai-feature`.
- **Reads:** the ticket and its criteria, `REPO-MAP.md`, `GLOSSARY.md`, `CLAUDE.md`, the contract, the example files.
- **Writes:** the brief; a new line in `CLAUDE.md` when you correct the AI twice for the same thing.

## Steps
1. **Decide what's yours.** You decide the design, the contract, the data model and the security rules. The AI types.
   - Skip it → you own code whose decisions you never made.
2. **The brief:**
   - the goal and the acceptance criteria;
   - the files to follow as examples, the contract, the glossary words;
   - what NOT to touch;
   - how to run the tests, and "don't change the tests to make them pass";
   - what "done" means: tests green, lint clean.
   - Skip it → it invents conventions and duplicates code that already exists.
3. **Ask small:** one slice at a time. For an area you don't know, ask for a plan first.
   - STOP: approve the plan before any code.
4. **The tests decide.** They come from the criteria, written by you or reviewed by you before the code. The AI makes them pass.
   - Skip it → "done" is its word against yours.
5. **Review it** → `/wow-review`, including the AI section.
   - STOP: you can explain every line before it's committed.
6. **Never put these in the context:** secrets, production data, customers' personal data.

## Done when
- [ ] you made the design decisions
- [ ] the diff is small enough to review
- [ ] the AI didn't change the tests, or you reviewed every change
- [ ] you can explain every line

## Frontend · Backend · Fullstack
- **Frontend:** name the design-system components to use, or it writes new ones with inline styles.
- **Backend:** point it to an existing endpoint as the pattern, and spell out the authorization rule.
- **Fullstack:** give it the OpenAPI contract first, so both sides match.

## Concepts if you get stuck
- AI in the frontend
- AI in the backend

## Next level
- Turn repeated corrections into `CLAUDE.md` lines, or into a skill.
- `staff` The team's AI rules: what may go into a prompt, and how AI code is reviewed.

## Next
`/wow-review`, `/wow-pr`. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
