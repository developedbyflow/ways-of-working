# How every skill runs

Every `/wow-*` skill reads this file first, then its page. This file says how the skills behave; the page says what they do.

## Start
1. **Read the whole page before doing anything.** The page is the process: don't add steps, and never drop one silently.
2. **Say which page you follow**, in one line, and check its "Use it when" and "Not when". If "Not when" fits better, name the other skill.
   - STOP: the user confirms.
3. **Look for the project files listed under "Reads".** Say which ones are missing. Create a file only when a step writes it.

## During
4. **One step at a time.** Say which step you're on.
5. **At every STOP:** ask the question, give your recommendation with the reason, and wait. Never answer a STOP yourself.
6. **When the user wants to skip a step:** say what breaks (the page's "Skip it →"), then do what they decide, and keep it for the retro.
7. **Facts:**
   - a claim about the code points to a file and a line;
   - a claim about a tool or a library points to its docs and version;
   - anything else is marked as an assumption.
8. **Stuck on a concept** (the user says they don't understand, or asks what something is) → run `/wow-explain-again`, then continue where you were.
9. **Nothing irreversible.** Never commit, push, merge, deploy, run a migration or a data fix on a shared database, delete data, send a message or spend money. Give the exact command in a `bash` block; the user runs it.
10. **Write the files from "Writes"**, in English, using the page's templates. Say which files you created or changed.

## End
11. **Check "Done when"** item by item, with the evidence for each.
12. **Hand-offs:** when "Next" names another skill, ask before starting it.
    - STOP: the user confirms.
13. **Run `/wow-retro`** in task mode, except in `/wow`, `/wow-retro` and `/wow-explain-again`.

## Talking
- In chat, use the user's language (Romanian with Florin). Everything written to files is in English.
- Short and plain:
  - name the thing before its parts;
  - anchor new things in TypeScript, React or the browser;
  - no metaphors.
- Recommend one option. Don't list the options you won't pursue.

## Paths
- **Pages:** `/Users/ionescuflorin-eugen/Desktop/TechProducts/ways-of-working/`
- **Lessons:** `LESSONS.md` in the pages folder.
- **Impact log (private):** `/Users/ionescuflorin-eugen/Desktop/TechProducts/impact-log.md`
