# HANDOFF — skill lab (2026-11-10)

Branch: `claude/vigilant-pasteur-flvf9w` (repo FloWsl/second-brain-os). Lab root: `skill-lab/`.
Rules: `AGENTS.md`. Plan: `PLAYBOOK.md`. Every decision with its reason: `log.md` (newest first).

## Status
| Stage | Output | State |
| --- | --- | --- |
| 1 Inventory | `analysis/00-inventory.md` | done (Ben AI copies removed, `sources/benai/DUPLICATES.md`) |
| 2 Cards | `analysis/cards/{benai,cole-medin,nate-herk,french}.md` | done; Karpathy only as outline (`sources/karpathy/llm-wiki-summary.md`) |
| 3 Matrix | `analysis/01-matrix.md` + decisions 1-9 in log.md | done |
| 4 Design | `analysis/02-design.md` | done |
| 5 Build | `build/skills/` (6 skills + `_shared/`), `build/install.sh`, `build/INSTALL.md` | done |
| 6 Evals | `sandbox-brain/`, `evals/cases.md`, `evals/results/2026-11-10.md` | 6/6 pass, fixes applied |
| Install | `build/install.sh` tested in a fake HOME (install, refusal without --force, backup outside skills/) | ready |
| Real trial | — | **next** |

## What the system is
One markdown brain folder; `AGENTS.md` (≤60 lines) + `hot.md` are the only files read at start; generated `index.md` per folder; frontmatter with status/updated/review_by/importance; decay settings in `context/config.md`.
- brain-setup: interview / brain dump → layout + core context files (no placeholders), grill mode.
- brain-capture (/done): sub-agent writes one queue entry in `notes/inbox.md` (certainty, verbatim), never edits notes.
- brain-daily: single writer; integrates queue + connectors, supersedes, daily note = state, hot.md, report.
- brain-lint: brain.py checks + judgment checks, safe fixes, health score before/after, monthly consolidation.
- brain-ask: ranked search with decay, freshness judgment, files syntheses back on OK.
- brain-evals: cases from the brain's `evals.md` on a disposable copy.
Code: `brain.py` (init, index, search, lint, health), `queue.py`, hooks `protect.sh` (raw/, archive/ always read-only; context/ during automated runs via `.claude/automated-run`), `session-end.sh` (stub if no /done).

## Real trial plan (2 weeks, Florian)
1. Install: `cd skill-lab/build && ./install.sh` (see `build/INSTALL.md`).
2. New empty folder (do NOT point at the existing personal-os yet), brain-setup with a real brain dump; git init + private remote.
3. Week 1: work in the brain folder, `/done` after real sessions, run brain-daily by hand each morning, read its report.
4. When the reports look right: schedule brain-daily and brain-lint; add 2-3 connectors to config.md.
5. Week 2: brain-lint on Friday; write 5 real cases in the brain's `evals.md` (one per thing it got wrong); run brain-evals.
6. Bring back to the lab: brain-daily/lint reports, log.md health lines, evals results, anything confusing. Next lab session fixes and re-runs `evals/cases.md`.

## Not yet verified (watch in the trial)
- Hooks in a live Claude Code session: SessionStart output, SessionEnd stub detection (relies on transcript containing `brain-capture`/`queue.py add` and `"type":"user"` lines), protect hook with the marker file.
- Scheduled runs (desktop task or cloud routine) and the marker cleanup after a crash (lint warns after 3 h).
- Real connectors (gather-then-reason, completion check); budgets in real volume.
- Capture from claude.ai chats: v1 has no reachable queue there (sub-agent writes a file only); Airtable adapter planned after evals (log 2026-11-10). Never put the webhook URL in a skill.
- Decay values are guide defaults; only supersession was tested. Health score is on trial (judge from log.md history).

## Open items
- Karpathy gist verbatim still missing (paste into `sources/karpathy/llm-wiki.md`).
- French masterclass skills and Nate grill-me not collected (cards rely on transcripts).
- Later options: Airtable queue adapter, dashboards/team/cloud (out of v1), Graphify as level-4 diagnostic only (log 2026-11-10).
- Migration of the existing personal-os into this structure: only after the trial passes.
