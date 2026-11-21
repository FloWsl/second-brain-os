---
title: Notes Granola de Florian - réunion du 9 novembre 2026 (process, paiement, pièces)
type: source
status: active
created: 2026-11-21
updated: 2026-11-21
review_by: 2026-12-20
importance: 4
summary: Prise de notes Granola de Florian (9/11, 14h51) - techniciens (10 meilleures entreprises d'abord, sectorisation, matching au-delà de la distance, équipe joker), paiement en 2 temps avec reversement par relevé mensuel validé et empreinte CB, pièces commandées par le bureau du technicien (2e passage hors plateforme), coûts de fonctionnement, nom trop proche de Doctolib, actions de Florian. Prime sur le process de Lancelot là où ils se contredisent (décision du 2026-11-21).
---
# Notes Granola de Florian — réunion du 9 novembre 2026
Source : Granola, « Processus de prise de commande, paiement et gestion des pièces détachées », note de Florian créée le 2026-11-09 à 14h51 (résumé généré par Granola à partir de l'enregistrement). Lien : https://notes.granola.ai/d/db493219-a3bd-4ba7-9e1b-e02e6e942daf
Importée le 2026-11-21. Complète le CR officiel du même jour ([[2026-11-09-cr-reunion]]), qui ne couvre pas ces sujets. Le diagramme de Lancelot ([[2026-11-09-process-operationnel]]) est daté du même jour (15h08) ; l'ordre entre les deux n'est pas établi.

✅ **Prime sur le process de Lancelot là où ils se contredisent** (décision de Florian du 2026-11-21, [[decisions]]) : paiement, reversement, pièces, 2e passage, stock. Le process reste la référence pour le reste. À présenter à l'équipe.

## Techniciens (« TECO »)
- Turnover élevé chez les indépendants : les restaurateurs fidèles à leur technicien historique refusent souvent d'en changer.
- Démarrage : cibler d'abord **les 10 meilleures entreprises**, pas les indépendants. Mais les grandes entreprises sont les plus réfractaires.
- **Sectorisation garantie** : un client reste le client du même technicien (pas de concurrence interne).
- Les indépendants restent nécessaires pour absorber les nouveaux contrats.
- **Matching pas seulement sur la distance** : tenir compte des clients préférentiels (historique de collaboration, autres critères à définir).
- Les mauvaises notes ne sont pas toujours représentatives (machine irréparable, friction humaine sans faute technique).
- Prévoir une **« équipe joker »** quand un technicien fait défaut.

## Flux de paiement
- Deux paiements distincts :
  - 1er : **la première heure, débitée dès l'entrée du technicien chez le client** (heure indivisible) ;
  - 2e : si un devis de pièce est soumis, **débité dès sa validation par le client**.
- **Reversement aux techniciens par relevé mensuel** (ou bimensuel en cas d'urgence de trésorerie) : le technicien valide son relevé, signale les erreurs, puis reçoit son CA. « Modèle type Vinted » : l'argent est bloqué jusqu'à la fin de la prestation.
- **Empreinte bancaire** si aucun technicien ne prend la course : pas de débit, libération automatique passé un délai (ex. minuit). Durée maximale des empreintes CB à vérifier.
- Litiges à prévoir : technicien absent après commande de pièce, remboursements client.

## Pièces détachées et 2e intervention
- **Le technicien commande la pièce via son bureau** (pas lui directement), qui intègre la pose dans sa tournée. La 2e intervention sort du périmètre de la plateforme jusqu'à l'arrivée chez le client : **pas de planning géré par la plateforme**, mais visibilité maintenue.
- Délais de pose : base de pièces avec prix publics et délais estimés par le fabricant ; délai fabricant + 1 jour de tolérance, puis relances automatiques (J+24 h, J+48 h…). **Délai non respecté : la pièce n'est pas payée au technicien.**
- Clôture de la 2e intervention : photo obligatoire + validation du client dans l'appli.

## Coûts de fonctionnement
- Paiement : ~2 % par transaction (entrant + sortant) ; 3 noms de domaine ; comptes développeur Apple et Google ; outils de dev et API (cartographie).
- Google Maps : 10 000 requêtes gratuites par mois depuis mars 2025 (itinéraire, géocodage, carte web), alternatives au-delà. Voir [[2026-11-09-cout-geolocalisation]].
- Prévisionnel en consolidation (2e onglet du fichier existant). Voir [[2026-11-09-previsionnel-financier]].

## Nom et pacte
- Nom actuel jugé trop proche de Doctolib (Doctolib défend activement le préfixe, précédents INPI). Piste : nom qui évoque l'urgence, mémorable, exportable. Idées : « Zéro Galère », « Coup de Feu », « Lève-Rideau », « Flash », « Express », « Rapid Doc », noms anglais ou français (le « made in France » marche en gastronomie). **Top 3-5 à voter la semaine suivante** (pas de trace du vote au 2026-11-21). Voir [[2026-11-09-recap-nom-inpi]].
- Pacte : clauses à préciser (entrée d'un nouvel associé, good/bad leaver, formulations vagues). Le pacte a été signé depuis (PDF du 2026-11-13, [[2026-11-02-pacte-associes]]).

## Actions notées
| Action | Qui | Statut au 2026-11-21 |
| --- | --- | --- |
| Envoyer le récap des modifications du pacte (good/bad leaver, entrée d'un associé) | Florian | probablement caduc (pacte signé le 13/11) |
| Vérifier les coûts du paiement et la durée maximale des empreintes CB ; affiner le prévisionnel mensuel | Florian | coûts et durées faits le 2026-11-21 ([[stack-technique]]) ; prévisionnel mensuel à faire (rejoint le chiffrage, [[stack-technique]]) |
| Proposer un rétroplanning de développement (version minimale, cible avril) | Florian | à faire (première estimation dans [[stack-technique]]) |
| Top 3-5 de noms pour vote | tous | pas de trace |
| Confirmer le rendez-vous du vendredi 13 novembre | — | passé |

## Écarts avec le process de Lancelot (tranchés le 2026-11-21 en faveur de cette discussion)
Précisions de Florian le 2026-11-21 : la 1re heure est couverte par le **forfait de diagnostic de 129 € HT du process, conservé** (déplacement + 1re heure d'intervention), débité à l'arrivée ; heures suivantes au taux horaire et pièce via le devis ; **prix calculé par la plateforme, revenu = marge** (process) ; le technicien déclare « camion » ou « à commander par son bureau » et **peut lancer le devis avant de quitter le client**.

| Sujet | Retenu (9/11) | Écarté (process) |
| --- | --- | --- |
| 1er paiement | 1re heure débitée à l'arrivée du technicien ; empreinte CB avant | Forfait de diagnostic payé ou préautorisé à l'engagement |
| 2e paiement | À la validation du devis de pièce | Reste payé à la clôture, après validation de la remise en service |
| Reversement | Relevé mensuel validé par le technicien | Après clôture (rythme non précisé) |
| Commande de pièce | Par le bureau du technicien | Par la plateforme (prix, livraison, délai tracés) |
| 2e passage | Hors plateforme, pas de planning | Programmé par la plateforme |
| Stock | Non évoqué | Réservé par mission |
| Dispatch | Sectorisation, clients préférentiels | Zone × dispo × métier × marque × historique (compatible, conservé) |
→ [[app-beta]], [[brief-prd]], [[stack-technique]]
