---
name: brain-daily
description: Daily second-brain update - integrate the capture queue and the last 24 hours from connected tools, extend existing notes, supersede changed facts, update today's daily note, decisions, hot.md, indexes and log, then report. Use on its daily schedule, or when the user says "run the daily", "update the brain now", "integrate my captures".
---

# brain-daily

Shared rules: `../_shared/contracts.md` (all sections, especially §3 decay, §4 daily = state, §6 queue, §7 write discipline). Read it and the brain's `AGENTS.md`, `context/config.md`, `hot.md` first.
Unattended run: no questions, no confirmations. Anything needing the user goes in the report.

**Automated-run marker**: first command of the run `touch .claude/automated-run` (the protect hook then blocks writes to context/); last command `rm -f .claude/automated-run`, also after a failure. On-demand runs started by the user skip the marker.

## Scheduling
Run from the brain root at `daily_time` (desktop scheduled task or cloud routine; the brain must be a synced git repo for cloud). Prompt: "Run the brain-daily skill on this brain." 

## 0. Budget and path
Budgets from config (`budget_reads`, `budget_writes`). Count as you go; when one runs out, stop that workstream and log what is left as `queued`.
**Short path**: `python3 queue.py list --status new` is empty and connectors show nothing new in 24 h → do not touch the daily note or hot.md; append one log line ("daily | nothing new") and report. Stop.

## 1. Gather before reasoning
In one batch, read: new queue entries; for each connector in `config.md` `connectors`, the last 24 h (meeting transcripts first, then calendar, CRM, project tool, email, chat). Keep only what is new or changed. Apply the test: evergreen knowledge (decisions, facts about clients, offer, strategy, lessons) is stored; changing operational data (single emails, CRM rows, payments, thread contents) is not, the connector stays the source.

## 2. Integrate each item (queue entries first, oldest first)
For each entity, fact and decision:
1. `python3 brain.py search "<entity or topic>"`; open the best match. Extend it; create a note only when nothing matches (frontmatter per §2, file name kebab-case).
2. Changed fact → rewrite it in place with date and source; if the old version had decision context keep it under `## History`; or mark the old note superseded (§3). Never leave two active versions.
3. Decision → `decisions.md` (`## date decision`, `Why:`, `Replaces:`), and a one-line link in the related project's about.md.
4. `certainty: hypothesis` → never an active fact: add it under `## Open questions` in the related note, or a `status: draft` note.
5. Open loops → the project's about.md (next step) or `notes/ideas.md`. Before adding a task, check it has not already been done (sent mail, document status, a later note). [Sales OS completion check]
6. `verbatim` lines → under `## Quotes` in the related note with the date. If one shows a voice pattern, propose it for `context/voice.md` in the report.
7. Anything that belongs in `context/` → do not write it; list it under "Proposed context edits" in the report.
8. After each write, read the file back and confirm the content is there; retry once, else report it (§7.2).
9. Set the queue status: `python3 queue.py set <id> integrated "<touched notes>"` or `rejected "<reason>"`.

**Uncaptured-session stubs** (facts start with "UNCAPTURED session"): if the transcript path is readable, extract from it as brain-capture would and integrate; else reject with "transcript unavailable". Skip trivial sessions with "rejected: nothing to capture".

## 3. Today's daily note (state, §4)
`notes/daily/<today>.md` with frontmatter `type: log`. Create it once if missing; otherwise edit the relevant section in place (`## Done`, `## Decisions`, `## Meetings`, `## Open loops`). Only items dated today. No timestamps per run, no "second pass" blocks. Nothing new for it → leave it untouched.

## 4. Close the run
1. `python3 brain.py index`.
2. Rewrite `hot.md` (max 500 words): priorities, open loops, decisions of the last 7 days. Rewrite, never append.
3. `python3 brain.py lint` and fix issues in files you touched this run (frontmatter, broken links). Leave the rest to brain-lint.
4. Append to `log.md`: `## [date] daily | <n> captures, <m> connector items | touched: <notes>`; plus `## [date] queued | <what is left>` if a budget ran out.
5. If the brain is a git repo: `git add -A && git commit -m "brain: daily <date>"`.

## 5. Report (the run's only output to the user)
Short sections, empty ones omitted: What changed (note → change) · Decisions logged · Needs you (conflicts between active notes, rejected captures, failed writes) · Proposed context edits · Queued for next run · Health score from lint.
Respect `proactivity` in config: observer and advisor never send messages or emails; drafts only.
