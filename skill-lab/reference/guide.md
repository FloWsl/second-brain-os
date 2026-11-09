# How to Build an AI Second Brain: The Complete Guide

Nov 9, 2026 · @Florian

## 1. What a second brain is and why it matters

An AI second brain is a folder of plain markdown files that every AI tool you use reads before working, so its output reflects how you and your business actually work. All four sources converge on the same definition: no database, no subscription, just well-organised text files plus a map that tells the agent where things live.

**The problem it solves.** Without it, every new chat starts from zero. You re-paste your offer, your prices, your tone, your client context. It is slow, costly in tokens, and the model weighs your 2024 price and your 2026 price as equally valid.

**How it works.** It is retrieval-augmented generation (RAG) done with files instead of a vector database: the agent searches first (by reading an index, grepping for words like "price" or "rate"), opens only the relevant files, then answers. Think of the context window as a desk and the folder as a filing cabinet: you only pull the drawers the task needs.

**Why files beat a database, a SaaS tool or built-in memory**

| Option | Strength | Weakness for a second brain |
| --- | --- | --- |
| Local markdown folder | Readable by you and any agent, editable by hand, portable across Claude, ChatGPT, Codex, Hermes, versionable with git | Needs a sync layer for teams or cloud agents |
| Vector database | Scales to very large corpora | Needs code and a server, opaque to humans, corrections need scripts |
| Notion / Google Drive via connector | Data already lives there | Every read and write goes through a connector: slower, less accurate, more tokens |
| Built-in assistant memory | Zero setup | Holds a limited number of facts, locks your context into one provider |

**Why now.** Coding agents (Claude Code, Codex and similar) are strong enough that a folder of text plus a few connectors replaces a pile of paid tools. One practitioner reports going from about 10 hours saved per week at launch to 25 to 30 hours, mostly by improving the brain with the brain itself. The value compounds: the earlier you start, the more context it holds in a month.

