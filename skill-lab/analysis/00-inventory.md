# 00 — Inventory (Prompt 1)

2026-11-09 · stage 1 of 6 · sources @ benai-skills 4c7a2ec, baalda 90929b5, second-brain-starter 74f7544.
Scope: every file under `sources/` (676 files, `find sources -type f`). Nothing in `sources/` was edited or executed.

**How to read this.** One table per creator. Ben AI ships 600+ files, most of them copies of the same reference sets across plugins, so rows are grouped by skill folder: a row = one SKILL.md plus its `references/`, `scripts/`, `templates/`, `assets/` (file count in brackets). Exact duplicates are listed once and marked **DUP →** with the canonical path (checked with `md5sum`). Paths are relative to `sources/`.

**Capability codes.** SET setup/onboarding · ROOT root file and routing · FMT note format · CAP capture (live session) · SCH scheduled update (connectors) · MNT maintenance (lint/optimize) · RET retrieval and ranking · DEC decay and supersession · SKB skills-from-brain references · DSH dashboards · TEAM sync, permissions · CLD cloud/always-on · EVL evals · — = out of scope for a second brain (domain workflow).

---

## 1. Ben AI (`benai/`) — 663 files, MIT except where noted (`benai/SOURCE.md`)

### 1a. `obsidian/` plugin (184 files) — canonical copy of the core OS skills

