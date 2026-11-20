---
title: Appli Doctoresto - version bêta
type: project
status: active
created: 2026-11-20
updated: 2026-11-20
review_by: 2026-12-20
importance: 5
sources: ["[[2026-10-13-cadrage-doctoresto]]", "[[2026-10-19-cr-reunion]]", "[[2026-10-26-odj-reunion]]", "[[2026-11-02-maquette-ecrans-v6]]"]
summary: Bêta de l'appli restaurateur et technicien pour avril 2027, testée sur tout Paris, limitée à quelques corps de métier CHR ; maquette v6 faite le 2026-11-02.
---
# Appli Doctoresto, version bêta
Responsable : Florian ([[me]]). Échéance : avant avril 2027 (CR 2026-10-19).
Statut : maquette des écrans v6 faite (2026-11-02). Budget de l'appli à faire.

## Périmètre
- Bêta sur tout Paris, quelques corps de métier CHR seulement. Le coût dépend entièrement des fonctionnalités retenues. (CR 2026-10-19)
- Équipements au lancement : four, pétrin, diviseuse, froid. (cadrage, 2026-10-13)

## Parcours client en 6 étapes (cadrage)
1. Demande : le boulanger déclare la panne (machine, symptôme, photo).
2. Qualification : l'opérateur confirme l'équipement et le type de panne ; l'appli suggère pièces et outillage.
3. Affectation : technicien choisi selon compétence, distance, disponibilité ; vérification de la pièce dans son véhicule ; itinéraire envoyé.
4. Préparation : ordre de travail avec historique et documentation de la machine.
5. Intervention : arrivée horodatée, consignes d'hygiène, photos avant, check-list, photos après.
6. Clôture : signature, rapport PDF, facturation, historique mis à jour.

## Fonctions
| Fonction | Statut | Commentaire |
| --- | --- | --- |
| Demande en ligne | Lancement | sans création de compte pour la première demande (ODJ 26/10) |
| Affectation du technicien | Lancement | manuelle au départ |
| Ordre de travail mobile | Lancement | historique et documentation machine |
| Photos, check-list, signature | Lancement | |
| Rapport PDF et facturation | Lancement | |
| Mode hors-ligne | Lancement | labos mal couverts en réseau |
| Affectation automatique | Plus tard | quand il y aura assez de techniciens |
| Diagnostic IA (photo) | Plus tard | nécessite un historique de pannes ; champ photo non obligatoire |
| Stock embarqué | Plus tard | |
| GPS temps réel | Non prioritaire | Waze suffit |

## Inspirations UX (ODJ 2026-10-26, point 14)
Parcours inspiré de MesDépanneurs, instinctif, sur le modèle Uber ou Airbnb : soigner à la fois l'appli restaurant et l'appli technicien. La création de compte est trop longue partout.

## Maquette v6 (2026-11-02)
23 écrans en thème clair et sombre : Marie (Boulangerie Martin, Nice) côté restaurateur, Karim côté technicien. Détail : [[2026-11-02-maquette-ecrans-v6]].

## Prochaines étapes
- Budget des premiers coûts de l'appli, avec le recensement de toutes les heures de dev et de visuels (bilan, valorisation). (ODJ 26/10, point 12)
- Choisir les corps de métier de la bêta.

## Open questions
- Ville de démo (Nice dans la maquette) et zone de lancement (Paris dans le CR) : à aligner.
