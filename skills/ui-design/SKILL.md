---
name: ui-design
description: "What people see and do: the screens, before the code. Who uses the product, where and on what; the map of every screen and the navigation, from the PRD's features; the main flows with their failure paths; the states a screen can be in (empty, loading, error, partial, offline, waiting, refused, read-only); the words, with a text for every error code; the visual direction and the design tokens, checked for contrast; the components with their states and keyboard; accessibility to WCAG 2.2 AA; screen sizes, the installed app and the speed people feel; the key screens in full and a test with people. The shared parts and the key screens in Design, every other screen one slice ahead of its code. Writes a folder: a README, one file per topic, one file per area's screens, wireframes and mockups as HTML pages checked by programs, the tokens, flow diagrams, and the big choices as ADRs. Use after the API design, before Planning; at work before a new screen or flow, a change that touches many screens, a new design system or an accessibility audit. Also: /ui-design slice <n> designs one slice's screens before its code; /ui-design validate <folder> judges an existing one."
argument-hint: "[the product or the change], slice <n>, or validate <folder>"
---

# UI design

## When to use it
After Architecture, almost in parallel with the data model and the API (04–06); once the API exists, after it, since every screen shows what an endpoint gives and every error code becomes a sentence on a screen. It needs the PRD's features, criteria, journeys and build order (and the prototype's results, if there was one), the system design's speed targets and what people see when a part fails, compliance's screens and texts (consents, minimum age, export, deletion, AI labels, source credits, the words never used), the architecture's routes, component library, languages, accessibility and testing, the data model's data on the device and its outbox states, and the API's answers and error catalog. **Before the first screen is coded:** a drawn screen changes in minutes, a built one in days, and a state missing at launch is found by the people using it.

Then once per slice in Build (`/ui-design slice <n>`), one slice ahead of the code: that slice's screens in full.

At work: a feature with screens; a flow that loses people (the funnel shows the step); a change that touches many screens (a colour, the buttons, a font); a new design system, or one nobody uses; an accessibility audit (the European Accessibility Act applies from 28 June 2025); a PR with a new component. Also in the first days at a new company: the design system (in Figma or in code) shows which components exist and how the product talks, before the code.

## The problem it solves
The API design said what every endpoint gives and which errors it can return. No document said what people see: which screens the app has and how they get from one to another; what the main screen shows the first time, with nothing in it; what it shows while loading, offline with three unsent entries, or when the server refuses one (how `subscription.read_only` reads on the screen, in each language); how many taps it takes to log a meal; how it looks on a 360 px phone with the text doubled, and on a desktop; whether someone using VoiceOver can use it; which colours, fonts and buttons the whole product has.

Without an answer, each component decides its screen in the first PR: five shades of green, three kinds of button, a spinner that spins forever offline, a blank screen on the first opening, "Error 422" instead of a sentence, a 20 px button nobody hits with a thumb at the gym, a translated label that overflows its button. And the missing states are found by the people using it.

UI design decides **what people see and do**: the map of screens and the navigation, the main flows with their failure paths, every screen with its data and all its states, the words (a sentence for every error code included), accessibility, how it looks at every size, and a small design system, the tokens and the components, that the code follows.

