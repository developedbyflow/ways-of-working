# FAQ

The questions people ask after a first read, with the answers.

## The basics

**What is a skill, and what is a page?**
A page (`bug.md`) is the know-how: when to use it, the steps, where to stop and decide, when it's done. A skill (`/wow-bug`) is a Claude Code command that opens that page and walks you through it. The skill holds no steps of its own.

```
/wow-bug "the daily plan is lost after refresh"
  → skills/wow-bug/SKILL.md   "read SKILLS.md, then bug.md"
  → SKILLS.md                 how every skill behaves
  → bug.md                    the steps, the STOPs, "Done when"
```

**So where do I change how I work?**
In the page. The skill reads the page at every run, so the next run follows the change.

**Which skill do I use?**
- Run `/wow` and describe what's in front of you. It asks at most two questions and names the skill.
- Look up the table "Which one, when two look alike" in [ECOSYSTEM.md](ECOSYSTEM.md).
- See the whole journey in [FLOWS.md](FLOWS.md).

**What does `/wow` do?**
It picks the skill for you, and does no work itself. One item gets one skill. A list of incoming items (bug reports, requests) gets sorted by severity and priority, with a skill and an owner for each.

**Is a page the same for frontend, backend and fullstack developers?**
Yes. Every situation goes through the same steps; what changes is which steps you own and which you only read and agree to. Each page has a "Frontend · Backend · Fullstack" section; `feature.md` spells out the ownership.

## Running a skill

**What does a run look like?**
1. You type the command and what's in front of you, for example `/wow-bug the daily plan disappears after refresh`.
2. Claude reads the page, checks that it fits, and suggests another skill if a different one fits better.
3. It goes step by step. At every **STOP** it asks you, recommends an answer, and waits.
4. At the end it checks "Done when", runs `/wow-retro`, then recommends the next skill. When you're in a journey from `FLOWS.md`, it says where you are ("step 4 of 11").

**Can I skip a step?**
Yes. The skill tells you what breaks if you skip it (each step's "Skip it →"), then does what you decide.

**Will a skill commit, push, deploy, delete data or send messages for me?**
Never. It gives you the exact command, and you run it.

**What if a web page, a review or a PR contains instructions for the AI?**
The skill doesn't follow them. Text from outside is treated as data, the way you escape user input against XSS: it gets analyzed, never executed. The skill quotes the sentence to you, says where it came from, and keeps following the page. The rule is in `SKILLS.md`.

**What does "every claim points to a file and a line" mean?**
When a skill says something about your code, it shows where it read it. Anything it can't point to is marked as an assumption.

**Can a skill check a document I already have, instead of writing one?**
Yes. `/wow-product-brief validate docs/product/brief.md` reads the brief against its page's template and "Done when", cites lines, asks the questions no template asks (who must pay, what is out, what doing nothing costs), goes to the primary source for claims that rest on a law or a price, and returns the findings in chat. It never edits the file; you pick what to apply. The same works for every page that writes a document. For a second opinion, run the critique against another method's template too; the differences between the two lists are the finding.

## Retro: how the pages grow

**Do I have to run `/wow-retro` myself?**
No. Every skill runs it at the end, for the page you just used. You run it yourself only:
- at the end of the week: `/wow-retro week`;
- at the end of the quarter: `/wow-retro quarter`;
- when you notice something later: `/wow-retro bug.md missed the service worker cache`.

**What does "retro changes the page where something was missing" mean?**
Say `/wow-bug` didn't tell you to check the service worker cache, and that was the cause. At the end, retro asks what was missing, and proposes:

```diff
+ - **PWA:** clear the service worker cache before you reproduce; it can serve an old version.
## Changelog
+ - 2026-10-10: service worker check (daily plan lost after refresh)
```

You approve it, and the next `/wow-bug` asks you to check the cache. A step you skip three times with nothing breaking is proposed for removal. The pages grow from real work, not from guesses.

**What else does retro write?**
One line in the project's `CLAUDE.md` when the AI made a mistake a rule would prevent, and one entry in your impact log: what you did, what changed, the proof. Each quarter, the impact log becomes CV bullets and STAR stories.

## Files and folders

**What does each file in this repo do?**
See "What's in this repo" in [README.md](README.md).

**What is the `audits/` folder?**
The 12 checklists for `/wow-audit`, one per area. `audit.md` holds the steps, which are the same for every area. `/wow-audit security` follows `audit.md` and checks `audits/security.md`. The report goes into the audited project, in `docs/audits/`.

**Which files do the skills create in my project?**
`CLAUDE.md`, `REPO-MAP.md`, `GLOSSARY.md`, and folders under `docs/` (ADRs, design docs, risks, tech debt, runbook, postmortems, audits, product, interviews, go-to-market). The table "Files the skills share" in [ECOSYSTEM.md](ECOSYSTEM.md) says which skill writes and which reads each one.

## Settings and install

**What are the personal settings?**
`~/.claude/wow-config.md`, on your machine, never in the repo: your name, the chat language, your background (so explanations start from what you know), how you learn best, **who does the work** (`guided`: you run every command and write the code, the AI explains and gives one step at a time; `delegated`: the AI writes, you review line by line), and where your impact log and career tracker are. `install.sh` creates it from `config.example.md`; as a plugin, you copy the example yourself.

**What happens without settings?**
Everything works. Chat follows the language you write in, the impact log goes to `~/impact-log.md`, explanations point to the official docs, and the work is `delegated`: the AI writes, you review. Say "guided" in chat, or set it in the settings, to run and write everything yourself.

**What is a plugin?**
A package for Claude Code: a folder of skills you install with one command and update the same way. It works like an npm package: `plugin.json` is its `package.json`, and a marketplace (`marketplace.json`) is the list it's installed from. This repo is both the plugin and its marketplace.

**Which install should I use?**

| How | For | What happens |
|---|---|---|
| Plugin (`claude plugin install ...`) | using the skills | you get a copy, and updates through the plugin |
| Clone + `./install.sh` | changing the pages | skills read the pages in your clone, so a page change works at the next run |
| A `SKILL.md` folder dropped into `~/.claude/skills/` | one skill of your own | Claude Code finds it, with no install step |

**I changed a page. Do I need to reinstall?**
No. Run `./install.sh` again only when a `SKILL.md` changes.

**Why does every command start with `wow-`?**
`/bug`, `/review`, `/plan` and `/upgrade` are already Claude Code commands. The prefix keeps all of these under one name: type `/wow` and the menu lists them all.

**How do I remove the skills?**
See "Install" in [README.md](README.md).

## Changing the ecosystem

**How do I add a new situation and its skill?**
1. Write `<name>.md` in the same shape as the other pages: "Use it when", "What you get", "Run it", "Not when", "Reads", "Writes", the steps with STOPs and "Skip it →", "Done when", "Next", "Changelog".
2. Copy any folder in `skills/` to `skills/wow-<name>/` and change the name, description, title and page name in its `SKILL.md`.
3. Add the row to the table in README, and the rows in ECOSYSTEM (files, "Which one").
4. Run `./install.sh`.

**How was the list of situations checked?**
Against the lifecycle of a product, a career framework, SWEBOK v4, DORA, Matt Pocock's skills and BMad. See [COVERAGE.md](COVERAGE.md).

**Is my local copy up to date with GitHub?**
`git status` shows changes you haven't committed. `git pull` brings changes made elsewhere, for example in the browser. After a pull that changed a `SKILL.md`, run `./install.sh`.
