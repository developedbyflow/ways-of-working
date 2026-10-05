# Understanding a codebase (repo-tour)

- **Use it when:** you need to understand a codebase fast: a new project, a colleague's service, a library.
- **Not when:** you are joining a team → `/wow-join`, which runs this inside.
- **Reads:** the code, the git history, README, `docs/`, the migrations, the routes.
- **Writes:** `REPO-MAP.md`, `GLOSSARY.md`.

Every claim points to a file and a line. Anything the code doesn't show is marked as an assumption. STOP after each step: you ask your questions before the next one.

## Steps
1. **What it does:** from README, the routes and the screens. One paragraph: who uses it, and for what.
2. **How to run and test it:** the exact commands, checked by running them.
   - Skip it → the map describes an app nobody can start.
3. **Folder map:** one line per top folder, plus the entry points (`Program.cs`, `main.tsx`, the router).
4. **One request, end to end:** take the main user action and follow it: click → component → API client → endpoint → service → database → back. Draw it as a sequence diagram, with file and line at every step.
   - Skip it → you know the folders but not how they work together.
5. **Data model:** tables and relations as a diagram, from the migrations or the ORM model.
6. **How a feature is usually added:** read 1–2 recent PRs that added one, and list the files they touched. That's the project's recipe.
7. **Risky areas.**
   - Look for: the files that change most often.
     ```bash
     git log --since=6.months --format= --name-only | sort | uniq -c | sort -rn | head -20
     ```
   - Also look for the biggest files, code without tests, and clusters of TODO and FIXME.
8. **Glossary:** the domain words, one line each.
9. **Check:** five questions you answer without looking. Example: "Where would you add a field to the order response?"
   - STOP: if you miss one, go back to that step.

## Done when
- [ ] `REPO-MAP.md` has steps 1–8, with file references
- [ ] you answered the five questions

## Concepts if you get stuck
- The request pipeline → Backend 02 Anatomy of a backend
- Tables and relations → Backend 04 Databases
- How a large frontend is organized → F14 Frontend architecture at scale

## Next level
- Keep `REPO-MAP.md` true. `/wow-review` asks for an update when a PR changes the structure.

## Next
Back to `/wow-join`, or on to `/wow-feature` or `/wow-bug`. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
