---
title: Handoff
type: log
status: active
created: 2026-11-20
updated: 2026-11-20
summary: Passation de la session du 2026-11-20 - état du cerveau, actions pour Florian, points pour l équipe, pièges.
---
# HANDOFF — cerveau Doctoresto (2026-11-20)

Branche : `claude/relaxed-thompson-cebfy0` (dépôt FloWsl/second-brain-os). Racine : `doctoresto/`.
Règles : `AGENTS.md`. État de la semaine : `hot.md`. Historique : `log.md`. Décisions : `decisions.md`.

## État
| Étape | Résultat | Statut |
| --- | --- | --- |
| Création du cerveau | `brain.py init`, contexte, 4 projets, 7 personnes | fait |
| Import du Drive « DOCTO RESTO » | 17 fiches dans `wiki/sources/`, carte dans `wiki/drive-map.md` | fait (parcours récursif complet) |
| Veille | skill `.claude/skills/veille-doctoresto/`, première note `wiki/veille/2026-11-20.md` | fait |
| Tâche planifiée « Veille Doctoresto » | tous les jours à 6h43 (Paris), id `trig_01SnF6fsy2rwdikZS66D94Q5` | **incomplète** : ni dépôt ni connecteur Google Drive |
| Lint | `python3 brain.py lint` | 100/100 |

## À faire pour Florian
1. **Compléter la tâche planifiée** dans claude.ai (tâches planifiées) : ajouter le dépôt `FloWsl/second-brain-os` et le connecteur Google Drive. Sinon, lancer à la main : ouvrir `doctoresto/` et demander « fais la veille ».
2. Supprimer l'environnement cloud « second-brain-os » (créé pour drive.google.com, inutile maintenant que le connecteur est actif).
3. Ta tâche dans le projet : **chiffrer le temps et le coût de la bêta** (à faire depuis le 26/10 ; Jess en a besoin pour le prévisionnel). Point de départ : `projects/app-beta/about.md` et `wiki/sources/2026-11-02-cahier-des-charges.md`.

## Points à remonter à l'équipe
- Prévisionnel : le CA trimestriel ne compte qu'un mois sur trois (CA probablement sous-estimé d'un facteur 3) ; clients fin 2027 : 1 500 dans la sheet, 500 dans les diapos. → `wiki/sources/2026-11-09-previsionnel-financier.md`
- Forfait : 80 € (maquette), 110 € (CDC, la référence), 129 € HT (process de Lancelot).
- Commission et reversement au technicien non votés (10 % dans le prévisionnel).
- Aucun entretien restaurateur documenté ; le questionnaire est prêt.
- Sirha : du 21 au 25 janvier 2027 (et non 21-23).

## Pièges connus
- Recherche Google Drive incomplète : `in ancestors` et les requêtes avec `or` ratent des fichiers. Toujours lister avec `parentId = '<id>'`, un dossier à la fois, en suivant la pagination (méthode écrite dans le skill de veille).
- Les fichiers Keynote (.key) sont illisibles.
- Ne jamais recopier de données personnelles (adresses du pacte, téléphones, IBAN).
- Les exécutions automatiques n'écrivent pas dans `context/` (hook) : elles proposent les modifications dans leur rapport.

## Non vérifié
- Tâche planifiée jamais exécutée.
- Hooks du cerveau (SessionStart, protect) jamais testés dans une session ouverte sur `doctoresto/`.
- Pierre : sorti du projet ? (Réglé le 2026-11-20 : Jessica présidente ; Corinne = « Maman ».)
