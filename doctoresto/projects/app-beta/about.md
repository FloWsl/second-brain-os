---
title: Appli Doctoresto - version bêta
type: project
status: active
created: 2026-11-20
updated: 2026-11-21
review_by: 2026-12-20
importance: 5
sources: ["[[2026-11-02-cahier-des-charges]]", "[[2026-11-09-cr-reunion]]", "[[2026-10-26-cr-reunion]]", "[[2026-11-09-process-operationnel]]", "[[2026-11-09-indicateurs-suivi]]", "[[2026-11-09-cout-geolocalisation]]", "[[2026-11-02-maquette-ecrans-v6]]"]
summary: Bêta à Paris en avril 2027 - interventions les plus demandées, 3 marques au début ; référence produit = process de Lancelot (forfait de diagnostic, prix calculé par la plateforme, marge, stock réservé, paiement à la clôture) ; écrans du CDC V1 ; Florian doit chiffrer le temps et le coût de la bêta.
---
# Appli Doctoresto, version bêta
Responsable dev : Florian ([[me]]). Échéance : bêta à Paris en avril 2027, société créée avant.
Statut au 2026-11-20 : CDC V1 rédigé par Jess (2026-11-02), à relire par tous ; maquette v6 de Flo (2026-11-02) ; process et indicateurs de Lancelot (2026-11-09). **Chiffrage du temps et du coût de la bêta : à faire (Flo).**
Brief et PRD compilés : [[brief-prd]]. Stack : [[stack-technique]] (première piste).
**Référence produit depuis le 2026-11-21 : le process de Lancelot** ([[2026-11-09-process-operationnel]]) prime sur le CDC V1 en cas de conflit (décision dans [[decisions]]). À présenter à l'équipe.

## Périmètre de la bêta
- Interventions les plus demandées, 3 marques au début, tout Paris. (CR 2026-10-26)
- Familles d'équipements du CDC : four et sauteuse, lave-verre et lave-vaisselle, café, fourneau et friteuse, frigo, robot. Marques : Rational, Unox, Hobart, MKN, Convotherm. Seul Rational est documenté (pannes, pièces, prix, poids) : [[2026-11-01-pannes-rational]].
- Second parcours « autre équipement » pour les artisans (électricien, plombier, maçon, peintre, bricoleur ; pannes à recenser par Lancelot).
- Pas dans la bêta : suivi du technicien en temps réel (coût de l'API Google), mais le technicien doit être dans le périmètre (CR 9/11). Coût estimé si on le fait : 0 à 50 € par mois, 1 500 à 5 000 € de dev ([[2026-11-09-cout-geolocalisation]]).
- Dans la bêta (process) : qualification et choix du prestataire par la plateforme, calcul du prix client, stock du prestataire réservé par mission, commande de pièces via la plateforme, 2e passage, clôture à double validation, SAV.
- Plus tard : machines connectées (codes d'erreur), paiement en 3 fois, abonnements, affectation entièrement automatique, diagnostic IA.

## Parcours (process de référence, écrans du CDC V1 adaptés ; détail dans [[brief-prd]])
Client : accueil à 2 boutons → compte (Apple, Google, Face ID) → famille → marque, modèle, plaque → description et photo → géolocalisation → **forfait de diagnostic** → paiement → prestataire et heure d'arrivée → prix ferme ou devis avec pièce (un seul total) → 2e passage si pièce à commander → validation de la remise en service et paiement du reste → notation.
Technicien : candidature validée par un EXPERT (back-office), tarif contractuel → mission proposée par la plateforme, acceptation et heure → arrivée horodatée → diagnostic (référence, quantité, temps de pose) → prix calculé par la plateforme, référence validée, pièce en stock réservée ou commandée → pose → PV et photos → payé par la plateforme.
Process opérationnel complet : [[2026-11-09-process-operationnel]].

## Indicateurs
Délai d'arrivée, réparation au premier passage, note moyenne (CDC) ; seuils continuer/alerte de Lancelot : [[2026-11-09-indicateurs-suivi]].

## Identité visuelle
6 pistes de style ; le bleu plaît (CR 9/11). [[2026-11-02-pistes-style]]

## Questions ouvertes (CDC)
Panne non réparable (remboursement du forfait ?), aucun technicien disponible (délai maximum ?), machine non listée, litiges, RGPD, statut et RC pro des artisans. Montants du modèle à marge : forfait (129 € HT à confirmer), tarifs contractuels, règle de marge.
Technique : **première piste (2026-11-21) : Expo + Convex (ou Supabase) + Stripe**, client en web app, MVP d'un mois découpé → [[stack-technique]]. Pas encore définitif ; no-code (Bubble, Sharetribe) écarté.

## History
- Cadrage (2026-10-13) : équipements de boulangerie (four, pétrin, diviseuse, froid), affectation manuelle, mode hors-ligne. Le CDC du 2/11 a élargi la cible à la cuisine pro (fours mixtes, laverie, café, froid, robots).
- Maquette v6 (2026-11-02) : forfait de 80 €, démo à Nice, suivi en direct. Remplacé par le CDC : forfait de 110 €, pas de suivi en temps réel dans la bêta.
- CDC V1 (2026-11-02) : forfait de 110 € avec 45 min, compteur démarré à l'arrivée, devis saisi par le technicien, alerte ouverte. Remplacé le 2026-11-21 par le process de Lancelot.
