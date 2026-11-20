---
title: Brain config
type: context
status: active
created: 2026-11-20
updated: 2026-11-20
review_by: 2027-02-18
summary: Settings every brain routine reads. Change values here, never in skills.
---
# Config
- timezone: Europe/Paris
- daily_time: "07:30"
- lint_day: friday
- lint_time: "16:00"
- connectors: [google-drive]   # Drive "DOCTO RESTO" ; groupe WhatsApp de l'équipe non connecté
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
## Veille (lu par .claude/skills/veille-doctoresto)
- veille_time: "07:00"
- drive_folder_id: 11_hvdzAeXYDdBmMBmcilxuZyMmzlmKRg   # DOCTO RESTO
- drive_extra_files: [10rWZKAzG9QXkowdNC3U7L_KlhLaHeb4CWfV6Qf1nYI8]   # doc "Doctoresto" (cadrage), hors du dossier
- git_branch: claude/relaxed-thompson-cebfy0
- veille_max_searches: 12
- veille_topics:
  - concurrents: MesDépanneurs.fr, Yoojo, AlloVoisins, Praxedo, Synchroteam, InterFast, Infraspeak (prix, commissions, levées, nouveautés)
  - depannage-chr: dépannage matériel cuisine professionnelle et fournil, Paris et Île-de-France, nouvelles plateformes
  - pieces: Horecatiger et distributeurs de pièces détachées CHR, SAV Bongard, Pavailler, Panimatic, VMI
  - sirha: Sirha Lyon 2027 (dates, exposants fabricants, inscriptions)
  - reglementation: plateformes de mise en relation (DAC7, CGU, Stripe Connect), fluides frigorigènes, RC pro des artisans
  - marche: boulangeries et restaurants en Île-de-France (défaillances, ouvertures, chiffres du secteur)
  - tech: logiciels FSM, diagnostic de panne par IA, applis d'intervention hors-ligne
