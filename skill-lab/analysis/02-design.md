# 02 — Design (Prompt 4)

2026-11-10 · stage 4 · inputs: `analysis/01-matrix.md`, decisions in `log.md` (stage 3, points 1-9), `reference/guide.md`, `reference/brain.py`, `reference/protect.sh`.

## 1. Skill set (6 skills, one owner per capability)
| skill | description (decides the trigger) | inputs | outputs / writes | reads | schedule |
| --- | --- | --- | --- | --- | --- |
| `brain-setup` | "Create or re-run the second brain: interview, scaffold folders, write AGENTS.md and core context files. Use on an empty folder or when asked to (re)onboard." | empty or existing folder; brain dump, files, links; optional "grill me on <topic>" | layout §2.1, `AGENTS.md`, `CLAUDE.md` (`@AGENTS.md`), `context/*.md`, `decisions.md`, `log.md`, `hot.md`, `notes/inbox.md`, `.claude/settings.json` hooks | everything the user gives | once; deep-interview mode on demand |
| `brain-capture` (`/done`) | "End-of-session capture: summarise this conversation into the brain's queue. Use when the user says /done, done, save this session." | current conversation | one queue entry (§2.6) in `notes/inbox.md` or the Airtable adapter | `AGENTS.md`, `hot.md` | on demand; SessionEnd hook adds a stub |
| `brain-daily` | "Daily brain update: integrate queue entries and the last 24 h from connectors, supersede changed facts, rebuild indexes and hot.md." | queue entries `status: new`; connectors listed in `context/config.md` | extended notes, `decisions.md`, today's daily (state), `hot.md`, `log.md`, index files, queue status | `AGENTS.md`, `config.md`, `brain.py search` hits | daily (config, default 07:30) |
| `brain-lint` | "Weekly health check of the brain: run brain.py lint and checks, fix safe issues, list the rest, compute the trial health score." | brain folder | safe fixes, report in `log.md`, items for user | whole brain via scripts, samples via agent | weekly (default Fri 16:00) + monthly consolidation step |
| `brain-ask` | "Answer a question from the brain with ranked search and citations; file good answers back. Use for any question about past decisions, clients, prices, projects." | question | answer with cited notes; optional new `concept` note | `brain.py search` top N, then the notes | on demand |
| `brain-evals` | "Run the brain's eval cases and report pass/fail. Use after changing AGENTS.md, folders, brain.py weights, skills or model." | `evals.md` in the brain | `evals/results/YYYY-MM-DD.md` | evals, brain via the other skills | after changes |

Merged away: Ben AI's operator + optimizer split into daily (state upkeep) and lint (audit); Cole's heartbeat + reflection fold into brain-daily; French cleanup = brain-lint; dashboards, team, cloud out of v1 (PLAYBOOK, matrix).

## 2. Shared contracts (one file: `build/skills/_shared/contracts.md`, skills point to it)
### 2.1 Folder layout (guide §4 starter, frozen after setup)
```
brain/
├── AGENTS.md  CLAUDE.md(@AGENTS.md)  hot.md  decisions.md  log.md  evals.md
├── context/  me.md business.md icp.md offer.md voice.md config.md
├── projects/<x>/about.md      clients/  people/   (index.md each, generated)
├── notes/daily/YYYY-MM-DD.md  notes/inbox.md  notes/ideas.md
├── wiki/  wiki/sources/       raw/ (read-only)   archive/ (read-only)
└── brain.py  .claude/hooks/{protect.sh,session-end.sh}
```
Identity mapping (decision 6): me.md replaces USER.md; AGENTS.md rules replace SOUL.md; decisions.md + hot.md replace MEMORY.md. Working material (rushes, tool-heavy skills) lives outside the brain (French `:71-73`).

### 2.2 Root file (decisions 1, 7, 8)
`AGENTS.md` ≤ 60 lines: routing table, then rules with reasons (guide §4.1 template). Only `AGENTS.md` + `hot.md` load at start. Includes the three decay lines (guide §5.1) and the business-first line (guide §7). No style rules beyond wikilinks for entities.

### 2.3 Frontmatter and note types
Guide §4.2 schema verbatim (type, status, created, updated, review_by, importance, supersedes, superseded_by, sources, tags, aliases, summary). Types: context, entity, project, concept, source, decision, log, inbox. Added (Ben AI `conventions.md:13`): every number in a note carries its date and source inline.

### 2.4 Supersession and decay (guide §5.1, all 3 layers)
Layer 1 status + superseded_by + archive; layer 2 half-lives in brain.py `HALF_LIFE`; layer 3 review_by. Plus Ben AI F8.3 rule in lint: a curated claim contradicted by newer session content gets rewritten, old wording kept under `## History`, link to the superseding note.

### 2.5 Daily note, log, hot.md (decision 3)
- `notes/daily/YYYY-MM-DD.md` is **state**: create once, update sections in place, no-op run writes nothing (Ben AI operator §Daily Update Style). Sections: Done, Decisions, Open loops, Meetings.
- `log.md` is append-only, one line per operation: `## [YYYY-MM-DD] <op> | <subject> | touched: a, b` (guide §4.2). Brain-update runs log; pure action runs do not (Ben AI `conventions.md:16-24`). A no-op run logs one line.
- `hot.md` ≤ 500 words, rewritten (not appended) by brain-daily.

