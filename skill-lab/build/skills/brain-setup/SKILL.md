---
name: brain-setup
description: Create or re-run the second brain in the current folder - interview the user, scaffold the frozen layout, write AGENTS.md and the core context files. Use on an empty folder, when the user asks to set up, onboard or restart their brain, or says "grill me about <topic>" to deepen one subject.
---

# brain-setup

Shared rules: `../_shared/contracts.md` (layout §1, frontmatter §2, write discipline §7). Read it first.

## 0. Check the folder
- `AGENTS.md` present → existing brain. Offer: (a) deepen one topic (go to step 4, grill mode), (b) redo the interview and update context files, (c) stop. Never reset or delete.
- The folder is someone's home directory, or holds unrelated projects → stop and ask for a dedicated folder.
- Otherwise continue.

## 1. Scaffold (script, no judgment)
Run `python3 ../_shared/scripts/brain.py init .` (path relative to this skill; use the absolute path of the skill folder). It creates folders, AGENTS.md, CLAUDE.md (`@AGENTS.md`), hot.md, decisions.md, log.md, evals.md, notes/inbox.md, notes/ideas.md, context/config.md, brain.py, queue.py, hooks and `.claude/settings.json`. It never overwrites. Show the user the tree in a few lines.

## 2. Brain dump
Tell the user, in one message: talk or paste freely for 5-30 minutes (dictation welcome) about who they are, what the business does, customers, offer and prices, goals, voice, team; drop any files, folders or links. No structure needed.
- Read every file and folder they give; fetch every link. Merge everything into one working corpus.
- If they prefer questions: interview mode, **one question at a time**, in this order: role and preferences, business and goal, ideal customer, offer and current prices, voice, team, tools they use daily. Stop when they say so.

## 3. Write the core files from real content only
- `context/me.md`, `business.md`, `icp.md`, `offer.md`, `voice.md`: frontmatter per contracts §2 (`type: context`, `review_by` = today + `review_days.context` from config, `summary` answer-first). Use their exact names, numbers and phrasing; every price carries its date and source.
- A topic with no real content gets no file. Never leave a placeholder or bracketed text.
- One project they mention → `projects/<name>/about.md` (status, goal, decisions, next step). Clients or people they describe → one file each in `clients/` or `people/`.
- Decisions they state with a reason → `decisions.md`. Leftover ideas → `notes/ideas.md`.
- Live data (emails, CRM rows, exports) is not copied: note which tool holds it in `context/config.md` `connectors`.
- `context/config.md` ships with defaults (Europe/Paris, daily 07:30, lint Friday 16:00, advisor). Change a value only if the user gave a different one; otherwise mention the defaults in the report.

## 4. Grill mode (deepen one topic, also on later runs)
Pick one entity or topic. Ask one question at a time and keep going until the user has nothing to add or says stop: facts, history, people involved, decisions and why, open questions. Then extend the existing note (search first, contracts §7), or create one if none exists.

## 5. Tune the root map
Edit AGENTS.md routing lines only where this brain differs (renamed or extra folders, business-specific rules the user stated with a reason). Keep it at 60 lines or fewer. Do not paste business content into it.

## 6. Finish
1. `python3 brain.py index`, then `python3 brain.py lint`; fix what lint reports for files you wrote.
2. Write hot.md (under 500 words): current priorities and open loops from the dump.
3. Append to log.md: `## [date] setup | <summary> | touched: <files>`.
4. If the folder is not a git repository, offer `git init` and a first commit.
5. Report in a short list: files created, topics with no content yet (suggest a grill session), config defaults kept, the final health score, next step (install brain-capture and brain-daily).
6. Context audit: suggest the user opens a fresh session and asks "what does my business do and who works there?"
