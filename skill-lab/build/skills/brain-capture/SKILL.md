---
name: brain-capture
description: End-of-session capture for the second brain (/done). Summarises what this conversation produced - new or changed facts, decisions with their reason, open loops - into the brain's capture queue for brain-daily to integrate. Use when the user says /done, "done", "save this session", "capture this", or accepts the end-of-session offer.
---

# brain-capture (/done)

Shared rules: `../_shared/contracts.md` §6 (queue format) and §7 (write discipline). This skill **only adds a queue entry**. It never edits brain notes: brain-daily is the single writer, which keeps captures fast and avoids near-duplicates.

## 1. Find the brain
Brain root = the current folder if it holds `AGENTS.md` and `queue.py`; else `$BRAIN_DIR`; else ask the user for the path once. If none is reachable (for example a claude.ai chat), give the user the entry as text to paste later and stop.

## 2. Decide if there is anything to capture
Skip and say so in one line if the session was casual chat, or only produced a deliverable with no new knowledge (a pure action does not log, contracts §5).

## 3. Extract (from this conversation, not from memory of other sessions)
Write each field as short plain lines, absolute dates, numbers with their date and source:
- **entities**: the clients, people, projects, topics touched, as note names when you know them (`acme-corp; pricing`).
- **facts**: what is new or changed, one per `;`. Include what it replaces when a fact changed ("Acme price now 1 200 EUR/month from 2027-01, was 1 000").
- **decisions**: `what | why: reason` per decision. A decision without a stated reason: ask the user for it once; if none, write `why: not stated`.
- **open_loops**: next actions and unanswered questions, with owner and date when known.
- **session**: a short title for this session (plus the session id if you have it).

Insights only: no raw email text, transcripts, exports or secrets. Mark anything uncertain with "(to confirm)".

For a long session, you may hand the conversation summary to a sub-agent to draft the fields, then check its draft against the conversation before queueing.

## 4. Show, confirm, queue
1. Show the user the entry in one compact block and ask "Queue this?" (one round of edits at most).
2. Run from the brain root:
   `python3 queue.py add --source claude-code --session "<title>" --entities "<...>" --facts "<...>" --decisions "<...>" --open-loops "<...>"`
3. Read back with `python3 queue.py list --status new` and confirm the id is there (contracts §7.2).

## 5. Report
One line: queued id, number of facts and decisions, "brain-daily will integrate it on its next run". If something must land in the brain right now (the user asks), tell them to run brain-daily on demand.
