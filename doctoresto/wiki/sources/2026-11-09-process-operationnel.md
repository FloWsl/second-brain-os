---
title: Process opérationnel de dépannage (Lancelot)
type: source
status: active
created: 2026-11-20
updated: 2026-11-21
review_by: 2027-11-21
importance: 5
drive_id: 1h4ZxjpqM5aaUylPIRpkfrETaPQjiAbik
summary: Diagramme en couloirs (restaurant, plateforme, prestataire) en 7 étapes, document le plus structurant pour le dev - la plateforme qualifie, choisit le prestataire et calcule le prix client ; le prestataire porte le diagnostic, la référence et la garantie ; stock du prestataire réservé par mission ; encaissement puis reversement ; marge à la plateforme. Analyse détaillée et écarts avec le CDC.
---
# Process opérationnel de dépannage (Lancelot)
Source : Google Drive, DEVELOPPEMENT/CAHIER DES CHARGES/« Synhtèse process »/**261109 Process.pdf** (1 page A2, diagramme en couloirs, auteur Lancelot, modifié le 2026-11-09 à 15h08). Lien : https://drive.google.com/open?id=1h4ZxjpqM5aaUylPIRpkfrETaPQjiAbik
Importée le 2026-11-20 ; **analysée en détail le 2026-11-21** (rendu de l'image + texte). **Document de référence pour le produit depuis le 2026-11-21** (décision de Florian, à présenter à l'équipe) : il prime sur le CDC V1 sur les 6 points ci-dessous. [[decisions]]
> ⚠️ **Amendé le 2026-11-21** : la discussion du 9/11 ([[2026-11-09-notes-granola-reunion]]) prime sur ce process là où ils se contredisent : empreinte CB puis 1re heure débitée à l'arrivée (au lieu du forfait de diagnostic de 129 € HT à l'engagement), devis payé à sa validation (au lieu de la clôture), pièces commandées par le bureau du prestataire et 2e passage hors plateforme (au lieu de la commande, du stock réservé et du planning par la plateforme), reversement par relevé mensuel.

Titre : « Process opérationnel de dépannage CHR ». Sous-titre (le principe) : **responsabilité commerciale centralisée • responsabilité technique portée par le prestataire**.

## Lecture du diagramme
Trois couloirs : **Restaurant** · **Plateforme** · **Prestataire**. Chaque ligne = un moment ; les cases d'une même ligne se passent en parallèle.
Légende des bordures : 🔵 flux commercial / financier · 🟠 décision / validation · 🔴 responsabilité technique · 🟢 exécution / résolution (cases sans couleur : action neutre).
Surlignés en jaune par l'auteur (points sur lesquels il insiste, ou encore à travailler) : « CAS 1 · NON, la pièce doit être approvisionnée » ; « Valide la commande technique » ; « Programme ou confirme l'intervention, selon le délai d'approvisionnement ou la disponibilité du prestataire » ; « Encaisse le client puis rémunère le prestataire ».

## Transcription complète, ligne par ligne
| # | Restaurant | Plateforme | Prestataire |
| --- | --- | --- | --- |
| 1 | **1 · SIGNALEMENT** — Déclare la panne : équipement, marque, modèle, plaque, symptômes, photos, urgence | 🔵 **QUALIFICATION** — Pré-diagnostic + urgence ; sélectionne métier et compétence nécessaires | — |
| 2 | 🟠 **2 · ENGAGEMENT** — Accepte le forfait diagnostic (ex. **129 € HT**) | Encaisse / préautorise ; prix connu avant déplacement | — |
| 3 | — | 🔵 **3 · DISPATCH** — Choisit le meilleur prestataire : zone × disponibilité × métier × marque × historique | 🟠 Accepte la mission ; tarif contractuel plateforme connu |
| 4 | Accueille le technicien | Suit l'intervention ; horodatage arrivée / début du diagnostic | 🔴 **4 · RESPONSABILITÉ TECHNIQUE** — Réalise le diagnostic ; le prestataire engage sa responsabilité sur son diagnostic |
| 5 | — | 🟠 Pièce nécessaire ? | Identifie panne + référence : référence, quantité, temps de pose |
| 6a | 🟢 **NON** — Valide le prix de réparation immédiate | 🔵 Prix ferme proposé : MO + éventuel consommable | 🟢 Répare immédiatement |
| 6b (OU) | **OUI** — Attend proposition | 🔵 **5 · APPROVISIONNEMENT** — Calcule le prix client : pièce + livraison + retour + MO + marge | 🔴 Valide la référence technique ; erreur de référence à sa charge |
| 7 | 🟠 Accepte le devis complémentaire ? Un seul prix total visible | Enregistre l'accord ; aucune commande sans validation client | — |
| 8 (↓ OUI) | — | 🟠 La pièce est-elle disponible dans le stock du prestataire ? Le prestataire confirme référence, quantité et disponibilité réelle | Contrôle son stock ; la pièce doit être physiquement disponible et affectable à la mission |
| 9a | **CAS 1 · NON** — la pièce doit être approvisionnée | 🔵 Commande la pièce via la plateforme ; prix fournisseur, livraison et délai tracés dans le dossier | Valide la commande technique ; référence validée sous sa responsabilité |
| 9b (OU) | **CAS 2 · OUI** — la pièce est déjà disponible | 🔵 Enregistre la réservation ; la pièce est affectée à cette intervention et intégrée au prix client | 🟢 Réserve la pièce en stock ; elle ne peut plus servir à une autre mission |
| 10 | Reçoit la 2e intervention, sauf réparation immédiate avec la pièce déjà présente dans le véhicule | Programme ou confirme l'intervention, selon le délai d'approvisionnement ou la disponibilité du prestataire | 🟢 Pose + essais + remise en service |
| 11 | 🟢 **6 · CLÔTURE** — Valide la remise en service | Rapport + facture client ; historique machine mis à jour | PV technique + photos : pièce posée, tests, temps passé |
| 12 | 🔵 Paie la plateforme | 🔵 Encaisse le client puis rémunère le prestataire ; la marge reste dans la plateforme | 🔵 Est payé par la plateforme |
| 13 | Interlocuteur : la plateforme ; en cas de SAV, le restaurant reste dans le parcours | 🔴 **7 · SAV** — Orchestre la réclamation ; pas de nouvelle facturation client si erreur prestataire | 🔴 Porte la garantie technique : erreur de diagnostic, mauvaise référence ou malfaçon = reprise à sa charge |

## Ce que le diagramme implique pour l'appli (analyse du 2026-11-21)
1. **La plateforme est un acteur actif, pas une simple place de marché** : elle qualifie (pré-diagnostic, métier, compétence), choisit le prestataire, calcule le prix client, commande les pièces, programme la 2e intervention, facture et gère le SAV. En bêta, une bonne part sera faite **à la main par l'équipe** (back-office « EXPERT ») : le back-office est un produit à part entière, pas un écran d'admin.
2. **Modèle de revenu = marge, pas commission** : le prestataire travaille à un **tarif contractuel plateforme** connu d'avance ; le client paie un prix calculé par la plateforme ; « la marge reste dans la plateforme ». Le prévisionnel raisonne en commission de 10 % : les deux modèles ne sont pas réconciliés.
3. **Le prix client est calculé par la plateforme, pas saisi par le technicien** : il faut des grilles (taux de MO contractuel, consommables, prix fournisseur des pièces, frais de livraison et de retour, règle de marge). Le technicien ne fournit que la référence, la quantité et le temps de pose.
4. **Deux types de devis** : réparation immédiate sans pièce (prix ferme MO + consommable, validé par le restaurant sur place) et devis complémentaire avec pièce (un seul prix total, accord enregistré avant toute commande).
5. **Gestion de stock côté prestataire** : déclaration du stock du camion, contrôle de disponibilité réelle, **réservation de la pièce pour une mission** (verrou). Le cadrage avait repoussé le « stock embarqué » à plus tard : à arbitrer.
6. **Commande de pièces via la plateforme** avec traçabilité (prix fournisseur, livraison, délai) : fournisseurs à référencer (Rational en premier ; Negoce CHR, GEV, Stock Direct CHR…), commande manuelle en bêta possible.
7. **Intervention en deux temps** : une mission peut avoir **plusieurs passages** (diagnostic, puis pose). Il faut planifier la 2e intervention selon le délai d'appro et la disponibilité, et la notifier au restaurant.
8. **Horodatages** : arrivée et début du diagnostic (sert aux indicateurs et au litige), PV technique avec temps passé.
9. **Clôture à double validation** : le prestataire produit le PV (pièce posée, tests, temps, photos) ; le restaurant valide la remise en service ; la plateforme émet rapport et facture et met à jour l'**historique machine** (objet équipement persistant).
10. **Flux d'argent** : préautorisation ou encaissement du forfait à l'engagement ; paiement du reste par le restaurant à la clôture ; reversement au prestataire par la plateforme. Conséquence technique : une préautorisation carte expire (environ 7 jours chez Stripe) ; avec un délai d'appro, prévoir encaissement au moment de l'accord ou nouvelle autorisation.
11. **SAV et garantie** : la plateforme orchestre, le prestataire reprend à ses frais. Il faut un objet « réclamation » lié à l'intervention, et un mécanisme pour faire porter le coût au prestataire (retenue sur reversements, garantie contractuelle) ; durée de garantie non précisée.
12. **Responsabilités = clauses contractuelles** : erreur de diagnostic ou de référence à la charge du prestataire → contrat prestataire, CGU, RC pro obligatoire.

## Écarts avec le CDC V1 ([[2026-11-02-cahier-des-charges]]) et les autres sources
Tranchés le 2026-11-21 : **la colonne « process » est retenue** (sauf le signalement, qui ajoute simplement modèle et plaque au CDC).
| Sujet | Process de Lancelot (retenu) | CDC V1 / autres (écarté) |
| --- | --- | --- |
| Forfait | Forfait **diagnostic**, ex. 129 € HT | 110 € incluant déplacement, diagnostic **et 45 min de dépannage** ; HT ou TTC non précisé |
| Réparation sans pièce | Facturée en plus : prix ferme MO + consommable | Incluse dans le forfait jusqu'à 45 min |
| Qui fait le devis | La plateforme calcule ; le prestataire valide la référence | Le technicien saisit durée + pièce depuis un catalogue par marque |
| Affectation | La plateforme choisit le meilleur prestataire (5 critères) | Alerte, acceptation, relance vers un autre si refus ; cadrage : affectation manuelle |
| Revenu | Marge plateforme ; tarif contractuel prestataire | Commission « à définir » ; prévisionnel : 10 % |
| Stock | Stock du prestataire contrôlé et réservé par mission | Cadrage : stock embarqué plus tard |
| Signalement | Modèle et **plaque** demandés | Famille, marque, connectée, description, photo |
| Paiement | Client paie à la clôture | Nouveau devis = nouveau paiement à l'acceptation |

## Ce que le diagramme ne couvre pas (à compléter)
Refus du forfait ; aucun prestataire disponible ou refus de mission ; **refus du devis complémentaire** (seule la branche OUI est dessinée ; le CDC dit : remise en état initial) ; panne non réparable ou machine à remplacer ; restaurant qui ne valide pas la remise en service (litige) ; annulation ; notation ; durée de la garantie ; délai de paiement du prestataire ; parcours artisan (électricien, plombier…) ; cas limites listés dans [[2026-11-09-indicateurs-suivi]].

→ [[app-beta]], [[brief-prd]], [[offer]]
