---
name: adr
description: "A tool for every phase after Design: record one decision that is hard to undo but small (one library, one data format, one convention, one module's choice) as an ADR, the architecture decision record. Checks first that it is one: easy to undo means a ticket; big, touching several parts, means a design doc with /design-doc change. Reads the index for an earlier decision on the same topic, writes the ADR with the user (context, lettered options with for and against, the decision, the consequences, when to revisit it), and in one commit adds its row to the index, marks a decision it reverses \"replaced by\" with links both ways, and updates the step documents it changes. Use in Build when a slice meets a decision the design didn't make, after launch, and at work whenever someone asks \"is there an ADR for this?\". Also: /adr validate <file> judges an existing ADR."
argument-hint: "\"<the decision>\" or validate <file>"
---

# ADR (any phase after Design)

## When to use it
When one decision is **hard to undo** (a one-way door: undoing it costs a migration, a rewrite, or moving data or people) but **small**: it touches one part. Which tool, in three questions:

| The change | Easy to undo? | Touches several parts? | What you write |
|---|---|---|---|
| a bug, a button's text, a screen on an existing API | yes | — | a ticket |
| a library, a data format, a convention, one module's choice | **no** | **no** | a ticket and **`/adr`** |
| a new service, a provider swapped, data in production changed | **no** | **yes** | a design doc, `/design-doc change "<name>"`, which writes its ADRs when it's approved |

It happens:
- **In Build:** a slice meets a decision the design didn't make ("which library crops the photo on the phone?", "how are the export's files named?").
- **After launch:** a library is replaced, a format changes, a convention is set.
- **At work:** "which library for X?", "a new module or the existing one?", "which date format does the API use?". Teams that keep ADRs write one for each; in review someone asks "is there an ADR for this?".
- **Not in Design:** each Design step writes its own ADRs, in the same template, with the same rules.

## The problem it solves
A small decision that's hard to undo is made in a chat or a PR comment, and the reasons are lost. A year later nobody knows why the code uses that library, what else was considered, or when it should be looked at again; someone "fixes" it and breaks what depended on it. Or the opposite: a document as heavy as a design doc for a choice that touches one module, so nobody writes one. One page, the template every ADR uses, an index anyone reads in a minute.

## How to run it
- `/adr "<the decision>"`, e.g. `/adr "photo cropping library"`: writes one ADR with the user.
- `/adr validate <file>`: judges an existing ADR, changes nothing.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, `docs/` in the current folder. ADRs live in `docs/00-project/adr/`, listed in its index `docs/00-project/adr/README.md` (created by `/docs-setup`).
- **The user decides.** You find the options, their facts and their costs, and recommend; the user chooses. Write the choice with its letter and the date.
- **Every fact checked:** a library's licence, size, last release and maintainers, a format's standard, read on its official page and dated; a guess marked `[ASSUMPTION]`.
- **One step at a time,** each confirmed before the next.

