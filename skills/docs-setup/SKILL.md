---
name: docs-setup
description: "Decide where the project documents live (a private docs repo, docs/ in the code repo, or the team's existing tool), create the place and its starting structure, and write the 'Project documents:' line in CLAUDE.md so every skill writes there. Also sets up the diagram tools, so every design drawing is in a standard notation (C4, UML, ER, DFD) drawn from text and checked against the table under it, and the check that stops on a document stating a count its source no longer has. Use when the user starts a new project, before /brainstorm."
argument-hint: "[the project name]"
---

# Docs setup

## When to use it
Once per project, before the brainstorm: decide where the documents live, create the place, and tell the skills where to write.

## The problem it solves
The code can be public while the strategy stays private. Each kind of document has one clear place, so nothing gets mixed, and every skill writes to the same place.

## How to run it
- **The bar:** do what a senior engineer or the C-level who owns this area (CEO, CPO, CTO, CFO, CMO, COO) at a well-run company would accept, in the simplest form that meets it. Use the real industry method and name it, so the user learns it. Senior also means knowing what to leave out: say what you skip and why.
- **One question at a time,** then wait.
- **Commands that create something outside this machine** (a GitHub repo) are given in a `bash` block for the user to run, or run only after the user confirms.
- **Verify, don't assume:** after each command, check the result.

## Steps

### 1. Where the documents live, by who reads them
Ask: will the code be public? Do you work alone? Is this for a team that already keeps documents somewhere? Then recommend:

| Situation | Where the project documents live |
|---|---|
| **Public code** (portfolio), private strategy | a **private docs repo** (for example `project-docs`), separate from the code |
| **Private code**, working alone | `docs/` in the code repo |
| **At a job** | where the team already keeps documents (Confluence, Notion) or `docs/` next to the code; don't invent a new place |

What goes where:
- **The code repo:** only what a stranger needs to run and contribute: README, LICENSE, `.env.example`.
- **The project documents:** `ideas.md`, problem, market research, brief, PRD, interview notes, later the ADRs.
- **The user's own framework** (how they work on any project) stays outside both, so it follows them to the next project.

Moving documents out of a public repo later doesn't hide them: the public git history keeps them. Decide before the first commit.

### 2. Create the place
For a private docs repo:
```bash
gh repo create <user>/<project>-docs --private --clone
gh repo view <user>/<project>-docs --json visibility
```
The second command must print `"visibility": "PRIVATE"`.

### 3. The starting structure
```
docs/
  00-project/       what belongs to the whole project, not to one phase
    ideas.md        every idea in your head, in any form
  01-discovery/     brainstorm, problem, market research, brief, PRD
```
`ideas.md` starts with one line: `# Ideas` and "Write every idea here, in any form. /brainstorm shapes it." Later phases add their folders when they start (`02-design/` starts with the diagram files of step 4); the decisions (ADRs) go in `00-project/adr/` from the first one.

### 4. The diagram tools
Every design drawing is in a **standard notation, drawn from text**, so it reads the same at any company and the drawings can't drift apart: C4 from one model, the rest as PlantUML files. Without this, each Design step draws in its own style, and the same part ends up with two names in two drawings.

- **Copy the starting files** from this skill's `assets/` into `docs/02-design/`:
  - `diagrams.sh`: checks the counts, then draws everything;
  - `c4/workspace.dsl` (an empty C4 model in the Structurizr DSL, with the styles) and `c4/legend.puml` (the legend every C4 drawing shares);
  - `c4/views.txt`: one line per view, `key:its SVG[:the Markdown with its table[:rows drawn in no view]]`. Several views can share one table (the map of the modules and one drawing per module): together they draw every row, except those named in the fourth field, which a sentence under the table says instead;
  - `c4/check-tables.py`: fails when a drawing and its table disagree (a numbered arrow without a row, a row no view draws and the fourth field doesn't name, an arrow whose two ends its row doesn't name);
  - three fixes to the drawing: `c4/pad-labels.py` (room inside every box: PlantUML draws a box exactly as wide as its text), `c4/add-groups.py` (draws a group, such as "Outside systems", in the container and component views, where the Structurizr export leaves it out), `c4/numbers-only.py` (a view with `properties { "labels" "numbers" }` keeps only the numbers on its arrows, for a drawing whose arrow texts would cross; the text stays in the table);
  - `checks/facts.py`, which `diagrams.sh` runs first: it counts each fact many documents repeat from its source and stops on a document that states another number, with the file and line. Its list `FACTS` holds one guard per count, grouped by the step that writes the source, each reading the header line that step's template writes: the system design's alerts to the phone; the data model's tables, database schemas and entities; the API's addresses, operations, operations behind a login and schemas with fields, plus a commented pattern for a part of the map one rule covers; the UI's screens, those designed with their slice, the flows, the contrast pairs and rings, the wireframe and mockup pages; security's threats, map flows, ways in that aren't addresses, secrets, accounts that reach production, alerts, protections with their check and the ASVS list's answers (yes, deviations, gaps); the ADRs. A guard is a pattern the project fills in: the source, the words after the number, a floor under which a number is a part rather than the total (half the count until a part trips the check and the project sets one), or a phrase of its own ("the other 30 screens"); a step that repeats another count adds a guard. A fact whose source isn't written yet is skipped, so on a new project the check passes. Journal lines, `changes/` and a count followed by "at this decision", "before" or "when drafted" aren't checked;
  - `checks/facts-history.txt`: a past count kept on purpose, one `path: text in the line` per line; only the counts inside that text are skipped, the rest of the line is still checked.

  `/system-design` fills the model. The C4 drawings come out in Structurizr's own look: the type under every name, the technology under every label.
