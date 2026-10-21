---
name: design-doc
description: "One short document a team reads before code. Two uses, one format: the architecture overview of a design that exists (all of Design in one document, linking to the details; elsewhere a system overview, an HLD or a SAD), or a design doc, the proposal for a big change (a new service, a feature that touches many parts, a provider swap, a change to live data), written before code, reviewed by a deadline, decided in writing, then the step documents and ADRs updated. Sections: summary, context and why now, goals and non-goals, requirements with numbers, C4 context and containers, 1–2 flows with failure paths, data, API and old app versions, screens, failures, security and personal data, operations, rollout and rollback, testing and the success metric, scale and cost, drawbacks and alternatives, plan and dependencies, risks, the decision, history; each with when to include it and its arc42 chapter. Use at the end of Design, then for every one-way-door change in Build, after launch or at work. Also: /design-doc change \"<name>\" writes a proposal; /design-doc validate <file> judges an existing one."
argument-hint: "[nothing: the architecture overview] or change \"<name>\" or validate <file>"
---

# Design doc

## When to use it
Two situations, one format:
1. **The architecture overview of a design that exists:** at the end of Design, one document that gathers what steps 01–08 decided, so someone from outside (a reviewer, a new colleague, an investor) understands the system without reading dozens of files. It lives at `docs/02-design/architecture-overview.md`. **The name matters:** in practice "design doc" means the proposal for one change (Ubl), while the view of a whole existing system is called an architecture or system overview, an `ARCHITECTURE.md` in a code repo (Aleksey Kladov, 2021: "the high-level architecture of the project"), or an HLD / SAD (high-level design, solution architecture document) in client projects. There is only ever one overview; it is updated after every approved proposal.
2. **A design doc, the proposal for a change:** any time after (in Build, after launch, at work): a new service, a feature that touches several parts, a provider swapped, a change to data in production, a new need for scale or availability. Written **before** code, reviewed, decided; only then the step documents change and the ADRs are written. Each lives at `docs/02-design/changes/NNNN-<name>.md`.

**The door test** (Jeff Bezos, 2015 letter to shareholders): a decision that is hard to undo (a "one-way door") is made "methodically, carefully, slowly"; one that is easy to undo (a "two-way door") "can and should be made quickly". A one-way door gets a proposal and a review; a two-way door gets a ticket, no document.

**When not to write one:**
- it would take less time to build than to write ("If implementing your idea will take less time than writing it up, you can probably go ahead without an RFC", HashiCorp);
- the solution is clear and has no real trade-offs: the document would only be an "implementation manual" (Malte Ubl, Google);
- the decision is yours alone (Sourcegraph);
- a bug, a screen on an existing API, a small change easy to reverse: a ticket, and an ADR if it is a one-way door.

## The problem it solves
At work nobody delivers 12 files for a new feature. They deliver **one document** the team reads in 15–20 minutes and discusses **before** code, while a change is still cheap. Without it: the review happens on diffs spread over many files and nobody sees the whole idea; the alternatives and reasons are lost, so a year later nobody knows why; security, cost and failures are found after the code, when they are expensive; and nobody knows who decided and when. A proposal without an explicit decision step ends, by default, in "no" (Jacob Kaplan-Moss, "Against RFCs", 2023).

