---
title: Cahier des charges V1 (diapos)
type: source
status: active
created: 2026-11-20
updated: 2026-11-21
importance: 3
drive_id: 1lj9FzIe1w1m_i0UU5hMnUSyhmj9JvKnP
summary: CDC V1 de Jess : 14 écrans client et 11 écrans technicien, forfait de 110 € (déplacement, diagnostic, 45 min), devis au-delà, validation des techniciens par un EXPERT, MVP iOS et Android.
---
# Cahier des charges V1 (diapos)
> **Depuis le 2026-11-21, le process de Lancelot fait référence** en cas de conflit : prix calculé par la plateforme, choix du prestataire par la plateforme, marge ; et, d'après la discussion du 9/11 ([[2026-11-09-notes-granola-reunion]]), empreinte CB puis 1re heure au taux horaire débitée à l'arrivée (et non 110 € avec 45 min), devis payé à sa validation, pièces commandées par le bureau du technicien, relevé mensuel. Voir [[2026-11-09-process-operationnel]] et [[decisions]]. Les écrans restent la base.
Source : Google Drive, DEVELOPPEMENT/CAHIER DES CHARGES/CDC Visuel (pptx de Jess, 2026-11-02 ; photos des pages papier à côté). Lien : https://drive.google.com/open?id=1lj9FzIe1w1m_i0UU5hMnUSyhmj9JvKnP
Importée le 2026-11-20.

## Vision
Panne en plein service = chiffre d'affaires perdu. Une appli, 2 profils : client (restaurateur, hôtelier, traiteur) et technicien (artisan ou expert d'une marque). Forfait de 110 € (déplacement, diagnostic, 45 min de dépannage). De la panne à la commande en moins de 2 minutes. Photos avant et après, notation.
## Parcours client (14 écrans)
Accueil à 2 boutons ("J'ai une panne" / "Je suis un technicien") → connexion (identifiants, Face ID, Apple, Google, saisie) → machine en panne ou autre équipement (parcours simplifié pour l'artisan) → 6 familles : four et sauteuse, lave-verre et lave-vaisselle, café, fourneau et friteuse, frigo, robot → marque (Rational, Unox, Hobart, MKN, Convotherm ; "autre marque" à valider) → machine connectée ou non → description et photo → récapitulatif et géolocalisation (RGPD) → conditions du forfait (devis si plus de 45 min ou pièce ; nouveau devis = nouveau paiement) → paiement (CB, Apple Pay, 3 fois à étudier) → heure d'arrivée et suivi → devis accepté ou refusé → réparée oui ou non (litige si non) → notation (ponctualité, professionnalisme, explications, appli, recommandation).
## Parcours technicien (11 écrans)
Accueil → connexion et géolocalisation → profil artisan (électricien, plombier, maçon, peintre, bricoleur) ou technicien de marque (Rational, Unox, MKN, RobotCoupe…) → candidature validée par un EXPERT DoctoResto (back-office) → alerte de mission (accepter et fixer son heure ; relance vers un autre technicien si refus) → détail de la panne → arrivée validée par géolocalisation (démarre les 45 min) → réparé, devis ou réparation impossible → devis (durée et pièce depuis un catalogue par marque) → réponse du client (refus = remise en état initial) → photos de clôture.
## Règles et questions ouvertes
Commission et reversement : à définir. Facture automatique par mail. Questions : panne non réparable (garantie, remboursement du forfait ?), paiement en 3 fois sur les devis seulement, machine non listée, aucun technicien disponible (délai maximum ?), statut et RC pro des artisans, litiges, conservation des données de géolocalisation et des photos (RGPD).
## Mise en œuvre
MVP : parcours client et technicien, paiement, notifications ; iOS et Android ; back-office (validation EXPERT, suivi, litiges). Phase 2 : machines connectées, paiement en 3 fois, abonnements. Indicateurs : délai d'arrivée, taux de réparation au premier passage, note moyenne.
→ [[app-beta]], [[offer]]