## How to run it
- **The bar:** do what a senior product designer or the head of design at a well-run company would accept, in the simplest form that meets it. Use the real industry method and name it, so the user learns it. Say what you leave out and why.
- **Teach while you go, starting from the problem.** The user may be a frontend developer: the screens are home ground, the decisions around them aren't. **Before any tool, file or check, say what problem it prevents, in a situation a frontend developer has lived** (the designer sent only the full screen, and the empty and loading states were invented in code; the green in Figma wasn't the green in the code; a list showed `undefined` when it was empty). Only then how it works; a "why" gets one sentence of purpose, never more "how". Every term gets one line on what it is, compared with something a frontend developer knows: `isPending`, `isError` and `data` in TanStack Query are already three of a screen's states; a toast after saving is already a status message; the variables in Tailwind 4's `@theme` are already tokens; shadcn/ui copied into the repo is already a small design system; the route tree is already the information architecture; a Playwright test is a flow, written after the code instead of drawn before it. **At a technical chunk, plain words and one example with numbers come first,** then what it means for the user; the tables after, or only in the file. A sentence that can be read two ways is settled with options A/B before anything is written.
- **One step per message, and big steps in chunks.** Show a step, wait for the user's OK, then the next. Steps 3, 5 and 8 are big: one area or one sub-topic per chunk; **count the chunks before announcing them** and say so if the count changes; save and commit each chunk once it's confirmed, **added to its file, never by rewriting the file** (`>>`, not `>`): after saving, the diff shows no line removed from the earlier chunks. Why: each decision needs to land before the next one builds on it; on MacroMate, from step 3's chunk 3 on, each save of the map erased the earlier chunks, and only their commits saved them.
- **Ask only when there's a real choice.** When all the arguments point one way and no realistic alternative fits, write it as decided, with its arguments, and move on to the next real choice. Ask when there are at least two options the user could reasonably pick; once chosen, the choice is final. When the user voices a fear or a doubt next to a choice, resolve it before recording the decision.
- **Before recommending, weigh two things besides the technique:** what most of the industry does, and what serves the user's purpose (what they'll meet at work counts as a real argument). When the options are technically equal, say so first and recommend on those grounds. Change a recommendation only for a new fact, and name the fact.
- **Every number, size and rule with its argument:** a known standard (named, its official page checked on the web), a target set earlier (cited: the PRD's 44 px, the system design's 0.1 s), or a guess marked `[ASSUMPTION]` with its reasoning. For a choice, an argument card: why; the main alternative and who uses it; when the alternative is better; what someone may answer, and the reply; the source. When the industry is split (validating on submit or on leaving a field; a bottom bar or a hidden menu), name the camps. Why: the user must be able to defend each choice in a design review or a technical discussion.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Write into `docs/02-design/06-ui-design/` and the ADRs into `docs/00-project/adr/`; create them if they don't exist.
- **Read first:** the PRD (`docs/01-discovery/04-prd.md`: features, criteria, journeys, the build order, the non-goals, the features after the MVP), the prototype if it exists, the system design (`docs/02-design/01-system-design/`: the speed targets, offline, what people see when each part fails), the compliance folder (the consent screens and their exact texts in `drafts/`, the words never used, AI labels, credits, the accessibility level), the architecture (`docs/02-design/03-architecture/`: the routes, the frontend's rules, the component library and the stack, accessibility, testing, the size budget, **what it left for UI design**), the data model (`docs/02-design/04-data-model/`: the data on the device, the outbox states and their texts, the display rules, **the questions it left for UI design**), the API design (`docs/02-design/05-api-design/`: the endpoints and their answers, the states inside answers, the error catalog, **its open questions for UI design**), and the ADRs. Search every earlier folder for "UI design" and "06". Ask only what's missing.
- **An existing app is a source of facts, not a model.** Read it for which screens exist, the navigation, the colours and fonts, what people use. A screen doesn't become right because it's there.
- **The routes, the component library, accessibility and testing come from the architecture; the data on the device from the data model; the answers and errors from the API; the legal texts from compliance; this step decides what people see.** Don't change a route, a table or an endpoint here; if one is wrong or missing, stop, say so, and on a yes fix it where it lives, with a journal line. **The same for the PRD and compliance:** any change, even a text that only closes a gap, is shown to the user first with its exact text.
- **Only the MVP's features.** What the PRD puts after the MVP doesn't appear on a screen, not even as "coming soon"; nor does anything compliance or the DPIA bans (streaks, nudges to eat less).
- **Two forms of the design, each with its reader** (chosen on 2026-10-14). The purpose in one sentence: **the screens are drawn in a form a program can open and check, so a contrast too low, a 30 px button, a text that overflows at 360 px or a missing state is found now, not in Build.**
  - **markdown, for people:** the map, the flows, every screen's data, states and texts, the rules, each with its **why**; the user reads and approves this;
  - **HTML pages, for eyes and programs:** wireframes in gray (what's on the screen and in what order) and mockups with the real tokens (how it looks), one page per screen, and per state that changes the layout, opened in a browser at the narrowest width and at the desktop width, **checked by the page check** (axe and our own rules for what axe doesn't see) and by **the contrast check on the tokens**, both in "The checks". The pages are throwaway drawings, not the production code; what the code reuses is the tokens file.
  - **The pages are made by scripts, not written by hand:** one script per screen writes its wireframes, a page per state, in every language, with the content worked out by the PRD's formulas (on MacroMate, 2,230 kcal for the PRD's example person; a recipe from 689 to 500 kcal), never invented; **the mockups are made from the approved wireframes** by one script: the same HTML, the grey stylesheet pointed at the tokens, the visual direction on top, so a mockup can't drift from what the user approved. Why: 30 wireframe pages and 24 mockups on MacroMate; a change to a shared part (the bottom bar, the status line) is one edit, like a component instead of a copy in every file. A designer does the same in Figma with components.
  - **At work, when a designer owns the screens** in Figma (or Penpot), this step writes the rest (the map, the flows, the state tables, the texts, the tokens' names, which are the same in the tool and in the code) and links the frames instead of drawing HTML.
  - Not a design tool alone, here: nobody would draw the screens, and nothing would check a frame against the tokens the code uses. Not markdown alone: nobody sees a screen before it's built.
- **The shared parts and the key screens in Design, every other screen one slice ahead of its code** (chosen on 2026-10-14). Design writes what every screen shares and what Planning needs: the context, **the map with one line per screen** (its address, feature, data source, the states that apply, the components it uses), the flows, the state patterns, the voice and the shared texts, the visual direction and the tokens, the base components, the accessibility rules, the sizes and speed, and **3–5 key screens in full**, with mockups. Each slice's other screens are designed in full by `/ui-design slice <n>` before that slice's first line of code. Why: product teams usually design one cycle ahead of development (Desirée Sy, Autodesk, 2007); screens change after the tests with people at the end of slices, and a screen drawn months before its code goes stale. Planning estimates the other screens from their map lines (data, states, components counted), marked rougher, and refines them per slice. The alternative (every screen as a wireframe now) wins when every screen must be estimated exactly up front (a fixed-price client project) and the PRD won't move.
- **The user decides** the map and the navigation, with the key screens (step 3), every real choice in the key screens (step 5), the visual direction (step 7), the test with people (step 11) and every ADR (step 12); in a slice, every real choice in its screens. You give the options and a recommendation; they choose. One decision at a time.
- **A number about the documents is counted by a script before it's written** (the screens, the pages, the rules, the pairs), and the script is run again at the check. On MacroMate, four counts made by hand were wrong and had reached the README's summary: 46 screens for 56, 41 in their slice for 47, 34 wireframe pages for 30, 8 rules for 7.
- **Check the standards on their official pages,** not from memory: WCAG 2.2 and its Understanding pages, the WAI-ARIA Authoring Practices Guide, the platforms' guidelines (Apple, Material), the framework's and the libraries' versions, the browsers' support. **Write "tried" only for what a test proved,** and keep every script in `checks/`. **A check is tried on planted mistakes** (a text/background pair under 4.5:1, a 30 px button, a field without a label, a focus hidden by a fixed bar), **one per rule**, each expected to be caught, and on a correct page where nothing must be found; a tool downloaded for the check (axe-core, a browser for Playwright) is named with its size and asked for first.
- **UML activity diagrams** for the flows, written as PlantUML (`.puml` next to its `.svg` in `diagrams/`): one per main flow, **drawn at step 4**, each with a title and a legend; each screen an action with its number and address, a choice the person makes as a decision, the failure paths as notes beside their screen. `docs/02-design/diagrams.sh` (set up by `/docs-setup`) draws every diagram of the design from text, in a standard notation (decided 2026-10-20), so they read the same at any company; never a hand-made SVG, a home style, or a script that draws SVG itself. The flow tables in `03-flows.md` and the diagrams say the same words. Open each one, and every HTML page, before committing: no text overlaps, nothing is cut off.
- **A number or a rule decided earlier changes everywhere at once** (decided 2026-10-21, after a whole-design check found ~160 stale mentions left behind by later steps): before committing, `grep` all of `docs/` for the old value and its wording (the number, the name, the phrase) and fix every place in the same commit, or say why one stays (a journal line keeps what was true that day; a past count kept on purpose goes into `docs/02-design/checks/facts-history.txt`). `diagrams.sh` runs `checks/facts.py`, which counts the main facts from their sources (tables, addresses, threats, secrets, screens, ADRs, alerts) and stops on a document that states another number; a new fact that many files repeat gets a line in it.
- **What isn't here:** the tables and the endpoints (04 Data model and 05 API design), the full legal texts (02 Compliance; here only where they appear), the session's length, CSRF and security headers (07 Security), what the AI does and its prompts (08 AI design; here how its result looks and its label), the public website and the pricing page (Launch), the components' code (Build, per slice).

## The states of a screen
Use this at steps 3, 5 and in every slice. Scott Hurff ("the UI stack", 2015): every screen has five states, **ideal, empty, error, partial and loading**, and the empty one comes in three kinds: first use, after the person cleared everything, and no results. An app that works offline has three more, and one with a subscription or roles one more:

| State | What the person must learn | Example |
|---|---|---|
| Ideal | — | the main screen with four meals |
| Empty, first use | what this is and what to do first | the first opening |
| Empty, done | that they finished, not that something broke | a shopping list all ticked |
| No results | what to try instead | a search with nothing: scan the barcode, or add a new food |
| Loading | the first time, the shape of the content; on a refresh, the old data stays | a 30-day report |
| Partial | that there's little data, without the screen looking broken | a weight chart with two weigh-ins |
| Error | what happened and what they can do now | the AI doesn't answer: add it by hand |
| Offline, waiting | that it's saved on the phone and how many wait for the network | "3 to send" |
| Refused | that the server didn't take a change, why, and what to do | "Not saved", the reason translated, fix or delete |
| Read-only, no right | what they can and can't do, and how to unlock it | after the trial: see, correct, delete, not add |
| Long content | nothing, if the screen is right | the longest name, a thousand rows, the text doubled at 360 px |

## Navigation
Use this at step 3.

| Kind | Worth it when | Weak at |
|---|---|---|
| A bottom bar (navigation bar) | three to five top-level sections used often, on a phone (Material 3, Android's guidance) | more than five doesn't fit |
| A sidebar or navigation rail | wide screens: desktop, tablet | takes width on a phone |
| A hidden menu (hamburger, drawer) | many sections, rarely used | hidden navigation is used less and later (NN/g, 2016: 179 people, six sites) |
| Tabs at the top | parts of the same thing | not for different sections |
| A side panel with its own address | a detail opened over a list that stays visible | without an address, Back leaves the page |

## How finished a drawing is
A **wireframe** (gray, real content) decides what's on the screen and in what order, cheap to change; a **mockup** decides how it looks, expensive to redo, so only once the wireframe is accepted; a **prototype** links mockups so a flow can be tried with people. The order matters: a discussion about a button's colour on a screen whose flow is wrong is time lost.

## Tokens
Use this at step 7. A token is a named design decision kept once and used everywhere. **Three levels,** the usual pattern (Atlassian, Salesforce, most design systems): **primitives** are the values (`green.600 = oklch(…)`), **semantic** tokens say what for (`color.text.success = {green.600}`), **component** tokens say where (`button.primary.background = {color.action.primary}`). The code uses only the last two. Why: a dark theme changes only the semantic links, not every component; a new brand colour changes in one place.

The file: one file a program reads. The **Design Tokens Format Module 2025.10** (the W3C community group's first stable version, October 2025; a community report, not a W3C standard: a `.tokens.json` file, converted to CSS variables by Style Dictionary 5) when a design tool or several platforms read the tokens; **the stack's own CSS variables** (Tailwind 4's `@theme`) when only the web app does. Either way the contrast check reads that file.

**The contrast check:** every text/background pair the screens use, in every theme, against 4.5:1 for text and 3:1 for large text and for UI parts (WCAG 1.4.3, 1.4.11); a colour with a meaning (a nutrient, a grade, an error) never stands alone (WCAG 1.4.1). How it runs is in "The checks".

## Component libraries
Use this at step 8; the architecture usually chose already.

| Kind | Examples | Worth it when |
|---|---|---|
| Styled | MUI, Ant Design | an internal admin, fast; their look is hard to make yours |
| Headless | Base UI (1.0, December 2025), Radix, React Aria Components, Headless UI, Ark UI | your look, with the keyboard and ARIA done by someone else |
| Copied into the repo, over a headless one | shadcn/ui (Base UI by default since July 2026; Radix and React Aria also) | the code is yours, with your tokens; you bring the updates |
| Your own, from scratch | IBM Carbon, Shopify Polaris (web components since October 2025), GOV.UK Design System | a company with a design system team; years of work |

**A component is shared** when two screens use it; otherwise it stays next to its screen until a second one needs it. Every shared component has: its variants and sizes, its states (default, hover, focus, pressed, disabled, loading, error), its keyboard behaviour and **its pattern from the WAI-ARIA Authoring Practices Guide** (dialog, combobox, tabs, listbox, disclosure), its touch target, and the library piece it starts from.

## Accessibility
Use this at step 9 and in every slice. **WCAG 2.2** (W3C Recommendation, October 2023, republished December 2024 with corrections only; also ISO/IEC 40500:2025; WCAG 3.0 is still a draft). The criteria that touch a screen most often:

| Criterion | Level | Asks |
|---|---|---|
| 1.4.3 Contrast | AA | 4.5:1; 3:1 for large text (at least 18 pt, or 14 pt bold: ~24 px and ~18.5 px) |
| 1.4.11 Non-text contrast | AA | 3:1 for a field's border, an icon, a chart's lines |
| 1.4.1 Use of colour | A | the meaning isn't in the colour alone |
| 1.4.4 Resize text | AA | up to 200% without losing anything |
| 1.4.10 Reflow | AA | at 320 px wide, no sideways scrolling |
| 1.4.12 Text spacing | AA | nothing breaks at line height 1.5×, paragraphs 2×, letters 0.12×, words 0.16× the font size |
| 2.1.1 Keyboard | A | everything works with the keyboard alone |
| 2.4.7 Focus visible, 2.4.11 Focus not obscured | AA (2.4.11 new in 2.2) | the focus shows, and isn't entirely hidden by a fixed bar or a banner |
| 2.5.7 Dragging | AA, new | every drag has a single-pointer alternative |
| 2.5.8 Target size (minimum) | AA, new | 24×24 px, or enough space around |
| 3.2.6 Consistent help | A, new | the help link sits in the same place on every screen |
| 3.3.7 Redundant entry | A, new | what was typed once in a process isn't asked again |
| 3.3.8 Accessible authentication | AA, new | no memory or calculation test to log in; pasting a password works |
| 4.1.3 Status messages | AA | a message that appears is announced without moving the focus (`aria-live`) |
| 2.3.3 Animation from interactions | AAA | motion started by an action can be turned off (`prefers-reduced-motion`) |

- **axe finds about 57% of WCAG problems** (its maker, Deque); some of the rest a script of our own can find ("The checks"), the others need a person with the keyboard and a screen reader, so every slice gets a manual pass from a written checklist.
- **"No ARIA is better than bad ARIA"** (the Authoring Practices Guide): the WebAIM Million 2026 found more errors on pages with ARIA (59.1 on average) than without (42). The right HTML element first.
- **Screen readers** (WebAIM survey 11, 2026): on phones VoiceOver 72%, TalkBack 30%; on desktops JAWS 55%, NVDA 33%. Test with VoiceOver on an iPhone and TalkBack on an Android at least.
- **The law:** the European Accessibility Act (Directive (EU) 2019/882) applies from 28 June 2025 to some services, e-commerce among them (any online sale of a product or a service); **micro-enterprises providing services are exempt** (fewer than 10 people and turnover or balance sheet up to €2 million). Its standard, EN 301 549, has a version 4.1.1 aligned with WCAG 2.2 (September 2026). Compliance decides the level; this step applies it.

## The checks
Use this at steps 5, 7, 9, 11 and in every slice. Two scripts in `checks/`, written for the project: the skill describes the rules, the scripts live with the pages they check.

**The page check** opens every HTML page in the installed Chrome (playwright-core, ~13 MB, no browser downloaded) at six settings: 320 px (WCAG 1.4.10's width), the narrowest phone supported (360 px), that phone with the text at 200% (1.4.4), the desktop (1280 px), the phone set to dark, and 1.4.12's spacing applied. At each, **axe** (axe-core, ~3 MB: WCAG 2.0–2.2, A and AA, `target-size` on) and **our own rules for what axe doesn't see:**

| Rule | Finds | Why axe misses it |
|---|---|---|
| `target` | a button, link or field under the target the PRD chose (a link inside a sentence exempt, as in WCAG) | axe asks 24 px (2.5.8) |
| `visible-label` | a field without a visible `<label>` | axe accepts a placeholder as a field's name, and a placeholder disappears as one types (3.3.2) |
| `sideways` | the page wider than the window | axe doesn't resize the window |
| `cut-off` | a text or a control past the window's edge | a fixed bar too wide doesn't make the page scroll, so `sideways` misses it |
| `clipped` | a text cut by a box that hides what overflows, with the spacing on | axe doesn't change the spacing |
| `obscured` | an element with the focus entirely under a fixed bar (2.4.11) | axe doesn't move the focus |
| `must-see` | an element a PRD criterion needs (`data-must-see`) below the first screen at 360 px | a criterion, not a WCAG rule |

What counts as visible is asked of the browser (`checkVisibility`): a button inside a closed `<details>` isn't. **Each rule gets its planted page,** and a correct page gets nothing; each page says what it expects (`<meta name="expect" content="cut-off">`), and a miss or an extra fails the run. On MacroMate (2026-10-15/16) axe alone caught 3 of the 9 planted mistakes; our rules caught the other 6; `must-see` had no planted page. A page that only shows other pages side by side (the directions compared) says `<meta name="checks" content="skip">`.

**The contrast check** reads the tokens file (no download: WCAG's formula is a few lines): every text/background pair the screens use, in every theme. **When the theme follows the phone and a switch in Settings, the dark values are written twice** (`@media (prefers-color-scheme: dark)` and `[data-theme="dark"]`): the check compares the two copies, since a colour changed in one passes unseen. Planted: a tokens file with bad pairs and one difference between the copies.

**In Build,** where the architecture runs axe in the end-to-end tests, propose our rules next to it, with the exact text for the architecture's file shown to the user first.

## Touch, reach and waiting
Use this at steps 8 and 10.

| Who | Target size |
|---|---|
| WCAG 2.5.8 (AA) | 24×24 px |
| WCAG 2.5.5 (AAA) | 44×44 px |
| Apple, Human Interface Guidelines | 44×44 pt by default, 28×28 pt minimum, on iPhone |
| Google, Material 3 | 48×48 dp, 8 dp between targets |

- **Reach:** Steven Hoober (2013) watched 780 people touching their phones: 49% held it in one hand, 36% cradled it and tapped with the other, 15% used both hands. The main action sits low, where the thumb reaches; a destructive one sits away from it.
- **Waiting** (Jakob Nielsen, 1993): under 0.1 s feels instant; under 1 s the train of thought holds; around 10 s attention goes, so beyond a few seconds show progress. A skeleton helps for waits between 1 and 10 s, not under 1 s (NN/g, 2023); a file upload gets a progress bar. The often-quoted "400 ms" (the Doherty threshold) isn't in the 1982 IBM paper, which asks only for "subsecond". Core Web Vitals (Google, at the 75th percentile): LCP under 2.5 s, INP under 200 ms, CLS under 0.1.
- **Optimistic updates:** for a write the app keeps locally (offline), the screen shows the change at once and marks it waiting; it undoes it, with the reason, only when the server refuses (React 19's `useOptimistic`, TanStack Query's `onMutate`).

## Rules every screen follows
Use this at steps 5, 6, 8, 9 and in every slice. Found on MacroMate's drawings (2026-10-15/16); the first three with the text enlarged.
- **Tap targets in px, text in rem, the root's size never in px.** A finger doesn't grow with the text: the 44 px minimum written as 2.75rem became 88 px at 200%, and five of them (440 px) didn't fit a 360 px bar. A root in px (`html { font-size: 16px }`) ignores the text size the person chose in the browser.
- **Every fixed bar leaves room for itself:** `scroll-padding` the bar's measured height, so Tab never leaves the focus under it (W3C's technique C43, for 2.4.11). **When the text is large for the screen, a bar of actions stops sticking:** at 200% a sticky bar of actions took a third of the phone. A container query in `rem` follows the text's size, not only the window's: on MacroMate under 15rem of width, since a 360 px phone is 22.5rem wide at 100% and 11.25rem at 200%. W3C's technique C34 un-fixes bars the same way, with a media query in px, which follows only the window.
- **Every word wraps:** `overflow-wrap: break-word` on the page, so a long word in a heading at 200% doesn't make the page wider than the phone.
- **Never a minus for "left":** past a target, "81 kcal over", not "−81 kcal left": the sign is one character, missed at a glance, and the sentence is a double negative. Found on the drawing, not a standard.
- **One status line at a time, the most urgent first:** offline, a trial ending and an entry not saved, stacked, push the content off the first screen and are announced together. Material and GitHub's Primer have the same rule for banners: one per page.
- **No link inside a checkbox's label:** on a phone the tap meant to tick opens the link, or the reverse; the links sit next to the box. The industry is split: Shopify's checkout puts the terms' links in the label; Coloplast's design system and a WebAIM discussion move them out, which is the choice here.

## Forms and words
Use this at steps 6 and 8.
- **When to validate, two camps:** GOV.UK validates on submit ("do not validate when the user moves away from a field"), with an error summary at the top that takes the focus, the message next to the field, and the page title starting with "Error:"; Baymard validates when the person leaves a field, not earlier, and removes the error as they fix it (31% of the sites it studied don't validate inline at all). The first fits long forms filled in rarely by anyone; the second short forms used often. Both: the message says what happened and how to fix it, without "invalid" or "please", and what the person typed stays.
- **The right keyboard:** `inputmode="decimal"` for grams, `autocomplete` on names, emails and passwords, a label above every field.
- **Error texts:** one per error code in the API's catalog, in every language; the code itself never shows.
- **Plurals and formats:** some languages have more than two plural forms (Romanian has three: "1 aliment", "2 alimente", "20 de alimente"), so a text with a number is an ICU message, never pieces glued together; numbers, dates and units through `Intl`. MessageFormat 2.0 is stable in Unicode CLDR 47 (March 2025); `Intl.MessageFormat` in JavaScript is still at TC39 stage 1. CSS logical properties (`margin-inline-start`) work in 97% of browsers and leave room for a right-to-left language.
- **A glossary,** the same as the PRD's: one word for one thing, on every screen and in every language.

## The installed app (PWA)
Use this at step 10, for a web app installed on the home screen.
- iPhone: notifications since iOS 16.4, only for an app added to the home screen and only after a gesture; Safari deletes a site's stored data after 7 days of use without visiting it, but a home-screen app has its own count; since iOS 26 every site added to the home screen opens as an app. **Safari has no install prompt** (`beforeinstallprompt` is Chromium only), so on iPhone the install is explained on a screen.
- Android: the install prompt, offered after a moment of value, never on the first opening.
- Both: the safe areas (`env(safe-area-inset-*)`) under the notch and the home bar; the app's icon, name and colours in the manifest; persistent storage asked once (the data model says when).
- **The manifest's `id` written explicitly, from the start:** without it the browser takes the `start_url` as the app's identity, so moving the start address later makes every installed copy a different app, left behind; with a fixed `id`, a new manifest is an update of the same app (MDN). A one-way door (step 3).

## Steps

### 1. Read what exists
The PRD, the prototype, the system design, compliance, the architecture, the data model, the API design and the ADRs, as in "Read first"; collect **every question the earlier steps left for UI design** in one list. List what's missing and ask only that.

**If an app exists,** read it for facts: the screens, the navigation, the colours and fonts. Not as a model.

### 2. Who uses it, where and on what
The people from the PRD and their **worst moments** (one hand at the gym, in a shop, in a dark kitchen, on a weak signal, at a desk), how often they open it, the devices and the narrowest width, the browsers, the languages, the accessibility level, installed or in a browser. Usually decided already by the PRD and compliance: then write it as decided, with the reasons.

### 3. The map of screens and the navigation
Per area (one chunk per area, counted first): **every screen in the product, one line each:** its address (from the architecture's routes), what it's for, the PRD feature, where its data comes from (an endpoint, or the device's table: zero requests), offline or online only, who sees it (a person, an admin, a read-only account), the states that apply, the components it uses, and **when it's designed: now (a key screen) or in slice N** (the PRD's build order).
- **every PRD criterion reaches a screen, or a written reason; every screen serves a feature:** no screen "we may need";
- **the navigation** on the phone and on the desktop: what's in the bar, how the person goes back, what opens as a panel with its own address;
- **count the taps** for the main tasks (a known food added to a meal; the PRD's main journey with its time target), from the map;
- **mark the one-way doors:** addresses that leave the app (in emails, notifications, bookmarks: a confirmation, an invite, an export) keep working forever, and so does the installed app's identity (the manifest's `id`);
- **propose the 3–5 key screens,** each with why: the entry screen (the most used), the main screen of the hardest flow, a screen whose decisions shape the design system (a form, a long list), the desktop layout.

**The user decides** the map, the navigation and the key screens. Planning estimates from these lines.

### 4. The main flows
One per PRD journey, plus the way in (sign-up, consents, age, the first questions, the first main screen). Each with a named person (from the PRD's journeys), the steps screen by screen, **the failure paths** (offline, a slow or failing outside service, a payment being confirmed, an expired link, a read-only account) and where the person comes in from (an email, a notification, the home screen). Draw each as a diagram now.

### 5. The key screens, in full
One chunk per key screen. For each:
- **the wireframe** (gray, real content: the longest name in the reference data, zero, a thousand rows, the language with the longest words), one HTML page per state that changes the layout, written by the screen's script;
- what it's for; **the data and where it comes from**, field by field; the actions;
- **the state table:** every state from the patterns that applies, with what it shows and its text;
- **every criterion of its features tried on the screen** ("can the person see what's left of today's protein without scrolling?");
- opened in a browser at the narrowest width and the desktop width, and with the text at 200%; the page check passing.

**The user decides** each real choice.

### 6. The words
The voice (plain, no guilt, nothing medical: compliance's banned words); the glossary; **the texts of the states shared by every screen** (offline, waiting, refused, read-only, the generic error with its request id) and **of the error codes every screen can get** (the shared ones: not logged in, too many requests, update required), in every language; plurals, numbers and dates through `Intl`; where the legal texts, the AI labels and the source credits appear (the exact texts come from compliance). Each module's own error codes get their texts with their screens: the key screens now, the rest in their slice.

### 7. The visual direction and the tokens
First **2–3 directions** drawn on the real main screen (colour, type, density), side by side; **the user decides.** Then the tokens on three levels: colours (light and, if wanted, dark), the type scale, spacing, radii, shadows, motion durations; the system's fonts or downloaded ones (against the architecture's size budget); the app's icon and the manifest's colours. **The contrast check runs on the tokens file,** tried on planted bad pairs, and passes in every theme.

### 8. The components
From the map's lines and the key screens: the base components (every one at least two screens use), each with the details in "Component libraries"; the shared patterns: forms (when to validate, from the two camps, with the argument card), lists ("Load more"), a dialog against a side panel, toasts, a confirmation against an undo after deleting, the empty states. One chunk per group. New components come with their slices.

### 9. Accessibility
The WCAG criteria applied to this product: the focus order, where the focus goes after a dialog closes or the screen changes, what's announced, a text alternative for every chart, an alternative for every drag, the focus never under a fixed bar, the text at 200% and the screen at 320 px. How it's checked: **now,** the page check on every HTML page ("The checks"), each rule tried on its planted page; **in Build,** what the architecture decided (axe in the end-to-end tests, with our rules proposed next to it; the contrast test; the target-size test), plus **the manual checklist for a slice, written here** (keyboard only; VoiceOver on an iPhone; TalkBack on an Android; the text at 200%; reduced motion).

### 10. Screen sizes, the platform and the speed people feel
The widths (from the content, not from devices: the narrowest the PRD supports, the desktop breakpoint) and what changes on a desktop; the installed app (the install on Android and the instructions on iPhone, the safe areas, the icon); a dark theme or not; **what people feel:** optimistic updates for local writes, a skeleton only for waits between 1 and 10 s, progress for long operations, motion off when the phone asks.

### 11. The key screens' mockups, and a test with people
The key screens as mockups with the tokens, made from their approved wireframes, in every theme, at both widths, the page check passing, opened in a browser. **The test with people:** if the riskiest flows weren't tried with people in Discovery, propose a test with 5 people on linked mockups of those flows (the tasks, the pass mark set before, for example 4 of 5 without help), run as a risk test (`/risk-tests`), **before the code of the first slice that builds those flows**, not before every slice; **the user decides** yes or no. What a mockup can't show (an AI's answer, the camera) is tested on the real app after its slice.

### 12. The big decisions become ADRs
Only one-way doors (for example the addresses that leave the app and the manifest's `id`, the token structure the code depends on, a navigation model that shapes the routes). First propose the list, with **what doesn't get an ADR and why** (most choices of look change easily). When a decision was already taken in the steps, write the ADR and give it to the user to check, a few at a time; otherwise one at a time, **the user chooses**. After each ADR, re-read the earlier files it changes.

### 13. Check it
- every PRD criterion reaches a screen, or has a reason; every screen has a line in the map with its slice;
- every count in the README matches the files, the counting script run again;
- every key screen has its data with their source, its state table, its texts and its pages;
- every outbox state and every subscription or role state appears on a screen;
- the shared error codes have their texts in every language;
- the tokens pass the contrast check in every theme; every HTML page passes the page check;
- no feature after the MVP and no banned word on a screen; the legal texts match compliance word for word;
- every question the earlier steps left for UI design is answered;
- nothing contradicts the architecture, the data model, the API design, compliance or the PRD.

Run the check with a **separate agent** that has only the documents (`/ui-design validate <folder>`), then verify its findings in the files before showing them: it can be wrong. Look especially for **contradictions left by a changed decision**, above all in files the step didn't touch. Tell the user upfront how long it usually takes (15–20 minutes) and that there's nothing for them to do meanwhile. Show the verified findings by severity with a recommendation; a rule that changes in another step's document is shown with its exact new text before it's written.

Write as you go: each step's file once the user confirms it, with a journal line in the README; **the README's summary, "not doing" and glossary grow with the steps**, not at the end. At the end, set this step's row in `docs/02-design/README.md` to done, with the date, and link the folder.

## A slice's screens
`/ui-design slice <n>`, in Build, **before the slice's first line of code** (one slice ahead: while slice N is built, slice N+1's screens are designed).
1. **Read** the slice's features in the PRD's build order, the map's lines for its screens, the endpoints they call, the flows that pass through them, and **what changed since Design**: the earlier slices, the tests with people, the journal.
2. **Each screen in full,** as the key screens were (step 5): the wireframe, the data and their source, the actions, the state table, the hardest content, every criterion of its features tried on it; one chunk per area; **the user decides** each real choice.
3. **The texts** of every error code its endpoints return, and of its states, in every language.
4. **The components** it needs: from the inventory, or new, with their states, keyboard and pattern; tokens only, no new values.
5. **The checks:** the page check on its pages, the contrast check if the tokens changed, each page opened at both widths and with the text at 200%; the manual checklist ready for the end of the slice.
6. **Update** the map (the line becomes "designed"), the inventory, the README's journal; the slice's screens are checked by a separate agent against the same list as step 13, for these screens only.

```
docs/02-design/06-ui-design/
  README.md            the entry: status, summary, files, what we skip, open questions, ADRs, glossary, journal
  01-context.md        02-map.md            03-flows.md
  04-states.md         05-words.md          06-visual.md
  07-components.md     08-accessibility.md  09-sizes-and-speed.md
  10-checks.md
  screens/             one file per area: the key screens now, the others in their slice
  tokens/              the tokens file the code reads
  wireframes/          the gray pages (HTML), one per screen and per state that changes the layout; the script per screen that writes them
  mockups/             the key screens with the tokens (HTML), made from the wireframes by a script
  diagrams/            the flows (.puml + SVG)
  checks/              the scripts: the page check (axe and our rules), the contrast check, their planted pages
docs/00-project/adr/
  NNNN-[title].md …
```

The README:

````markdown
# UI design – [Product]
| | |
|---|---|
| **Status** | draft / confirmed by [who], [date]; slices designed: [n] |
| **Author** | |
| **Updated** | |
| **Next** | 07 Security; each slice's screens with /ui-design slice <n> |
## In one page
The people and their worst moments, screens per area and the key ones, the navigation, the main choices: 5–6 lines.
## The files
| File | What it answers |
## Not doing, and why
| Not doing | Why | It comes back when |
## Open questions
| Question | Answered by | When |
## Decisions (ADRs)
| ADR | Decision |
## Glossary
- **Term:** what it is, compared with something the reader already knows
## Journal
- [date]: [what was decided, by whom, what it changed]
````

Each topic file starts with `# NN – [Topic]` and a link back to the README, then:

| File | Holds |
|---|---|
| `01-context.md` | `\| Person \| Worst moment \| Device and width \| Language \|`; the browsers, the accessibility level, installed or not |
| `02-map.md` | per area `\| Screen \| Address \| Feature \| Data from \| Offline \| Who \| States \| Components \| Designed \|`; the navigation; the taps per main task; the one-way doors; the key screens with why |
| `03-flows.md` | per flow: the person, the steps, the failure paths, the diagram |
| `04-states.md` | the shared patterns: `\| State \| What it shows \| Text \| Component \|` |
| `05-words.md` | the voice, the glossary, `\| Code or state \| Text (each language) \| What the person can do \|` |
| `06-visual.md` | the direction chosen and why; the tokens per level, with why; the contrast results |
| `07-components.md` | `\| Component \| Variants \| States \| Keyboard and pattern \| Target \| From \|`; the shared patterns |
| `08-accessibility.md` | the criteria applied, the focus rules, what's announced, the manual checklist |
| `09-sizes-and-speed.md` | the widths, the desktop, the installed app, the theme, what people feel per kind of wait |
| `10-checks.md` | the checks now and in Build, each tried on planted mistakes |
| `screens/[area].md` | per screen: what it's for, the data `\| Field \| From \| Why \|`, the actions, the states `\| State \| Shows \| Text \|`, the criteria tried, links to its pages |

And one file per decision in `docs/00-project/adr/NNNN-[title].md`, with the same sections as every ADR: status, date, context, options (for and against), decision, consequences, revisit when.

## Validate mode
`/ui-design validate <folder>`: judge an existing UI design (documents, a design file, or a running app's screens), change nothing.
1. Read the folder, its pages, its ADRs and the README's journal, the PRD, compliance, the architecture, the data model and the API design; the running app's screens if they exist.
2. Check the template and "Done when" item by item, citing the lines; run the contrast check and the page check on the pages.
3. Then ask: does every PRD criterion reach a screen? Does every screen have its data source and its states? Is any state missing (empty, offline, refused, read-only)? Does any error code show as a code? Is any value written outside the tokens? Is anything said by colour alone? Is any target under the chosen size? Does a feature after the MVP or a banned word appear? Is every term explained? **Then the decisions that changed during the steps:** is the old version still written anywhere, above all in files the step didn't touch?
4. Report: findings by severity, each with the line, what's wrong and what to change; then what's done well; then what you couldn't evaluate. The user picks what to apply.

## The bad version and why not
- Only the ideal screen drawn: the empty, loading, error and offline states are invented in code, each differently.
- One screen per table: screens that look like the database, not like what the person wants to do.
- "Error 422", or the server's message, on the screen: the person doesn't know what to do, and the server's text is in one language.
- Colours and sizes written into components (`#22c55e`, `p-[13px]`): five greens, and a dark theme becomes impossible.
- Meaning in colour alone (green good, red bad): about 1 man in 12 can't tell red from green (nidirect, Northern Ireland's government).
- A `div` with `onClick` instead of a `button`: the keyboard and the screen reader don't see it.
- ARIA everywhere "to be accessible": pages with ARIA have more errors than pages without (WebAIM Million 2026).
- A full-screen spinner on every request: offline it spins forever, and the person can do nothing.
- Lorem ipsum and short names: the first real food name breaks the line.
- The whole menu behind a hamburger on a phone: what's hidden is used less, and later.
- A big design system before the screens: components nobody uses.
- "1 foods": plurals have more forms than two in many languages.
- Accessibility "at the end": the base components rebuilt, so every screen.
- Streaks and notifications that push to eat less: banned by the DPIA and by the rules for minors.
- The cancel button hidden: consumer law asks it to be as easy as subscribing.
- Screens drawn in a tool with colours that aren't the code's tokens: the screen in the code never matches the drawing.

## What breaks if you skip it
Every screen is decided by the first PR that touches it, with whatever components and colours exist that day. The API's error codes have no texts, so every one becomes "Something went wrong". Planning can't estimate screens nobody listed. The navigation's problems are found by the testers at the end of a slice, after the slices are built. And accessibility added afterwards means the base components rebuilt, so every screen.

## The principle behind it
**Design for the hardest moment, not for the demo.** The screen is used with one hand, at the gym, on a weak signal, with the text enlarged, by someone who has never seen the app; if it works there, it works everywhere. It's Microsoft's Inclusive Design principle, "Solve for one, extend to many": what works for someone with one hand works for someone holding a shopping basket. And Nielsen's first heuristic, the visibility of system status, is why an app that works offline needs its states: the person must always know whether the meal is saved, waiting for the network or refused. A design without its states is just a picture.

## How to apply it at work
- At a new company: walk the main flows as a new user, once with the keyboard only and once with VoiceOver; read the design system and count how many screens use it.
- In code review, for a new screen: where are the empty, loading, error and offline states? Tokens, or values written by hand? Does it work with Tab? Does the text fit at 200%? Does every error code have a text in every language?
- With a designer: ask for the states and the long content before the coloured mockups; give them the error catalog; the tokens' names in Figma (its variables) are the code's names.
- As a senior or a head of engineering: a design system with an owner, a rule for who adds a component, and a count of the screens that use it; accessibility in the definition of done and in CI, plus a manual pass; a test with people for every big flow; the European Accessibility Act once the company isn't a micro-enterprise; usability measures (tasks completed, time on task, SUS, average 68) next to the product's metrics.

## Done when
Design:
- [ ] the people, their worst moments, the devices and widths, the languages, the accessibility level
- [ ] the map: every screen with its address, feature, data source, states, components and slice; every PRD criterion reaches one or has a reason; the navigation; the taps per main task; the one-way doors; the key screens; chosen by the user
- [ ] every main flow with its failure paths, drawn as a UML activity diagram by `diagrams.sh`, its texts the same as its table
- [ ] every key screen in full: wireframe pages, data with their source, the state table, the texts, the criteria tried; chosen by the user where there was a choice
- [ ] the voice, the glossary, the texts of the shared states and shared error codes in every language
- [ ] the visual direction, chosen by the user; the tokens file on three levels; the contrast check passing in every theme, tried on planted pairs
- [ ] the base components and the shared patterns, each with its states, keyboard and pattern
- [ ] the accessibility rules, the checks with each rule tried on its planted page, the manual checklist for a slice
- [ ] the widths, the desktop, the installed app, the theme, what people feel per kind of wait
- [ ] the key screens' mockups, at both widths and in every theme, the page check passing; the test with people proposed, and decided by the user
- [ ] every one-way door an ADR, chosen by the user; the earlier files re-read after each one
- [ ] every question the earlier steps left for UI design answered
- [ ] a glossary for every term the files use, grown with the steps
- [ ] the README: status, summary, what we skip and why, open questions, the ADR table
- [ ] the row in `docs/02-design/README.md` set to done

Each slice:
- [ ] every screen of the slice in full, its map line marked designed, before the slice's first code
- [ ] the texts of its error codes and states in every language
- [ ] its components in the inventory; no value outside the tokens
- [ ] the page check and the contrast check passing; the pages opened at both widths and at 200%
- [ ] checked by a separate agent; the README's journal updated

## Sources
1. W3C, [WCAG 2.2](https://www.w3.org/TR/WCAG22/) (2023, republished 2024), [what's new in 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/), [ISO/IEC 40500:2025](https://www.w3.org/WAI/news/2025-10-21/wcag22-iso); [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/); techniques [C43, scroll-padding](https://www.w3.org/WAI/WCAG22/Techniques/css/C43) and [C34, un-fixing sticky headers and footers](https://www.w3.org/WAI/WCAG22/Techniques/css/C34); Josh W. Comeau, [The Surprising Truth About Pixels and Accessibility](https://www.joshwcomeau.com/css/surprising-truth-about-pixels-and-accessibility/).
2. European Union, [Directive (EU) 2019/882](https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng) (art. 2, 3(23), 3(30), 4(5)); ETSI, [EN 301 549](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/), V4.1.1, 2026.
3. Apple, [Human Interface Guidelines: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility); Google, [Material 3: structure](https://m3.material.io/foundations/designing/structure), [48 dp targets](https://support.google.com/accessibility/android/answer/7101858), [Android navigation patterns](https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-and-nav-patterns), [Material banners](https://material.io/components/banners); GitHub, [Primer banner](https://primer.style/product/components/banner/guidelines); Shopify, [checkout checkbox](https://shopify.dev/docs/api/checkout-ui-extensions/2025-07/components/forms/checkbox); Coloplast, [checkbox](https://designsystem.coloplast.com/latest/build/components/form-fields/checkbox/usage-and-guidelines-D4koILyy); WebAIM, [links in a label](https://webaim.org/discussion/mail_message?id=37249).
4. Scott Hurff, [Why your user interface is awkward: you're ignoring the UI stack](https://www.scotthurff.com/posts/why-your-user-interface-is-awkward-youre-ignoring-the-ui-stack/), 2015.
5. Nielsen Norman Group: [10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/), [Response Times](https://www.nngroup.com/articles/response-times-3-important-limits/), [Test with 5 Users](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/), [Hidden navigation on mobile](https://www.nngroup.com/articles/find-navigation-mobile-even-hamburger/) and [its method](https://www.nngroup.com/articles/hidden-navigation-methodology/), [Skeleton Screens 101](https://www.nngroup.com/articles/skeleton-screens/).
6. W. J. Doherty and A. J. Thadani, [The Economic Value of Rapid Response Time](https://web.archive.org/web/2015/http://www.vm.ibm.com/devpages/jelliott/evrrt.html), IBM, 1982; Google, [Web Vitals](https://web.dev/articles/vitals).
7. Steven Hoober, [How Do Users Really Hold Mobile Devices?](https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php), 2013.
8. Design Tokens Community Group, [Format Module 2025.10](https://www.designtokens.org/tr/2025.10/format/); [Style Dictionary and DTCG](https://styledictionary.com/info/dtcg/); [Tailwind CSS v4](https://tailwindcss.com/blog/tailwindcss-v4).
9. [shadcn/ui changelog](https://ui.shadcn.com/docs/changelog); [Base UI releases](https://base-ui.com/react/overview/releases); [React Aria](https://react-spectrum.adobe.com/react-aria/); Brad Frost, [Atomic Design](https://atomicdesign.bradfrost.com/chapter-2/); [GOV.UK Design System](https://design-system.service.gov.uk/); [Shopify Polaris](https://github.com/Shopify/polaris); [IBM Carbon](https://github.com/carbon-design-system/carbon).
10. GOV.UK, [validation](https://design-system.service.gov.uk/patterns/validation/), [error messages](https://design-system.service.gov.uk/components/error-message/), [Prototype Kit](https://prototype-kit.service.gov.uk/); Baymard Institute, [Inline form validation](https://baymard.com/research-articles/inline-form-validation).
11. [axe-core](https://github.com/dequelabs/axe-core) (57%, `target-size` off by default); WebAIM, [The WebAIM Million](https://webaim.org/projects/million/), [Screen Reader User Survey #11](https://webaim.org/projects/screenreadersurvey11/), 2026.
12. Unicode, [CLDR 47 and MessageFormat 2.0](http://blog.unicode.org/2025/03/unicode-cldr-47-release-messageformat-2.html); TC39, [Intl.MessageFormat](https://github.com/tc39/proposal-intl-messageformat); [Can I use: CSS logical properties](https://caniuse.com/css-logical-props).
13. WebKit, [Web Push on iOS 16.4](https://webkit.org/blog/13878/), [7-day storage cap](https://webkit.org/blog/10218/), [storage quotas](https://webkit.org/blog/14403/), [home-screen web apps in iOS 26](https://webkit.org/blog/17333/); MDN, [beforeinstallprompt](https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeinstallprompt_event), [the manifest's `id`](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/id).
14. John Brooke, "SUS: A quick and dirty usability scale", 1996; Jeff Sauro, [Measuring Usability with the SUS](https://measuringu.com/sus/), 2011.
15. Desirée Sy, [Adapting Usability Investigations for Agile User-Centered Design](https://uxpajournal.org/?p=1523), Journal of Usability Studies, 2007.
16. Microsoft, [Inclusive Design](https://inclusive.microsoft.design/); nidirect, [Colour vision deficiency](https://www.nidirect.gov.uk/conditions/colour-vision-deficiency-colour-blindness); React, [useOptimistic](https://react.dev/reference/react/useOptimistic).

## Next
Security (`/security`) checks what 01–06 decided: the session, the limits, CSRF, Row-Level Security. Then AI design (`/ai-design`), for products with AI. In Build, before each slice's code: `/ui-design slice <n>`.
