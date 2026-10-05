# When an explanation doesn't land (explain-again)

- **Use it when:** an explanation, a term or a piece of code doesn't make sense, in any skill.
- **Not when:** you need the whole topic from zero. Open the lesson.
- **Reads:** the project's GLOSSARY.md, `LESSONS.md` (local only: it maps each lesson name to its private link).
- **Writes:** a new line in GLOSSARY.md when the term belongs to the project.

## Steps
1. **Name the thing first:** what it *is*, in one sentence, with words you already know. "ASP.NET Core has a user-management package" comes before `IdentityDbContext`.
   - Skip it → you learn the pieces without knowing what they belong to.
2. **Anchor it in what you know:** the closest thing from TypeScript, React or the browser. A C# interface is a TypeScript interface; `yield` is infinite scroll for a function.
   - Skip it → the new word stays abstract.
3. **A small example:** 2–5 lines, with the names from your current code. No `Foo`, no `Bar`.
4. **A diagram** (Mermaid) when something moves: a request, data, steps.
5. **Check:** you say it back in one sentence.
   - STOP: if it still doesn't land, change the anchor. Don't add more words.
   - Skip it → you think you got it, until the interview question.
6. **The lesson link** from LESSONS.md, for the full version.

## Rules
- Every new term is defined the first time it appears.
- No metaphors that need their own explanation.
- No "see chapter N": what the explanation needs is right there.
- "Bad" always comes with what breaks.

## Done when
- [ ] you can say it back in one sentence and name one case where you would use it

## Next
Back to the skill that called it.

## Changelog
- 2026-10-05: v1
