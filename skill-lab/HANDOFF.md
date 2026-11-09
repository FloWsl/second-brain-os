# HANDOFF — skill lab (2026-11-09)

Branch: `claude/vigilant-pasteur-flvf9w` (repo FloWsl/second-brain-os). Lab root: `skill-lab/`.
Plan: `PLAYBOOK.md` (6 gated stages). Rules: `AGENTS.md`. Decisions: `log.md`. Reference: `reference/guide.md` + `brain.py` + `protect.sh`.

## Status
- Stage 0 (Collect): DONE except gaps below. Stages 1-6: NOT STARTED. `analysis/`, `build/`, `sandbox-brain/` are empty.

## Sources (see each `sources/<creator>/SOURCE.md`)
| Creator | Have | Missing |
| --- | --- | --- |
| benai | obsidian, baalda-os, other-os (aios, agentic-os, marketing-os), sales plugins @4c7a2ec (MIT); baalda-app README+AGENTS @90929b5; zip-video (= baalda-os, identical) + video-prompts.md; sales/routines-guide.md (7 routines); transcript-18-tips.md; sales/transcript-sales-os.md | — |
| cole-medin | second-brain-starter @74f7544 (no licence: no text reuse); transcript.md | — |
| nate-herk (5th creator, added) | transcript.md (5 levels) | grill-me skill, example project, slides (Free School) |
| french | transcript.md (EN translation) | masterclass + mini-course, mlv.sh/fx (/done, cleanup, skill-manager, interview) |
| karpathy | — | llm-wiki.md (gist host blocked from cloud; download by hand) |

## Findings so far (to verify with path:line in stage 1-2)
- Ben AI optimizers use **10 frameworks** (not "22 passes / 9 frameworks" as playbook says); health score /100 exists.
- baalda-os skills are named setup/operator/optimizer; obsidian os-* variants differ by 3-8 files.
- Ben AI root/skill files are long (os-optimizer 925 lines, os-setup 745) vs guide's 60-line target.
- Nate Herk: pick search level per folder, climb only on pain; keeps duplicate CLAUDE.md/AGENTS.md (conflicts with guide); manual ingestion (conflicts with daily auto-capture).
- Sales routines: reusable patterns for brain-daily (routine boundaries, completion check before task, signal-gated brief, always-log, dependency guard, deploy from temp dir).
- Matrix must have **5 creator columns + guide**.

## Next step
Run Prompt 1 (Inventory) from PLAYBOOK.md, include nate-herk, flag missing items. Stop for review.
