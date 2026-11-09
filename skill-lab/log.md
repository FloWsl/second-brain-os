# log.md — decisions, newest first

## 2026-11-09 — 5th creator added
- Nate Herk (5 levels video) added to sources/nate-herk/. Inventory and matrix get one more column.

## 2026-11-09 — Lab created
- Sources collected: Ben AI (benai-skills @4c7a2ec, baalda README @90929b5), Cole Medin (@74f7544).
- Missing: guide.md, brain.py, Karpathy gist, French material, Ben AI ZIP + Sales guide. Transcripts added 2026-11-09.

## Merge decision rules (apply in prompt 3)
1. **Mechanism beats instruction.** If one source enforces something with a script or hook and another asks the agent nicely, keep the script.
2. **Simpler wins ties.** Fewer files loaded per session, fewer folders, fewer dependencies.
3. **Portable over proprietary.** Plain markdown and stdlib scripts over an app, plugin runtime or paid service; the app stays an optional adapter.
4. **Evidence over enthusiasm.** Research or our own eval beats a creator's anecdote.
5. **One owner per capability.** If two skills touch the same files for the same reason, merge them.
6. **Keep the unique good idea.** An idea only one creator has gets a trial in evals before being dropped.
7. **Every rule earns its line.** Anything that does not change a test outcome or prevent a known failure stays out of the root file.
