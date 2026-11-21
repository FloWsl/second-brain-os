---
title: Stack technique de la bêta - première piste
type: project
status: draft
created: 2026-11-21
updated: 2026-11-21
review_by: 2026-12-05
importance: 5
sources: ["[[2026-11-09-notes-granola-reunion]]", "[[app-beta]]", "[[brief-prd]]", "[[2026-11-09-process-operationnel]]", "[[2026-11-15-feuille-de-route-ia]]", "[[me]]"]
summary: Première piste de réflexion (Florian, 2026-11-21) - Expo + Convex + Stripe, client en web app, technicien en app, back-office web ; MVP d'un mois découpé ; flux d'argent en charges et transferts séparés (Stripe Connect : empreinte, 1re heure à l'arrivée, devis payé à sa validation, relevé mensuel) ; 5 principes d'architecture pour passer à l'échelle ; Convex ou Supabase selon la maîtrise de Convex ; questions ouvertes.
---
# Stack technique de la bêta — première piste (2026-11-21)
**Statut : piste de réflexion validée par Florian le 2026-11-21, pas une décision définitive.** À confirmer après les questions ouvertes ci-dessous et le chiffrage. Contexte produit : [[app-beta]], [[brief-prd]] (process de Lancelot = référence).

## Stack envisagée
| Brique | Choix | Pourquoi |
| --- | --- | --- |
| Front | **Expo** (React Native + web, une seule base de code) | iOS, Android et web ; une app à 2 rôles (accueil à 2 boutons du CDC) ; mises à jour à distance (EAS Update) sans repasser par les stores, utile pendant l'absence de Florian en mars-avril 2027 |
| Backend | **Convex** (alternative : Supabase / Postgres) | Machine à statuts en mutations transactionnelles, tâches planifiées (relance dispatch, rappels 2e passage), temps réel, stockage des photos, webhooks Stripe ; backend open source et auto-hébergeable (code cédé à WRLJ, pacte art. 1) |
| Paiement | **Stripe** (Checkout hébergé côté web : empreinte CB, forfait de 129 € HT (déplacement + 1re heure) capturé à l'arrivée, devis payé à sa validation) ; **Stripe Connect Express** en charges et transferts séparés (voir Flux d'argent), possible dès le MVP | Modèle à marge = charges et transferts séparés ; Connect gère la vérification d'identité des techniciens |
| Connexion | Clerk (ou Convex Auth) ; Face ID = déverrouillage local (`expo-local-authentication`) | Apple et Google ; Clerk plus mûr sur Expo |
| Facturation | Outil externe via API | Réforme de la facturation électronique B2B (émission obligatoire pour les PME en septembre 2027) |
| Analyse | Export nocturne (cron) vers Airtable ou Google Sheets | Pas de SQL dans Convex ; indicateurs de Lancelot et prévisionnel de Jess |

Coûts récurrents en bêta : Convex, EAS et Clerk gratuits au début ; Apple Developer 99 €/an ; Google Play 25 € une fois ; frais Stripe (voir « Coûts Stripe » ci-dessous : ~1,5 % + 0,25 € par paiement carte, Connect 2 € par technicien actif et par mois + 0,10 € + 0,25 % par virement). Tient dans les 3 500 € du prévisionnel tant que le dev est fait par Florian.

## Répartition par canal
- **Client : web app** (lien, magnet QR, Apple Pay dans le navigateur), pas de store en V1 : cohérent avec « panne → commande en moins de 2 minutes » et « déclarer sans compte ». ⚠️ Écart avec le CDC (apps natives iOS et Android) : à présenter à l'équipe.
- **Technicien : app** Expo (notifications, photos, géolocalisation). Publication sur les stores à lancer dès la semaine 1 (1 à 2 semaines de risque : validation Apple, compte de démo), sinon web le premier mois.
- **Back-office : web**, dans la même app Expo derrière un rôle admin (ou Next.js à part, à trancher). C'est le poste le plus lourd (~30 à 40 % des heures).

## Principes d'architecture (base pour passer à l'échelle, quelle que soit la stack)
1. Machine à statuts de l'intervention dans **une seule fonction serveur** (`transition(intervention, événement)`) avec les transitions autorisées ; aucune logique métier dans le front.
2. **Journal d'événements horodatés** : indicateurs ([[2026-11-09-indicateurs-suivi]]), litiges, SAV, migration future.
3. **Calcul de prix en fonctions pures testées** (les règles de marge vont changer).
4. **Modules aux frontières nettes** (paiement, facturation, notifications) branchés sur des services externes.
5. **Modèle de données du PRD tel quel** ([[brief-prd]] §2.11), y compris intervention → plusieurs passages, devis à lignes internes et un seul total client.

## Convex ou Supabase
- Contre Convex : technologie de niche (recrutement, reprise par une agence), API propre (en sortir = réécrire le backend), pas de SQL (BI, due diligence), géospatial moins natif que PostGIS pour un dispatch national.
- Pour Convex : le volume n'est pas un sujet (2 250 interventions/mois fin 2027 au prévisionnel) ; plus rapide à coder seul avec l'IA (temps réel, planification, transactions intégrés).
- **Règle retenue : Convex si Florian le connaît déjà ; Supabase s'il le découvre** (tant qu'à apprendre, apprendre le standard).

