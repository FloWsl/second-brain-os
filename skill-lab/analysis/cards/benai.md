# Card — Ben AI (`sources/benai/`)

2026-11-09 · stage 2 · MIT (skills), Apache-2.0 (baalda-app), personal use (routines guide, transcripts).
Canonical paths only (copies removed, see `sources/benai/DUPLICATES.md`). Paths below are relative to `sources/benai/`; `os-*` = `obsidian/skills/os-*`.

## 1. Philosophy
The vault is both knowledge base and operating system, and its value comes from being kept alive by machinery: an onboarding that turns a brain dump into real context, a scheduled Operator that updates it, and an optimizer that audits it against named frameworks (`transcript-18-tips.md:63-77`). Ben AI sells breadth: one plugin per tier (skill-only, cloud, local, Obsidian, Baalda app, team, marketing, sales). The recurring stance is "mechanise the upkeep, keep the human on the curated layer" (operator never edits `CLAUDE.md` or the context root, `os-operator/references/operator-prompt-template.md` Hard Rules).

## 2. Architecture
- **Folders** (`os-setup/SKILL.md:71-117`): `Context/ Projects/ Daily/ Resources/ Skills/ Intelligence/{meetings/*,competitors,market,decisions,archive}`; business mode adds `Departments/ Team/ Onboarding/ Intelligence/processes/`.
- **Root files**: root `CLAUDE.md` (107 lines, `os-setup/references/claude-md-template.md`) plus one routing `CLAUDE.md` per folder (`os-setup/SKILL.md:142-160`). No AGENTS.md; the video prompt asks for one (`zip-video/video-prompts.md` tip 4).
- **What loads when**: root CLAUDE.md auto-loads; on first response read latest `Daily/` + `Context/me.md` (`claude-md-template.md:9-15`). Folder CLAUDE.md files load when the agent enters the folder.
- **Hooks**: claimed but not shipped. `os-setup` says it creates hooks (`os-setup/SKILL.md:3`) and runs `chmod +x .claude/hooks/*.sh` (`:188-191`), yet `settings-json-template.md` is an empty `{}` and no `.sh` file exists in the plugin.
- **Schedules**: `os-operator` renders a prompt and hands it to an external `schedule` skill (`os-operator/SKILL.md:16, 215-255`). Marketing OS ships 10 routines (`other-os/marketing-os/skills/marketing-os-routines/assets/`), Sales OS 7 (`sales/routines-guide.md`).

## 3. Mechanism per capability
| capability | mechanism | files |
| --- | --- | --- |
| setup/onboarding | Mode choice (solo/business), automated scaffold, then 3 forms × 4 categories brain dump, fetch every pasted link/file, build only files with real content | `os-setup/SKILL.md:29-50, 209-551, 733-745`; leaner tier `other-os/aios/skills/skill-os-builder/SKILL.md:27-75` |
| root file and routing | Type → file routing table in root, folder CLAUDE.md for details; 15 numbered rules | `claude-md-template.md:17-39, 79-95` |
| note format | Frontmatter `type,date,project,status,tags`; wikilinks for every entity; no H1 duplicating filename; no em dashes | `claude-md-template.md:65-77, 97-105`; `other-os/marketing-os/skills/marketing-os-setup/references/conventions.md:45-61` |
| capture (live session) | Instruction only: write session log to `Daily/` when meaningful work happens, persist before final answer, corrections become rules | `claude-md-template.md:81-82, 87-90` |
| scheduled update | Operator prompt: budgets, short/full path, daily-as-state (create / update in place / no-op), freshness 24 h, read-back verification, task-list queue, report | `os-operator/references/operator-prompt-template.md` §Cadence, §Freshness, §Daily Update Style, §Path Selection, §Hard Rules |
| maintenance | Optimizer: role discovery, 10 frameworks, score /100, per-finding apply/plan walk, HTML report; Operator does capped rotating housekeeping + lint each run | `os-optimizer/SKILL.md:11-34, 213-330, 401-446, 465+`; template §6-7 |
| retrieval and ranking | None as code. Grep / `obsidian search` and folder routing; "scan before read" | `claude-md-template.md:63, 86`; template §Principles 2 |
| decay and supersession | F8.3 stale entries: rewrite curated claim, move old wording to `## History`, link superseder; Operator flags "stale dates in frontmatter"; dailies hold only today | `os-optimizer/references/passes-reflection.md:96-115`; template §Freshness, §6 |
| skills-from-brain | Skill references point into vault; marketing skills read ICP/voice/offer from `Context/` and file output back | `zip-video/video-prompts.md` tip 12; `conventions.md:9`; `other-os/marketing-os/skills/marketing-os-newsletter/SKILL.md:3` |
| dashboards | Obsidian command center or Next.js app; Marketing control center; Sales dashboard routine deploying from a temp copy | `obsidian/skills/agentic-os-setup/SKILL.md`; `marketing-os-dashboard/SKILL.md`; `sales/routines-guide.md:5-31` |
| team | Relay fork with RBAC (Obsidian), profile-first `Team/` scaffolding, Baalda app (CRDT sync) | `obsidian/skills/team-os/SKILL.md:1-30`; `os-setup/SKILL.md:679-702`; `baalda-app/README.md:41-57` |
| cloud/always-on | Relay MCP server on user's Railway; cloud-folder or Notion variant | `obsidian/skills/os-mcp/SKILL.md:3-31`; `other-os/aios/skills/cloud-os-builder/SKILL.md` |
| evals | None. Optimizer score is a lint score, not task evals | `os-optimizer/SKILL.md:405-421` |

