---
title: Appli Doctoresto - version bêta
type: project
status: active
created: 2026-11-20
updated: 2026-11-21
review_by: 2026-12-20
importance: 5
sources: ["[[2026-11-02-cahier-des-charges]]", "[[2026-11-09-cr-reunion]]", "[[2026-11-09-notes-granola-reunion]]", "[[2026-10-26-cr-reunion]]", "[[2026-11-09-process-operationnel]]", "[[2026-11-09-indicateurs-suivi]]", "[[2026-11-09-cout-geolocalisation]]", "[[2026-11-02-maquette-ecrans-v6]]"]
summary: Bêta à Paris en avril 2027 - interventions les plus demandées, 3 marques au début ; référence produit = process de Lancelot amendé par la discussion du 9/11 (empreinte CB, forfait de 129 € HT pour le déplacement et la 1re heure débité à l'arrivée, devis calculé par la plateforme et payé à sa validation, marge, pièces commandées par le bureau du technicien, relevé mensuel) ; écrans du CDC V1 ; Florian doit chiffrer le temps et le coût de la bêta.
---
# Appli Doctoresto, version bêta
Responsable dev : Florian ([[me]]). Échéance : bêta à Paris en avril 2027, société créée avant.
Statut au 2026-11-20 : CDC V1 rédigé par Jess (2026-11-02), à relire par tous ; maquette v6 de Flo (2026-11-02) ; process et indicateurs de Lancelot (2026-11-09). **Chiffrage du temps et du coût de la bêta : à faire (Flo).**
Brief et PRD compilés : [[brief-prd]]. Stack : [[stack-technique]] (première piste).
**Référence produit depuis le 2026-11-21 : le process de Lancelot** ([[2026-11-09-process-operationnel]]) prime sur le CDC V1 en cas de conflit ; **la discussion du 9/11** ([[2026-11-09-notes-granola-reunion]]) prime sur le process là où ils se contredisent (paiement, reversement, pièces, 2e passage, stock). Décisions dans [[decisions]]. À présenter à l'équipe.

## Périmètre de la bêta
- Interventions les plus demandées, 3 marques au début, tout Paris. (CR 2026-10-26)
- Familles d'équipements du CDC : four et sauteuse, lave-verre et lave-vaisselle, café, fourneau et friteuse, frigo, robot. Marques : Rational, Unox, Hobart, MKN, Convotherm. Seul Rational est documenté (pannes, pièces, prix, poids) : [[2026-11-01-pannes-rational]].
- Second parcours « autre équipement » pour les artisans (électricien, plombier, maçon, peintre, bricoleur ; pannes à recenser par Lancelot).
- Pas dans la bêta : suivi du technicien en temps réel (coût de l'API Google), mais le technicien doit être dans le périmètre (CR 9/11). Coût estimé si on le fait : 0 à 50 € par mois, 1 500 à 5 000 € de dev ([[2026-11-09-cout-geolocalisation]]).
- Dans la bêta : qualification et choix du prestataire par la plateforme (sectorisation, clients préférentiels), calcul du prix client, suivi des délais de pièces (relances), clôture avec photo et validation du client, relevés mensuels, SAV.
- Hors plateforme (décision du 2026-11-21, [[2026-11-09-notes-granola-reunion]]) : commande des pièces et planning du 2e passage, faits par le bureau du technicien ; pas de stock géré (le technicien déclare « camion » ou « à commander »).
- Plus tard : machines connectées (codes d'erreur), paiement en 3 fois, abonnements, affectation entièrement automatique, diagnostic IA.

## Parcours (process amendé, écrans du CDC V1 adaptés ; détail dans [[brief-prd]])
Client : accueil à 2 boutons → compte (Apple, Google, Face ID) → famille → marque, modèle, plaque → description et photo → géolocalisation → conditions (**forfait de 129 € HT, déplacement + 1re heure, dû à l'arrivée** ; heures suivantes au taux horaire) → **empreinte CB** (libérée si aucun technicien) → prestataire et heure d'arrivée → 1re heure débitée à l'arrivée → si besoin, devis (heures en plus et/ou pièce, un seul total) **payé à sa validation** → pose immédiate ou 2e passage organisé par le bureau du technicien → validation de la remise en service → notation.
Technicien : candidature validée par un EXPERT (back-office), tarif contractuel → mission proposée par la plateforme, acceptation et heure → arrivée horodatée → diagnostic (référence, quantité, temps de pose) → pièce « dans le camion » ou « à commander par son bureau », devis lancé avant de quitter le client, prix calculé par la plateforme, référence validée → pose (son bureau planifie le 2e passage ; délai fabricant + 1 jour, sinon pièce non payée) → photo et PV → relevé mensuel validé → payé par la plateforme.
Process opérationnel complet : [[2026-11-09-process-operationnel]].
Amendements de la discussion du 9/11 : [[2026-11-09-notes-granola-reunion]].

## Indicateurs
Délai d'arrivée, réparation au premier passage, note moyenne (CDC) ; seuils continuer/alerte de Lancelot : [[2026-11-09-indicateurs-suivi]].

## Identité visuelle
6 pistes de style ; le bleu plaît (CR 9/11). [[2026-11-02-pistes-style]]

## Questions ouvertes (CDC)
Panne non réparable (forfait dû ?), aucun technicien disponible (délai de libération de l'empreinte, délai maximum ?), client en cas de retard de pièce, machine non listée, litiges (dont technicien absent après commande de pièce), RGPD, statut et RC pro des artisans. Montants du modèle à marge : taux horaire des heures suivantes, tarifs contractuels, règle de marge.
Technique : **première piste (2026-11-21) : Expo + Convex (ou Supabase) + Stripe**, client en web app, MVP d'un mois découpé → [[stack-technique]]. Pas encore définitif ; no-code (Bubble, Sharetribe) écarté.

## History
- Cadrage (2026-10-13) : équipements de boulangerie (four, pétrin, diviseuse, froid), affectation manuelle, mode hors-ligne. Le CDC du 2/11 a élargi la cible à la cuisine pro (fours mixtes, laverie, café, froid, robots).
- Maquette v6 (2026-11-02) : forfait de 80 €, démo à Nice, suivi en direct. Remplacé par le CDC : forfait de 110 €, pas de suivi en temps réel dans la bêta.
- CDC V1 (2026-11-02) : forfait de 110 € avec 45 min, compteur démarré à l'arrivée, devis saisi par le technicien, alerte ouverte. Remplacé le 2026-11-21 par le process de Lancelot.
- Process de Lancelot (2026-11-09), référence le 2026-11-21 : forfait de diagnostic de 129 € HT à l'engagement, reste payé à la clôture, commande de pièces et stock réservé par la plateforme, 2e passage planifié par la plateforme. Remplacé sur ces points le même jour par la discussion du 9/11.
