# log.md — decisions, newest first

## 2026-11-09 — Stage 3 decisions (Florian)
1. Root file: AGENTS.md only, no CLAUDE.md content (guide over Ben AI/Nate). Open point: Claude Code only auto-loads CLAUDE.md, so a one-line pointer may be technically required.
2. Folder routing: generated index.md (guide); Ben AI per-folder CLAUDE.md rejected (all load, conflict risk).
3. Daily note = state, rewritten in place, no-op writes nothing (Ben AI operator); append-only kept for log.md only. Deviates from guide 5.
5. Ingestion: automatic daily from connectors (guide, Ben AI) + manual add possible (Nate grill-me / ingest on demand). Ask before deletes.
8. Ben AI style hard rules dropped from root file; wikilinks for entities kept.
9. Health score /100 (Ben AI): trial in evals.
4. Capture (2026-11-10, inspired by Florian's own /os-capture system): /done runs a sub-agent that writes a structured summary (date, source, entities, new/changed facts, decisions with reason, status) into a queue; queue adapter = notes/inbox.md by default, Airtable optional for chats outside Claude Code; brain-daily integrates entries with status new -> integrated/rejected (idempotent, one writer, search-first). SessionEnd hook only queues an "uncaptured session" line. Rejected: Cole background flush agent, Ben AI silent auto-save (duplicate risk).
Pending confirmation: 6 identity files, 7 startup reads, 1(a)/(b) CLAUDE.md pointer.

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