## 4. Assumptions and dependencies
Claude Code or Cowork (`mcp__visualize__show_widget` is Cowork-only, `os-setup/SKILL.md:217`); Obsidian or Baalda app; Claude `schedule` skill; MCP connectors (transcripts, chat, community); optional Railway account + CLI, Vercel, Notion/Drive. Optional `defuddle` CLI (`claude-md-template.md:91`). Paid: Baalda app tiers, Railway.

## 5. Strengths vs `reference/guide.md`
- **Daily is state, not a log.** Three behaviours (create / update in place / no-op) and "no-op runs do not write" (`operator-prompt-template.md` §Daily Update Style). The guide only says "append to daily"; this avoids its noise and git churn (guide §5.1 "reinforce on confirmation, not on reading").
- **Run budgets + rotating queue.** Each run caps reads/writes/fixes and queues the rest (§Cadence, §6). Guide's weekly lint has no budget.
- **Write verification.** Read back every write and confirm content, retry once (§Principles 4). Not in guide.
- **Brain-update vs action routines.** "If it changes what the OS knows, it logs; if it just acts, it does not" (`conventions.md:16-24`). Sharper than guide's "log everything that changes".
- **Every number carries pulled date and source** (`conventions.md:13`). Matches guide's "absolute dates" and goes further.
- **Instance literals in one `Context/config.md`** (`conventions.md:89-95`). A clean "one fact one place" for routines.
- **Measurable quality bar**: root < 200 lines, folder < 120, auto-loaded ≈ 3 000 tokens, file < 10 KB, 3-hop reachability (`conventions.md:71-87`).
- **Sales routine patterns**: explicit boundary per routine, completion check before adding a task, dependency guard, deploy from a temp folder never the vault (`sales/routines-guide.md:216, 238, 25, 29`).
- **Undigested-source check** (F2.8, `passes-karpathy-wiki.md:266-298`) and raw-source immutability (F2.9).
- **Human-owned curated layer**: operator never edits CLAUDE.md or context root (template §Hard Rules). Same idea as guide's view-only context/, enforced by instruction.

