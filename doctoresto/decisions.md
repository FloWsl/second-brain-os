---
title: Decisions
type: decision
status: active
created: 2026-11-20
updated: 2026-11-21
summary: Dated decisions with their reason, newest first.
---
# Decisions
Format: `## YYYY-MM-DD <decision>` then `Why:` and `Replaces:` if any.

## 2026-11-21 La discussion du 9/11 prime sur le process de Lancelot là où ils se contredisent (Florian, responsable dev)
Why: décision de Florian ; la discussion du 9/11 ([[2026-11-09-notes-granola-reunion]]) simplifie la bêta (pas de stock, pas de commande ni de planning côté plateforme, pas d'avance de trésorerie sur les pièces) et colle au fonctionnement réel des entreprises de maintenance (le bureau intègre la pose dans la tournée). Le process reste la référence pour le reste (qualification, dispatch, prix calculé par la plateforme, marge, responsabilités, clôture, SAV). **À présenter à l'équipe.**
Conséquences :
- **Empreinte CB à la commande**, libérée si aucun technicien avant un délai (ex. minuit).
- **Taux horaire, 1re heure indivisible débitée à l'arrivée du technicien** ; heures suivantes et pièce via le devis.
- **Devis calculé par la plateforme** (heures + pièce + marge), un seul total, **payé à sa validation** ; le technicien peut lancer le devis avant de quitter le client.
- **Pièces commandées par le bureau du technicien**, qui planifie la pose (2e passage hors plateforme, visibilité maintenue) ; le technicien déclare « dans le camion » ou « à commander » ; **pas de stock géré** ; délai fabricant + 1 jour, relances, sinon pièce non payée au technicien.
- **Reversement par relevé mensuel** (bimensuel si urgence), validé par le technicien.
Replaces: forfait de diagnostic de 129 € HT à l'engagement, reste payé à la clôture, commande de pièces et stock réservé par la plateforme, 2e passage planifié par la plateforme (process de Lancelot, décision du même jour ci-dessous).

## 2026-11-21 Stack de la bêta : première piste Expo + Convex + Stripe (piste de réflexion, pas définitive)
Why: code TypeScript qui appartient à la société (pacte, art. 1), rapide à coder seul avec l'IA, machine à statuts, tâches planifiées et temps réel intégrés pour le process de Lancelot ; le no-code colle mal au prix calculé après diagnostic et aux passages multiples. Client en web app, technicien en app, back-office web ; MVP d'un mois découpé. Convex si Florian le maîtrise déjà, sinon Supabase. [[stack-technique]]
Replaces: piste no-code Bubble ou Sharetribe du doc IA ([[2026-11-15-feuille-de-route-ia]]).

## 2026-11-21 Le process opérationnel de Lancelot fait référence pour le produit (Florian, responsable dev) — amendé le même jour par la discussion du 9/11 (paiement, reversement, pièces, stock)
Why: c'est le document le plus complet et le plus cohérent sur le déroulé d'une intervention (rôles, responsabilités, flux d'argent) ; il sert d'ossature au PRD. Décision de Florian pour le dev, **à présenter à l'équipe** : le CDC V1 de Jess et le prévisionnel sont à aligner. [[2026-11-09-process-operationnel]], [[brief-prd]]
Conséquences, sur les 6 points où il contredit le CDC :
- Forfait = **forfait de diagnostic** (réf. 129 € HT, donné « à titre d'exemple », montant à confirmer), sans temps de réparation inclus ; réparation sans pièce facturée en prix ferme (MO + consommable).
- **La plateforme calcule le prix client** (pièce + livraison + retour + MO + marge, un seul total) ; le prestataire fournit et valide la référence.
- **La plateforme choisit le prestataire** (zone × disponibilité × métier × marque × historique) ; le prestataire accepte.
- **Revenu = marge** ; le prestataire est payé à un tarif contractuel plateforme.
- **Stock du prestataire contrôlé et réservé par mission dès la bêta.**
- **Paiement** : forfait à l'engagement, reste à la clôture après validation de la remise en service ; la plateforme reverse ensuite au prestataire.
Replaces: forfait de 110 € avec 45 min (CDC V1, CR du 9/11) ; commission de 10 % (prévisionnel) ; devis saisi par le technicien et alerte ouverte (CDC) ; stock embarqué plus tard (cadrage 2026-10-13) ; paiement à l'acceptation du devis (CDC).

## 2026-11-20 Jessica est présidente de la SAS (confirmé)
Why: désignée dans le pacte signé (PDF du 2026-11-13) ; confirmé par Florian.
Replaces: « président à désigner » (CR du 9/11).

## 2026-11-09 Créer la société avant la bêta d'avril 2027
Why: sans société ni assurance, un incident après une intervention (pièce mal remontée, départ de feu la nuit) retomberait sur les associés en personne. (CR 9/11)
Replaces: création de la société en septembre 2027 (diapos du 19/10).
Voir [[creation-societe]].

## 2026-11-09 Pacte d'associés rédigé entre nous, sans avocat ; signé via DocuSign (PDF du 2026-11-13)
Why: 300 € HT de l'heure jugés disproportionnés pour un projet familial. (CR 9/11)
Replaces: pacte rédigé avec un avocat en droit des affaires (ODJ du 26/10).
Contenu : WRLJ SAS, capital de 20 000 €, présidente Jessica, 37,5/37,5/15/10, vesting 12 mois, majorité de 3 sur 4. [[2026-11-02-pacte-associes]]

## 2026-11-09 Pas de suivi du technicien en temps réel dans la bêta
Why: coût de l'API Google ; le technicien doit seulement être dans le périmètre. (CR 9/11)
Voir [[app-beta]].

## 2026-11-09 Forfait client de 110 € (déplacement, diagnostic, 45 min) puis devis payé à part — remplacé le 2026-11-21 (forfait de diagnostic du process)
Why: prix d'appel clair, connu avant le déplacement. (CDC V1 du 2/11, repris au CR du 9/11)
Replaces: forfait de 80 € de la maquette v6.
Voir [[offer]].

## 2026-11-09 Nom de l'appli : plutôt DoctoResto (pas encore définitif)
Why: efficace et mémorable (trouvé spontanément par Lancelot et un installateur), aucune marque ni entreprise à ce nom à l'INPI ni sur TMview ; proximité avec Doctolib à vérifier. (CR 9/11)

## 2026-10-26 Bêta rapide : interventions les plus demandées, 3 marques au début, tout Paris
Why: tester vite avec un périmètre réduit. (CR 26/10)

## 2026-10-26 Capital : 15 % Léa, 10 % Flo, le reste à Jess et Lancelot (37,5 % chacun dans le pacte)
Why: base retenue en réunion. (CR 26/10)
Replaces: proposition 5/5/45/45 du 19/10.

## 2026-10-19 Bêta de l'appli en avril 2027, sur tout Paris, avec quelques corps de métier CHR seulement
Why: tester vite sur une zone dense ; le coût de l'appli dépend des fonctionnalités retenues. Le Sirha (janvier 2027) sert à rencontrer les fournisseurs. (CR 19/10, version Drive du 2026-10-21)
Replaces: bêta prête pour le Sirha avec 100 restaurateurs et 30 techniciens inscrits (copie du CR dans le doc de cadrage).
Voir [[app-beta]], [[sirha-2027]].

## 2026-10-19 Réunion d'équipe chaque lundi à 13h
Why: rythme hebdomadaire (CR 19/10).
Replaces: lundi 14h (copie du CR dans le doc de cadrage).

## 2026-10-13 Périmètre de lancement : 4 équipements (four, pétrin, diviseuse, froid), affectation manuelle, mode hors-ligne ; IA, stock embarqué et GPS plus tard (stock : remplacé le 2026-11-21)
Why: l'affectation automatique demande assez de techniciens, l'IA un historique de pannes ; les labos sont mal couverts en réseau ; Waze suffit pour le GPS. (cadrage)
Voir [[app-beta]].

## 2026-10-13 Vérifier le besoin sur le terrain avant de développer
Why: personne n'avait encore parlé à un boulanger ni à un technicien. Critère d'arrêt : moins de la moitié des boulangers citent une panne récente mal gérée. (cadrage)
Voir [[validation-terrain]].