## Charge et MVP d'un mois
Périmètre complet du process : **~90 à 100 h** avec l'IA (estimation du 2026-11-21) : installation, connexion et rôles ~6 h ; parcours client ~12 h ; app technicien ~20 h ; back-office ~20 h ; Stripe ~10 h ; Connect ~8 h ; notifications ~6 h ; facturation ~6 h ; stores et tests ~10 h.
En 1 mois, il faut ~25 h par semaine ; au rythme actuel (~1 h par jour, [[me]]), ces 90-100 h représentent déc.-fév. L'objectif d'un mois impose de couper le périmètre, pas de changer de stack. Livré fin décembre, il donne une démo qui marche au Sirha (21-25 janvier 2027, [[sirha-2027]]).

MVP d'un mois (~30 à 40 h) :
| Dans le MVP | Fait à la main ou reporté |
| --- | --- |
| Client web : déclaration, photos, empreinte CB par paiement Stripe hébergé, carte enregistrée, validation du devis | Dispatch : choisi par l'équipe dans le back-office |
| App technicien : mission, arrivée (débit du forfait), diagnostic, « camion / à commander », devis lancé sur place, photo de clôture | Commandes de pièces : par le bureau du technicien (hors plateforme), délai et relances suivis |
| Back-office web : file, dispatch, statuts, calcul du prix, suivi des délais de pièces, clôture | Stock : aucun (le technicien déclare « camion » ou « à commander ») |
| Journal d'événements et export des indicateurs | Reversements : relevé mensuel ; Stripe Connect si les techniciens s'inscrivent à Stripe Express à la candidature (sinon virements manuels et Connect au mois 2) ; relevés générés à la main le premier mois |
|  | Facturation : outil externe à la main au début |

