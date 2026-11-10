---
name: brain-lint
description: Weekly health check of the second brain - run brain.py lint plus judgment checks (contradictions, near-duplicates, stale claims, undigested sources, root map accuracy), fix the safe issues, list the rest, record the health score; on the first run of a month also consolidate. Use on its weekly schedule, or when the user asks to clean up, audit, lint or check the brain.
---

# brain-lint

Shared rules: `../_shared/contracts.md`. Read it, the brain's `AGENTS.md` and `context/config.md` first.
Principle: fix small things directly, ask before anything big, never delete. [guide §5, Ben AI optimizer]
Scheduled run: from the brain root at `lint_day` `lint_time` with `BRAIN_AUTOMATED=1`, prompt "Run the brain-lint skill on this brain." Unattended: questions go in the report.

## 1. Script checks
`python3 brain.py index`, then `python3 brain.py lint`. Note the health score (before).
Fix directly, up to `budget_fixes`, then log the rest as `queued`:
- missing frontmatter field: derive it from the note (type from folder, summary from first paragraph, `updated` from git log or today);
- broken link: repoint to the note that clearly matches (renamed file, alias); if none is clear, list it;
- superseded without `superseded_by`: find the newer note via search; else list it;
- orphan: add a link from the most related note (project about.md, entity) when the relation is obvious; else list it;
- folder without index, AGENTS.md over 60 lines, hot.md over 500 words: re-index; shorten hot.md; for AGENTS.md propose cuts in the report (never rewrite rules unasked);
- daily note with repeated sections or per-run blocks: merge into one section each.
- over-300-line note: propose a split in the report.

## 2. Overdue reviews (`review_by` passed)
For each: if a connector holds the live value (price, CRM stage, invoice), check it. Same → bump `updated` and `review_by` (contracts §3). Different → rewrite with date and source, or supersede. No way to check → list under "Confirm with you". Context notes: never edit, list them.

## 3. Judgment checks (sample by budget, most recently updated first)
- **Contradictions**: two active notes stating different values for the same fact (price, date, owner, status). Prefer the newer `updated` only if its source is newer; otherwise list both. [Ben AI F8.1, Karpathy lint]
- **Near-duplicates**: same entity in two notes (similar titles, aliases, same client). Propose a merge (target note, what moves); merge directly only when one is a stub with nothing unique.
- **Stale claims**: a project, entity or concept claim contradicted by a newer decision or daily note. Rewrite it, keep the old wording under `## History` with a link to the newer note. Context notes: propose only. [Ben AI F8.3]
- **Undigested sources**: files in raw/ or wiki/sources/ with no note citing them in `sources:`, or a source whose entities were not updated. List what should be updated. [Ben AI F2.8]
- **Missing pages**: an entity or concept linked or named in 3+ notes without its own note. Propose creating it.
- **Root map accuracy**: every folder in the brain appears in AGENTS.md "Where things live", and every line there still matches reality. Propose fixes.
- **Queue**: entries still `new` after 2 days (lint lists them) → report; do not integrate here (brain-daily owns it).
- **Retrieval pressure**: a folder index over ~150 notes, or repeated "not found" in log.md → suggest in the report: split the folder index first; a local search tool next; vector search or a graph tool (e.g. Graphify, run read-only on a copy as a diagnostic) only if that fails and evals show relation-type misses. [Nate's level ladder]

## 4. Monthly consolidation (first lint run of the month)
1. Projects with no update in 30 days → list them and ask whether to archive (never archive unasked).
2. Summarise last month's `notes/daily/` into `notes/daily/YYYY-MM.md` (type log: main events, decisions, lessons), then move those dailies with `git mv` (or `mv`) to `archive/daily/`.
3. Re-read context/ against last month's decisions; propose edits in the report.

## 5. Close
1. `python3 brain.py index`, `python3 brain.py lint`: health score (after).
2. Append to log.md: `## [date] lint | health <before> -> <after>, <n> fixed, <m> for you | touched: <notes>`. The score history in log.md is how the trial of the health score is judged.
3. Git commit if the brain is a repo: `brain: lint <date>`.
4. Report, empty sections omitted: Fixed · Needs your decision (contradictions, merges, archives, deletions) · Confirm with you (overdue reviews) · Proposed context and AGENTS.md edits · Queued · Health before → after.
