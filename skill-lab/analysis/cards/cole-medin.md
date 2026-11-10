# Card — Cole Medin (`sources/cole-medin/`)

2026-11-09 · stage 2 · **No licence**: everything below is paraphrase; no text may be reused in build/.
Paths relative to `sources/cole-medin/`; `ARCH` = `.claude/skills/create-second-brain-prd/references/architecture-reference.md`.

## 1. Philosophy
A second brain is a personal agent built on Claude Code and the Agent SDK, where markdown is memory, Python is logic and JSON is state (ARCH:123-128). The four Cs (borrowed from Nate Herk, `transcript.md:19`) are audits you run on your own brain, and the audits become your eval suite after every big change (`transcript.md:81-83`). Build in phases, add autonomy as trust grows (README.md:143-152, ARCH:127).

## 2. Architecture
- **Folders**: `<Vault>/Memory/` with SOUL, USER, MEMORY, HEARTBEAT, HABITS, BOOTSTRAP, `daily/` (ARCH:18-26); `Memory/drafts/{active,sent,expired}` (ARCH:88-95); code in `.claude/scripts/`, `.claude/hooks/`, `.claude/chat/`, state in `.claude/data/` (ARCH:28-117).
- **Root files**: CLAUDE.md for project instructions (ARCH:7-14); SOUL.md (agent behaviour) and USER.md (user profile) are the identity layer.
- **What loads when**: SessionStart hook injects SOUL + USER + MEMORY + recent dailies into every session (ARCH:29-30). MEMORY.md must stay short because it always loads (ARCH:22).
- **Hooks**: SessionStart, PreCompact, SessionEnd; the last two spawn a background flush agent with no tools that decides what to save; recursion guard via an env variable (ARCH:28-35). A PreToolUse hook blocks secrets (ARCH:106) and another write-protects SOUL.md during reflection (ARCH:77).
- **Schedules**: heartbeat every 30 min in active hours (ARCH:62-70; `transcript.md:87`), daily reflection at 08:00 (ARCH:72-78).
- **Code is described, not shipped.** The repo holds the PRD skill, templates and docs; none of the Python files named in ARCH exist (inventory §6).

## 3. Mechanism per capability
| capability | mechanism | files |
| --- | --- | --- |
| setup/onboarding | Fill requirements template → PRD skill writes a phased build plan; BOOTSTRAP interviews one question at a time, fills USER/SOUL/HEARTBEAT, then deletes itself | `README.md:21-96, 101`; `.claude/skills/create-second-brain-prd/SKILL.md:18-131`; `templates/memory/BOOTSTRAP.md:10-70` |
| root file and routing | Short CLAUDE.md + SOUL "where things go" list (user facts → USER, decisions/lessons → MEMORY, sessions → daily, behaviour → SOUL) | `templates/memory/SOUL.md:74-87`; ARCH:7-14 |
| note format | Fixed-section templates; drafts have YAML frontmatter and a dated file name | `templates/memory/MEMORY.md:5-27`; ARCH:94 |
| capture (live session) | Hooks flush context on compaction and session end; agent also writes to daily during long sessions (hook = safety net) | ARCH:28-35; `SOUL.md:87` |
| scheduled update | Heartbeat: Python pulls integration data first, then Claude reasons; state snapshot diff → notify only on change; ~$0.05/run vs $0.38 with MCP | ARCH:62-70; `README.md:133-136`; `HEARTBEAT.md:5-60` |
| maintenance | Daily reflection promotes items from yesterday's log into MEMORY.md; heartbeat flags tasks stale after a week | ARCH:72-78; `HEARTBEAT.md:27, 41-44` |
| retrieval and ranking | Hybrid search: ~400-token chunks, local embeddings, 0.7 vector + 0.3 keyword, SQLite or Postgres; "search memory before answering about the past" hard rule | ARCH:37-42; `SOUL.md:89-104` |
| decay and supersession | Only implicit: dailies append-only, MEMORY curated; drafts expire after 24 h | ARCH:24, 88-95 |
| skills-from-brain | Standard skill layout with progressive disclosure; voice matching by searching past sent replies | ARCH:53-60, 93 |
| dashboards | None | — |
| team | None (single user) | — |
| cloud/always-on | VPS with systemd timers, git-sync every 2 min, Slack/Discord chat adapter | ARCH:97-115 |
| evals | Four-C audits re-run after every big change (habit, not files) | `transcript.md:45-49, 59-83` |