- **The tools**, free, once per machine, in `~/Desktop/TechProducts/tools/` (or the folder in `DIAGRAM_TOOLS`): PlantUML (a `.jar`, runs on Java 17+), the Structurizr CLI (the C4 author's tool) and **Graphviz** (`brew install graphviz`), the layout engine C4-PlantUML is made for: it keeps the outside systems together and the arrows straight. Without it, `diagrams.sh` falls back to PlantUML's own layouts (ELK for C4), which work but read worse. The ER diagrams keep PlantUML's `smetana` layout (a pragma in their files): with Graphviz the wide ones come out as a staircase, cut at 4,096 px. Pick a release a few weeks old, not one from the last days. Say the file, the source and the size, and download only after the user says yes:
  ```bash
  mkdir -p ~/Desktop/TechProducts/tools && cd ~/Desktop/TechProducts/tools
  curl -sSLO https://github.com/plantuml/plantuml/releases/download/v<version>/plantuml-<version>.jar
  curl -sSLO https://github.com/structurizr/cli/releases/download/v<version>/structurizr-cli.zip && unzip -q structurizr-cli.zip -d structurizr-cli
  brew install graphviz
  ```
- **Check it:** `docs/02-design/diagrams.sh` says every fact is skipped (no source written yet) and draws the empty model's two views; open them.

| Drawing | Notation | Source |
|---|---|---|
| context, containers, components, where things run | C4 (levels 1–3, deployment) | `c4/workspace.dsl` |
| a flow, a request through the parts | UML sequence diagram | `.puml` next to its `.svg` |
| a screen flow, a pipeline | UML activity diagram | idem |
| the tables | ER diagram, crow's foot, generated from `schema.sql` | idem |
| the security map | data flow diagram with trust boundaries | idem |

### 5. Tell the skills where it is
In `CLAUDE.md` of the folder where the user works with Claude, one line with the absolute path to the documents folder:
```markdown
Project documents: /Users/<user>/<path>/<project>-docs/docs
```
Every skill reads this line and writes there. Without it, skills write to `docs/` in the current folder. Show the line and check the path exists.

### 6. Access and personal data
- **Who else needs access, and what role?** Least privilege, for a limited time, removed explicitly afterwards.
  - On a personal GitHub account a collaborator always gets **write** access (there's no read-only role); a free **organization** gives a **Read** role. For a one-off look (an interview), share the screen or a PDF instead.
- **Interview notes hold personal data:** no real names, only in the private place.

### 7. First commit
Commit the structure (for a git repo): `docs: start the project documents`. The tools stay outside the repo; the starting diagram files go in.

## The bad version and why not
- **Everything in one public repo** → strategy and prices reach the competition.
- **Moving old documents from the public repo to the private one** and thinking they're hidden → the public git history still has them.
- **The personal framework inside the project repo** → it stays stuck there and doesn't follow you to the next project or your job.
- **Not telling the skills where the documents are** → each step writes somewhere else.
- **Drawing each diagram by hand, in a home style** → the next company can't read them, and the drawings disagree with each other.

## What breaks if you skip it
Either the strategy is exposed, or the documents scatter and nobody knows which one is true.

## The trade-off
Documents kept away from the code fall behind (drift). Many teams keep ADRs next to the code for that reason. The rule that keeps them current: the PR that changes a decision updates its document in the same step.

## The principle behind it
Separate by reader and by rate of change; every split has a sync cost, so split only when the gain is bigger. Least privilege, time-boxed, removed explicitly. Verify, don't assume.

## How to apply it at work
Use the place the team already keeps documents in, instead of creating a new one. Know who has access to which repo and with what role, where the ADRs live and who updates them. When someone leaves or a collaboration ends, remove their access explicitly.

## Done when
- [ ] the place is decided, with the reason
- [ ] it exists, and a private repo is verified as private
- [ ] `docs/00-project/ideas.md` and `docs/01-discovery/` exist
- [ ] the diagram tools work: `docs/02-design/diagrams.sh` passes the counts check (every fact skipped) and draws the empty C4 model
- [ ] the `Project documents:` line is in `CLAUDE.md`, pointing to a path that exists
- [ ] access is decided: who, which role, until when
- [ ] the structure is committed

## Next
Brainstorm (`/brainstorm`): write every idea into `ideas.md` first.