## Steps
1. **Is it an ADR?** Put it through the three questions above. Easy to undo: say so, and suggest a ticket instead. Big, touching several parts (a new service, a provider, production data, the shape of the system): stop, and propose `/design-doc change "<name>"`. Only a small one-way door goes on.
2. **Read what exists.** The index (`adr/README.md`): is there an ADR on the same topic, which this one would change or reverse? The step documents the decision touches (the architecture's stack and conventions, the data model, the API…), the PRD's requirements that constrain it, and `ideas.md` if an idea led to it (keep its F-number).
3. **The context:** what forces the decision now, the constraints (the requirements with their numbers, the stack, the budget, the law), and what happens if nothing is decided. Facts only.
4. **The options:** 2–4 real ones, lettered A, B, C, each with what it wins and what it costs (`| Option | For | Against |`, a cost column when they differ in money), "keep what we have" among them when something exists. Each fact with its source and date. Recommend one, with why and when the other would win.
5. **The user decides.** Write the decision in one or two sentences, with the letter and the date.
6. **The consequences:** what becomes easier, what becomes harder, what it costs, what other documents must change; and **Revisit when:** the number or the event that would reopen it (a library unmaintained for a year, a size over the budget, a second module needing the same).
7. **Write it, in one commit:**
   - `docs/00-project/adr/NNNN-<short-title>.md`, the next number from the index, in the template below, status "accepted";
   - its row in the index, and the index's next number moved on;
   - an ADR it reverses: the old one's status becomes "replaced by ADR-NNNN", linked both ways; the old file stays;
   - the step documents it changes (the stack, a convention, a table…), each README with a journal line pointing to the ADR;
   - an idea it came from: its line in `ideas.md` names the ADR;
   - the counts check run (`docs/02-design/checks/facts.py`, it checks the index too) and every link checked.
   Then the ticket links the ADR; the PR cites its number.
8. **Later, a fact changes but the decision holds** (a measurement replaces a guess, a version moves on): a dated mark in the text, `(added <date>)` or `(corrected <date>: it said …)`, and an entry in the header's one Updated line. **The decision flips:** a new ADR that replaces it (steps 1–7), never the old one edited into the new decision.

The template, the same one every ADR uses (the `/system-design` skill's):

```markdown
# ADR-NNNN: [Decision]
- **Status:** accepted | replaced by ADR-NNNN (linked both ways)
- **Date:** [the day it was decided] (decided in [where: a step, "Build, slice 2", "after launch"])
- **Updated:** [date]: [what changed]; …; the decision doesn't change. (only once a dated change exists)
## Context
## Options
| Option | For | Against |
(A., B., C., the chosen one in bold)
## Decision
## Consequences
## Revisit when
```

## Validate mode
`/adr validate <file>`: judge an existing ADR, change nothing.
1. Read the ADR, the index, the ADRs it names, and the step documents it touches.
2. Check: is it really a one-way door, and a small one (or should it be a ticket, or a design doc)? Does the context say what forces it, with facts? Are there at least two real options, each with for and against, "keep what we have" among them when something exists? Is the decision one or two sentences, with who and when? Are the consequences honest, the costs included? Is "Revisit when" a number or an event someone will notice? Is its row in the index, with the right status? Does an ADR it reverses say "replaced by", linked both ways? Is every dated change in the Updated line? Do the step documents it changes say the same today?
3. Report: findings by severity, each with the line, what's wrong and what to change; then what it does well; then what you couldn't judge.

## The bad version and why not
- An ADR for everything, a button's colour included: nobody reads the index any more.
- No ADR for a library that every module now imports: a year later nobody knows why, or what it would cost to leave.
- One option, the chosen one: it's an announcement, not a decision.
- The old ADR edited into the new decision: the history of why is gone, and every link to it now says something else.
- An ADR written after the code, to tick a box: the options were never weighed.
- A big change squeezed into an ADR to skip the review: the other parts it touches find out after the code.

## What breaks if you skip it
The reasons behind the small irreversible choices live in people's heads and leave with them; the same discussion is had again with every new colleague; a library is swapped without anyone knowing what depended on it.

## The principle behind it
Michael Nygard's architecture decision records (2011): one short file per decision, numbered, never reused, with its context, decision and consequences; a reversed decision kept and marked, replaced by a new one. Jeff Bezos's doors (2015 letter): a one-way door is decided carefully, a two-way door quickly. The size of the record follows the size of the decision: a ticket, an ADR, or a design doc.

## How to apply it at work
Use the team's template and place if there is one (MADR, a `docs/adr/` folder per repository, Confluence); the questions are the same. Before deciding something hard to undo in your module, ask whether an ADR already covers it; write yours, link it from the PR, and ask the reviewers to comment on the options, not only the code. When a decision crosses teams, it isn't small: propose a design doc.

## Done when
- [ ] it's a small one-way door (a ticket or a design doc otherwise, said so)
- [ ] the context with facts, at least two real options with for and against, each fact with its source and date
- [ ] the decision chosen by the user, with the letter and the date; the consequences and "Revisit when" written
- [ ] the file with the next number, its row in the index, the next number moved on
- [ ] an ADR it reverses marked "replaced by", linked both ways
- [ ] the step documents it changes updated, each with a journal line; the idea it came from names it
- [ ] the counts check passes, every link resolves; one commit

## Sources
- Michael Nygard, [Documenting architecture decisions](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions), 2011.
- [MADR](https://adr.github.io/madr/), Markdown Architectural Decision Records.
- AWS Prescriptive Guidance, [ADR process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html).
- Microsoft, [Maintain an architecture decision record](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record).
- Jeff Bezos, Amazon's 2015 letter to shareholders (one-way and two-way doors).

## Next
Back to the work that raised the decision: the ticket links the ADR, the PR cites it. A decision that turned out big goes to `/design-doc change "<name>"`.
