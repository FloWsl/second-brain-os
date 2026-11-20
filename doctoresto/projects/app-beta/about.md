---
title: Appli Doctoresto - version bêta
type: project
status: active
created: 2026-11-20
updated: 2026-11-20
review_by: 2026-12-20
importance: 5
sources: ["[[2026-11-02-cahier-des-charges]]", "[[2026-11-09-cr-reunion]]", "[[2026-10-26-cr-reunion]]", "[[2026-11-09-process-operationnel]]", "[[2026-11-09-indicateurs-suivi]]", "[[2026-11-09-cout-geolocalisation]]", "[[2026-11-02-maquette-ecrans-v6]]"]
summary: Bêta à Paris en avril 2027 - interventions les plus demandées, 3 marques au début, CDC V1 (14 écrans client, 11 technicien, forfait de 110 €) ; Florian doit chiffrer le temps et le coût de la bêta.
---
# Appli Doctoresto, version bêta
Responsable dev : Florian ([[me]]). Échéance : bêta à Paris en avril 2027, société créée avant.
Statut au 2026-11-20 : CDC V1 rédigé par Jess (2026-11-02), à relire par tous ; maquette v6 de Flo (2026-11-02) ; process et indicateurs de Lancelot (2026-11-09). **Chiffrage du temps et du coût de la bêta : à faire (Flo).**

## Périmètre de la bêta
- Interventions les plus demandées, 3 marques au début, tout Paris. (CR 2026-10-26)
- Familles d'équipements du CDC : four et sauteuse, lave-verre et lave-vaisselle, café, fourneau et friteuse, frigo, robot. Marques : Rational, Unox, Hobart, MKN, Convotherm. Seul Rational est documenté (pannes, pièces, prix, poids) : [[2026-11-01-pannes-rational]].
- Second parcours « autre équipement » pour les artisans (électricien, plombier, maçon, peintre, bricoleur ; pannes à recenser par Lancelot).
- Pas dans la bêta : suivi du technicien en temps réel (coût de l'API Google), mais le technicien doit être dans le périmètre (CR 9/11). Coût estimé si on le fait : 0 à 50 € par mois, 1 500 à 5 000 € de dev ([[2026-11-09-cout-geolocalisation]]).
- Plus tard : machines connectées (codes d'erreur), paiement en 3 fois, abonnements, affectation automatique, diagnostic IA.

## Parcours (CDC V1, détail dans [[2026-11-02-cahier-des-charges]])
Client : accueil à 2 boutons → compte (Apple, Google, Face ID) → famille → marque → connectée ou non → description et photo → géolocalisation → forfait de 110 € → paiement → heure d'arrivée → devis → réparée oui ou non → notation.
Technicien : candidature validée par un EXPERT (back-office) → alerte, acceptation et heure → arrivée géolocalisée (démarre les 45 min) → réparé, devis (catalogue de pièces par marque) ou impossible → photos avant et après.
Process opérationnel complet (dispatch, pièces, SAV) : [[2026-11-09-process-operationnel]].

## Indicateurs
Délai d'arrivée, réparation au premier passage, note moyenne (CDC) ; seuils continuer/alerte de Lancelot : [[2026-11-09-indicateurs-suivi]].

## Identité visuelle
6 pistes de style ; le bleu plaît (CR 9/11). [[2026-11-02-pistes-style]]

## Questions ouvertes (CDC)
Panne non réparable (remboursement du forfait ?), aucun technicien disponible (délai maximum ?), machine non listée, litiges, RGPD, statut et RC pro des artisans, commission et reversement.
Technique (doc IA de la feuille de route) : no-code (Bubble ou Sharetribe + Stripe Connect) ou sur mesure ; à trancher dans mon chiffrage.

## History
- Cadrage (2026-10-13) : équipements de boulangerie (four, pétrin, diviseuse, froid), affectation manuelle, mode hors-ligne. Le CDC du 2/11 a élargi la cible à la cuisine pro (fours mixtes, laverie, café, froid, robots).
- Maquette v6 (2026-11-02) : forfait de 80 €, démo à Nice, suivi en direct. Remplacé par le CDC : forfait de 110 €, pas de suivi en temps réel dans la bêta.
