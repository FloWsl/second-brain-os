---
name: brain-capture
description: End-of-session capture for the second brain (/done). A sub-agent reads this conversation and queues new or changed facts, decisions with their reason, open loops and a few verbatim lines for brain-daily to integrate. Use when the user says /done, "done", "save this session", "capture this", or accepts the end-of-session offer.
---

# brain-capture (/done)

Shared rules: `../_shared/contracts.md` §6 (queue) and §7 (write discipline). This skill only adds a queue entry; brain-daily is the single writer of notes.
Goal: no load on the main context. The main agent does not summarise or re-read the conversation; a sub-agent does all the work. [Florian's /os-capture]

## Main agent: 4 actions
1. Find the brain root: current folder if it holds `AGENTS.md` and `queue.py`, else `$BRAIN_DIR`, else ask once. None reachable (e.g. a claude.ai chat): the sub-agent writes the entry to a file only and says "not queued".
2. Launch one sub-agent (general-purpose, fast model, foreground) with the SUB-AGENT brief below, filling `<ROOT>`, `<NOW>` (YYYY-MM-DD HH:MM), `<SOURCE>` (conversation tool, or the session transcript path if known), `<OUT>` (scratch folder).
   No sub-agent tool available (e.g. you are already a sub-agent): follow the brief yourself, in the same order.
3. If it answers `READ KO`: write `<OUT>/discussion.md` (user messages verbatim, assistant replies summarised, deliverables and links) and relaunch it with "Source: <OUT>/discussion.md".
4. Send the user the entry file it names, then answer in one line: queued id (or "not queued" + reason), certainty, uncertain points. Never re-run the queueing yourself: a second run creates a duplicate.

If `capture_confirm: true` in `context/config.md`, show the entry and ask "Queue this?" before step 4 instead of after.

## SUB-AGENT brief
```text
You capture the current session for the user's second brain. Now: <NOW>. Brain root: <ROOT>.
1. READ the whole session from <SOURCE>, ignoring the last turn (the /done call).
   If you cannot read it, answer only "READ KO: <reason>" and stop.
2. SKIP if it was casual chat or only produced a deliverable with no new knowledge:
   answer "nothing to capture: <reason>" and stop.
3. EXTRACT, only what is in the session, no invention, absolute dates, numbers with date and source:
   - session: short title (3-8 words).
   - certainty: hypothesis if the core is still exploratory, else fact.
   - entities: clients, people, projects, topics, as existing note names when
     `python3 <ROOT>/brain.py search "<name>"` finds one; separated by "; ".
   - facts: new or changed facts, "; " separated; when a fact changed, say what it replaces.
   - decisions: "what | why: reason" per decision, "; " separated; no reason given -> "why: not stated".
   - open_loops: next actions and open questions, with owner and date when known.
   - verbatim: 1 to 3 exact sentences from the user worth keeping for their voice, or empty.
   No raw emails, transcripts, exports or secrets.
4. CHECK: every field matches the session; no secret or token; dates absolute. Fix directly.
5. QUEUE once from <ROOT>:
   python3 queue.py add --source claude-code --session "..." --certainty fact|hypothesis \
     --entities "..." --facts "..." --decisions "..." --open-loops "..." --verbatim "..."
   Then `python3 queue.py list --status new` and confirm the printed id is there.
   Also write the same entry to <OUT>/<YYYYMMDD-HHMM>-<slug>.md.
6. ANSWER in 3 lines max:
   File: <absolute path>
   Queue: <id> | not queued: <reason>
   Certainty: <fact|hypothesis> | Uncertain: <points or "none">
```
