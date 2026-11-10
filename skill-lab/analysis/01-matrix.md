# 01 — Comparison matrix (Prompt 3)

2026-11-09 · stage 3 · inputs: `analysis/cards/*.md`, `reference/guide.md`, merge rules in `log.md`.
Karpathy column is **second-hand** (`sources/karpathy/llm-wiki-summary.md`, no card); it informs, never wins alone.
Scores (simplicity/token/freshness/portability/maintainability/safety): Ben AI 2/2/3/2/2/3 · Cole 2/3/2/2/3/4 · Nate 4/4/2/3/3/3 · French 5/4/2/5/3/3.

## Matrix
| capability | Ben AI | Cole Medin | Nate Herk | French | Karpathy (2nd-hand) | Guide | Best choice |
| --- | --- | --- | --- | --- | --- | --- | --- |
| setup/onboarding | Scaffold + 3×4 brain-dump forms; fetch every link; no placeholder files | Requirements → PRD; BOOTSTRAP interview, one question at a time | "Grill me": relentless interview on one topic | Interview prompt, one question at a time; 5-min voice dump | Paste idea file, agent builds specifics with you | 30-min dump or interview → 5-10 core files | **Guide flow + Ben AI "no placeholders, fetch links" + Nate grill-me as deep mode.** Simplest (rule 2); Ben rules prevent empty scaffolds (known failure). |
| root file and routing | 107-line CLAUDE.md + CLAUDE.md per folder | Short CLAUDE.md + SOUL/USER/MEMORY loaded by hook | CLAUDE.md routing table, duplicated as AGENTS.md | agent.md, "just enough" + about.md entry points | Schema file (CLAUDE/AGENTS.md) | AGENTS.md ≤60 lines, CLAUDE.md = @AGENTS.md, index.md per folder | **Guide.** Evidence-backed (rule 4); French about.md entry point kept; folder CLAUDE.md dropped (all load, conflict risk). |
| note format | type/date/project/status/tags; wikilinks; no H1 = filename | Fixed-section templates; dated drafts | Unspecified | about.md rules, decisions with reason | Wiki pages, sources layer | Typed notes + full frontmatter (updated, review_by, supersedes, importance, summary) | **Guide schema + Ben AI "every number has date and source".** Only guide supports ranking/decay. |
| capture (live session) | Instruction: persist before final answer (hooks promised, not shipped) | SessionEnd + PreCompact hooks → background flush | Manual "ingest together" | /done + auto-save after 20 min idle | Query answers filed back | /done skill, file good answers back | **/done skill (French, guide) triggered by a SessionEnd/PreCompact hook (Cole) + idle trigger.** Mechanism beats instruction (rule 1). |
| scheduled update | Operator: budgets, short/full path, daily-as-state, read-back, task queue, report | 30-min heartbeat: script gathers, diff, then Claude reasons | None | None | Ingest on demand | Daily 07:30 capture prompt + brain.py index | **Guide daily prompt + Ben daily-as-state, budgets, read-back + Cole gather-then-reason/diff + Sales completion check.** Each prevents a named failure (rule 7). |
| maintenance (lint) | Optimizer: 10 frameworks, agent-run, score /100, walk per fix | Daily reflection promotes to MEMORY | — | cleanup skill (content unknown) | Lint: contradictions, stale, orphans, missing links, gaps | Weekly: brain.py lint + agent fixes, ask before deletes | **brain.py lint (script) + ported Ben checks (contradictions, merge candidates, stale entries, undigested sources) + optional score.** Script beats agent-run regex (rule 1). |
| retrieval and ranking | Grep / obsidian search, scan before read | Hybrid vector 0.7 + keyword 0.3 | Level per folder: route → wiki → vector → graph | Grep words (price, rate, euros) | index.md first; qmd later | brain.py ranked search (relevance, recency half-life, importance) | **Guide brain.py + Nate's level ladder as the upgrade rule.** Only scripted ranking; vector only on proven pain (rules 2, 3). |
| decay and supersession | F8.3 stale rewrite + History; dailies today-only | Drafts expire 24 h; flagged stale tasks | Changing data stays in tools | One fact one place; archive | Lint flags stale claims | 3 layers: supersession, half-life ranking, review_by | **Guide (all 3 layers) + Ben F8.3 as lint check.** Nobody else has a model. |
| skills-from-brain | Skill refs point into vault; marketing skills read Context/ | Progressive disclosure; voice match on sent drafts | — | skill-manager (unknown) | — | Skills reference single brain file; skills live outside brain | **Guide + Ben `config.md` for routine literals.** |
| dashboards | Obsidian/Next.js command center; sales routine deploys from temp dir | — | — | — | — | Decision-useful page refreshed by morning task | **Out of v1** (PLAYBOOK). Keep Sales temp-dir deploy rule for later. |
| team | Relay fork RBAC, Baalda app, profile-first Team/ | — | Names sync/adoption as the problem | — | — | Staged rollout, one owner, per-folder permissions | **Out of v1.** Guide principles only. |
| cloud/always-on | Railway MCP server; cloud-folder/Notion builders | VPS + systemd + git-sync + chat bot | GBrain (level 5) | Same files on a VPS | — | Cloud routines or small VPS | **Out of v1.** Git-synced repo + cloud routine when needed (portable, rule 3). |
| evals | None (lint score only) | Four-C audits re-run after changes | — | — | — | evals.md, 5 real questions, run after changes | **Guide evals.md + Cole's 4-C audits as cases.** Only real task tests (rule 4). |

