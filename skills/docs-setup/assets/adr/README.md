# Architecture decisions (ADRs)

| | |
|---|---|
| **What this is** | the index of the project's architecture decisions: one-way doors only (a choice that costs a migration, a rewrite or a move of paying users to undo), one decision a file, from every Design step |
| **Updated** | |
| **Next number** | 0001 |

**The numbers:** each ADR gets the next number (`NNNN-short-title.md`) when it's written and keeps it for good; a number is never reused, not even for a decision that's replaced. A two-way door (reversible in a day) is no ADR: its step's file says it.

**The template:** the ADR template in the [`system-design` skill](https://github.com/developedbyflow/ways-of-working/blob/main/skills/system-design/SKILL.md) (`# ADR-NNNN: [Decision]`, just before its "Validate mode"; step 14 says what's a one-way door): status, date, updated, context, options, decision, consequences, revisit when.

- **Date:** `- **Date:** <date> (decided in <step>)`: the day it was decided and the step that decided it; when it was written down on another day or in another step, that follows (`decided in 03 Architecture; written 2026-10-13`, `03 Architecture, written in 04 Data model`); a decision two steps share names both (`03 Architecture → 07 Security`).
- **Statuses:** **accepted**, or **replaced by ADR-NNNN**: the old one keeps its file with a link to the new one, and the new one says which it replaces, linked both ways.

**The change rule:**
- **A dated addition that keeps the decision is allowed:** in the text `(added <date>)` or `(corrected <date>: it said …)`; in the header, one line, `- **Updated:** <date>: <what changed>; <date>: …; the decision doesn't change.`
- **A decision that flips is a new ADR** that replaces the old one, linked both ways; the old one is never edited into the new decision. Nygard keeps the old one "but mark it as superseded" ([Documenting architecture decisions](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions), 2011); AWS: "When the team accepts an ADR, it becomes immutable", a new one supersedes it ([ADR process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)); Microsoft: "The ADR serves as an append-only log" ([Maintain an ADR](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)) (all read 2026-11-11). MADR, an open ADR template kept on GitHub (Markdown Architectural Decision Records), dates a record "when the decision was last updated" ([MADR 4.0](https://adr.github.io/madr/), read 2026-11-11), so it expects records to be updated. **Why we allow the dated additions, which AWS and Microsoft don't**: the ADRs were written in Design, before the code, and later steps measured their guesses (the data's size, the addresses' count); a new ADR for each number would bury the decisions under copies. Theirs wins on a team, where an accepted record is a signed agreement; ours keeps the facts current and the decision untouched, and the Updated line shows every change.
- **A big one-way door** (hard to undo and touching several parts) is first proposed as a design doc in `docs/02-design/09-architecture-overview/changes/` (`/design-doc change`); its ADRs are written when it's approved. A small one is only an ADR. After Design, a small one-way door (one library, one format, one module's choice) is written directly with `/adr "<the decision>"`, which adds its row here.
- **Every new ADR adds its row below** in the same commit, and the next number moves on (`checks/facts.py` checks both).

## The decisions

| # | Decision | Status | Decided in | Last change |
|---|---|---|---|---|
