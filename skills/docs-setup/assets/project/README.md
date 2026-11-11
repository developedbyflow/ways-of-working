# 00 Project

| | |
|---|---|
| **What this is** | the entry to the project-wide documents: what belongs to the whole project, not to one phase, and every phase writes to |
| **Updated** | |

## What's here

| Part | What it holds | Who writes it | Who reads it |
|---|---|---|---|
| [`ideas.md`](ideas.md) | every feature idea since the first brainstorm, each with its ID (F-01…, the next free one in its header): the MVP in the PRD's dependency order, the rest in priority buckets, what was merged, moved or dropped, each with why | /brainstorm writes it, the PRD sorts it, every Design step adds what it decides not to do now and drops what it rules out; Planning and Build sort it again | the PRD (its MVP and its "Out of scope"), the Design steps' "Not doing", the ADRs, Planning |
| [`adr/`](adr/README.md) | the architecture decisions, one hard-to-undo decision a file, and their index with the template, the statuses and the change rule | the Design step that makes the decision; later, an approved design doc in `02-design/09-architecture-overview/changes/` | every step, the architecture overview, Build, a reviewer |

## The rules they share
- **An ID or a number is given once and never reused:** the next free idea, the next ADR; a tombstone or a replaced ADR keeps its number, so every link to it still leads somewhere. An ID says nothing about priority or phase.
- **Every change is dated:** `(added <date>)` or `(corrected <date>: it said …)` in the text; an ADR's header has one Updated line listing them; `ideas.md` has its History.
- **Nothing is deleted:** a dropped idea stays under "Dropped" with its date and the decision that forbids it; a decision that flips is a new ADR, and the old one is kept, marked replaced, linked both ways.
- **Other documents cite them by ID or number** (F-11, ADR-0007), never by a position or a range.

## How `changes/` relates to `adr/`
A big one-way door after Design (hard to undo and touching several parts) is first a design doc in step 09's `changes/`, reviewed and decided before code. Once it's approved, its one-way doors are written here as ADRs, each linked to the proposal, and an ADR it reverses is kept as replaced. A small one-way door is only an ADR. An idea that leads to a change keeps its F-number in the proposal and in the ADR.

## Journal
- <date>: created by /docs-setup.
