---
title: Offre et modèle économique
type: context
status: active
created: 2026-11-20
updated: 2026-11-21
review_by: 2027-02-18
importance: 5
sources: ["[[2026-11-02-cahier-des-charges]]", "[[2026-11-09-cr-reunion]]", "[[2026-11-09-previsionnel-financier]]", "[[2026-11-09-process-operationnel]]", "[[2026-11-09-notes-granola-reunion]]"]
summary: Depuis le 2026-11-21 (process de Lancelot amendé par la discussion du 9/11) - empreinte CB à la commande, forfait de diagnostic de 129 € HT (déplacement + 1re heure d'intervention) débité à l'arrivée, heures suivantes au taux horaire, devis calculé par la plateforme et payé à sa validation ; revenu = marge sur un tarif contractuel prestataire ; reversement par relevé mensuel.
---
# Offre et modèle économique
Référence depuis le 2026-11-21 : le process de Lancelot ([[2026-11-09-process-operationnel]]), amendé par la discussion du 9/11 ([[2026-11-09-notes-granola-reunion]]) sur le paiement et les pièces ; décisions dans [[decisions]]. À présenter à l'équipe : le CDC V1 et le prévisionnel disent autre chose (voir History).

## Prix au client
Depuis le 2026-11-21 : discussion du 9/11 ([[2026-11-09-notes-granola-reunion]]), qui prime sur le process de Lancelot sur le paiement.
- **Empreinte CB à la commande**, sans débit ; libérée automatiquement si aucun technicien ne prend la course avant un délai (ex. minuit).
- **Forfait de diagnostic : 129 € HT, couvre le déplacement et la 1re heure d'intervention** (diagnostic et réparation dans l'heure), heure indivisible, **débité à l'arrivée du technicien** (soit 154,80 € TTC avec une TVA à 20 %). (précision de Florian du 2026-11-21 : le montant du process est conservé, le moment du débit vient de la discussion du 9/11)
- **Au-delà de la 1re heure ou avec pièce** : devis calculé par la plateforme (heures suivantes au taux horaire + pièce au prix de la base + marge), **un seul prix total** ; **débité dès la validation du devis par le client**. Le technicien peut lancer le devis avant de quitter le client. Refus : machine remise en l'état (CDC).
- **Pièces** : commandées par le bureau du technicien, qui planifie la pose ; délai fabricant + 1 jour de tolérance, relances automatiques. Ce qui revient au client en cas de retard : à trancher.
- CB, Apple Pay, 3-D Secure. Paiement en 3 fois : gros devis seulement, hors bêta.
- Pas tranché : 1re heure due si la panne n'est pas réparable ; délai de libération de l'empreinte.
- SAV : pas de nouvelle facture si l'erreur vient du prestataire (reprise à sa charge).

## Revenu de la plateforme
- **Marge** : le prestataire travaille à un **tarif contractuel plateforme** connu d'avance ; la plateforme encaisse le client, paie le prestataire et garde la différence. Seuil de marge brute : > 25 % pour continuer, < 15 % en alerte ([[2026-11-09-indicateurs-suivi]]).
- **Reversement par relevé mensuel** (bimensuel en cas d'urgence de trésorerie), validé par le technicien ; pièce posée hors délai non payée au technicien. ([[2026-11-09-notes-granola-reunion]])
- À fixer : taux horaire client des heures suivantes, grille des tarifs contractuels, règle de marge. **Prévisionnel à refaire** sur ce modèle (il compte 10 % de commission sur 350 € HT : [[2026-11-09-previsionnel-financier]]).
- Arguments pour les techniciens : paiement sécurisé, plus d'affaires, interventions proches (moins de circulation à Paris). (CR 9/11)

## Montants en circulation
| Montant | Source |
| --- | --- |
| 80 € (forfait déplacement + 1re heure) | maquette v6, 2026-11-02 (remplacé) |
| 110 € (forfait, 45 min) | CDC V1 et CR du 2026-11-09 (remplacé le 2026-11-21) |
| **129 € HT (forfait de diagnostic : déplacement + 1re heure d'intervention, débité à l'arrivée)** | process de Lancelot (montant) + discussion du 9/11 (débit à l'arrivée) : **référence depuis le 2026-11-21** |
| Taux horaire des heures suivantes | à fixer |
| 240 € de panier et 12 % de commission | doc IA de la feuille de route, 2026-11-15 |

## Repère concurrent
MesDépanneurs.fr : 90 € affichés pour un petit dépannage, 30 % de commission d'après le technicien. Voir [[marche-et-concurrence]].

## History
- Cadrage (2026-10-13) : commission de 20 à 30 %. CR du 19/10 : 10 à 15 %. Prévisionnel : 10 %. Remplacé le 2026-11-21 par une marge.
- Maquette v6 (2026-11-02) : forfait de 80 € (déplacement et 1re heure), remplacé par 110 € au CDC.
- CDC V1 (2026-11-02) et CR du 9/11 : forfait de 110 € (déplacement, diagnostic, 45 min), devis saisi par le technicien, nouveau devis = nouveau paiement. Remplacé le 2026-11-21 par le process de Lancelot.
- Process de Lancelot (référence le 2026-11-21) : forfait de diagnostic de 129 € HT à l'engagement, reste payé à la clôture. Amendé le même jour par la discussion du 9/11 : forfait conservé à 129 € HT mais élargi à la 1re heure d'intervention et débité à l'arrivée ; devis payé à sa validation ; relevé mensuel.