## 4. Assumptions and dependencies
Claude Code + Claude Agent SDK + Claude Max (~$100/month), Python, FastEmbed model (~80 MB), SQLite-vec/FTS5 or Postgres/pgvector, OS notifications, Slack app, Google OAuth, optional VPS ($5-24/month) (ARCH:111-115). Obsidian optional (ARCH:19).

## 5. Strengths vs guide
- **Hooks as mechanism for capture.** SessionStart/PreCompact/SessionEnd make capture automatic (merge rule 1); guide §5.2 has hooks for protection, capture only as /done.
- **Deterministic gather, LLM reasons.** Script collects data before the model runs, with diffing so it only acts on change; cheaper than tool calls (ARCH:62-70).
- **API keys never reach the model** (CLI wrapper, ARCH:44-51) and secret-blocking hook (ARCH:106). Stronger than guide's connection hygiene.
- **Write-protected identity file** during automated runs (ARCH:77). Mechanism for guide §7 "context view-only".
- **Proactivity levels** (Observer → Partner, `README.md:143-152`): an explicit autonomy dial; guide only says "draft, not send".
- **Search-before-answering rule with exceptions** (`SOUL.md:89-104`): concrete and bounded.
- **Audits as eval suite** (`transcript.md:81-83`): same as guide §5.2 step 7, from the practitioner side.
- **HABITS.md** with auto-check only for objectively verifiable pillars (`HABITS.md:15-38`). Unique idea (rule 6).
- **Robustness utilities**: file lock, retry with backoff, atomic writes (ARCH:117-121).

## 6. Weaknesses and risks
- **Nothing runnable.** All code is a spec for the agent to write; quality depends on the build session. Cannot compare against `brain.py`.
- **Heavy stack.** Vector DB, embeddings, Agent SDK daemons, chat bot, VPS. Guide §1/§4.2 says markdown + grep suffices at this scale.
- **No supersession or decay model.** Append-only dailies and a curated MEMORY.md; no status/updated/review_by; MEMORY.md mixes decisions, projects, facts in one file (`MEMORY.md:5-27`), against "one fact one place" once projects grow.
- **Identity split across SOUL/USER/MEMORY** loaded every session; no folder routing for business context (offer, ICP, clients).
- **Self-deleting BOOTSTRAP** and background agents with file writes: hard to audit; recursion risk mitigated only by an env flag.
- **Licence**: none, so no reuse of text or templates.

## 7. Scores vs guide (1-5)
| axis | score | why |
| --- | --- | --- |
| simplicity | 2 | Memory layer is small, but full design has 9 phases, DB, daemons, bot. |
| token cost | 3 | Pre-gathered heartbeat is cheap; SessionStart injects several files every session. |
| freshness/decay | 2 | Reflection promotes, stale tasks flagged, drafts expire; no supersession or ranking. |
| portability | 2 | Claude Agent SDK, Claude-specific hooks, vector stack; markdown memory itself is portable. |
| maintainability | 3 | Clear module boundaries and shared utils, but lots of custom code to own. |
| safety | 4 | Secret blocking, key isolation, sanitising, write-protected SOUL, proactivity dial. |

## 8. Keep / adapt / drop
| item | verdict | reason |
| --- | --- | --- |
| SessionEnd / PreCompact capture hooks | adapt | Mechanism beats instruction; rebuild as a small stdlib hook calling brain-capture. Recursion guard needed. |
| SessionStart load | adapt | Load only AGENTS.md + hot.md (guide), not three identity files. |
| Gather-then-reason + diff before notify | keep | Lowers cost; good pattern for brain-daily. |
| Key isolation + secret-blocking hook | keep | Pairs with guide's protect.sh. |
| Write-protect canonical context during automated runs | keep | Turns "human-owned layer" into a hook. |
| Proactivity levels | adapt | One setting in setup, read by scheduled skills. |
| Search-memory-first rule | adapt | One root-file line pointing to brain.py search. |
| HABITS.md | trial | Unique; test in evals or drop. |
| BOOTSTRAP self-deleting interview | adapt | Keep one-question-at-a-time; no self-deletion. |
| PRD generator | drop | Builds a different, heavier system. |
| Hybrid vector search, chat bot, VPS daemons | drop for v1 | Guide: not needed at this scale; Nate level 3+ only on pain. |
| Draft lifecycle (active/sent/expired) | drop for v1 | Connector feature, not brain core. |
