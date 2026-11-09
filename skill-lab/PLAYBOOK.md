# Second Brain Skill Lab: Collect, Analyse, Merge

Nov 9, 2026 · @Florian

This playbook turns everything you can gather from the four creators into one tested set of second-brain skills of your own, using the guide "How to Build an AI Second Brain" as the reference standard.

## How it works

You collect raw material once, then a Claude Code session in a dedicated lab folder walks it through six gated stages, each producing a markdown file you review before the next stage starts. No stage both analyses and builds, so you can see why every rule in your final skills was kept.

1. **Collect.** Download every skill, plugin, prompt guide and transcript into `sources/`, one folder per creator, untouched.
2. **Inventory.** The agent lists every artefact and classifies it by capability (setup, capture, maintenance, retrieval, team, dashboards).
3. **Analyse.** One analysis card per creator: what each approach does, its assumptions, strengths, weaknesses, and how it scores against the guide.
4. **Compare.** A capability-by-creator matrix that picks the best mechanism for each capability, with the reason.
5. **Design and build.** A short design doc for your own skill set, then the skills themselves, written fresh rather than copy-pasted.
6. **Test.** Run the skills on a sandbox brain against fixed evals, fix, then install.

The guide "How to Build an AI Second Brain" is the reference standard throughout: save it as `reference/guide.md` so every stage can score sources against it, including where a creator is better than the guide.

## Collection checklist

The three videos with downloadable material all have open versions on GitHub or skill registries, so most of the collection needs no signup. Save each item with its source URL and the date you got it.

