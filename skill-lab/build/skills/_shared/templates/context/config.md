---
title: Brain config
type: context
status: active
created: {{TODAY}}
updated: {{TODAY}}
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
- queue: inbox            # inbox (notes/inbox.md); airtable adapter later