| file | kind | capability | one-line purpose |
| --- | --- | --- | --- |
| `obsidian/.claude-plugin/plugin.json` | doc | — | Plugin manifest. |
| `obsidian/skills/os-setup/SKILL.md` (745 l) + `references/` (35) | skill + templates | SET, ROOT, FMT, CAP | Bootstraps vault folders, CLAUDE.md, memory, hooks and output styles, then interviews the user; solo vs business mode (`os-setup/SKILL.md:3`). Hooks made executable at `os-setup/SKILL.md:188-191`. |
| ↳ `references/claude-md-template*.md`, `claude-md-<folder>.md` (12) | template | ROOT | Root CLAUDE.md and one routing CLAUDE.md per folder (context, daily, departments, intelligence, onboarding, processes, projects, resources, skills, team). |
| ↳ `references/context-*.md` (15) | template | SET, FMT | Starter context files: me, business, brand, ICP, market, offer/services, strategy, team, stakeholders, pain points, infrastructure, operator. |
| ↳ `references/settings-json-template.md`, `gitignore-template.md`, `claudeignore-template.md` | template | ROOT, CAP | Claude Code settings (hooks wiring), ignore files. |
| ↳ `references/team-profile-template.md`, `team-tasks-template.md` | template | TEAM | Per-member profile and task file. |
| ↳ `references/skills-placeholder-{linkedin,newsletter}-*.md` (4) | template | SKB | Example skill whose references point into the vault. |
| `obsidian/skills/os-operator/SKILL.md` (265 l) + `references/operator-prompt-template.md`, `connector-fragments.md` | skill + prompt | SCH, MNT, DEC | Builds a personalised autonomous "Operator" prompt and schedules it via the `schedule` skill; cadence, freshness, daily-as-state, failure handling (`os-operator/SKILL.md:3,9,16`). |
| `obsidian/skills/os-optimizer/SKILL.md` (925 l) + `references/` (24) | skill + docs + html | MNT, DEC, ROOT, EVL | Audit of any markdown vault with **10 frameworks** F1-F6, G7, F10, F8, F9 (`os-optimizer/SKILL.md:21-34`), score /100 (`:401-442`), per-finding apply/plan gate (`:465`), stale-entry rewrite with `## History` + link to superseding source (`:637`). |
| ↳ `references/<framework>.md` (8: anthropic-claude-md, karpathy-llm-wiki, caveman-compression, chroma-context-rot, anthropic-managed-memory, progressive-disclosure, anthropic-dreams, anthropic-architecture, claude-5-rules) | doc | MNT | The "why" for each framework (Ben AI's paraphrase of Karpathy, Anthropic, Chroma). |
| ↳ `references/passes-*.md` (10) | prompt | MNT | The "how": regex/heuristics and finding format per framework. |
| ↳ `references/practitioner-notes.md` | doc | MNT | Field notes feeding G7 hygiene. |
| ↳ `references/report-*.html` (4) | template | DSH, MNT | HTML before/after audit report. |
| `obsidian/skills/team-os/SKILL.md` (170 l) + `reference/benai-relay-fork/{main.js,manifest.json,styles.css}` | skill + code | TEAM | Replaces the Relay Obsidian plugin with a BenAI fork for a shared vault. **Third-party JS: read before any use.** |
| `obsidian/skills/os-mcp/SKILL.md` (177 l) + `reference/relay-mcp-server/` (19: TS src, auth/, Dockerfile, railway.json, package*.json, .env.example, AUTH.md) | skill + code | CLD, TEAM | Deploys a Relay MCP server on the user's Railway account so cloud agents can read/write the vault. |
| `obsidian/skills/agentic-os-setup/SKILL.md` (620 l) + `references/obsidian/` (dashboard JS/CSS, templates, `frappe-charts.min.js`, `plugins/`) + `references/standalone/` (Next.js template, RAILWAY.md, personalization.md) | skill + code + templates | DSH, CLD | Command-center dashboard either inside Obsidian (5 bundled plugins, button bar) or as a standalone Next.js app with MCP integrations. 94 files, mostly front-end template. |
| `obsidian/skills/*/scripts/.gitkeep` (several) | — | — | Empty placeholders. |

### 1b. `baalda-os/` plugin (69 files) — Baalda-app variant of 1a

| file | kind | capability | one-line purpose |
| --- | --- | --- | --- |
| `baalda-os/.claude-plugin/plugin.json` | doc | — | Manifest. |
| `baalda-os/skills/setup/SKILL.md` (803 l) + `references/` (35) | skill + templates | SET, ROOT, FMT | Same as os-setup, targeted at a Baalda vault, adds per-folder routing indexes. 31/35 references **DUP →** `obsidian/skills/os-setup/references/`; differ: `claude-md-template.md`, `claude-md-template-business.md`, `gitignore-template.md`, `claudeignore-template.md`. |
| `baalda-os/skills/operator/SKILL.md` (288 l) + 2 refs | skill + prompt | SCH, MNT | Baalda variant of os-operator; SKILL.md and both refs differ slightly from 1a. |
| `baalda-os/skills/optimizer/SKILL.md` (1001 l) + `references/` (24) | skill + docs | MNT, DEC, EVL | Baalda variant of os-optimizer, same 10 frameworks. 17/24 refs **DUP →** 1a; differ: anthropic-dreams, anthropic-managed-memory, passes-anthropic-claude-md, passes-anthropic-memory, passes-architecture, passes-general-hygiene, practitioner-notes. |
| `baalda-os/skills/baalda-guide/SKILL.md` (111 l) + `references/{faq,features,file-formats,sources}.md` | skill + doc | — (product FAQ) | Answers questions about the Baalda app. Unique to this plugin. |

### 1c. `zip-video/` (65 files) — free ZIP from the 18-tips video

| file | kind | capability | one-line purpose |
| --- | --- | --- | --- |
| `zip-video/{setup,operator,optimizer}/**` (64) | skill | SET, SCH, MNT | **DUP →** `baalda-os/skills/{setup,operator,optimizer}/` — byte-identical (`diff -rq`, confirmed by `benai/SOURCE.md`). |
| `zip-video/video-prompts.md` (31 l) | prompt | ROOT, DSH, SKB | Four prompts from the video: write AGENTS.md as routing table (tip 4), build a dashboard (tip 11), point skill references at the brain (tip 12), business-first rule (tip 18). |

### 1d. `other-os/` (246 files) — alternative OS tiers

| file | kind | capability | one-line purpose |
| --- | --- | --- | --- |
| `other-os/aios/skills/local-os-builder/SKILL.md` (747 l) + 35 refs | skill + templates | SET, ROOT | Local Obsidian vault builder. Refs are the os-setup set (**DUP**); SKILL.md near-copy of os-setup (differs). |
| `other-os/aios/skills/cloud-os-builder/SKILL.md` (898 l) + 43 refs | skill + templates | SET, CLD | Same OS hosted in Google Drive / OneDrive / iCloud / Dropbox or Notion. Unique refs: `google-drive.md`, `onedrive.md`, `icloud.md`, `dropbox.md`, `notion-os-skill-template.md`, `notion-template-spec.md`, `structure-spec.md`, `comparison.md`; rest **DUP**. |
| `other-os/aios/skills/skill-os-builder/SKILL.md` (86 l) + `references/{structure-spec,routing-patterns}.md` + `templates/_SKILL.md.tmpl`, `templates/context/*.md.tmpl` (5) | skill + templates | SET, ROOT, SKB | Whole "OS" inside one skill: short router SKILL.md + context files, no vault. **Shortest root file in Ben AI's set** — closest to the guide's 60-line target. |
| `other-os/aios/.claude-plugin/plugin.json` | doc | — | Manifest. |
| `other-os/agentic-os/skills/agentic-os-obsidian/SKILL.md` (381 l) + 23 | skill + code | DSH | Obsidian half of `agentic-os-setup` (older split version). |
| `other-os/agentic-os/skills/agentic-os-standalone/SKILL.md` (228 l) + 3 | skill + code | DSH, CLD | Next.js half of `agentic-os-setup`. |
| `other-os/agentic-os/skills/os-mcp/**` (21) | skill + code | CLD | **DUP →** `obsidian/skills/os-mcp/`. |
| `other-os/agentic-os/skills/web-artifacts-builder/` (SKILL.md 74 l, `scripts/init-artifact.sh`, `bundle-artifact.sh`, `shadcn-components.tar.gz`, LICENSE.txt) | skill + script | DSH | React/Tailwind artifact bundler. **Shell scripts + tarball: do not run.** |
| `other-os/marketing-os/skills/marketing-os-setup/SKILL.md` (212 l) + `references/{structure,conventions,interview,folder-indexes,context-templates,channel-templates,connectors}.md` | skill + templates | SET, ROOT, FMT, DEC | Marketing second brain as single source of truth for marketing skills; has its own conventions file. Much shorter than os-setup. |
| `other-os/marketing-os/skills/marketing-os-routines/SKILL.md` (188 l) + `assets/` (11 routine prompts: morning-performance-sweep, content-pipeline-sync, campaign-sync, dashboard, pipeline-hygiene, market-scan, competitor-radar, customer-intel, monthly/quarterly-report, `_register.md`) | skill + prompt | SCH | Ten scheduled routines in two groups + a register. |
| `other-os/marketing-os/skills/marketing-os-dashboard/` (SKILL.md 214 l, `assets/control-center.html`, 2 refs) | skill + template | DSH | Single-page control center rendered from OS files. |
| `other-os/marketing-os/skills/marketing-os-{research,market-intel}/` (239 l each, 2 refs each) | skill | RET, SCH | Answers open questions filed in the OS and promotes them to findings; scored intel briefs into a backlog. |
| `other-os/marketing-os/skills/marketing-os-{newsletter,carousel}/` (+ `scripts/footer.py`, `assets/fonts/mono.ttf`) | skill + script | SKB | Content skills that read ICP/voice/offer from the OS and file the output back. Good SKB examples. |
| `other-os/marketing-os/skills/instant-ui/` (32 l + 6) | skill + template | DSH | BenAI-branded HTML design language. `references/design-tokens.md` **DUP →** `sales/skills/sales-rep-analyzer/references/instant-ui/design-tokens.md`. |
| `other-os/marketing-os/skills/{os-optimizer,os-operator,os-mcp,team-os}/**` | skill | MNT, SCH, CLD, TEAM | **DUP →** `obsidian/skills/` (identical, `diff -rq` empty). |

### 1e. `sales/` (83 files) and `baalda-app/` (2)

| file | kind | capability | one-line purpose |
| --- | --- | --- | --- |
| `sales/routines-guide.md` (248 l) — personal use | prompt | SCH, DSH, MNT | Seven Sales OS routines: morning (`:204`), pipeline hygiene (`:145`), call scoring (`:92`), campaign sync (`:73`), monthly (`:52`) and quarterly (`:32`) reports, live dashboard rebuild (`:5`). |
| `sales/transcript-sales-os.md` | transcript | SCH, DSH, SKB | Sales OS video: connectors + skills + sales second brain + dashboard + routines. |
| `sales/skills/*` (14 skills, 76 files): win-loss-analysis (+`scripts/generate_charts.py`), pipeline-review, call-prep, crm-prospect-mining (+2 agents), lead-generation, lead-qualification, lead-intelligence, email-personalization, linkedin-post-engagers, post-disco-followup (+templates), setup-post-disco, client-onepager (+`assets/template.html`), create-an-asset, sales-rep-analyzer (+`scripts/generate_report.js`) | skill + script | — / SKB | Domain sales workflows (CRM, Fireflies, Gmail, Vercel). Relevant only as examples of skills reading context; `setup-post-disco` is an onboarding-wizard pattern (SET). |
| `sales/agents/{icebreaker-writer,lead-qualifier,lead-researcher,linkedin-scraper}.md` | prompt | — | Sub-agent definitions. |
| `sales/.claude-plugin/plugin.json` | doc | — | Manifest. |
| `baalda-app/README.md`, `AGENTS.md` — Apache-2.0 | doc | TEAM, CLD | Baalda app: markdown on disk as source of truth + real-time collaboration, MCP access (`README.md:41-57`). |
| `transcript-18-tips.md` | transcript | ROOT, MNT, DSH, SKB, TEAM | 18 tips; credits Karpathy for the index concept (`transcript-18-tips.md:53`); points to the free optimizer (`:71`). |
| `SOURCE.md` | doc | — | Origins, commits, licences. |

---

## 2. Cole Medin (`cole-medin/`) — 15 files, **no licence: read only, no text reuse**

| file | kind | capability | one-line purpose |
| --- | --- | --- | --- |
| `README.md` (158 l) | doc | SET, CAP, SCH, CLD | Fill a requirements template → generate a phased PRD; phases incl. hooks SessionStart/PreCompact/SessionEnd (`README.md:88`) and heartbeat + daily reflection (`:92`); proactivity levels (`:143`). |
| `.claude/skills/create-second-brain-prd/SKILL.md` (144 l) | skill | SET | Turns the filled requirements file into a personalised build plan (PRD). |
| `.claude/skills/create-second-brain-prd/my-second-brain-requirements.md`, `example-my-second-brain-requirements.md` | template | SET | Blank and worked requirements template. |
| `.claude/skills/create-second-brain-prd/references/architecture-reference.md` | doc | ROOT, CAP, SCH, CLD | Reference architecture the PRD draws from. |
| `templates/memory/BOOTSTRAP.md` | template | SET | First-run interview, fills USER/SOUL/HEARTBEAT then deletes itself (`README.md:101`). |
| `templates/memory/SOUL.md`, `USER.md` | template | ROOT, FMT | Agent persona and user profile. |
| `templates/memory/MEMORY.md` | template | FMT, CAP | Long-term curated memory. |
| `templates/memory/HEARTBEAT.md` | template | SCH, DEC | Checklist for the 30-min proactive run; flags tasks overdue > 1 week as stale (`HEARTBEAT.md:27`). |
| `templates/memory/HABITS.md` | template | FMT | Habits/routines file (unique idea, rule 6). |
| `templates/memory/daily/.gitkeep` | — | CAP | Empty daily-log folder. |
| `SecondBrainArchitecture.png`, `WhyBuildYourOwnSecondBrain.png` | image | — | Diagrams. **Not greppable**; need visual read in stage 2. |
| `transcript.md` | transcript | CAP, SCH, RET | 4 Cs video: Karpathy-style wiki (`transcript.md:25`), hook loads the top-level KB at session start (`:57`), 30-min heartbeat (`:87`). |
| `SOURCE.md` | doc | — | Origin, commit, licence. |

---

## 3. Nate Herk (`nate-herk/`) — 2 files, licence unknown

| file | kind | capability | one-line purpose |
| --- | --- | --- | --- |
| `transcript.md` | transcript | ROOT, RET, CLD, SET | 5 levels: routing CLAUDE.md + folders, LLM wiki + indexes, per-folder vector search, knowledge graph (LightRAG), always-on (GBrain); choose level per data type (`transcript.md:105`); uses a `grill me` interview skill (`:115-117`). |
| `SOURCE.md` | doc | — | Origin and level summary. |

## 4. French creator (`french/`) — 3 files, gated, personal use

| file | kind | capability | one-line purpose |
| --- | --- | --- | --- |
| `transcript.md` (EN translation) | transcript | SET, ROOT, CAP, MNT, SKB | agent.md + about.md; "interview" prompt for onboarding; `/done` end-of-session command; skills create-project, project, cleanup, skill-manager (`transcript.md:5`). |
| `SOURCE.md`, `.gitkeep` | doc | — | Origin + TODO. |

## 5. Karpathy (`karpathy/`) — 2 files

| file | kind | capability | one-line purpose |
| --- | --- | --- | --- |
| `SOURCE.md`, `.gitkeep` | doc | — | Gist URL + TODO. **No content.** Only second-hand versions exist: `benai/obsidian/skills/os-optimizer/references/karpathy-llm-wiki.md` (Ben AI's paraphrase) and mentions in Cole (`transcript.md:25`) and Nate transcripts. |

---

## 6. Flags

### Missing (named somewhere, absent from files)
| item | named in | impact |
| --- | --- | --- |
| Karpathy `llm-wiki.md` | `karpathy/SOURCE.md`, PLAYBOOK | Karpathy column would rest on second-hand paraphrase. **Blocks a fair card.** |
| French masterclass + mini-course: interview prompt, `/done`, cleanup, skill-manager, create-project, project skills | `french/transcript.md:45-55`, `french/SOURCE.md` | Only the transcript exists; capture (`/done`) is the guide's planned brain-capture source. |
| Nate Herk `grill-me` skill, level 1-4 example project, slides | `nate-herk/transcript.md:115-117`, `nate-herk/SOURCE.md` | Interview and retrieval levels unverifiable in files. |
| Cole Medin's actual hook scripts (SessionStart/PreCompact/SessionEnd) and heartbeat runner | `cole-medin/README.md:88,92`, `transcript.md:57,87` | Repo only describes them as PRD phases; no code to compare with `reference/protect.sh`/`brain.py`. |
| Sales OS dashboard / setup skill | `sales/routines-guide.md:5`, `sales/transcript-sales-os.md` | No sales-specific setup or dashboard skill in `sales/skills/`; closest are `marketing-os-dashboard` and `agentic-os-setup`. |
| `schedule` skill invoked by os-operator | `obsidian/skills/os-operator/SKILL.md:16` | External Claude skill, not shipped; operator cannot schedule outside Claude. |
| Playbook claims "22-pass audit", "9-framework optimizer" | `PLAYBOOK.md` collection table | Not found: optimizers declare 10 frameworks (`os-optimizer/SKILL.md:21-34`). Playbook text is out of date. |

### Duplicated
- **Inside Ben AI (heavy):** `zip-video/` = `baalda-os/` (64 files identical). `marketing-os/{os-optimizer,os-operator,os-mcp,team-os}` = `obsidian/`. `os-mcp` exists 3×, `team-os` 2×. The 35-file os-setup reference set exists 5× (obsidian, baalda, zip, local-os-builder, cloud-os-builder); 4 of them differ only in root/ignore templates. `agentic-os-setup` (obsidian) merges `agentic-os-obsidian` + `agentic-os-standalone` (other-os). About **400 of 663 Ben AI files are copies**; stage 2 should read only the canonical paths above plus the listed diffs.
- **Cleanup 2026-11-09:** the byte-identical copies (zip-video skills, marketing-os os-optimizer/os-operator/os-mcp/team-os, agentic-os/os-mcp) were removed from `sources/`, see `benai/DUPLICATES.md`. Rows marked DUP above for those folders now point to the only remaining copy. 538 files remain.
- **Across creators (ideas, not files):** Karpathy LLM wiki appears in Ben AI (`os-optimizer` F2), Cole (`transcript.md:5`), Nate (level 2). Onboarding interview appears in Ben AI os-setup, Cole BOOTSTRAP.md, French interview prompt, Nate grill-me. Scheduled agent appears as Ben AI Operator/routines and Cole heartbeat. Root routing file appears everywhere (CLAUDE.md, AGENTS.md, agent.md). No file-level duplication across creators.

### Unreadable or hard to cite
- Binary: 2 PNGs (Cole), `mono.ttf`, `shadcn-components.tar.gz`, `frappe-charts.min.js` (minified).
- Transcripts re-wrapped on 2026-11-09 (5 sentences per paragraph, text unchanged, checked by script), so `transcript.md:N` cites are now precise.
- Scripts to treat as untrusted, not run: `web-artifacts-builder/scripts/*.sh`, `marketing-os-carousel/scripts/footer.py`, `win-loss-analysis/scripts/generate_charts.py`, `sales-rep-analyzer/scripts/generate_report.js`, `team-os` relay fork `main.js`, `os-mcp` relay server (TS, Docker, OAuth), hook wiring in `os-setup/references/settings-json-template.md`.

### Coverage at a glance (who has a file for it)
| capability | benai | cole-medin | nate-herk | french | karpathy |
| --- | --- | --- | --- | --- | --- |
| setup/onboarding | os-setup, setup, skill-os-builder, marketing-os-setup | PRD skill, BOOTSTRAP | transcript only | transcript only | — |
| root file and routing | claude-md templates, video-prompts tip 4 | SOUL/USER | transcript | transcript | — |
| note format | context-* templates, marketing conventions | memory templates | — | — | — |
| capture (live session) | hooks via os-setup | README phase only | — | transcript (`/done`) | — |
| scheduled update | os-operator, marketing routines, sales routines | HEARTBEAT | — | — | — |
| maintenance | os-optimizer (10 frameworks) | — | — | transcript (cleanup) | — |
| retrieval and ranking | marketing-os-research only | transcript | transcript (levels 2-4) | — | — |
| decay and supersession | optimizer F8.3, operator freshness | HEARTBEAT stale tasks | — | — | — |
| skills-from-brain | video-prompts tip 12, marketing content skills | — | — | transcript (skill-manager) | — |
| dashboards | agentic-os-setup, marketing dashboard, sales routine 7 | — | — | — | — |
| team | team-os, baalda-app | — | — | — | — |
| cloud/always-on | os-mcp, cloud-os-builder | README phases | transcript (GBrain) | — | — |
| evals | optimizer score /100 (audit, not evals) | — | — | — | — |

Early signal for stage 3: nobody ships a real **eval** suite or **ranked retrieval with decay**; both will lean on `reference/guide.md` (§5.1, §5.2) and `reference/brain.py`.

## Next
Stop for review. Before Prompt 2: paste the Karpathy gist (Raw view) into `karpathy/llm-wiki.md`; until then `karpathy/llm-wiki-summary.md` is a second-hand outline.
