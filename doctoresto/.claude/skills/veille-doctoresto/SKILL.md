---
name: veille-doctoresto
description: Veille quotidienne Doctoresto. Synchronise le Drive "DOCTO RESTO" (nouveaux docs et docs modifiés) dans le cerveau, puis fait une veille web (concurrents, dépannage CHR, fournisseurs de pièces, Sirha, réglementation des plateformes, outils) et écrit wiki/veille/AAAA-MM-JJ.md. À utiliser chaque matin (tâche planifiée) ou quand on demande "fais la veille", "synchronise le drive", "quoi de neuf pour Doctoresto".
---

# Veille quotidienne Doctoresto

Racine du cerveau : le dossier `doctoresto/` (celui qui contient ce `.claude/`). Lire d'abord `AGENTS.md`, `hot.md`, `context/config.md` (section Veille).
Règles du cerveau : `AGENTS.md`. Formats : `skill-lab/build/skills/_shared/contracts.md` si présent dans le dépôt.
Exécution sans surveillance : aucune question ; tout ce qui demande Florian va dans le rapport.
Exécution automatique : `touch .claude/automated-run` en premier, `rm -f .claude/automated-run` à la fin, même en cas d'échec. Pas d'écriture dans `context/` : proposer les modifications dans le rapport.

## 1. Synchronisation du Drive (connecteur Google Drive)
1. Dossier racine : `drive_folder_id` dans config.md. **Parcours récursif obligatoire** : `search_files` avec `parentId = '<id>'` (une requête par dossier, sans `or` : les requêtes combinées et `in ancestors` renvoient des résultats incomplets), suivre chaque `nextPageToken` jusqu'à une réponse vide, puis recommencer sur chaque sous-dossier trouvé. La liste des dossiers connus est dans `wiki/drive-map.md` : la mettre à jour si un dossier apparaît. Ajouter les fichiers listés dans `drive_extra_files`.
2. Date de dernière synchro : la dernière ligne `veille` de `log.md` (sinon 2026-11-20). Garder les fichiers créés ou modifiés depuis (`modifiedTime`), et ceux dont l'id n'apparaît dans aucune note de `wiki/sources/` (champ `drive_id`).
3. Pour chacun : `read_file_content` (Doc, Sheet, PDF, docx, pptx, xlsx ; commentaires inclus), `download_file_content` pour les images. Fichier trop gros : le lire par tranches avec python. Keynote (.key) : illisible, le noter. Ne jamais recopier de données personnelles (adresses, téléphones, IBAN) dans le cerveau.
   - Pas encore de fiche → créer `wiki/sources/<date du doc>-<slug>.md` (type source, `drive_id`, résumé, liens vers les notes concernées).
   - Fiche existante → la mettre à jour (statuts d'actions, votes, nouveaux points).
4. Intégrer les faits durables dans les notes existantes (search d'abord : `python3 brain.py search "..."`) : projets, personnes, décisions (`decisions.md` avec `Why:`), questions ouvertes. Un fait qui change : on le réécrit, et l'ancien passe sous `## History`. Ce qui touche `context/` va dans le rapport.
5. Ne jamais modifier ni supprimer de fichier sur le Drive (lecture seule).

## 2. Veille web
Sujets et requêtes : section Veille de `context/config.md`. Pour chaque sujet, 1 ou 2 recherches web (WebSearch, mode standard), uniquement des résultats des 7 derniers jours (sinon rien). Budget : `veille_max_searches`.
Garder seulement ce qui peut changer une décision de l'équipe : nouveau concurrent ou changement de prix ou de commission, levée de fonds d'une plateforme de dépannage, réglementation (plateformes, DAC7, habilitations fluides frigorigènes, RC pro), fournisseurs de pièces, dates et inscriptions du Sirha, faillites ou ouvertures de boulangeries et restaurants en Île-de-France, outils (FSM, diagnostic IA). Ignorer le reste.

## 3. Écrire la note du jour
`wiki/veille/<AAAA-MM-JJ>.md`, frontmatter `type: log`, `status: active`, `created`/`updated` = aujourd'hui, `summary` = l'info la plus utile en une ligne. Sections (omettre les vides) :
- `## Drive` : documents nouveaux ou modifiés → notes touchées.
- `## À retenir` : 3 à 7 puces au maximum : fait, pourquoi ça compte pour Doctoresto, lien source (URL) et date.
- `## À creuser` : questions ou actions proposées (rattacher au projet concerné).
Rien de neuf → ne pas créer de note ; une ligne dans log.md suffit.
Faits durables (concurrent, prix, fournisseur) : les ajouter aussi dans `wiki/marche-et-concurrence.md` sous `## Signaux de veille` (`- AAAA-MM-JJ : fait (source)`).

## 4. Clôture
1. `python3 brain.py index`, puis `python3 brain.py lint` ; corriger ce qui concerne les fichiers touchés.
2. Réécrire `hot.md` (500 mots max) si quelque chose a changé.
3. Ajouter à `log.md` : `## [AAAA-MM-JJ] veille | drive: <n> docs, web: <m> signaux | touched: <notes>`.
4. Git : `git add -A && git commit -m "doctoresto: veille <date>"` puis push sur la branche de travail (voir config.md `git_branch`).
5. Rapport court : ce qui a changé, signaux importants, ce qui demande Florian, modifications de contexte proposées.
