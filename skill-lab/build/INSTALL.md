# Install and first run

Skills: brain-setup, brain-capture (/done), brain-daily, brain-lint, brain-ask, brain-evals, plus `_shared/` (contracts, scripts, hooks, templates). Evals: 6/6 on the sandbox (`../evals/results/2026-11-10.md`).

## 1. Install the skills (your computer)
```bash
git clone <this repo> && cd second-brain-os/skill-lab/build && ./install.sh
```
Installs into `~/.claude/skills/` (`--target DIR` for another place, `--force` to replace with a backup). Needs Python 3 and bash; `jq` optional.
Claude Desktop / Cowork: upload each `brain-*` folder **together with** `_shared/` next to it, since every skill reads `../_shared/`.

## 2. Create the brain
1. Make a new empty folder (not your home folder), e.g. `~/brain`, open it in Claude Code.
2. Ask: "Set up my second brain." Do the brain dump (voice is fine) or answer the questions.
3. Accept `git init`. Optionally push to a private repo (backup, needed for cloud routines).
4. Context audit in a new session: "What does my business do and who works there?"

## 3. Daily use
- Work in sessions opened on the brain folder; ask questions normally (brain-ask triggers on questions about your business).
- End a working session with `/done`. Forgot? The SessionEnd hook queues a stub; the daily run handles it.
- Add things by hand any time: `/done` after a quick chat, or "grill me about <topic>" (brain-setup deep mode).

## 4. Schedules
Create two scheduled tasks (Claude desktop scheduled tasks, or cloud routines if the brain is a synced git repo), working directory = the brain folder:
- Daily at `daily_time` (config.md, default 07:30): "Run the brain-daily skill on this brain."
- Weekly at `lint_day lint_time` (default Friday 16:00): "Run the brain-lint skill on this brain."
The skills create `.claude/automated-run` during the run, so the hook keeps `context/` read-only; lint warns if a crashed run left it behind.
Connectors (calendar, email, meeting notes, CRM): add them to Claude, then list them in `context/config.md` `connectors`.

## 5. After any change
Change of AGENTS.md, folders, decay settings, skills or model → run brain-evals ("test my brain"). Add a case to `evals.md` each time the brain gets something important wrong.

## Settings (context/config.md)
times, connectors, budgets, proactivity (advisor = drafts, never sends), capture_confirm, decay_half_life, decay_status_mult, decay_weights, review_days.

## Uninstall
Delete the seven folders from `~/.claude/skills/`. The brain folder is plain markdown and stays usable by any agent.
