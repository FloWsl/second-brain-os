---
title: Stack technique de la bêta - première piste
type: project
status: draft
created: 2026-11-21
updated: 2026-11-21
review_by: 2026-12-05
importance: 5
sources: ["[[app-beta]]", "[[brief-prd]]", "[[2026-11-09-process-operationnel]]", "[[2026-11-15-feuille-de-route-ia]]", "[[me]]"]
summary: Première piste de réflexion (Florian, 2026-11-21) - Expo + Convex + Stripe, client en web app, technicien en app, back-office web ; MVP d'un mois découpé ; flux d'argent en charges et transferts séparés (Stripe Connect) ; 5 principes d'architecture pour passer à l'échelle ; Convex ou Supabase selon la maîtrise de Convex ; questions ouvertes.
---
# Stack technique de la bêta — première piste (2026-11-21)
**Statut : piste de réflexion validée par Florian le 2026-11-21, pas une décision définitive.** À confirmer après les questions ouvertes ci-dessous et le chiffrage. Contexte produit : [[app-beta]], [[brief-prd]] (process de Lancelot = référence).

## Stack envisagée
| Brique | Choix | Pourquoi |
| --- | --- | --- |
| Front | **Expo** (React Native + web, une seule base de code) | iOS, Android et web ; une app à 2 rôles (accueil à 2 boutons du CDC) ; mises à jour à distance (EAS Update) sans repasser par les stores, utile pendant l'absence de Florian en mars-avril 2027 |
| Backend | **Convex** (alternative : Supabase / Postgres) | Machine à statuts en mutations transactionnelles, tâches planifiées (relance dispatch, rappels 2e passage), temps réel, stockage des photos, webhooks Stripe ; backend open source et auto-hébergeable (code cédé à WRLJ, pacte art. 1) |
| Paiement | **Stripe** (Checkout hébergé côté web, carte enregistrée, débit à la clôture) ; **Stripe Connect Express** en charges et transferts séparés (voir Flux d'argent), possible dès le MVP | Modèle à marge = charges et transferts séparés ; Connect gère la vérification d'identité des techniciens |
| Connexion | Clerk (ou Convex Auth) ; Face ID = déverrouillage local (`expo-local-authentication`) | Apple et Google ; Clerk plus mûr sur Expo |
| Facturation | Outil externe via API | Réforme de la facturation électronique B2B (émission obligatoire pour les PME en septembre 2027) |
| Analyse | Export nocturne (cron) vers Airtable ou Google Sheets | Pas de SQL dans Convex ; indicateurs de Lancelot et prévisionnel de Jess |

Coûts récurrents en bêta : Convex, EAS et Clerk gratuits au début ; Apple Developer 99 €/an ; Google Play 25 € une fois ; frais Stripe par transaction. Tient dans les 3 500 € du prévisionnel tant que le dev est fait par Florian.

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
| Client web : déclaration, photos, forfait par paiement Stripe hébergé, carte enregistrée | Dispatch : choisi par l'équipe dans le back-office |
| App technicien : mission, arrivée, diagnostic, PV et photos | Commandes de pièces : par l'équipe, juste tracées |
| Back-office web : file, statuts, saisie du prix, clôture, débit du reste | Stock : case « pièce dans le camion oui/non » |
| Journal d'événements et export des indicateurs | Reversements : Stripe Connect si les techniciens s'inscrivent à Stripe Express à la candidature, sinon virements manuels et Connect au mois 2 |
|  | Facturation : outil externe à la main au début |

## Flux d'argent (piste de Florian, 2026-11-21)
**Principe : « charges et transferts séparés » de Stripe Connect.** Le client paie la plateforme (compte Stripe de WRLJ). Plus tard, quand la plateforme le décide, elle transfère au compte connecté (Express) du prestataire. Entre les deux, l'argent attend sur le solde de la plateforme. La marge, c'est ce qui n'est pas transféré.

**Mécanique**
1. Forfait de diagnostic : Checkout Session avec `payment_intent_data[transfer_group]=<id intervention>` et `setup_future_usage=off_session` (la carte est enregistrée pour la suite).
2. Webhook `checkout.session.completed` : récupérer le PaymentIntent, puis sa `latest_charge` (`ch_xxx`), et la stocker sur l'intervention (l'événement ne donne pas directement la charge).
3. Clôture validée par le restaurant : PaymentIntent `off_session` pour le reste, même `transfer_group`. Si la banque exige 3-D Secure : envoyer un lien de paiement au client.
4. Reversement : `POST /v1/transfers` avec `destination=acct_<prestataire>` et `source_transaction=ch_xxx`, **un transfert par paiement** (un transfert ne peut pas dépasser la charge sur laquelle il s'appuie). Avec `source_transaction`, la demande réussit toujours et le transfert part quand les fonds sont disponibles ; sans lui, un transfert supérieur au solde échoue et Stripe ne réessaie pas.

**Règles**
- **Montant transféré = ce qui revient au prestataire** d'après les lignes internes du devis (tarif contractuel : MO, consommables, pièce s'il la fournit de son stock), calculé par la même fonction de prix que le devis. Pas « total − commission ».
- **Reversement à J+X après validation de la remise en service** (fenêtre SAV), pas dès la clôture : annuler un transfert (`/transfers/{id}/reversals`) échoue si le prestataire a déjà vidé son solde. Délai court et annoncé (les techniciens se plaignent d'être payés en retard, [[brief-prd]] §1.2).
- **Clé d'idempotence par transfert** (`intervention:paiement`) : un webhook rejoué ou une tâche Convex relancée ne doit jamais payer deux fois.
- **Aucune mission proposée** tant que le compte Express du technicien n'a pas la capacité `transfers` active (contrôle à la validation de la candidature).
- **Frais et risques chez la plateforme** : frais Stripe (non rendus en cas de remboursement) et rétrofacturations ; la fonction de prix les intègre, la marge doit les couvrir.
- **TVA des deux côtés** : client facturé TTC ; transfert = montant de la facture du technicien (TTC, ou sans TVA s'il est en franchise).
- **Ne pas parler de « séquestre »** dans les CGU ni dans le marketing : le séquestre de fonds pour le compte d'un tiers est une activité réglementée. Dans le modèle à marge, la plateforme vend le service : l'argent encaissé est son chiffre d'affaires, et elle paie un sous-traitant. À valider avec l'expert-comptable (avec la TVA et DAC7).

**Conséquence pour le MVP** : le schéma coûte peu. Si les techniciens font leur inscription Stripe Express pendant leur candidature, **Stripe Connect peut entrer dans le MVP d'un mois** à la place des virements manuels.

## Points d'attention
- Paiement à la clôture : forfait encaissé tout de suite, carte enregistrée, débit du reste client absent ; si la banque exige 3-D Secure, repli par lien de paiement. Pas de préautorisation (expire en ~7 jours).
- SDK Stripe différent sur web (`@stripe/stripe-react-native` ne marche pas sur le web) → Checkout hébergé côté client web.
- ⚠️ Modèle à marge : la plateforme vend le service et facture la TVA sur le total, le technicien facture la plateforme ; effet possible sur DAC7. **À faire valider par un expert-comptable avant de coder la facturation.**

## Questions ouvertes
1. Florian a-t-il déjà livré avec Convex ? (décide Convex ou Supabase et double ou non l'estimation)
2. « 1 mois » = combien d'heures par semaine ?
3. Le Sirha est-il l'objectif réel du premier mois ?
4. Client : web seul, ou aussi app ? (écart avec le CDC à présenter)
5. Back-office dans l'app Expo ou en Next.js à part ?
6. Le prototype Claude de Léa est-il réutilisable ?
7. **Avance de trésorerie sur les pièces commandées** : la plateforme paie le fournisseur (sans compte Stripe connecté) avant que le client règle le reste à la clôture (jusqu'à 810 € pour la pièce Rational la plus chère). Encaisser la part « pièce » à l'acceptation du devis (écart avec le process) ou accepter l'avance avec un plafond ? À trancher avec Lancelot.
8. **Délai de reversement au prestataire** (J+X après validation de la remise en service) : rejoint la question ouverte du délai de paiement du prestataire.
9. Durée maximale de détention des fonds sur le solde plateforme avant transfert : à vérifier dans la documentation Stripe.

## Écarté
- Sharetribe : surtout web, modèle de transaction mal adapté au prix calculé après diagnostic et aux passages multiples.
- Bubble : workflow complexe pénible, code non exportable (contraire à la cession du code), coûts qui montent.
- Estimations du doc IA (no-code 3-6 semaines, 0-3 500 €) : supposaient une marketplace simple, sous-estiment le process de Lancelot. [[2026-11-15-feuille-de-route-ia]]