## Flux d'argent (piste de Florian du 2026-11-21, adaptée à la discussion du 9/11)
**Principe : « charges et transferts séparés » de Stripe Connect.** Le client paie la plateforme (compte Stripe de WRLJ). Plus tard, quand la plateforme le décide, elle transfère au compte connecté (Express) du prestataire. Entre les deux, l'argent attend sur le solde de la plateforme (« modèle Vinted » : bloqué jusqu'à la fin de la prestation). La marge, c'est ce qui n'est pas transféré.
Règles de paiement retenues le 2026-11-21 ([[2026-11-09-notes-granola-reunion]], prime sur le process de Lancelot sur ce point) : empreinte CB à la commande, **forfait de diagnostic de 129 € HT (déplacement + 1re heure d'intervention, indivisible) débité à l'arrivée**, **2e paiement à la validation du devis**, **reversement par relevé mensuel** validé par le technicien.

**Mécanique**
1. **Commande** : empreinte CB = PaymentIntent en `capture_method=manual` (Checkout côté web), avec `transfer_group=<id intervention>` et `setup_future_usage` pour enregistrer la carte. Montant autorisé = le forfait TTC (154,80 € avec une TVA à 20 %).
2. **Aucun technicien avant le délai** (ex. minuit) : tâche planifiée qui annule le PaymentIntent → empreinte libérée, rien n'est débité.
3. **Arrivée horodatée du technicien** : capture du PaymentIntent (forfait). Webhook : récupérer la `latest_charge` (`ch_xxx`) et la stocker sur l'intervention (`checkout.session.completed` ne donne pas directement la charge).
4. **Validation du devis** (heures en plus et/ou pièce) : le client est sur place et valide dans l'appli → nouveau PaymentIntent avec la carte enregistrée, **client présent** : si la banque exige 3-D Secure, il s'authentifie tout de suite. Même `transfer_group`.
5. **Relevé mensuel** (bimensuel si urgence de trésorerie) : la plateforme génère le relevé du technicien ; il le valide ou signale des erreurs ; à la validation, `POST /v1/transfers` avec `destination=acct_<prestataire>` et `source_transaction=ch_xxx`, **un transfert par paiement** (un transfert ne peut pas dépasser la charge sur laquelle il s'appuie). Avec `source_transaction`, la demande réussit toujours et le transfert part quand les fonds sont disponibles ; sans lui, un transfert supérieur au solde échoue et Stripe ne réessaie pas.

**Règles**
- **Montant transféré = ce qui revient au prestataire** d'après les lignes internes (tarif contractuel : heures, consommables, pièce achetée par son bureau), calculé par la même fonction de prix que le devis. Pas « total − commission ».
- **Pièce posée hors délai** (délai fabricant + 1 jour, après relances) : la ligne « pièce » sort du relevé, elle n'est pas payée au technicien. Ce qui revient au client reste à trancher.
- **Pas d'avance de trésorerie** : le bureau du technicien achète la pièce, le client l'a déjà payée à la validation du devis, la plateforme rembourse le technicien au relevé.
- Le relevé mensuel laisse une fenêtre SAV avant de payer (moins de transferts à annuler), mais paie plus lentement des techniciens qui se plaignent des retards de paiement : d'où l'option bimensuelle.
- **Clé d'idempotence par transfert** (`intervention:paiement`) : un webhook rejoué ou une tâche Convex relancée ne doit jamais payer deux fois.
- **Aucune mission proposée** tant que le compte Express du technicien n'a pas la capacité `transfers` active (contrôle à la validation de la candidature).
- **Frais et risques chez la plateforme** : frais Stripe (non rendus en cas de remboursement) et rétrofacturations ; la fonction de prix les intègre, la marge doit les couvrir. Stripe ne recommande ce mode que si la plateforme **assume les soldes négatifs des comptes connectés** : remboursements et litiges sont à sa charge, à elle de récupérer l'argent chez le prestataire par une annulation de transfert (« transfer reversal »). Le relevé mensuel aide : tant que le relevé n'est pas payé, rien n'est à récupérer.
- **Toujours renseigner `source_transaction`** : les virements automatiques du compte plateforme vers sa banque (calendrier de payout) peuvent vider le solde dont dépendraient des transferts qui n'en ont pas.
- **TVA des deux côtés** : client facturé TTC ; transfert = montant de la facture du technicien (TTC, ou sans TVA s'il est en franchise).
- **Ne pas parler de « séquestre »** dans les CGU ni dans le marketing : le séquestre de fonds pour le compte d'un tiers est une activité réglementée. Dans le modèle à marge, la plateforme vend le service : l'argent encaissé est son chiffre d'affaires, et elle paie un sous-traitant. À valider avec l'expert-comptable (avec la TVA et DAC7). Pour démontrer qu'on ne touche pas aux fonds des prestataires, Stripe propose une fonction de cantonnement des fonds (« funds segregation » : fonds placés dans un état réservé avant transfert), **en preview** : à suivre, pas à prévoir pour la bêta.
- **Accès au mode « charges et transferts séparés »** : la documentation indique qu'il faut parfois contacter Stripe pour l'activer. **À vérifier sur le compte Stripe dès sa création.**

**Coûts Stripe (France, tarif standard à vérifier sur la grille du compte ; extrait d'une discussion Claude.ai de Florian, 2026-11-21)**
| Poste | Tarif | Exemple |
| --- | --- | --- |
| Paiement carte européenne standard | ~1,5 % + 0,25 € par paiement | Intervention de 400 € en 2 paiements (forfait + devis) : 6 € + 2 × 0,25 € ≈ **6,50 €** |
| Connect, compte actif (plateforme qui gère la tarification des prestataires) | 2 € par compte actif et par mois | 30 techniciens payés dans le mois : 60 € |
| Connect, virement envoyé au prestataire | 0,10 € + 0,25 % du montant | Relevé de 3 000 € : 7,60 € |
| Virement instantané | 1 % du montant | À éviter, sauf urgence de trésorerie (option bimensuelle plutôt) |
Ordre de grandeur : ~1,6 % côté encaissement, plus ~0,3 % et 2 € par technicien et par mois côté reversement, soit cohérent avec les ~2 % estimés le 9/11. Le relevé mensuel limite les frais Connect (un seul virement par technicien et par mois) : régler le calendrier de virement des comptes Express en conséquence. Hypothèses des exemples (400 €, 3 000 €) : illustratives.

**Conséquence pour le MVP** : le schéma coûte peu, et la commande des pièces par le bureau du technicien supprime le stock, les commandes et le planning côté plateforme. Si les techniciens font leur inscription Stripe Express pendant leur candidature, **Stripe Connect peut entrer dans le MVP d'un mois** ; les relevés peuvent être générés à la main le premier mois.

## Points d'attention
- Empreinte CB : courte (même jour), donc compatible avec la durée de validité d'une autorisation carte (~7 jours chez Stripe pour la plupart des cartes, à vérifier). Le montant capturé ne peut pas dépasser le montant autorisé : autoriser au moins le forfait TTC.
- SDK Stripe différent sur web (`@stripe/stripe-react-native` ne marche pas sur le web) → Checkout hébergé côté client web.
- ⚠️ Modèle à marge : la plateforme vend le service et facture la TVA sur le total, le technicien facture la plateforme ; effet possible sur DAC7. **À faire valider par un expert-comptable avant de coder la facturation.**

## Questions ouvertes
1. Florian a-t-il déjà livré avec Convex ? (décide Convex ou Supabase et double ou non l'estimation)
2. « 1 mois » = combien d'heures par semaine ?
3. Le Sirha est-il l'objectif réel du premier mois ?
4. Client : web seul, ou aussi app ? (écart avec le CDC à présenter)
5. Back-office dans l'app Expo ou en Next.js à part ?
6. Le prototype Claude de Léa est-il réutilisable ?
7. ~~Avance de trésorerie sur les pièces~~ → supprimée : le bureau du technicien commande, le client paie à la validation du devis (décision du 2026-11-21, [[2026-11-09-notes-granola-reunion]]).
8. Rythme du relevé : mensuel par défaut, bimensuel pour qui ? (critère « urgence de trésorerie » à définir).
9. Durée maximale de détention des fonds sur le solde plateforme avant transfert (un mois avec le relevé mensuel) et durée maximale d'une empreinte CB : **toujours à vérifier** (non couvert par l'extrait du 2026-11-21). Coûts : réglé (voir « Coûts Stripe »). Frais éventuels d'une empreinte libérée sans débit : à vérifier.
12. Le mode « charges et transferts séparés » est-il activé d'office sur le compte, ou faut-il contacter Stripe ?
10. Client en cas de retard de pièce (au-delà du délai fabricant + 1 jour) : remboursement de la pièce, geste commercial ?
11. Délai de libération de l'empreinte si aucun technicien (minuit ? selon l'heure de la demande ?).

## Écarté
- Sharetribe : surtout web, modèle de transaction mal adapté au prix calculé après diagnostic et aux passages multiples.
- Bubble : workflow complexe pénible, code non exportable (contraire à la cession du code), coûts qui montent.
- Estimations du doc IA (no-code 3-6 semaines, 0-3 500 €) : supposaient une marketplace simple, sous-estiment le process de Lancelot. [[2026-11-15-feuille-de-route-ia]]