## How to run it
- **The bar:** what a senior engineer or a staff engineer at a well-run company would accept in a design review, in the shortest form that meets it. Name the industry practice so the user learns it: the design doc (Google), the RFC (Uber, HashiCorp, Sourcegraph, Rust), the RFD (Oxide), the KEP (Kubernetes) are the same idea.
- **Teach while you go:** every term gets one line on what it is and what it brings, compared with something a frontend developer knows (a proposal is a big PR's description, written before the code; the step documents are the diff, after the decision).
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, `docs/` in the current folder. The overview goes to `docs/02-design/architecture-overview.md`; proposals to `docs/02-design/changes/`, created with the first one, with a README listing them. At work, use the team's place and template (Confluence, Notion, the client's arc42): the arc42 column below says where each section goes.
- **The proposal is the "why"; the step documents and the overview are the truth now.** A proposal never replaces them: once approved, they are updated and point back to it.
- **Link, don't copy.** The document is short for the reader and links to the details (the requirements file, `schema.sql`, `openapi.yaml`, the ADRs). Ubl: "copy-pasting complete schema definitions should be avoided"; formal definitions "quickly get out of date". No code.
- **Length:** a proposal of 1–3 pages for a change of a few weeks (Ubl's "mini design doc", "especially helpful for incremental improvements or sub tasks"); 10–20 pages only for a new system ("around 10-20ish pages" for a larger project, Ubl); the architecture overview of an existing design, readable in an hour. Sections that don't apply are removed (Squarespace: "Remove sections that are not applicable"), with half a line saying why when a reviewer would expect them.
- **Use what exists:** the C4 drawings and flows already generated by `docs/02-design/diagrams.sh`; a proposal that changes the shape changes the model (`c4/workspace.dsl`) after approval, not before; the proposal shows the new drawing as a draft.
- **The user decides** what the proposal proposes and, at work, who decides and who approves. You write, check and recommend; one decision at a time.

## The header
Title; author; status; created; **comments due by** (3–5 working days: Oxide, "3-5 business days"; Rust keeps a final comment period open "for at least 5 business days"); **decider**; **approvers**, each with yes / not yet / date (Squarespace); other reviewers, who don't block; a security and privacy reviewer when the change touches personal data; the ticket; supersedes / superseded by; links (PRD, ADRs, the step documents it changes).

**Statuses:** draft, in review, approved, rejected, withdrawn (by the author), done (delivered), superseded (by another, linked both ways). Numbers are never reused (as for ADRs, Nygard).

## The sections
A core that is always there (**bold**), the rest only when it applies. The arc42 column says where the section goes in a client's arc42 template.

| Section | What it holds | When | arc42 |
|---|---|---|---|
| **Summary** | 3–5 lines: if someone reads only this, what must they know | always | 1 |
| **Context and scope** | what exists today (facts only, no opinions), what we build, **why now** and what doing nothing costs; the terms the reader doesn't know | always | 1, 12 |
| **Goals and non-goals** | what we want; what could reasonably be a goal but we choose not to make one; what we leave for later | always | 1 |
| **Requirements** | the numbers with their source (people, speed, the availability target measured as an SLO, how much may be lost), the top 3 qualities, the constraints; the short calculation when a number decides the shape | always | 1, 2, 10 |
| **Design: context (C4 level 1)** | the drawing and its relationship table | always | 3 |
| Design: containers (C4 level 2) | the drawing and its table; which parts are new or change | always in the overview; in a proposal when the parts change | 5 |
| Design: components (C4 level 3) | a container's modules | only for a new service with an inner structure that matters | 5 |
| **Design: flows** | 1–2 UML sequence diagrams; their failure paths point to the failure table | always | 6 |
| Design: data | only what changes, in short, linked to the real schema; what is sensitive; how long it's kept and how it's deleted; the migration | when the data changes | 5, 8 |
| Design: API | new or changed endpoints, in short, linked to the contract; **old app versions keep working** | when the contract changes | 5, 8 |
| Design: screens | the screen flow, the states (empty, loading, error, offline), accessibility | when what people see changes | — |
| **What happens when something fails** | one table: every new dependency slow, down or wrong; what the person sees | always | 8, 11 |
| **Cross-cutting concerns** | security and personal data (what data, who has access, which threats, who reviews); the law; monitoring and **operations** (who runs it, the alerts and what to do for each, what support needs to know); AI if any; always, at least as "unchanged, because…" | always | 8, 11 |
| Rollout | where it runs, how it reaches production, **how it is switched off** (a feature flag), **which number triggers a rollback**, the data migration | when what runs or how it runs changes | 7 |
| Testing and the success metric | how we know it works (which tests, which provider is faked); the number that, after launch, says it was worth it, and where it comes from | in a proposal | 10 |
| Scale and cost | what breaks first at 10× and the number that triggers a change; the monthly cost now and at 10× | when load or cost changes | 10 |
| **Drawbacks and alternatives** | why **not** to do it; the reasonable alternatives, always including "do nothing", with what each wins and costs; what others do; the ideas dropped in review and why | always: this is the document's value | 9 |
| Plan and dependencies | the stages, a rough estimate, who does what; who we depend on and whether **they know**, with a name and a date | in a proposal | — |
| **Risks and open questions** | what we don't know yet, who answers, by when | always | 11 |
| **Decision** | the date, the outcome, the conditions ("yes, if…"), the dissent written down, the link to the meeting notes; the ADRs for the one-way doors | always | 9 |
| History | status and design changes, dated; the note after launch | in a proposal | — |

## Steps

### A proposal: `/design-doc change "<name>"`
1. **Number and name:** `docs/02-design/changes/NNNN-<name>.md` (the next number), status "draft".
2. **Summary, context, goals and non-goals first:** if they aren't clear, nothing else makes sense. Ask the user what they don't know yet.
3. **Read what exists:** the step documents the change touches, the ADRs, the PRD. The proposal says only what changes.
4. **The design,** only the sections that apply; for one skipped where a reviewer would expect it, half a line: why.
5. **Drawbacks and alternatives,** with "do nothing" among them.
6. **The header:** who decides, the approvers (the people who will use it, the teams it depends on, anyone who gets extra work from it: Squarespace), the comment deadline, a security and privacy reviewer if it touches personal data.
7. **Validate it** (below), fix what it finds, then status "in review".
8. **Review:** written comments first, until the deadline. A meeting only if the comments don't converge or it is a one-way door: at most ten people, no presentation, the document read at the start (Amazon reads its memos in silence first, a "study hall"), the last 10 minutes for the decision (Squarespace).
9. **Decision:** made by the decider with the approvers; not unanimity: "yes", "not yet" or "yes, if…" (Squarespace); the dissent written in the document, then everyone commits ("disagree and commit", Bezos, 2016). Written in the Decision section; the one-way doors become ADRs.
10. **After approval:** a ticket that links the proposal; PRs cite its number. A small design change during the work is written into the proposal with a history line; a big one becomes a new proposal, with "supersedes / superseded by" in both (Rust: "More substantial changes should be new RFCs, with a note added to the original RFC").
11. **When delivered:** the step documents and the architecture overview updated, each with a journal line pointing to the proposal; every number or rule the change touches found with `grep` across `docs/` and fixed in the same commit (`checks/facts.py` checks the main counts); the C4 model and diagrams redrawn; the team told; status "done".
12. **After launch:** a dated note in History: the success metric reached or not, what was confirmed, what wasn't. Ubl: re-read your own design docs a year or two later.

### The architecture overview: `/design-doc`
1. Read every step README in `docs/02-design/` ("In one page", "Not doing", open questions), the ADRs and the PRD.
2. Write the core and every section that has content, each a few lines with links to the files that hold the detail; use the generated drawings (C4 context and containers, the flows).
3. Check that every number in it matches its source file; where two files disagree, say so and fix the older one with the user's yes.
4. Redo it when a step changes a lot; its header says the date and which steps it reflects.

## Validate mode
`/design-doc validate <file>`: judge a design doc (one written here or a colleague's), change nothing.
1. Read the document and what it links to.
2. Check it against the questions below, citing the lines.
3. Report: findings by severity, each with the line, what's missing and what to change; then what the document does well; then what you couldn't judge. The user picks what to apply.

**The questions:**
- [ ] Does the summary say, in 5 lines, what and why?
- [ ] Is the context facts only, and does it say why now?
- [ ] Are the non-goals written?
- [ ] Do the requirements have numbers with a source, the availability target included?
- [ ] Is the context drawn (C4) with its table, and the containers when they change?
- [ ] Do the flows have their failure paths, and does every new dependency have a row in the failure table?
- [ ] Are security, personal data, the law and operations covered, at least with "unchanged, because…"?
- [ ] Do old app versions keep working?
- [ ] Can it be switched off and rolled back, and at which number?
- [ ] Are testing and the success metric written?
- [ ] Are the drawbacks written, and at least one real alternative plus "do nothing"?
- [ ] Do the dependencies have a name and a date, and do they know?
- [ ] Does the header say who decides, who approves and by when?
- [ ] Is every one-way door an ADR?
- [ ] No code, no copied schema or contract?
- [ ] Readable in 15–20 minutes (a proposal) or an hour (the overview)?

## The bad version and why not
- The document written **after** the code, to tick a box: it changes nothing.
- No alternatives and no drawbacks, only "how we'll do it": it can't be defended in a review.
- No decider and no deadline: the proposal stays "in review" forever.
- A meeting with slides instead of written comments: whoever can't come doesn't contribute, whoever comes hasn't read it.
- 40 pages for a week's change: nobody reads it.
- Only the happy path, no security, operations or failures.
- The schema and the contract copied in: they disagree with the real ones after the first change.
- The proposal approved, the step documents never updated: the "truth" falls behind.

## What breaks if you skip it
Big changes are discussed in pieces, in PRs, when changing them is already expensive. Nobody from outside can understand the system without reading everything. A year later, "why did we choose this?" and "who decided?" have no answer.

## The principle behind it
Trade-offs are written and discussed before code, when a change costs an hour, not a month. The effort follows the door: hard to undo, a careful review; easy to undo, a quick decision. The document is short for the reader and points to the details instead of repeating them. The proposal is the history of "why"; the step documents are the truth now.

## How to apply it at work
Use the team's template and place; the arc42 column says where each section goes, and the validate questions work on any template. For every one-way door, write a short proposal, ask for comments by a date, get a written decision, and turn the decisions into ADRs. When reviewing someone else's proposal, use the same questions. In system design interviews, the same sections, said out loud.

## Sources
Checked on 2026-10-21:
- Malte Ubl, [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/), 2020.
- HashiCorp, [RFC template](https://www.hashicorp.com/en/how-hashicorp-works/articles/rfc-template) and [writing practices](https://www.hashicorp.com/en/how-hashicorp-works/articles/writing-practices-and-culture).
- Gergely Orosz, [Scaling engineering teams via RFCs](https://blog.pragmaticengineer.com/scaling-engineering-teams-via-writing-things-down-rfcs/) (Uber).
- Squarespace, [The power of "yes, if"](https://engineering.squarespace.com/blog/2019/the-power-of-yes-if) and [their template](https://slab.com/library/templates/squarespace-rfc-template/).
- Sourcegraph, [RFCs](https://raw.githubusercontent.com/sourcegraph/handbook/main/content/company-info-and-process/communication/rfcs/index.md).
- Rust, [RFC template](https://github.com/rust-lang/rfcs/blob/master/0000-template.md) and [process](https://github.com/rust-lang/rfcs/blob/master/README.md).
- Kubernetes, [KEP template](https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/README.md).
- Oxide, [RFD 1](https://rfd.shared.oxide.computer/rfd/0001).
- Michael Nygard, [Documenting Architecture Decisions](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions), 2011.
- Jeff Bezos, letters to shareholders: [2015](https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm) (the doors), [2016](https://www.sec.gov/Archives/edgar/data/1018724/000119312517120198/d373368dex991.htm) ("disagree and commit"), [2017](https://www.sec.gov/Archives/edgar/data/1018724/000119312518121161/d456916dex991.htm) (memos read in the meeting).
- Aleksey Kladov, [ARCHITECTURE.md](https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html), 2021.
- Jacob Kaplan-Moss, [Against RFCs](https://jacobian.org/2023/dec/1/against-rfcs/), 2023.
- Google SRE, [Reliable product launches](https://sre.google/sre-book/reliable-product-launches/).
- arc42, [docs.arc42.org](https://docs.arc42.org/home/); C4, [c4model.com](https://c4model.com/).

## Done when
**A proposal:**
- [ ] the header complete: status, comment deadline, decider, approvers, a security and privacy reviewer when personal data is touched, the ticket
- [ ] the core sections written; every other section present or skipped with half a line where a reviewer would expect it
- [ ] drawbacks and at least one real alternative, plus "do nothing"
- [ ] the validate questions passed
- [ ] the decision written; the one-way doors as ADRs
- [ ] after delivery: the step documents updated with journal lines pointing back, the diagrams redrawn, status "done"

**The architecture overview:**
- [ ] the core and every section with content, each linking to the file that holds the detail
- [ ] every number matches its source file
- [ ] the C4 context and containers and the main flows shown
- [ ] readable in an hour

## Next
Planning, after the overview. A proposal leads to its ticket and its slice.
