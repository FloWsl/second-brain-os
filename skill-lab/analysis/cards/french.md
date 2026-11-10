# Card — French creator (`sources/french/`)

2026-11-09 · stage 2 · transcript only (EN translation, gated material, personal use). Missing: masterclass, mini-course, interview prompt text, /done, cleanup, skill-manager, create-project skills.
All cites are `transcript.md:<line>`.

## 1. Philosophy
Most people's work folders are broken by copy-pasted systems from many videos; the fix is radical simplicity (`:7-11`). A second brain is one folder of text that the agent searches before answering, a "RAG without a database" (`:13-29`). It holds only what lives in your head (projects, offer, decisions); live data stays in tools reached through connectors (`:43, :55-61`).

## 2. Architecture
- **Folders**: `brain/` with `agent.md`, `projects/<x>/about.md`, `notes/` (journal, ideas, to-dos), `archive/` (`:31-35, :69`). Heavy working material (video rushes, editing skills) lives in a separate folder (`:71-73`).
- **Root file**: `agent.md`, read at the start of every conversation, "just enough" information (`:31, :35`).
- **Entry point per project**: `about.md` with status, decisions, next step (`:35-41`).
- **What loads when**: agent.md always; about.md when a project is named (`:37`).
- **Schedules / hooks**: auto-save after 20 minutes of inactivity and a `/done` command, backups to GitHub (`:51`). Mechanism not shown.

## 3. Mechanism per capability
| capability | mechanism | cite |
| --- | --- | --- |
| setup/onboarding | Interview prompt: one question at a time (client, offer, price, goal), write to the project's about.md; or a 5-min voice dump | `:45-47` |
| root file and routing | agent.md + about.md entry points, few folders | `:31-37, :69` |
| note format | about.md always up to date, "follows specific rules"; decisions logged with reason | `:39-41` |
| capture (live session) | `/done`, plus auto-save after 20 min idle; daily notes | `:47-51, :63` |
| scheduled update | — | — |
| maintenance | `cleanup` skill "to tidy up" | `:55, :63` |
| retrieval and ranking | Agent greps words like price/rate/euros, reads the matching file | `:23-29` |
| decay and supersession | One fact in one place, edit one line when the price changes; archive finished projects | `:33, :61` |
| skills-from-brain | `skill-manager` skill; skills = repeatable processes | `:53-55` |
| dashboards | — | — |
| team | — | — |
| cloud/always-on | Same files usable from Hermes on a VPS | `:53` |
| evals | — | — |

## 4. Assumptions and dependencies
Claude Code / Codex / Hermes; connectors (Gmail, Notion, Stripe, course platform); GitHub for backup (`:51-65`). No app, no database.

## 5. Strengths vs guide
- **Simplest coherent model** (agent.md + about.md + notes + archive); the guide's starter structure is largely built from it.
- **about.md as project entry point** with status, decisions and next step (`:35-41`) — adopted by the guide.
- **Idle-timeout capture (20 min)** in addition to `/done` (`:51`): a trigger the guide mentions but nobody ships.
- **Separate working folders from the brain** (`:71-73`): keeps skills and rushes out of thinking space.
- **Atomic information + AI tends to duplicate** warning (`:61`).

## 6. Weaknesses and risks
- **No files**: every skill is named, none is readable; mechanism for auto-save unknown.
- **No frontmatter, index, decay, ranking or evals** described.
- **No guidance on root file length or content** beyond "just enough".
- Gated content: analysis only, nothing redistributable.

## 7. Scores vs guide (1-5)
| axis | score | why |
| --- | --- | --- |
| simplicity | 5 | Fewest folders and files of all sources. |
| token cost | 4 | One small root file + entry points; untested at scale. |
| freshness/decay | 2 | One-place rule and archive only. |
| portability | 5 | Plain files, any agent, explicit multi-agent claim (`:53`). |
| maintainability | 3 | Simple, but no index or lint mechanism visible. |
| safety | 3 | Connectors instead of copies; nothing on permissions or scripts. |

## 8. Keep / adapt / drop
| item | verdict | reason |
| --- | --- | --- |
| agent.md + about.md + notes + archive layout | keep | Core of guide's structure; simplest. |
| Interview prompt (one question at a time) | keep | Shared with Cole BOOTSTRAP and Nate grill-me; write our own text. |
| `/done` + 20-min idle capture | adapt | brain-capture skill + a hook or schedule for the idle trigger; needs a mechanism. |
| cleanup skill | adapt | Becomes brain-lint (content unknown, use guide + Ben AI checks). |
| skill-manager | trial | Unknown content; revisit if the masterclass is collected. |
| Separate working folders | keep | One AGENTS.md line or setup note. |
