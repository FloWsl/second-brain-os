---
title: Handoff
type: log
status: active
created: 2026-11-20
updated: 2026-11-22
summary: Passation des sessions du 2026-11-20 au 2026-11-22 - modèle produit de la bêta (process de Lancelot amendé par la discussion du 9/11), première piste de stack et flux d'argent Stripe, actions pour Florian, points pour l'équipe, pièges.
---
# HANDOFF — cerveau Doctoresto (2026-11-22)

Branche : `claude/relaxed-thompson-cebfy0` (dépôt FloWsl/second-brain-os). Racine : `doctoresto/`.
Règles : `AGENTS.md`. État de la semaine : `hot.md`. Historique : `log.md`. Décisions : `decisions.md`.

## État
| Étape | Résultat | Statut |
| --- | --- | --- |
| Création du cerveau et import du Drive « DOCTO RESTO » | contexte, projets, personnes, 17 fiches sources, carte du Drive | fait (2026-11-20) |
| Brief projet et PRD de la bêta | `projects/app-beta/brief-prd.md` (brouillon, > 300 lignes) | fait, aligné sur les décisions du 2026-11-21 |
| Modèle produit | process de Lancelot = référence, **amendé par la discussion du 9/11** (notes Granola) sur paiement, reversement, pièces, stock ; forfait de 129 € HT conservé pour déplacement + 1re heure | décidé par Florian le 2026-11-21, **à présenter à l'équipe** |
| Stack technique | `projects/app-beta/stack-technique.md` : Expo + Convex (ou Supabase) + Stripe Connect, client en web app, MVP d'un mois, ~90-100 h pour le périmètre complet | première piste (2026-11-21), pas définitive |
| Flux d'argent | charges et transferts séparés Stripe Connect ; empreinte sur le forfait seulement ; devis débité à sa validation ; relevé mensuel ; coûts, durées et pièges Stripe | documenté (2026-11-21) |
| Notes Granola du 9/11 | `wiki/sources/2026-11-09-notes-granola-reunion.md` | importées (notes.granola.ai autorisé dans l'environnement cloud Default) |
| `context/me.md`, `context/icp.md` | tâches de Florian ; stratégie techniciens du 9/11 | mis à jour le 2026-11-22 (accord de Florian) |
| Tâche planifiée « Veille Doctoresto » | tous les jours à 6h43 (Paris), id `trig_01SnF6fsy2rwdikZS66D94Q5` | **incomplète** : ni dépôt ni connecteur Google Drive |
| Lint | `python3 brain.py lint` | 99/100 (brief-prd > 300 lignes) |

## Modèle produit retenu (2026-11-21)
Empreinte CB à la commande (annulée explicitement si aucun technicien avant le délai) → **forfait de diagnostic de 129 € HT (déplacement + 1re heure) débité à l'arrivée** → devis calculé par la plateforme (heures suivantes au taux horaire + pièce + marge), un seul total, **débité à sa validation** → pièce dans le camion (pose immédiate) ou commandée par le **bureau du technicien**, qui planifie la pose (hors plateforme ; délai fabricant + 1 jour, sinon pièce non payée) → clôture avec photo et validation du client → **relevé mensuel** validé par le technicien → transfert Stripe Connect. Revenu = marge. Détail : `decisions.md`, `context/offer.md`, `brief-prd.md` §2.3.

## À faire pour Florian
1. **Chiffrage final et rétroplanning de dev**, puis envoyer les estimations de coûts à Jess. Questions qui décident : maîtrise de Convex, heures par semaine pour « 1 mois », Sirha comme objectif, client web seul ou app (voir questions de `stack-technique.md`).
2. **Présenter à l'équipe** le modèle produit et la piste de stack (CDC de Jess et prévisionnel à aligner).
3. Stripe : confirmer la gratuité d'une empreinte annulée et l'activation des « charges et transferts séparés » sur le compte.
4. Faire valider par l'expert-comptable la TVA et DAC7 du modèle à marge, et ne pas parler de « séquestre » dans les CGU.
5. **Compléter la tâche planifiée de veille** (dépôt + connecteur Google Drive) ; supprimer l'environnement cloud « second-brain-os » s'il ne sert plus.

## Points à remonter à l'équipe
- Modèle produit du 2026-11-21 (ci-dessus) : remplace le forfait de 110 € avec 45 min du CDC et la commission de 10 % du prévisionnel.
- À fixer ensemble : taux horaire des heures suivantes, tarifs contractuels, règle de marge ; client en cas de retard de pièce ; délai de libération de l'empreinte ; forfait dû si panne non réparable.
- Prévisionnel : CA trimestriel sur un seul mois ; 1 500 clients fin 2027 dans la sheet contre 500 dans les diapos. → `wiki/sources/2026-11-09-previsionnel-financier.md`
- Nom : jugé trop proche de Doctolib le 9/11, top 3-5 à voter (pas de trace du vote).
- Aucun entretien restaurateur documenté ; le questionnaire est prêt.
- Sirha : du 21 au 25 janvier 2027.

## Pièges connus
- Recherche Google Drive incomplète : lister avec `parentId = '<id>'`, un dossier à la fois, avec pagination (méthode dans le skill de veille). Fichiers Keynote illisibles.
- Liens Granola : la page renvoie une erreur 500, mais le texte de la note est dans le code de la page (charge utile Next.js) ; WebFetch ne résout pas l'hôte, `curl` passe par le proxy.
- Ne jamais recopier de données personnelles (adresses du pacte, téléphones, IBAN).
- Les exécutions automatiques n'écrivent pas dans `context/` (hook) : elles proposent les modifications dans leur rapport.

## Non vérifié
- Tâche planifiée de veille jamais exécutée.
- Hooks du cerveau (SessionStart, protect) jamais testés dans une session ouverte sur `doctoresto/`.
- Gratuité d'une empreinte annulée chez Stripe (pas de source écrite).
