# Brain contracts (shared by every brain-* skill)

Every skill reads this file instead of keeping its own copy. Source of each rule in brackets.

## 1. Layout (frozen after setup) [guide §4]
```
AGENTS.md  CLAUDE.md (one line: @AGENTS.md)  hot.md  decisions.md  log.md  evals.md  brain.py
context/    me.md business.md icp.md offer.md voice.md config.md   canonical, human-owned
projects/<name>/about.md                                           entry point per project
clients/  people/                                                  one file per entity
notes/daily/YYYY-MM-DD.md   notes/inbox.md   notes/ideas.md
wiki/  wiki/sources/        syntheses and source summaries
raw/  archive/              read-only (hook-enforced)
evals/results/YYYY-MM-DD.md  eval runs (not notes, not indexed)
.claude/settings.json  .claude/hooks/{protect.sh,session-end.sh}  queue.py
```
Every folder with 2+ notes has a generated `index.md` (`python3 brain.py index`). Never hand-edit an index.
Heavy working material (video rushes, tool-specific skills) lives outside the brain.

## 2. Frontmatter [guide §4.2]
```yaml
title: Acme Corp
type: entity          # context|entity|project|concept|source|decision|log|inbox
status: active        # active|superseded|archived|draft
created: 2026-03-02
updated: 2026-11-07   # bump on substantive edit or re-confirmation, never on read
review_by: 2027-05-07 # updated + review_days[type] from config.md
importance: 3         # 1-5
supersedes: ""        # "[[old-note]]"
superseded_by: ""
sources: []           # ["[[2026-11-07-acme-call]]"]
aliases: []
summary: One line, answer first. Copied into the index.
```
File names: kebab-case; dated notes start with the ISO date. Any number in a note carries its date and source inline, e.g. `1 200 EUR/month (offer.md, 2026-11-07)`. [Ben AI conventions]
Wikilinks `[[note]]` on first mention of an entity. A project is linked by its folder name: `[[borel-renewal]]` → `projects/borel-renewal/about.md`.
Source of a fact from onboarding: `(setup brain dump, YYYY-MM-DD)`.

## 3. Decay [guide §5.1]
Settings live in `context/config.md` (Decay section), never in skills or code:
- `decay_half_life`: days for a note type's recency weight to halve (0 = no decay). Defaults: project 30, entity 180, concept and source 365, log 7, inbox 3, context and decision none.
- `decay_status_mult`: score multiplier by status (superseded 0 = never returned).
- `decay_weights`: weights of relevance, recency, importance in the search score.
- `review_days`: set `review_by` = `updated` + this many days when writing a note (decision and source: none).
brain.py reads the first three at every run; skills read `review_days`.
- When a fact changes: rewrite the note in place, or set the old note `status: superseded` + `superseded_by`. Never two active versions. Moving it to archive/ (`git mv`) is done in interactive runs; automated runs list the move in their report (archive/ is write-protected).
- A curated claim contradicted by newer material: rewrite it, keep the old wording under `## History` with the date and a link to what superseded it. [Ben AI F8.3]
- Past `review_by`: still usable, but say "as of <updated>" and check the live connector if one exists.

## 4. Daily note = state [Ben AI operator, decision 3]
`notes/daily/YYYY-MM-DD.md`, sections `## Done`, `## Decisions`, `## Meetings`, `## Open loops`.
- Does not exist → create it once. Exists and new content → edit the right section in place. Nothing new → do not touch it.
- Never add per-run blocks ("second pass", timestamps). Run narration goes to log.md.
- Only items dated today. Older open items live in the project's about.md or `notes/ideas.md`.

## 5. log.md, hot.md, decisions.md [guide §4.2, §5; Ben AI conventions]
- log.md is append-only: `## [YYYY-MM-DD] <op> | <subject> | touched: a, b` with op in setup|capture|daily|lint|ask|evals|queued.
- A run that changes what the brain knows logs. A run that only produces a deliverable does not. A run that found nothing logs one line saying so.
- hot.md: at most 500 words, rewritten (never appended) by brain-daily: priorities, open loops, this week's decisions.
- decisions.md: append `## YYYY-MM-DD <decision>` + `Why:` + `Replaces:` (if any).

## 6. Capture queue [Florian's /os-capture, decision 4]
`notes/inbox.md`, one section per entry, managed by `queue.py` (never edit statuses by hand):
```
## q-20261110-1432 | new
- date: 2026-11-10
- source: claude-code          # claude-code|claude.ai|other
- session: <id or short title>
- certainty: fact               # fact|hypothesis (hypothesis = mostly exploratory)
- entities: acme-corp; pricing
- facts: Acme accepted 1 200 EUR/month from January (call 2026-11-10)
- decisions: Drop the starter tier | why: under 5% of revenue, high support load
- open_loops: send Acme the contract
- verbatim: "We stop the starter tier, it costs more than it brings."
- result:
```
`verbatim`: 1-3 exact user sentences worth keeping for voice, or empty. brain-daily stores `hypothesis` entries as draft notes or open questions, never as active facts.
Statuses: `new` → `integrated` (result = touched notes) or `rejected` (result = reason). Only brain-daily integrates.

## 7. Write discipline (all writing skills)
1. Search first: `python3 brain.py search "<entity or topic>"`; extend the best match, never create a near-duplicate.
2. After each write, read the file back and confirm the new content is there; retry once, then report. [Ben AI operator]
3. Respect the run budget in `context/config.md`; put what is left in log.md as `queued`.
4. Never delete; propose deletions in the report.
5. Automated runs (marker file `.claude/automated-run`, or env `BRAIN_AUTOMATED=1`) never write to context/, raw/, archive/ (hook-enforced). Propose context edits in the report.
6. Live data (email, CRM, payments) is read through connectors, not copied in. Only insights are stored. [guide §2, Nate]
7. After creating or renaming notes: `python3 brain.py index`.

## 8. config.md keys
`timezone, daily_time, lint_day, lint_time, connectors[], budget_reads, budget_writes, budget_fixes, proactivity (observer|advisor|assistant|partner), queue (inbox), capture_confirm (false)`. Skills read values here; never hard-code them. [Ben AI conventions; Cole proactivity levels]