### 2.6 Capture queue (decision 4)
Entry fields: `id, date, source (claude-code|claude.ai|other), session_ref, entities[], facts_new_or_changed[], decisions[{what, why}], open_loops[], status (new|integrated|rejected), result_note`. Default adapter: one `## <id> | <status>` section per entry in `notes/inbox.md`, managed by queue.py (changed at build: simpler to parse than YAML with stdlib). Optional adapter: Airtable table with the same fields (Florian's `/os-capture` pattern). brain-daily is the **only writer** of brain notes from the queue; it sets status so re-runs are idempotent.

### 2.7 Write discipline (all writing skills)
Search before creating (`brain.py search`), extend never near-duplicate (guide §4.1); read back every write and confirm content, retry once (Ben AI operator §Principles 4); budgets per run from `config.md` (reads, writes, fixes), excess queued in `log.md` as `## [date] queued |` (Ben AI §Cadence); never delete without asking; no write to `context/`, `raw/`, `archive/` in automated runs.

### 2.8 config.md (Ben AI `conventions.md:89-95`)
All routine literals: schedule times, connectors, budgets, proactivity level (Cole README:143-152, default "advisor": drafts, never sends), queue adapter. Skills never hard-code these.

## 3. Code versus instructions
| piece | form | why |
| --- | --- | --- |
| index generation, ranked search, lint checks (frontmatter, links, orphans, overdue review, superseded w/o target, size, duplicate titles) | `brain.py` (reuse reference, stdlib) | deterministic bookkeeping, merge rule 1 |
| added lint checks: root ≤ 60 lines, every folder with 2+ notes has index, 3-hop reachability, daily state violations (per-run blocks), queue entries `new` older than 2 days, health score /100 (trial) | new functions in `brain.py` | measurable thresholds from Ben AI `conventions.md:71-87`; scriptable |
| block writes to raw/, archive/, and context/ when `BRAIN_AUTOMATED=1` | `protect.sh` extended (PreToolUse) | Cole write-protect idea as mechanism (ARCH:77) |
| SessionEnd stub: append "uncaptured session <id> <date>" to queue unless /done ran | `session-end.sh` (bash, ~10 lines) | no session lost, no hidden agent (decision 4) |
| queue read/write (inbox.md parser; Airtable adapter) | `queue.py` (stdlib; Airtable via HTTPS, optional) | idempotent status handling must not depend on the agent |
| gather connector data before reasoning | instruction in brain-daily (connectors are MCP, not scriptable portably) | Cole gather-then-reason kept as step order; diffing via "no-op writes nothing" |
| judgment: summarise, extend notes, resolve contradictions, F8 reflection, interview | SKILL.md instructions | needs reading and judgment |
| schedule | cloud/desktop scheduled task running the skill prompt | guide §5.2 step 5; no external `schedule` skill dependency |

## 4. Per-skill credits (ideas, re-written in our own words)
- **brain-setup**: guide §4 steps and starter layout; French interview one question at a time and agent.md + about.md; Ben AI os-setup rules "fetch every link, never ship placeholders, only files with real content" (`os-setup/SKILL.md:733-745`) and skill-os-builder short-router approach; Cole BOOTSTRAP one-question pacing (paraphrased, no text); Nate grill-me as deep mode (own text, original missing).
- **brain-capture**: Florian's `/os-capture` (sub-agent summary into a queue); French /done; Cole SessionEnd idea (ARCH:28-35) reduced to a stub.
- **brain-daily**: guide §5.2 daily prompt; Ben AI operator (daily-as-state, freshness 24 h, budgets, read-back, report, never touch curated layer); Sales OS completion check before adding a task and routine boundary (`sales/routines-guide.md:216, 238`); Cole gather-then-reason; Nate evergreen-vs-changing test (`:155-159`).
- **brain-lint**: guide §5 weekly + monthly consolidation; brain.py lint; Ben AI optimizer checks F2.3-F2.9, F8.1-F8.3, quality bar, score /100 (trial), "fix small, ask before big"; Karpathy lint list (second-hand); Nate level ladder as advice when an index grows past ~100-200 notes.
- **brain-ask**: guide §5.1 ranking + brain.py search; Cole "search memory before answering about the past" with its exceptions; Karpathy "file good answers back" (second-hand, confirmed by guide §5).
- **brain-evals**: guide §5.2 step 7; Cole four-C audits as standing cases (`transcript.md:81-83`); PLAYBOOK starter cases.

## 5. Open points for your review
1. Airtable adapter in v1 or later? Proposal: v1 ships inbox.md only, Airtable adapter after evals pass.
2. Scheduling target: desktop scheduled tasks vs cloud routines (brain must be in a synced git repo for cloud). Proposal: write prompts runtime-agnostic; you choose at install.
3. Health score: computed by brain.py from lint counts (deterministic), not by the agent. OK?
4. `wiki/` and `wiki/sources/` (Karpathy/guide) kept in layout even if empty at start?