The idea is old. Vannevar Bush described the Memex in 1945, a personal store of books, letters and notes with associative trails between them. What he could not solve was who does the upkeep; [Karpathy's LLM Wiki note](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) argues the LLM now handles that, because it does not get bored of bookkeeping.

## 2. Core principles

The sources agree that most second brains fail from over-engineering, not under-engineering. Five principles prevent that.

1. **Keep it simple.** A folder, a root map file and a few subfolders. Skip the 3D graphs, vector databases and 10-step pipelines sold on YouTube. One creator found that about 80% of the people he audited had copy-pasted systems from dozens of videos into an unusable mess.
2. **Store insights, not raw data.** The brain is a filtered layer on top of your tools. Save takeaways, decisions and syntheses; leave raw emails, CRM rows and Stripe data where they are and reach them through connectors on demand.
3. **One fact, one place.** Never duplicate information. If your price changes, you edit one line. AI tends to duplicate, so the agent must be told to update existing files rather than create new ones (Karpathy-style implementations call this "extend, don't create").
4. **Capture what lives only in heads.** Strategy, the reason you raised prices, what a failed launch taught you, preferences. None of that sits in a CRM, and it is the highest-value content.
5. **Record decisions with their reason.** A decision log stops the agent from repeating past mistakes or reopening settled questions.

**The 80/20 rule.** In a brain of thousands of files, 5 to 10 files deliver most of the value because they are relevant to almost every task: strategy, ideal customer profile (ICP), offer and pricing, brand voice, team, and who you are. Build those first.

## 3. The framework: the 4 Cs

A working second brain needs four components, in this order: Context, Connections, Capabilities, Cadence. The framework comes from AI educator Nate Herk; get these right and the underlying model barely matters (the same brain has been run on Haiku, Sonnet, Opus, Codex and Kimi with good results). Use each audit both when building and when reviewing an existing brain.

| C | What it is | Audit test (open a fresh session) | Start small with |
| --- | --- | --- | --- |
| **Context** | What the brain knows about you and your business, available without digging | Ask "what does my business do and who works there?" It should answer like a teammate, without deep searching | A few core files (who you are, business, behaviour rules) + a growing wiki |
| **Connections** | Access to where you actually work: email, calendar, tasks, CRM, Drive, GitHub, Slack | Ask for a "Monday morning catch-up": priorities, emails to answer, people needing attention. It should find everything quickly | 2 or 3 MCP connectors for the tools you use daily |
| **Capabilities** | Skills: your codified workflows (edit a video, prep a call, write a proposal) | Give a one-line request for a weekly job. A real output should come back without many clarifying questions or reinventing the process | One skill for your most repetitive task |
| **Cadence** | Proactive, scheduled work done without being asked | Put one trusted workflow on a schedule. It should run and report back on its own | A "heartbeat" that drafts email replies |

**How they fit together.** Context tells the agent when to use a connection; capabilities chain connections into a process; cadence runs proven capabilities automatically. Automate only what already works by hand: build the skill, use it with supervision, then schedule it.

**The universal fix.** When an audit fails, tell the brain exactly that ("you don't feel like you know my business off the top of your head, what can we change?") and design the fix together. Using the brain to improve itself is how most of the gains are made.

**Connection hygiene.** Wrap connectors so the agent only gets the tools you want, for example "draft email" but not "send email". Where no MCP server exists, have the brain build a small CLI tool for that platform.

## 4. Setup in about 30 minutes

You can get roughly 80% of the value in one sitting. Follow these steps in order.

1. **Create one folder on your computer.** One brain, not one per client or project: clients, departments and businesses are subfolders, and the root map routes the agent. Only split if two businesses share no context at all, or to separate personal from business. Keep heavy working material elsewhere: a video-editing folder with rushes and editing skills lives outside the brain, which stays your thinking space.
2. **Do a brain dump.** Open the folder in Claude (or your agent), turn on voice dictation (Wispr Flow, Whisper) and ramble for 5 to 30 minutes: who you are, what you do, customers, goals, strategy, writing style, team. Or use an interview prompt: "Interview me to fill in \[project\]. Ask one question at a time: client, offer, price, goal. Then write it to the right files." The agent turns the mess into 5 to 10 clean files.
3. **Lock in a simple folder structure.** The names matter less than never changing them, because every move forces the map to be rewritten and the agent starts saving in the wrong place.
4. **Write the root map (AGENTS.md / CLAUDE.md).** Read first in every session. It is a routing table, not a manual.
5. **Add an index file per subfolder** once a folder holds more than a handful of files.
6. **Open the folder in a viewer.** Obsidian (free) shows the files and a graph of links; it changes nothing for the AI but makes the brain easy for you to read, check and fix. Apps such as Balda add team sync on top of the same folder.
7. **Start every chat by selecting the folder**, so the agent reads context and saves new information back. The brain then grows as you work.

**A starter structure** (merge of the four sources; rename freely, then freeze it):

```markdown
brain/
├── AGENTS.md            # root map: routing table + rules (read every session)
├── CLAUDE.md            # one line: @AGENTS.md (see note below)
├── context/             # the 5-10 core files
│   ├── me.md            # who you are, role, preferences
│   ├── business.md      # what you do, strategy, goals
│   ├── icp.md           # ideal customer profile
│   ├── offer.md         # offers and current prices
│   └── voice.md         # tone and writing style
├── projects/
│   └── <project>/
│       ├── about.md     # entry point: summary, status, decisions, next step
│       └── ...
├── clients/ · people/ · sales/   # one file per entity, each folder with index.md
├── notes/
│   ├── daily/           # what happened each day
│   └── ideas.md · todo.md
├── decisions.md         # decision + date + reason
└── archive/             # finished projects move here
```

**What goes in the root map.** For each folder: what is in it, when to read it, where to save new things. Plus a handful of rules: update existing files rather than creating duplicates, log decisions with their reason, never store raw exports. Keep it under 200 lines; Anthropic's guidance is that longer files consume more context and reduce adherence ([summary of the guidance](https://mcp.directory/blog/karpathy-claude-md-annotated-2026)), and many good files are around 60 lines. Ask of each line: would removing it cause a mistake? If not, cut it.

```markdown
# AGENTS.md
Always act in the best interest of the business, based on context/business.md.
If a request conflicts with it, say so clearly instead of agreeing.

## Routing
| Folder | Contains | Read when | Save here |
| context/ | identity, strategy, ICP, offer, voice | almost every task | only on explicit change |
| projects/<x>/ | about.md + working files | task names the project | progress, decisions |
| clients/ | one file per client, index.md | proposals, calls, emails | call notes, status |
| notes/daily/ | daily log | "what did I do this week" | end of each session |

## Rules
- Read the folder's index.md before opening files.
- One fact, one place: edit, never duplicate.
- Decisions go to decisions.md with date and reason.
- Live data (email, CRM, payments) comes from connectors, not files.
```

**AGENTS.md vs CLAUDE.md.** AGENTS.md is the cross-tool open standard, read by Codex, Cursor, Gemini CLI and others and now stewarded by the Linux Foundation's Agentic AI Foundation ([agents.md](https://agents.md/)). Claude Code historically read only CLAUDE.md; since version 2.1.277 (18 September 2026) it reads AGENTS.md when no CLAUDE.md exists, but if both exist it reads only CLAUDE.md ([Developers Digest](https://www.developersdigest.tech/blog/claude-code-agents-md-support)). The safest setup is a CLAUDE.md containing the single line `@AGENTS.md`, which imports the shared file ([travis.media](https://travis.media/blog/claude-md-import-agents-md)). Never maintain two diverging copies.

**Index files.** Borrowed from [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): each index lists every file with a link and a one-line summary. The agent reads the index first, then drills into only the relevant pages. Karpathy reports this works well up to about 100 sources and hundreds of pages without any embedding search; beyond that, add a local search tool such as qmd.

**Two-layer context (optional upgrade).** One practitioner loads three small files into every session through a Claude Code hook: soul.md (how the agent should behave), user.md (you and your business) and memory.md (the most important facts bubbled up from the wiki, such as current objectives). Everything else lives in the wiki and is read on demand.

## 4.1 Writing AGENTS.md in 2026

The best root file is short, hand-written, and holds only what the agent cannot infer by itself. That is the main lesson of 2026's research, and it changes how the "map" from section 4 should be written.

**What the evidence says.** An ETH Zurich study (Gloaguen et al., [arXiv 2602.11988](https://arxiv.org/abs/2602.11988), February 2026) tested Claude Code, Codex and Qwen Code with no context file, an LLM-generated one, and a human-written one. Auto-generated files lowered task success by about 3% on average and raised inference cost by over 20%; human-written files gained only about 4%, at roughly 19% extra cost ([Engineer's Codex summary](https://engineerscodex.com/agents-md-making-ai-worse)). The agents were not ignoring the files: they obeyed them too well, running more searches and reading more files without reaching the right ones faster. Overviews of the folder structure did not speed up navigation ([InfoQ](https://infoq.com/news/2026/03/agents-context-file-value-review/)). A separate study (Lulla et al.) found well-structured files cut runtime 28% and tokens 16%, so quality, not presence, is what decides ([summary](https://blog.clawsouls.ai/en/posts/agents-md-hurts-or-helps/)).

The studies measured code repositories, not knowledge bases, but the mechanism transfers directly: every instruction is obeyed and paid for on every turn.

**Rules for a second-brain root file**

1. **Write it yourself, then let the agent tighten it.** Never ship a file generated with /init or "write me an AGENTS.md" unedited; generated files restate the obvious.
2. **Only non-inferable knowledge.** Your naming conventions, where things are saved, which file wins on conflict, business rules. Not "this folder contains projects" when the folder is called projects/.
3. **Aim for 60 lines; 200 is the ceiling.** Anthropic's memory docs state that longer files consume more context and reduce adherence.
4. **Pointers, not copies.** Link to context/offer.md instead of pasting the offer. Note that `@` imports in Claude Code load the imported file at session start, so they organise but do not shrink context; plain backticked paths are read only when needed ([Claude Code memory docs](https://code.claude.com/docs/en/memory)).
5. **Every rule checkable and with its reason.** "Prices live only in context/offer.md, because duplicates went stale twice" beats "keep things tidy". A reason lets the agent handle cases the rule did not foresee.
6. **Pair each prohibition with a direction.** "Do not create new client files; append to the existing one in clients/".
7. **No contradictions across files.** Claude Code concatenates every CLAUDE.md and rules file it loads; nothing overrides anything, and conflicting instructions may be resolved arbitrarily.
8. **Grow it from failures.** Add a line only after the agent gets something wrong twice. Remove a line when deleting it would cause no mistake.

**Progressive disclosure: three layers of instructions**

| Layer | File | Loaded | Holds |
| --- | --- | --- | --- |
| Always | AGENTS.md (via CLAUDE.md `@AGENTS.md`) | Every session | Routing table, 5 to 10 hard rules, business-first rule |
| On location | Nested AGENTS.md or CLAUDE.md in a subfolder; `.claude/rules/*.md` with `paths:` frontmatter | When the agent reads files there | Folder-specific conventions (e.g. client file template) |
| On task | Skills (SKILL.md) | When the task matches the skill description | Multi-step procedures: ingest, weekly lint, call prep |

Codex reads nested AGENTS.md files from root to leaf with deeper files taking precedence; Claude Code loads subfolder CLAUDE.md files and path-scoped rules only when it reads matching files ([Daniel Vaughan on AGENTS.md bloat](https://codex.danielvaughan.com/2026/03/27/agents-md-bloat-problem/)). Move anything that matters for one folder or one procedure out of the root.

**Survive compaction.** In long sessions Claude Code summarises the conversation. Root CLAUDE.md and unscoped rules are re-read from disk; path-scoped rules and nested files loaded mid-session can be summarised away. If a few lines must always be present (current objectives, today's focus), print them from a SessionStart hook with the `compact` matcher ([field test](https://dev.to/naman_here/why-claude-code-ignores-your-claudemd-and-how-to-fix-it-4pk0)).

**Instructions guide; hooks enforce.** Memory files are context, not configuration. For rules that must never be broken (never edit raw/, never delete from archive/), add a PreToolUse hook that blocks the action, and keep the line in AGENTS.md so the agent knows why.

**A 2026-style root file** (about 40 lines):

```markdown
# AGENTS.md
Second brain of <name>, <role>. Language: English. Today's date comes from the system, never assume it.

Act in the best interest of the business (context/business.md).
If a request conflicts with it, say so instead of agreeing.

## Where things live (read the folder's index.md first)
- context/   identity, strategy, ICP, offer, voice. Canonical. Edit only when I state a change.
- projects/  one folder per project; about.md is the entry point.
- clients/ people/  one file per entity, named kebab-case: clients/acme-corp.md
- notes/daily/YYYY-MM-DD.md  session log. notes/inbox.md  unsorted captures.
- decisions.md  dated decisions with reason. archive/  finished or superseded material.
- raw/  source documents. Read only.

## Rules (why in brackets)
- Search before creating: extend an existing note, never make a near-duplicate. [duplicates drift]
- One fact, one file. Link with [[note-name]] instead of copying. [single source of truth]
- Every note has frontmatter: type, status, updated, review_by. Update `updated` on every edit. [freshness ranking]
- When a fact changes, rewrite it and add `supersedes:` or move the old note to archive/. Never leave two versions active. [stale facts win otherwise]
- Prefer the note with the newest `updated` and status: active when sources disagree; flag the conflict.
- Live data (email, CRM, payments) comes from connectors, not from notes.
- End of session: append to notes/daily/, update touched about.md files, log decisions.
```

## 4.2 Markdown-only engineering

You can run a serious second brain with nothing but markdown, frontmatter, links and a few shell scripts, as long as every file follows the same conventions. The conventions are what make plain grep behave like a database.

**Why no vector store is needed at this scale.** Agents navigate by reading an index and grepping words, which is precise, auditable and free. Karpathy reports the index-first approach working at around 100 sources and hundreds of pages ([LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)); some implementers see index.md become unwieldy past roughly 100 to 200 pages, which is the signal to split indexes per folder or add a local search tool like qmd, not to abandon markdown.

**Note types.** Give every note one type; each type has a fixed template and a fixed home.

| Type | Home | Purpose | Changes |
| --- | --- | --- | --- |
| `context` | context/ | Canonical truths: identity, strategy, offer, voice | Rarely, only on explicit decision |
| `entity` | clients/, people/, tools/ | One person, company or thing; everything known about it | Often, rewritten in place |
| `project` | projects/\<x>/about.md | Status, goal, decisions, next step | Weekly |
| `concept` | wiki/ | A synthesised idea or method, built from several sources | When new sources arrive |
| `source` | wiki/sources/ | Summary of one raw document, with a link to it | Never after ingest |
| `decision` | decisions.md (or decisions/) | What was decided, when, why, what it replaces | Append-only |
| `log` | notes/daily/, log.md | What happened; timeline | Append-only |
| `inbox` | notes/inbox.md | Unsorted captures waiting for triage | Emptied weekly |

**Frontmatter schema.** YAML at the top of every note gives scripts and agents something structured to filter and rank on.

```yaml
---
title: Acme Corp
type: entity                # context | entity | project | concept | source | decision
status: active              # active | superseded | archived | draft
created: 2026-03-02
updated: 2026-11-07         # bump on every substantive edit
review_by: 2027-02-07       # when this must be re-confirmed (see 5.1)
importance: 4               # 1-5, set at write time
supersedes: "[[acme-pricing-2025]]"
superseded_by:
sources: ["[[2026-11-07-acme-call]]"]
tags: [client, retail]
aliases: [Acme, ACME SA]
summary: Retail client since 2026, renewal in Q1, prefers email.
---
```

The `summary` line doubles as the one-line description the index generator copies, so the agent can choose files without opening them.

**File naming.** kebab-case, no spaces, no dates in evergreen notes (`acme-corp.md`), ISO dates first in dated notes (`2026-11-07-acme-call.md`) so they sort chronologically. One concept per file: if a section keeps getting linked on its own, split it out.

**Writing for retrieval.** The agent finds notes by matching words, so:

- Put the answer in the first paragraph ("bottom line up front"); keep detail below.
- Use the literal words people will search for, and list synonyms in `aliases`.
- Use headings as handles (`## Pricing`, `## Decisions`) so the agent can grep for a section and read only it.
- Keep notes under about 300 lines; long notes get partially read.
- Write absolute dates ("2026-11-07"), never "last week" or "recently", which rot immediately.

**Links.** Use `[[wikilinks]]` (Obsidian resolves them, agents grep them). Link entities on first mention. Backlinks then show every note touching a client, and orphan detection becomes a simple script.

**Index format.** One `index.md` per folder, generated rather than hand-written, grouped by type, one line per note:

```markdown
# clients/ index (generated 2026-11-09, 23 notes)
## active
- [[acme-corp]] (updated 2026-11-07, imp 4): Retail client since 2026, renewal in Q1.
- [[borel-sa]] (updated 2026-10-12, imp 3): Pilot ended, decision pending on extension.
## archived
- [[old-client]] (updated 2025-06-01): Contract ended June 2025.
```

**Log format.** Append-only, one consistent prefix so the last entries are one grep away: `## [2026-11-09] ingest | Q4 strategy call | touched: acme-corp, decisions`. Then `grep "^## \[" log.md | tail -5` gives the five latest operations.

**A hot cache.** Some implementations keep a `hot.md` of about 500 words: current priorities, open loops, this week's decisions. It is the only file besides AGENTS.md read every session, and it is rewritten (not appended) at the end of each day, so it never grows ([example stack](https://github.com/ScrapingArt/Karpathy-LLM-Wiki-Stack)).

**raw/ versus wiki/.** Keep original documents (transcripts, PDFs, clipped articles) in raw/, immutable. The agent writes only the compiled layer. You can always re-derive a note from its source, and verify a claim by following `sources:` back to the original.

## 5. Keeping it alive

Most second brains do not fail at setup; they go stale within weeks. Four routines keep yours current.

**Daily: capture and update.** Run a scheduled task that reviews the last 24 hours across your key sources (meeting transcripts first, since that is where decisions are made and nowhere else records them; then CRM, project tool, email, Slack), extracts only what is new or changed, updates the relevant files and appends a short entry to the daily log. The same pass should revise or delete older files the new information makes obsolete. Also capture from your own chats: at the end of a session (or after about 20 minutes of inactivity, or with a /done command), have the agent summarise the conversation into the daily note, update each touched project's about.md and log decisions. Chat history is often kept for a limited time, so extract what matters.

**Weekly or fortnightly: health check (lint).** Run a cleanup skill on a schedule that:

- rebuilds the root map and index files so every folder is on the map and the root stays under 200 lines;
- fixes broken links, merges duplicates, resolves notes that contradict each other, flags orphan files nothing links to;
- flags stale claims superseded by newer sources and concepts mentioned but lacking their own page;
- shortens bloated files, clarifies unclear file names and adds missing labels;
- fixes small issues directly and asks before bigger restructures, ending with a short report.

**Log everything that changes.** Keep an append-only log.md with a consistent prefix per entry, for example `## [2026-11-09] ingest | Q4 strategy call`. It gives the agent a timeline of recent activity and is greppable.

**File good answers back.** A comparison, analysis or synthesis you asked for is valuable; save it as a new page instead of letting it vanish in chat history. Your explorations then compound like ingested sources do.

**Run evals before big changes.** Keep a short list of real tasks the brain must handle well (a weekly report, a diagram, a video edit, a news digest). Re-run them whenever you switch model, change the root map or restructure folders, before you hit problems in real work.

**Version it with git.** Plain files in a git repository give you history, rollback and an off-machine backup for free.

## 5.1 Relevance decay: stopping old facts from winning

Word search has no sense of time: a 2024 price note matches "price" exactly as well as the 2026 one. A second brain needs three layers of decay, from strongest to softest: structural supersession, time-weighted ranking, and review deadlines.

**Layer 1: supersession (deterministic, always on).** When a fact changes, the old version must stop being a candidate at all. Rewrite the note in place and record the change, or set `status: superseded` with `superseded_by:` and move it to archive/. The index generator lists superseded notes under a separate heading and the agent is told to skip them unless asked for history. This alone fixes most "old price" errors and needs no maths.

**Layer 2: time-weighted ranking (for ties among active notes).** The reference design comes from Stanford's Generative Agents paper, which ranks memories by a weighted sum of recency, importance and relevance, each scaled to 0 to 1, with recency as exponential decay (factor 0.995 per hour since last retrieval) ([Park et al. 2023](https://arxiv.org/pdf/2304.03442)). Adapted to markdown notes:

```latex
\text{score} = w_{rel} \cdot \text{relevance} + w_{rec} \cdot 0.5^{\,\text{age}/h_{type}} + w_{imp} \cdot \frac{\text{importance}}{5}
```

- relevance: share of query terms found in title, aliases, summary and headings (title hits count double);
- age: days since `updated` (or since the fact was last confirmed), not since `created`;
- h\_type: half-life for the note's type, the age at which its recency weight halves;
- importance: the 1 to 5 value in frontmatter;
- multiply the whole score by 0 for `superseded`, by 0.3 for `archived`.

Start with equal weights, as the paper did, then raise w\_rel if old but exact matches get buried.

**Half-life by note type.** Category-specific decay matters: a name barely ages, while "currently travelling" is stale in days ([Nakrani on recall scoring](https://alpeshnakrani.com/books/context-windows/reading-memory-recency-relevance-and-policy/)). Suggested starting values:

| Type | Half-life | review\_by after update | Rationale |
| --- | --- | --- | --- |
| context | none (no decay) | 90 days | Canonical; reviewed, never ranked down |
| decision | none | none | Only supersession retires it |
| concept | 365 days | 12 months | Syntheses age slowly |
| entity | 180 days | 6 months | People and companies change gradually |
| source | 365 days | none | Immutable summary of a dated document |
| project | 30 days | 1 month | Status moves weekly |
| daily log | 7 days | none | Useful for "what happened", not for facts |
| inbox | 3 days | 7 days | Must be triaged or it is noise |

**Layer 3: review deadlines (decay of trust, not rank).** `review_by` marks when a note must be re-confirmed. Past that date the note is still retrieved, but the agent must present it as "as of \<updated>" and, where a connector holds the live value (CRM stage, invoice status, price in the billing tool), check it there before relying on it. The weekly lint lists every overdue note so you confirm, edit or archive it in a few minutes.

**Principles that keep decay safe**

- Decay breaks ties; it never hides a precise match. A specific question about a 2023 contract should still find the 2023 note.
- Never decay canonical context or decisions by age. An old authoritative fact may still be the truth; supersede it explicitly instead.
- Reinforce on confirmation, not on reading. Bump `updated` when a fact is re-confirmed or edited; do not rewrite files just because they were opened, which floods git history with noise.
- Consolidate instead of accumulating. Rewrite a note's summary when new information arrives rather than appending a dated paragraph; append-only notes end up with five contradictory versions of the same fact. A periodic merge pass that folds near-duplicate notes together keeps the corpus small.
- Make time explicit in the text. Absolute dates in every status line let both you and the agent judge freshness without metadata.

**Tell the agent in AGENTS.md** (three lines are enough): skip `status: superseded` unless asked for history; when two active notes disagree, prefer the newer `updated` and flag the conflict; when a note is past `review_by`, say so and verify through the connector if one exists.

## 5.2 Technical build: scripts, hooks and schedules

Everything above can be automated with one dependency-free Python script, two Claude Code hooks, a git hook and three scheduled prompts. The agent does the writing; deterministic code does the bookkeeping (indexes, link checks, ranking), because a script never forgets a step.

&#91;embedded content: retrieval and write-back loop · 6 steps\]

The loop closes on itself: what the agent writes in step 5 is re-indexed and re-ranked before the next question, so freshness is maintained by code rather than by memory.

**Step 1: brain.py (index, ranked search, lint).** Save at the brain root. Standard library only; tested on a sample brain where the superseded 2025 price note scored zero and was excluded, and lint caught a broken link and an overdue review.

```python
#!/usr/bin/env python3
"""brain.py - markdown-only second brain helper (stdlib only).
  python3 brain.py index              # rebuild index.md in every folder
  python3 brain.py search "acme price" [-n 5]
  python3 brain.py lint               # report problems, exit 1 if any
"""
import datetime as dt, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKIP = {"raw", "archive", ".git", ".obsidian", ".claude"}
SPECIAL = {"index.md", "AGENTS.md", "CLAUDE.md", "log.md", "hot.md"}
HALF_LIFE = {"project": 30, "entity": 180, "concept": 365, "source": 365,
             "log": 7, "inbox": 3}            # days; types absent = no decay
STATUS_MULT = {"active": 1.0, "draft": 0.8, "archived": 0.3, "superseded": 0.0}
W_REL, W_REC, W_IMP = 1.0, 1.0, 1.0
TODAY = dt.date.today()
LINK = re.compile(r"\[\[([^\]|#]+)")


def parse(path):
    text = path.read_text(encoding="utf-8")
    meta, body = {}, text
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            for line in text[4:end].splitlines():
                if ":" in line and not line.startswith(" "):
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"')
            body = text[end + 4:]
    return meta, body


def date(s):
    try:
        return dt.date.fromisoformat(s[:10])
    except (TypeError, ValueError):
        return None


def notes():
    for p in sorted(ROOT.rglob("*.md")):
        rel = p.relative_to(ROOT)
        if rel.parts[0] in SKIP or p.name in SPECIAL:
            continue
        meta, body = parse(p)
        yield p, meta, body


def score(meta, body, stem, terms):
    head = " ".join([stem.replace("-", " "), meta.get("title", ""),
                     meta.get("aliases", ""), meta.get("summary", "")]).lower()
    text = body.lower()
    hits = sum(2 if t in head else 1 if t in text else 0 for t in terms)
    relevance = hits / (2 * len(terms))
    if relevance == 0:
        return 0.0
    upd = date(meta.get("updated", "")) or TODAY
    hl = HALF_LIFE.get(meta.get("type", ""))
    recency = 1.0 if hl is None else 0.5 ** ((TODAY - upd).days / hl)
    importance = int(meta.get("importance", 3) or 3) / 5
    mult = STATUS_MULT.get(meta.get("status", "active"), 1.0)
    return mult * (W_REL * relevance + W_REC * recency + W_IMP * importance)


def cmd_search(query, n=5):
    terms = [t for t in query.lower().split() if len(t) > 2]
    ranked = sorted(((score(m, b, p.stem, terms), p, m) for p, m, b in notes()),
                    key=lambda x: x[0], reverse=True)
    for s, p, m in [r for r in ranked if r[0] > 0][:n]:
        print(f"{s:.2f}  {p.relative_to(ROOT)}  ({m.get('updated', '?')}) "
              f"{m.get('summary', '')}")


def cmd_index():
    by_dir = {}
    for p, m, _ in notes():
        by_dir.setdefault(p.parent, []).append((p, m))
    for d, items in by_dir.items():
        groups = {}
        for p, m in items:
            groups.setdefault(m.get("status", "active"), []).append((p, m))
        out = [f"# {d.relative_to(ROOT) or 'root'}/ index "
               f"(generated {TODAY}, {len(items)} notes)"]
        for status in ["active", "draft", "archived", "superseded"]:
            rows = sorted(groups.get(status, []),
                          key=lambda x: x[1].get("updated", ""), reverse=True)
            if rows:
                out.append(f"\n## {status}")
                out += [f"- [[{p.stem}]] (updated {m.get('updated', '?')}, "
                        f"imp {m.get('importance', '?')}): {m.get('summary', '')}"
                        for p, m in rows]
        (d / "index.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"indexed {sum(len(v) for v in by_dir.values())} notes "
          f"in {len(by_dir)} folders")


def cmd_lint():
    all_md = {p.stem for p in ROOT.rglob("*.md")}
    linked, problems, titles = set(), [], {}
    for p, m, b in notes():
        rel = p.relative_to(ROOT)
        for field in ("type", "status", "updated", "summary"):
            if not m.get(field):
                problems.append(f"{rel}: missing frontmatter '{field}'")
        targets = set(LINK.findall(b))
        for f in ("supersedes", "superseded_by", "sources"):
            targets |= set(LINK.findall(m.get(f, "")))
        for t in targets:
            linked.add(t.strip())
            if t.strip() not in all_md:
                problems.append(f"{rel}: broken link [[{t.strip()}]]")
        rb = date(m.get("review_by", ""))
        if rb and rb < TODAY and m.get("status", "active") == "active":
            problems.append(f"{rel}: review overdue since {rb}")
        if m.get("status") == "superseded" and not m.get("superseded_by"):
            problems.append(f"{rel}: superseded but no superseded_by")
        if len(b.splitlines()) > 300:
            problems.append(f"{rel}: over 300 lines, consider splitting")
        key = (m.get("title") or p.stem).lower()
        if key in titles:
            problems.append(f"{rel}: duplicate title of {titles[key]}")
        titles[key] = rel
    for p, m, _ in notes():
        if p.stem not in linked and m.get("type") not in ("log", "inbox", "context"):
            problems.append(f"{p.relative_to(ROOT)}: orphan (nothing links here)")
    print("\n".join(problems) or "clean")
    return 1 if problems else 0


if __name__ == "__main__":
    args = sys.argv[1:] or ["lint"]
    if args[0] == "index":
        cmd_index()
    elif args[0] == "search" and len(args) > 1:
        n = int(args[args.index("-n") + 1]) if "-n" in args else 5
        cmd_search(args[1], n)
    else:
        sys.exit(cmd_lint())
```

Limits to know: the frontmatter parser is deliberately flat (one key per line, lists written inline), relevance is substring matching rather than BM25, and archive/ is skipped entirely. When the brain passes a few hundred notes, swap `cmd_search` for a call to a local engine such as qmd and keep the decay multiplier on top.

**Step 2: tell the agent to use it.** Add to AGENTS.md: "To find notes, run `python3 brain.py search \"<terms>\"` before grepping; open the top results only. After creating or renaming notes, run `python3 brain.py index`."

**Step 3: Claude Code hooks** in `.claude/settings.json` at the brain root. The SessionStart hook injects the hot cache and the top lint warnings at startup and after compaction; the PreToolUse hook makes raw/ and archive/ physically read-only for the agent.

```json
{
  "hooks": {
    "SessionStart": [
      { "matcher": "startup|resume|compact",
        "hooks": [{ "type": "command",
          "command": "cat \"$CLAUDE_PROJECT_DIR/hot.md\"; python3 \"$CLAUDE_PROJECT_DIR/brain.py\" lint | head -5" }] }
    ],
    "PreToolUse": [
      { "matcher": "Edit|Write",
        "hooks": [{ "type": "command",
          "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/protect.sh\"" }] }
    ]
  }
}
```

```bash
#!/bin/bash
# .claude/hooks/protect.sh : exit code 2 blocks the tool call and shows stderr to the agent
FILE=$(jq -r '.tool_input.file_path // empty')
case "$FILE" in
  */raw/*|*/archive/*) echo "raw/ and archive/ are read-only. Write to the compiled note instead." >&2; exit 2 ;;
esac
exit 0
```

**Step 4: git as the safety net.** Initialise the brain as a git repository and add a pre-commit hook so indexes can never drift from the files:

```bash
#!/bin/bash
# .git/hooks/pre-commit
python3 brain.py index >/dev/null && git add $(git ls-files -mo --exclude-standard '*index.md')
```

A nightly `git add -A && git commit -m "brain: $(date +%F)"` (or the end-of-day scheduled task) gives you a daily snapshot to diff and roll back.

**Step 5: three scheduled prompts.** Run them as scheduled tasks, or as cloud routines if the brain lives in a synced repository.

```markdown
## Daily capture (07:30)
Read AGENTS.md. Pull the last 24h from: meeting transcripts, calendar, email, CRM.
For each item: run brain.py search for the entities involved, then EXTEND the
matching note (never create a near-duplicate). Record decisions in decisions.md
with date and reason. When a fact changes, rewrite it and mark the old note
status: superseded with superseded_by. Bump `updated`. Run brain.py index.
Rewrite hot.md (max 500 words: priorities, open loops, this week's decisions).
Append one line per touched note to log.md. Report: what changed, what needs me.

## Weekly lint (Friday 16:00)
Run brain.py lint. Fix broken links, missing frontmatter and orphans directly.
For each overdue review: check the live source via connector if one exists,
then confirm (bump updated + review_by) or rewrite. Merge near-duplicates.
List contradictions and anything you would delete; do not delete without asking.
Keep AGENTS.md under 60 lines. Commit. Report a short health summary.

## Monthly consolidation (1st of month)
For each project with no update in 30 days: ask whether to archive.
Re-read context/ files against the last month's decisions; propose edits.
Summarise notes/daily/ of last month into one month note; archive the dailies.
```

**Step 6: a /done skill for live sessions.** Create `.claude/skills/done/SKILL.md` with a description like "End-of-session capture for the second brain" and steps mirroring the daily capture, scoped to the current conversation. Invoke it when you finish a working session, so chat insights land in the brain before the chat is forgotten.

**Step 7: evals.** Keep `evals.md` with five real questions and their expected answers (for example "What is Acme's current monthly price?" expects 1200 EUR, not the 2025 price). Run them after any change to AGENTS.md, the folder structure, brain.py weights or the model.

## 6. Skills and dashboards on top of the brain

Once context is solid, skills turn it into repeatable work and dashboards turn it into decisions.

**Skills: codify, don't re-explain.** If you explain the same process to the agent more than three times, turn it into a skill (for example /edit-video, /create-diagram, /call-prep), then supply only the per-run details. Skills are just markdown instructions, so they are easy to review and tweak daily.

**Point skills at the brain instead of copying references.** Many skills share the same reference files (strategy, brand voice, offer and pricing). Ten skills with ten copies of your strategy doc means ten stale copies after the next change. Have each skill reference the single file in the brain, so one edit updates every skill. Keep the skills themselves in your Claude account or skills folder, not inside the brain: mixing them makes both harder to maintain.

**Dashboards: make the brain visible to you.** Markdown is great for the agent and poor for a human scanning status. Build a page on top of the brain and refresh it with a morning scheduled task. Three useful kinds:

| Dashboard | Shows | Example |
| --- | --- | --- |
| General overview | Today's priorities, this week's decisions, who works on what, upcoming meetings with a quick prep | Personal or founder cockpit |
| Function-specific | The working view of one department | Sales: today's calls already prepped, deal status, follow-ups due |
| Problem-specific | A one-off investigation across notes, projects and decisions | "Why is client onboarding slower this quarter?" |

Favour decision-useful data over impressive graphs: a graph view of connections looks good but rarely changes what you do. To build one, open the brain folder and describe what you want to see; publish it as a Claude artifact (shareable within your Claude team) or host it on a live URL (for example through Vercel) for wider sharing.

## 7. Running in the cloud and rolling out to a team

**Keep it running when your laptop is closed.** Desktop scheduled tasks only run while your computer and the app are on, so the brain stops updating on weekends and trips. Two fixes from the sources:

- Run the same prompts as cloud routines (for example Claude Code routines on Anthropic's servers). The brain must then also be reachable from the cloud, through a connector or a synced copy.
- Host the agent and the brain on a small VPS (about $20 a month on DigitalOcean or Hostinger), synced to your devices, and talk to it from Slack, WhatsApp, Telegram or Discord.

**Share one brain across a team.** Everyone needs the same files and every change must sync. Plain Google Drive, Notion or Obsidian Sync setups tend to create edit conflicts, require a technical owner, or lack permissions. Options: a git repository (versioned, technical), a dedicated sync app that installs the brain locally for each member, or a connector for non-technical members (simpler, but slower than local files, so prefer local where possible).

**Roll out in stages.** Use it alone for a few weeks until the folder structure is proven, then add one teammate, then one department, then the whole company. Launching to everyone on day one produces a mess of inconsistent files.

**Name one owner.** They run the weekly cleanup, approve any change to the folder structure or root map, manage access and fix what breaks. When everyone owns the brain, nobody maintains it.

**Control who can see and edit what.** Set permissions per folder or file: for example, context/ and the root map view-only for everyone so no one's agent rewrites the strategy, finance visible only to founders. Permissions on the files themselves apply whatever AI tool a person uses.

**Build team dashboards.** The owner builds one per department (sales pipeline, marketing performance and customer insights, operations deadlines and decisions) and optionally one per person.

**Turn individual AI into institutional AI.** Agents tend to agree with whoever is talking to them, so a salesperson's agent backs the salesperson and a marketer's backs the marketer. Add one line to the shared root map: "Always act in the best interest of the business based on our goals and strategy. If a request or output conflicts with that, say so clearly instead of just agreeing." Every agent on the team reads it first, so one line aligns them all to the same source of truth.

## 8. Worked example: a sales second brain

One team uses the pattern to run most of its sales process; reps report barely opening the CRM any more. It shows every principle above working together.

**The five layers.** Raw sales tools at the bottom feed an AI filtering layer (scheduled routines), which writes insights into the sales brain. On top, a personalised dashboard tells each rep what to do today, and the AI tool runs skills that read the brain and write their results back.

&#91;embedded content: sales second brain architecture · 5 layers\]

Raw data never enters the brain directly: routines filter it into insights, and everything above reads only the brain.

**Connections.** Their own stack: CRM (Attio), meeting transcription (Fireflies, the first one to add if you have none), proposals (PandaDoc), Google Workspace, calling (Aircall), Slack, Vercel for hosting dashboards. Research and prospecting: a scraper such as Apify for LinkedIn and web data, plus lead databases (Apollo, Sales Navigator) and outreach platforms if you do outbound.

**Folder structure.**

| Folder | Holds |
| --- | --- |
| context/ | ICP, offer, positioning and objections, sales process, tone of voice (build these first) |
| calls/ | Each transcript with a summary and a call score |
| deals/ | One file per lead with its full history: "the CRM for AI" |
| intelligence/ | Monthly and quarterly reports |
| campaigns/ | Each outreach campaign with sequence, metrics and results |
| templates/ | Email templates, NDA, one-pager, pitch deck, proposal |

Each folder has its own index file, and the sales brain can live as a subfolder of a company-wide brain.

**Routines that keep it current.**

| Routine | When | What it does |
| --- | --- | --- |
| Morning routine | Daily | Pulls calendar, emails and yesterday's transcripts; preps today's calls; adds new deals; logs what it did |
| CRM sync | Daily | Checks proposal status, cleans deal fields, freezes won and lost deals, flags cold ones, updates deal files |
| Call scoring | Daily (optional) | Grades recent calls to coach reps |
| Dashboard refresh | Daily | Rebuilds the dashboard from the latest brain data and redeploys it |
| Monthly and quarterly reports | Monthly, quarterly | Summarise pipeline and performance |
| Campaign metrics | Periodic | Track outbound results |

**Skills on top.** Call prep, client one-pager, lead generation, LinkedIn scraping, outreach, pipeline review, follow-up and proposal generation. Some are event-triggered: call prep runs when a meeting is booked; a follow-up email draft and proposal are generated when a meeting ends. Because they read the deal file, proposals reflect the client's real objections rather than generic copy.

**The dashboard.** Tabs for today (calls with prep briefs and qualification scores, top tasks), pipeline and metrics, the core sales documents, the connected tool stack, running automations, plus a monthly report per rep.

## 9. Common mistakes, checklist and sources

**Mistakes to avoid**

| Mistake | Fix |
| --- | --- |
| Copy-pasting complex systems from many videos | Start with one folder, a root map and 5 to 10 core files |
| Waiting weeks to build the "perfect" setup | Do a 30-minute brain dump today; context compounds from day one |
| Dumping raw exports (emails, CRM, spreadsheets) into the brain | Save insights only; reach live data through connectors |
| Duplicating facts across files and skills | One fact, one place; skills reference brain files |
| Constantly reorganising folders | Freeze the structure; change it only through the owner |
| A long root map full of business content | A routing table under 200 lines; detail lives in subfolders |
| Keeping both CLAUDE.md and AGENTS.md with different content | One AGENTS.md, imported from CLAUDE.md with @AGENTS.md |
| One brain per client or project | One brain, subfolders, routed by the map |
| Mixing tool-heavy work (video rushes, editing skills) into the brain | Separate working folders; the brain stays your thinking space |
| No maintenance routine | Daily capture, weekly lint, a log, evals before big changes |
| Automating before trusting | Build, use by hand, then schedule with a report back |
| Fancy graph dashboards | Dashboards that drive a decision today |
| Whole-company launch on day one | Stage the rollout; one owner; permissions per folder |

**Build checklist**

- [ ] One brain folder created and opened in your agent and in Obsidian
- [ ] Brain dump done; 5 to 10 core files written (me, business, ICP, offer, voice, team)
- [ ] Folder structure chosen and frozen
- [ ] AGENTS.md routing table under 200 lines, with the business-first rule; CLAUDE.md imports it
- [ ] index.md in every folder with more than a handful of files
- [ ] decisions.md and log.md started
- [ ] Context audit passed: a fresh session explains your business like a teammate
- [ ] Key connectors added, with write access limited (draft, not send)
- [ ] Connections audit passed: Monday catch-up works
- [ ] First skill built for your most repeated task, referencing brain files
- [ ] Daily capture task scheduled; weekly lint scheduled
- [ ] Eval list of 3 to 5 real tasks saved
- [ ] Brain under git (or another backup)
- [ ] Optional: dashboard, cloud routine or VPS, team rollout with owner and permissions

**Sources**

The four transcripts provided: an 18-tip guide from a second-brain app founder (setup, maintenance, team rollout), a sales operating system walkthrough by the same team, a "4 Cs" fundamentals video building on Nate Herk's framework, and a French-language simplification guide (folder + agent.md + about.md). Web sources consulted:

- [Karpathy, LLM Wiki (gist)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): raw / wiki / schema layers; ingest, query, lint; index.md and log.md
- [AGENTS.md open format](https://agents.md/)
- [Developers Digest: Claude Code now reads AGENTS.md](https://www.developersdigest.tech/blog/claude-code-agents-md-support)
- [travis.media: importing AGENTS.md from CLAUDE.md](https://travis.media/blog/claude-md-import-agents-md)
- [Karpathy's CLAUDE.md, annotated (quotes Anthropic's 200-line guidance)](https://mcp.directory/blog/karpathy-claude-md-annotated-2026)

Added for sections 4.1 to 5.2:

- [Gloaguen et al., Evaluating AGENTS.md (arXiv 2602.11988)](https://arxiv.org/abs/2602.11988) and summaries by [InfoQ](https://infoq.com/news/2026/03/agents-context-file-value-review/) and [Engineer's Codex](https://engineerscodex.com/agents-md-making-ai-worse)
- [Lulla et al. versus Gloaguen et al., compared](https://blog.clawsouls.ai/en/posts/agents-md-hurts-or-helps/)
- [Claude Code memory documentation](https://code.claude.com/docs/en/memory)
- [Daniel Vaughan: the AGENTS.md bloat problem](https://codex.danielvaughan.com/2026/03/27/agents-md-bloat-problem/)
- [Why Claude Code ignores your CLAUDE.md (compaction, hooks)](https://dev.to/naman_here/why-claude-code-ignores-your-claudemd-and-how-to-fix-it-4pk0)
- [Park et al., Generative Agents (recency, importance, relevance)](https://arxiv.org/pdf/2304.03442)
- [Nakrani: recency, relevance and policy in memory recall](https://alpeshnakrani.com/books/context-windows/reading-memory-recency-relevance-and-policy/)
- [Karpathy LLM Wiki stack example (hot.md, log.md)](https://github.com/ScrapingArt/Karpathy-LLM-Wiki-Stack)