## 6. Weaknesses and risks
- **Bloat.** os-optimizer 925 lines + 2 825 lines of pass files; os-setup 745; baalda optimizer 1 001. Root CLAUDE.md 107 lines vs guide's 60 target (§4.1 rule 3).
- **Instruction, not mechanism.** No scripts for index, lint, search or score: the optimizer's "regex" checks are run by the agent reading files (`os-optimizer/SKILL.md:21-34`). Costly and non-deterministic vs `brain.py`.
- **Phantom hooks.** Hooks are promised but settings template is `{}` (§2). Capture relies on the agent remembering rule 10.
- **No supersession schema.** Frontmatter lacks `updated`, `review_by`, `supersedes`, `importance` (`claude-md-template.md:67-77`); decay only via F8.3 judgment and "today only" dailies. No ranking.
- **Rule 9 "never ask permission to save, auto-save"** (`claude-md-template.md:89`) conflicts with guide's "update existing, don't create near-duplicates" unless search-first is enforced.
- **Duplication across plugins.** Same skills in 3-5 copies with small diffs; drift between Obsidian and Baalda variants already visible (§1b inventory).
- **Vendor lock-in**: Obsidian syntax (callouts, embeds) vs Baalda CommonMark rules contradict each other (`baalda-os/skills/setup/references/claude-md-template.md` §Baalda Syntax); Cowork-only onboarding widget; schedule skill.
- **Unsafe / unauditable code**: `team-os` ships an 886 KB minified `main.js` that replaces an Obsidian plugin; `os-mcp` deploys an OAuth MCP server with a Railway token; `web-artifacts-builder/scripts/*.sh` and a tarball. Do not install.
- **Style rules as hard rules** (no em dashes, callout quotas) cost root-file lines without preventing a known failure (merge rule 7).
- **Two root files rule absent**: CLAUDE.md only; fine for Claude, not portable to Codex (guide §9).

## 7. Scores vs guide (1-5)
| axis | score | why |
| --- | --- | --- |
| simplicity | 2 | 12-16 folders, folder CLAUDE.md everywhere, 700-1 000-line skills; skill-os-builder is the simple exception. |
| token cost | 2 | Large skills and per-folder CLAUDE.md files; agent-run lint reads every file; budgets help the operator only. |
| freshness/decay | 3 | Strong daily freshness and stale-claim reflection, but no `updated`/`review_by`/supersedes fields or ranking. |
| portability | 2 | Markdown vault, but Obsidian/Baalda syntax, Cowork widget, schedule skill, Railway, CLAUDE.md-only. |
| maintainability | 2 | Many near-identical copies across plugins; long prose specs to keep in sync. |
| safety | 3 | Good guards in operator (no deletes, no channel posts, human-owned layer, temp-dir deploy), but opaque JS and remote server installers. |

## 8. Keep / adapt / drop
| item | verdict | reason |
| --- | --- | --- |
| Daily-as-state + no-op rule | keep | Directly prevents log noise; testable. |
| Operator budgets + rotating housekeeping queue | adapt | Make it a short section of brain-daily/brain-lint, not a 364-line prompt. |
| Read-back verification of writes | keep | Cheap, prevents silent failures. |
| Brain-update vs action logging rule | keep | One line, clear owner per routine. |
| `config.md` for instance literals | adapt | Fold into guide's context/ (one file for routine settings). |
| Quality bar table | adapt | Use as lint thresholds in brain.py (root 60, folder index, file size, hops). |
| Optimizer frameworks F2 (wiki), F8 (reflection) checks | adapt | Port contradictions, merge candidates, stale entries, undigested sources as lint checks; script what is scriptable. |
| Optimizer score /100 | trial | Unique idea (merge rule 6); test whether it changes behaviour in evals. |
| Sales routine patterns (boundary, completion check, dependency guard, temp-dir deploy) | keep | Reusable for brain-daily and dashboards. |
| Onboarding: brain dump, fetch links, never ship placeholders | adapt | Keep the rules; drop the Cowork-only 3×4 forms. |
| skill-os-builder layout | keep as reference | Closest to guide's simplicity. |
| Per-folder CLAUDE.md | drop | Guide uses generated index.md; folder CLAUDE.md files all load and conflict risk (guide §4.1 rule 7). |
| Obsidian/Baalda syntax rules, em-dash ban, callout quota | drop | Style, not failure prevention; tool-specific. |
| team-os relay fork, os-mcp, agentic-os dashboards | drop for v1 | Out of scope (PLAYBOOK target set); unauditable code. |
| Sales/marketing domain skills | drop | Not second-brain mechanics; keep only as SKB examples. |
