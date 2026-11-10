---
title: Brain config
type: context
status: active
created: 2026-11-10
updated: 2026-11-10
summary: Settings every brain routine reads. Change values here, never in skills.
---
# Config
- timezone: Europe/Paris
- daily_time: "07:30"
- lint_day: friday
- lint_time: "16:00"
- connectors: []          # e.g. [calendar, gmail, fireflies, crm]
- budget_reads: 60
- budget_writes: 25
- budget_fixes: 15
- proactivity: advisor    # observer | advisor (drafts, never sends) | assistant | partner
- capture_confirm: false  # true = /done shows the entry before queueing
- queue: inbox            # inbox (notes/inbox.md); airtable adapter later
## Decay (read by brain.py; days; 0 = no decay)
- decay_half_life: project=30, entity=180, concept=365, source=365, log=7, inbox=3, context=0, decision=0
- decay_status_mult: active=1, draft=0.8, archived=0.3, superseded=0
- decay_weights: relevance=1, recency=1, importance=1   # raise relevance if old exact matches get buried
- review_days: context=90, concept=365, entity=180, project=30, inbox=7   # review_by = updated + this; read by skills