## Conflicts that need your decision
1. **Root file: AGENTS.md + `@AGENTS.md` (guide) vs CLAUDE.md only (Ben AI) vs duplicated CLAUDE.md/AGENTS.md (Nate).** Proposed: guide.
2. **Per-folder routing: generated `index.md` (guide) vs hand-written `CLAUDE.md` per folder (Ben AI, `os-setup/SKILL.md:142-160`).** Proposed: index.md (generated, not auto-loaded).
3. **Daily note: append session entries (guide §5) vs daily-as-state, rewritten in place, no-op writes nothing (Ben AI operator).** Proposed: state for the daily note, append-only only in log.md. Conflicts with guide text; needs your OK.
4. **Capture trigger: /done on demand (French, guide) vs automatic hooks (Cole) vs auto-save without asking (Ben AI rule 9).** Proposed: /done + SessionEnd hook that runs it; no silent auto-save of new files (risk of near-duplicates).
5. **Ingestion: automatic daily from connectors (guide, Ben AI) vs manual with human in the loop (Nate).** Proposed: automatic, with report-back and ask before deletes.
6. **Identity files: context/me.md, business.md… (guide/Ben) vs SOUL.md + USER.md + MEMORY.md (Cole).** Proposed: guide's context/; no MEMORY.md (decisions.md + hot.md cover it).
7. **Hot cache: hot.md (guide) vs "read latest Daily/ + me.md" at startup (Ben AI) vs inject several files by hook (Cole).** Proposed: AGENTS.md + hot.md only.
8. **Style hard rules (Ben AI: no em dashes, callout quotas, wikilink-everything).** Proposed: drop from root file; keep wikilinks for entities only.
9. **Health score /100: keep, trial, or drop?** Proposed: trial in evals (rule 6).

## Ideas present in only one source that look valuable
- Daily-as-state + no-op rule; run budgets with rotating queue; read-back write verification (Ben AI operator template).
- "If it changes what the OS knows it logs; if it acts it doesn't" (Ben AI `conventions.md:16-24`).
- Every number carries pulled date and source; instance literals in one config file (Ben AI `conventions.md:13, 89-95`).
- Measurable quality bar: root/folder line caps, auto-loaded tokens, file size, 3-hop reachability (Ben AI `conventions.md:71-87`).
- Undigested-source check (Ben AI F2.8) and stale-claim rewrite with History (F8.3).
- Completion check before adding a task, routine boundaries, dependency guard, temp-dir deploy (Ben AI `sales/routines-guide.md:216, 238, 25, 29`).
- Gather-then-reason with state diffing (Cole ARCH:62-70); write-protect canonical files during automated runs (ARCH:77); key isolation (ARCH:44-51); proactivity levels (README:143-152); HABITS.md (Cole).
- Retrieval level ladder with symptoms, chosen per folder; evergreen vs changing-data test (Nate `:155-165`).
- 20-minute idle auto-capture (French `:51`).

## Capabilities nobody covers well
- **Decay and supersession**: only the guide has a model; no source has `updated`/`review_by`/`supersedes` fields or ranking code.
- **Evals**: no files anywhere; Cole's habit is the only practice. Ours (`evals/cases.md`) will be the first.
- **Deterministic lint/index**: every source relies on the agent; only `reference/brain.py` scripts it.
- **Live-session capture as working code**: Cole describes hooks, Ben AI promises them, French shows none.
- **Retrieval at scale**: untested by anyone between grep and vector DB; guide suggests qmd, Nate a ladder.

## Proposed skill set (confirms PLAYBOOK hypothesis)
brain-setup, brain-capture (/done), brain-daily, brain-lint, brain-ask, brain-evals — six skills, no change. Details in stage 4 after your decisions.

**Stop: waiting for your decisions on conflicts 1-9.**
