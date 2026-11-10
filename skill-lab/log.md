# log.md — decisions, newest first

## 2026-11-10 — Stage 6 evals: 6/6 pass (evals/results/2026-11-10.md)
- Fixes from evals: brain.py about.md naming and orphan rule for superseded notes; contracts/AGENTS template project link syntax and onboarding source; archive moves interactive-only; setup config defaults; capture inline fallback; seed dates.
- Open (needs real use): hooks in live sessions, connectors, schedules, health-score trial over several weeks.

## 2026-11-10 — Graphify evaluated: not in v1
- What: open-source Claude Code skill (PyPI `graphifyy`) turning a folder into a knowledge graph (tree-sitter for code, Claude extraction for docs), exports Obsidian/Neo4j/MCP.
- Rejected for v1: code-first (notes cost Claude tokens per ingest); 71.5x token claim is a self-run size comparison on 52 files, no answer-quality test, not independently reproduced; baseline is "read all files", not our ranked search + indexes; installs its own rules + PreToolUse hook (lab rule: never install a source's hooks); second index to keep in sync (one fact one place); Claude-specific; licence inconsistent (Apache-2.0 vs MIT).
- Kept as level-4 candidate (Nate ladder): read-only diagnostic on a copy when a folder exceeds ~150 notes or evals show relation-type retrieval misses. Mentioned in brain-lint retrieval-pressure advice.

## 2026-11-10 — Stage 5, step 6: brain-evals built (all 6 skills done)
- Runs evals.md cases on a disposable copy (BRAIN_AUTOMATED=1), one fresh sub-agent per case; mechanical Must contain / Must not contain checks before judgment; root cause per fail; results in evals/results/<date>.md, regressions vs previous run; never applies fixes.
- Template evals.md now holds the four C audits (Cole/Nate via guide 3). brain.py: evals/ skipped from notes, evals/results created by init.

## 2026-11-10 — Stage 5, step 5: brain-ask built
- brain.py search first (guide 5.1), freshness judgment (review_by, conflicts, hypotheses), connectors for live values; search-before-answering rule with exceptions (Cole SOUL); file syntheses back as wiki/ concept notes on user OK (Karpathy query, guide 5); "not found" lines in log.md feed brain-lint's retrieval-pressure check.
- Conflicts are reported, not fixed (brain-lint owns fixes: one owner per capability).

## 2026-11-10 — Stage 5, step 4: brain-lint built
- Script checks via brain.py (fix safe, budget_fixes); overdue reviews checked against connectors; judgment checks from Ben AI optimizer (F8.1 contradictions, near-duplicates, F8.3 stale, F2.8 undigested) and Karpathy lint (missing pages); root map accuracy; Nate ladder as advice only; guide monthly consolidation.
- Not ported: Ben AI frameworks F3 caveman, F4 context rot, F5 memory, F10 rule rewriting, HTML report, per-finding walk (cost, Claude-specific, rule 7). Health score logged before/after each run to judge the trial.

## 2026-11-10 — Stage 5, step 3: brain-daily built
- Single writer of notes from the queue. Borrowed: guide daily prompt (5.2); Ben AI operator (budgets, short path, daily = state, read-back, report, curated layer untouched); Cole gather-then-reason; Nate evergreen vs changing data; Sales OS completion check before tasks.
- Choices: hypothesis entries go to Open questions or draft notes; verbatim lines to ## Quotes in the related note, voice patterns proposed for context/voice.md; uncaptured stubs read from transcript if available, else rejected.

## 2026-11-10 — brain-capture revised from Florian's /os-capture (AskUserQuestion answers)
- Kept: sub-agent does all the work (zero main-context load); READ KO fallback (export then relaunch); no confirmation, a copy of the entry is sent instead (config capture_confirm: false); never re-run queueing (duplicates); certainty (fact|hypothesis) + 1-3 verbatim lines, added to queue.py and contracts §6.
- Rejected by Florian: decision vs "retenu" rule, canonical-name priority list, before/after results table, site fields (visibilite, contenu, cadre).
- Not copied: the Airtable webhook URL (secret in plain text in os-capture; future adapter must read it from an env var or secret).

## 2026-11-10 — Stage 5, step 2: brain-capture built
- build/skills/brain-capture/SKILL.md: queue-only (brain-daily single writer), confirm with user before queueing, read-back check, fallback text when no brain folder reachable. Sub-agent drafting optional for long sessions (from Florian /os-capture).

## 2026-11-10 — Stage 5, step 1: shared base + brain-setup built
- build/skills/_shared/: contracts.md, scripts/brain.py (reference + init, lint checks root/index/hot/queue/daily, health score), scripts/queue.py, hooks/protect.sh (context/ blocked when BRAIN_AUTOMATED=1), hooks/session-end.sh (stub only), templates/.
- build/skills/brain-setup/SKILL.md (45 lines).
- Queue format changed from YAML blocks to `## id | status` sections (stdlib parsing). Smoke test in scratchpad passed; init no longer substitutes {{TODAY}} inside copied scripts (bug found and fixed).

## 2026-11-10 — Stage 4 open points accepted (Florian: "très bien continue")
1. v1 queue adapter = notes/inbox.md only; Airtable adapter after evals pass.
2. Scheduled prompts written runtime-agnostic (desktop task or cloud routine chosen at install).
3. Health score computed by brain.py from lint counts, not by the agent.
4. wiki/ and wiki/sources/ created at setup even if empty.

## 2026-11-10 — Stage 4 design written
- analysis/02-design.md: 6 skills, shared contracts, code vs instructions, credits. 4 open points for Florian.

## 2026-11-09 — Stage 3 decisions (Florian)
1. Root file: AGENTS.md only, no CLAUDE.md content (guide over Ben AI/Nate). Open point: Claude Code only auto-loads CLAUDE.md, so a one-line pointer may be technically required.
2. Folder routing: generated index.md (guide); Ben AI per-folder CLAUDE.md rejected (all load, conflict risk).
3. Daily note = state, rewritten in place, no-op writes nothing (Ben AI operator); append-only kept for log.md only. Deviates from guide 5.
5. Ingestion: automatic daily from connectors (guide, Ben AI) + manual add possible (Nate grill-me / ingest on demand). Ask before deletes.
8. Ben AI style hard rules dropped from root file; wikilinks for entities kept.
9. Health score /100 (Ben AI): trial in evals.
4. Capture (2026-11-10, inspired by Florian's own /os-capture system): /done runs a sub-agent that writes a structured summary (date, source, entities, new/changed facts, decisions with reason, status) into a queue; queue adapter = notes/inbox.md by default, Airtable optional for chats outside Claude Code; brain-daily integrates entries with status new -> integrated/rejected (idempotent, one writer, search-first). SessionEnd hook only queues an "uncaptured session" line. Rejected: Cole background flush agent, Ben AI silent auto-save (duplicate risk).
6. Identity (2026-11-10): context/me, business, icp, offer, voice, config + AGENTS.md rules + decisions.md + hot.md. Rejected Cole SOUL/USER/MEMORY (MEMORY mixes fact types). context/ write-protected in automated runs (Cole idea).
7. Startup reads: AGENTS.md + hot.md only (guide 4.1 evidence). Rejected Cole multi-file injection, Ben AI latest-daily read.
1a. CLAUDE.md = one line @AGENTS.md, no content.

## 2026-11-09 — Stage 3 matrix written
- analysis/01-matrix.md. 9 conflicts open, awaiting Florian. Proposed skill set unchanged (6 skills).

## 2026-11-09 — Stage 2 cards written (no Karpathy, by decision of Florian)
- analysis/cards/{benai,cole-medin,nate-herk,french}.md. No merge decision yet; keep/adapt/drop lists are proposals for stage 3.
- Finding: Ben AI os-setup promises hooks but ships an empty settings.json and no hook scripts; Cole Medin describes all code but ships none.

## 2026-11-09 — Sources cleanup (authorised by Florian)
- Removed byte-identical Ben AI copies (list in sources/benai/DUPLICATES.md); kept differing variants. Re-wrapped 5 transcripts, text unchanged. Karpathy gist still missing: outline only in karpathy/llm-wiki-summary.md.

## 2026-11-09 — Stage 1 inventory written
- analysis/00-inventory.md: 676 files, ~400 Ben AI copies; missing Karpathy gist, French skills, Nate grill-me, Cole hook code. No merge decision yet.

## 2026-11-09 — Ben AI free resources added
- ZIP (setup/operator/optimizer) = identical to baalda-os plugin; obsidian os-* variants differ slightly. Routines guide (7 prompts) and video prompts saved.

## 2026-11-09 — 5th creator added
- Nate Herk (5 levels video) added to sources/nate-herk/. Inventory and matrix get one more column.

## 2026-11-09 — Lab created
- Sources collected: Ben AI (benai-skills @4c7a2ec, baalda README @90929b5), Cole Medin (@74f7544).
- Missing: guide.md, brain.py, Karpathy gist, French material, Ben AI ZIP + Sales guide. Transcripts added 2026-11-09.

## Merge decision rules (apply in prompt 3)
1. **Mechanism beats instruction.** If one source enforces something with a script or hook and another asks the agent nicely, keep the script.
2. **Simpler wins ties.** Fewer files loaded per session, fewer folders, fewer dependencies.
3. **Portable over proprietary.** Plain markdown and stdlib scripts over an app, plugin runtime or paid service; the app stays an optional adapter.
4. **Evidence over enthusiasm.** Research or our own eval beats a creator's anecdote.
5. **One owner per capability.** If two skills touch the same files for the same reason, merge them.
6. **Keep the unique good idea.** An idea only one creator has gets a trial in evals before being dropped.
7. **Every rule earns its line.** Anything that does not change a test outcome or prevent a known failure stays out of the root file.