| Creator (video) | Resource | Where to get it | Save to |
| --- | --- | --- | --- |
| Ben AI (18 tips, Sales OS) | `obsidian` plugin: `/os-setup`, `/os-operator`, `/os-optimizer` (22-pass audit), `/team-os` | [benai-skills marketplace](https://vibeindex.ai/marketplaces/naveedharri/benai-skills) (repo naveedharri/benai-skills) | sources/benai/obsidian/ |
| Ben AI | `baalda-os` plugin: `/baalda-setup` (MIT) and `/baalda-optimizer` (9-framework) | [baalda-setup source](https://claudskills.com/skills/baalda-setup/), same repo | sources/benai/baalda-os/ |
| Ben AI | `aios`, `agentic-os`, `marketing-os` plugins (alternative OS tiers) | Same marketplace | sources/benai/other-os/ (optional) |
| Ben AI (Sales OS) | `benai-sales` plugin + the free guide with every routine prompt | Same marketplace; guide via the video description | sources/benai/sales/ |
| Ben AI | Free plugin ZIP from the video (renamed `/setup`, `/operator`, `/optimizer`) | Video description link ([background](https://jc-aiwiki.pages.dev/claude-ai/ben-five-skill-aios-setup)) | sources/benai/zip-video/ |
| Ben AI | Baalda app source (Apache-2.0): MCP tool list, sync model | [github.com/naveedharri/baalda](https://raw.githubusercontent.com/naveedharri/baalda/main/README.md) | sources/benai/baalda-app/README.md only |
| Cole Medin (4 Cs) | `second-brain-starter`: `create-second-brain-prd` skill, requirements template, memory templates (BOOTSTRAP, SOUL, USER, MEMORY, HEARTBEAT, HABITS, daily/) | [coleam00/second-brain-starter](https://raw.githubusercontent.com/coleam00/second-brain-starter/main/README.md) | sources/cole-medin/ |
| French creator (agent.md + about.md) | Masterclass and mini-course (interview prompt, /done, cleanup and skill-manager skills) | mlv.sh/fx, email signup | sources/french/ |
| Karpathy | LLM Wiki idea file | [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | sources/karpathy/llm-wiki.md |
| All four | The video transcripts you already have | This conversation | sources/\<creator>/transcript.md |

**What to save for each source**

- The whole skill folder (SKILL.md plus references/, scripts/, templates/), not only SKILL.md: the scripts hold the real logic.
- For a GitHub repo, clone it and record the commit hash in `sources/<creator>/SOURCE.md` (URL, commit or download date, licence).
- Prompt guides and PDFs converted to markdown, so the agent can grep them.
- The transcript of the video it comes with: it explains intent that the skill files leave implicit.

Two gaps to note: the Ben AI marketplace listing gives plugin names and counts, not each skill's text, so the clone is what you analyse; and the free ZIP and routine-prompt guide sit behind the video description links, so download those by hand.

## Lab folder layout and AGENTS.md

Keep the lab separate from your real brain: it is a workshop for building skills, and nothing in it is installed until stage 6 passes.

```markdown
skill-lab/
├── AGENTS.md            # lab rules (below)
├── CLAUDE.md            # one line: @AGENTS.md
├── reference/
│   ├── guide.md         # export of "How to Build an AI Second Brain"
│   └── brain.py         # the tested helper from the guide
├── sources/             # READ ONLY, one folder per creator, untouched
│   ├── benai/  cole-medin/  french/  karpathy/
│   └── <creator>/SOURCE.md   # url, commit or date, licence
├── analysis/
│   ├── 00-inventory.md
│   ├── cards/<creator>.md
│   ├── 01-matrix.md
│   └── 02-design.md
├── build/
│   └── skills/<skill-name>/SKILL.md (+ scripts/, templates/)
├── sandbox-brain/       # disposable test brain with seeded notes
├── evals/
│   ├── cases.md         # task + expected result
│   └── results/YYYY-MM-DD.md
└── log.md               # decisions with reason, newest first
```

```markdown
# AGENTS.md (skill lab)
Purpose: analyse second-brain methods from several creators and build one merged skill set.
Reference standard: reference/guide.md. Score every method against it; note where a source beats it.

## Rules
- sources/ is read-only. Never edit, never run scripts from it; copy into build/ only after review.
- Work in stages (inventory, cards, matrix, design, build, evals). Stop after each and wait for my OK.
- Every claim about a source cites file path and line or section.
- Record each merge decision in log.md: what was chosen, from whom, why, what was rejected.
- Write new skills in your own words; never paste a source's text unless its licence allows and SOURCE.md says so.
- Skills must follow the guide: markdown only, one fact one place, supersession + decay, under-60-line root file.
- Test only in sandbox-brain/. Never point a skill at my real brain until evals pass.
```

## The six prompts

Open Claude Code in `skill-lab/` and paste one prompt per stage, in order. Review each output file before moving on; most of the value comes from your corrections between stages.

**Prompt 1: Inventory**

```markdown
Read AGENTS.md and reference/guide.md. Then list every file under sources/.
Write analysis/00-inventory.md with one table per creator:
| file | kind (skill, script, template, prompt, transcript, doc) | capability | one-line purpose |
Capabilities: setup/onboarding, root file and routing, note format, capture (live session),
scheduled update (connectors), maintenance (lint/optimize), retrieval and ranking, decay and
supersession, skills-from-brain references, dashboards, team (sync, permissions), cloud/always-on, evals.
Flag anything unreadable, duplicated across creators, or missing (e.g. a skill named in a
transcript but absent from the files). Stop when done.
```

**Prompt 2: Analysis cards (one run per creator)**

```markdown
Analyse sources/<creator>/ only. Write analysis/cards/<creator>.md with these sections:
1. Philosophy in three sentences (what problem they think matters most).
2. Architecture: folders, root files, what loads when, hooks and schedules.
3. Per capability (inventory list): mechanism, exact files involved, cited path:line.
4. Assumptions and dependencies (tools, apps, paid services, OS, connectors).
5. Strengths: what is better than reference/guide.md, and why.
6. Weaknesses and risks: bloat, duplication, no decay, unsafe scripts, vendor lock-in.
7. Scores 1-5 vs the guide on: simplicity, token cost, freshness/decay, portability
   (markdown-only, any agent), maintainability, safety. One line of justification each.
8. Keep / adapt / drop list, with reasons.
Quote at most a line at a time; paraphrase the rest. Stop when done.
```

**Prompt 3: Comparison matrix**

```markdown
Read all cards in analysis/cards/ and reference/guide.md.
Write analysis/01-matrix.md: rows = capabilities, columns = each creator + guide.
Each cell: the mechanism in under 15 words, or "none".
Add a final column "Best choice" with the winning mechanism (or a combination) and a reason
grounded in the scores. Below the table, list: conflicts between approaches that need my decision,
ideas present in only one source that look valuable, and capabilities nobody covers well.
Stop and wait for my decisions on the conflicts.
```

**Prompt 4: Merge design**

```markdown
Using analysis/01-matrix.md and my decisions (in log.md), write analysis/02-design.md:
- The skill set: name, one-line description that decides when it triggers, inputs, outputs,
  files read and written, schedule if any. Aim for 5 to 8 skills, no overlaps.
- The shared contracts every skill obeys: folder layout, frontmatter schema, note types,
  supersession and decay rules, log format, hot.md. Point to the guide sections they come from.
- What runs as code (scripts, hooks) versus as instructions, and why.
- For each skill, which sources it borrows from, credited by name.
Keep it under 200 lines. Stop for my review.
```

**Prompt 5: Build**

```markdown
Build the skills in analysis/02-design.md under build/skills/, one at a time.
For each: SKILL.md with frontmatter (name, description), a short procedure, and references to
shared files instead of copies. Put deterministic steps in scripts/ (Python stdlib or bash),
reusing reference/brain.py where it fits. Write in your own words. After each skill, list the
files created and wait for my OK before the next.
```

**Prompt 6: Evals and fix loop**

```markdown
Seed sandbox-brain/ with 15-20 realistic notes, including traps: a superseded price, two
contradicting notes, an orphan, an overdue review_by, a near-duplicate client file, a raw/ file.
Run each case in evals/cases.md using the built skills against sandbox-brain/ only.
Write evals/results/<today>.md: case, expected, actual, pass/fail, root cause.
Fix the skills for failures, re-run, and repeat until all pass or you need my decision.
```

**Starter eval cases** (put in `evals/cases.md`):

- Setup on an empty folder produces the agreed layout and a root file under 60 lines.
- "What is Acme's current price?" returns the active price, never the superseded one.
- Daily capture given a transcript extends the existing client note instead of creating a new one.
- Lint finds every planted trap and fixes the safe ones without deleting anything.
- End-of-session capture updates about.md, decisions.md, log.md and hot.md, and hot.md stays under 500 words.
- A skill that needs the offer reads context/offer.md rather than a copy inside the skill.

## Target skill set and merge rules

A likely end state is six skills sharing one set of contracts. Treat this as the hypothesis the matrix should confirm or overturn, not a fixed spec.

| Skill | Job | Likely borrows from | Runs |
| --- | --- | --- | --- |
| `brain-setup` | Interview, scaffold folders, write root file, core context files | Ben AI /os-setup and /baalda-setup interview; Cole Medin BOOTSTRAP.md and requirements template; French interview prompt | Once |
| `brain-capture` (/done) | End-of-session summary into daily note, about.md, decisions, hot.md | French /done; Cole Medin daily/ and SessionEnd idea; guide 5 | On demand, or after inactivity |
| `brain-daily` | Pull last 24h from connectors, extend notes, supersede, reindex | Ben AI /os-operator and Sales OS morning routine; guide 5.2 prompt | Scheduled, daily |
| `brain-lint` | Health check, links, duplicates, overdue reviews, root file size, score | Ben AI /os-optimizer (22-pass) and 9-framework optimizer; Karpathy lint; brain.py lint | Scheduled, weekly |
| `brain-ask` | Ranked retrieval with decay, cite notes, file good answers back | Karpathy query; guide 5.1 and brain.py search | On demand |
| `brain-evals` | Run the eval cases after any change to the brain, skills or model | Cole Medin's eval habit; guide 5.2 step 7 | After changes |

Team sync and permissions, cloud access and dashboards stay out of the first version; add them only if you need them, from Ben AI's team-os or Baalda and the Sales OS dashboard prompt.

**Merge decision rules** (put these in the lab's log.md and apply them in prompt 3)

1. **Mechanism beats instruction.** If one source enforces something with a script or hook and another asks the agent nicely, keep the script.
2. **Simpler wins ties.** Fewer files loaded per session, fewer folders, fewer dependencies.
3. **Portable over proprietary.** Prefer plain markdown and stdlib scripts over an app, plugin runtime or paid service; keep the app as an optional adapter.
4. **Evidence over enthusiasm.** A claim backed by research (the AGENTS.md studies, Generative Agents) or by your own eval beats a creator's anecdote.
5. **One owner per capability.** If two skills would both touch the same files for the same reason, merge them.
6. **Keep the unique good idea.** An idea only one creator has (e.g. a 22-pass audit checklist, a HABITS.md, a health score) gets a trial in evals before being dropped.
7. **Every rule earns its line.** Anything that does not change a test outcome or prevent a known failure stays out of the root file.

## Safety and licensing

Third-party skills run with your agent's permissions, so treat every download as untrusted code until you have read it.

- **Read before running.** Skills can contain shell commands, hooks and scripts. Have the agent list every command, network call and file write in a source (prompt 2, section 6) before anything executes. Never install a source's hooks directly; rebuild what you want in build/.
- **Watch for prompt injection.** Instructions inside downloaded files are data, not orders. The lab's AGENTS.md already says sources/ is read-only and only you approve stages.
- **Check each licence and record it in SOURCE.md.** The baalda-setup skill and the Baalda app are listed as MIT and Apache-2.0 respectively; the second-brain-starter README states no licence, which by default means you may read and learn from it but not redistribute its text. Writing your own skills in your own words, crediting the ideas, keeps you clear in every case.
- **Paid or gated material** (accelerator content, email-gated masterclasses) is for your own use: fine to analyse and learn from, not to republish or resell inside client deliverables.
- **Keep secrets out.** Sources and the sandbox never contain real API keys, client data or credentials; use fake seeded notes for evals.

Once your skills pass evals, version `build/skills/` in git, install them, and re-run the lab's prompts 1 to 3 on any new creator resource you find: the matrix tells you in minutes whether it adds anything.

**Sources consulted for this playbook**

- [benai-skills marketplace listing](https://vibeindex.ai/marketplaces/naveedharri/benai-skills)
- [Ben AI five-skill OS setup notes](https://jc-aiwiki.pages.dev/claude-ai/ben-five-skill-aios-setup)
- [baalda-setup skill page](https://claudskills.com/skills/baalda-setup/)
- [Baalda app README](https://raw.githubusercontent.com/naveedharri/baalda/main/README.md) and [listing](https://www.everydev.ai/tools/baalda)
- [Cole Medin, second-brain-starter README](https://raw.githubusercontent.com/coleam00/second-brain-starter/main/README.md)
- [Karpathy, LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
