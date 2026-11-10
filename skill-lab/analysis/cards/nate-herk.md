# Card — Nate Herk (`sources/nate-herk/`)

2026-11-09 · stage 2 · transcript only (licence unknown, paraphrased). Missing: grill-me skill, example project, slides.
All cites are `transcript.md:<line>` (ASR text, "claw.mmd" = CLAUDE.md).

## 1. Philosophy
Retrieval should be chosen per folder from the questions you will ask, working backwards from the question (`:17`). Five levels exist, from a routing file to an always-on system, and the highest level is not the best: climb only when a folder hurts (`:25, :105, :163`). The real bottleneck is usually missing context, not retrieval quality, so feed the brain deliberately and stay in control of what goes in (`:115-119, :125, :147-149`).

## 2. Architecture
- **Level 1**: root CLAUDE.md as a "where things live" routing table + plain folders (context, projects, decision log); exact-word search (`:29-45`).
- **Level 2**: LLM wiki per topic (concepts, comparisons, sources, techniques) with indexes, plus Claude Code auto-memory (`:53-67`).
- **Level 3**: semantic/vector search for folders where exact words fail (`:81-101`).
- **Level 4**: knowledge graph (LightRAG) for entity relationships (`:129-141`).
- **Level 5**: always-on sync (GBrain) (`:145-147`).
- **Root files**: keeps CLAUDE.md and AGENTS.md as identical copies so Codex and Claude both read one (`:69`).
- **Hooks / schedules**: none described for his own setup; ingestion is manual, in brainstorm sessions (`:149`).

## 3. Mechanism per capability
| capability | mechanism | cite |
| --- | --- | --- |
| setup/onboarding | "Grill me" interview skill: relentless questions on one topic until complete, writes a brainstorm file (adapted from Matt Pocock) | `:115-119` |
| root file and routing | Routing table in CLAUDE.md; "if it doesn't know where something lives it won't find it" | `:29-37` |
| note format | Not specified; projects as folders or files, quarterly priorities with decisions and statuses | `:41-45, :151-153` |
| capture (live session) | Manual: brainstorm, then "ingest it together" | `:149` |
| scheduled update | None (level 5 tools only) | `:145-147` |
| maintenance | Not described; notes wikis degrade as they grow | `:71` |
| retrieval and ranking | Level chosen per folder: routing (exact words), wiki + index (30+ notes forgotten), vector (meaning), graph (relationships); ask the agent which fits | `:105-109, :163-165` |
| decay and supersession | Evergreen context vs changing data: changing data (Slack, email, customer data) stays in tools, reached on demand | `:155-161` |
| skills-from-brain | — | — |
| dashboards | — | — |
| team | Raises sync and adoption as the real team problem, no mechanism | `:167-169` |
| cloud/always-on | GBrain as level 5, with a warning about too much context | `:145-147` |
| evals | — | — |

## 4. Assumptions and dependencies
Claude Code (auto-memory, `:65-67`), Codex; level 3-5 need embedding tools, LightRAG, GBrain; Obsidian optional ("I hardly ever open it", `:61`). Privacy note: everything goes to the model provider (`:121`).

## 5. Strengths vs guide
- **Decision rule for retrieval upgrades** with symptoms per level (`:163-165`). Guide §4.2 only says "add qmd past 100-200 pages".
- **Per-folder choice**, not whole-brain migration (`:105`).
- **Evergreen vs changing data** test for what to ingest (`:155-159`). Same as guide principle 2, phrased as a usable test.
- **Context is the bottleneck, not retrieval** (`:125`): supports guide's "keep it simple".
- **Grill-me interview** builds depth on one entity, complementing a broad brain dump.

## 6. Weaknesses and risks
- **Duplicate CLAUDE.md and AGENTS.md** with the same content (`:69`): guide §9 lists this as a mistake (use `@AGENTS.md`).
- **Manual ingestion only** (`:149`): conflicts with guide §5 daily capture; brain goes stale without discipline.
- **Relies on Claude auto-memory** (`:65-67`), a provider-locked second store against "one fact one place".
- **No maintenance, decay or evals.** No files to verify; key asset (grill-me) missing.
- Levels 3-5 add servers and opaque indexes (guide §1 table).

## 7. Scores vs guide (1-5)
| axis | score | why |
| --- | --- | --- |
| simplicity | 4 | Level 1-2 is the guide's model; complexity only on demand. |
| token cost | 4 | Routing + index first; heavier levels only per folder. |
| freshness/decay | 2 | Only the "don't ingest changing data" rule. |
| portability | 3 | Markdown + both root files, but auto-memory and level 3-5 tools lock in. |
| maintainability | 3 | Simple at low levels; duplicated root files drift. |
| safety | 3 | Privacy warning, human-controlled ingestion; nothing else. |

## 8. Keep / adapt / drop
| item | verdict | reason |
| --- | --- | --- |
| Level ladder + symptoms, per folder | keep | Becomes the "when to add search" rule in design; default stays level 1-2. |
| Evergreen vs changing-data test | keep | One line in AGENTS.md / brain-daily. |
| Grill-me interview | adapt | Deep interview mode in brain-setup (one entity at a time); write our own since the skill is missing. |
| "Ask the agent which level fits" | adapt | Option inside brain-lint report when an index gets too big. |
| Duplicate CLAUDE.md/AGENTS.md | drop | Guide rule: one file + import. |
| Manual-only ingestion | drop | Daily capture wins (guide §5). |
| Auto-memory | drop | Second store, provider lock-in. |
| Levels 3-5 | drop for v1 | Out of scope until evals show retrieval failures. |
