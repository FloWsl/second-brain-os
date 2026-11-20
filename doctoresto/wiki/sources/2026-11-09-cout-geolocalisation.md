---
title: Coûts de la géolocalisation en direct
type: source
status: active
created: 2026-11-20
updated: 2026-11-20
importance: 3
drive_id: 1Cw2Sa2qGLVWWBjCv0lBj54OopMoINaCHGXIGI957tcg
summary: Suivi façon Uber : 0 à 50 € par mois au lancement ; GPS et carte mobile gratuits ; payant : itinéraire et géocodage Google au-delà de 10 000 appels par mois ; développement du suivi chez un freelance : 1 500 à 5 000 €.
---
# Coûts de la géolocalisation en direct
Source : Google Drive, DEVELOPPEMENT/CAHIER DES CHARGES (doc de Léa, 2026-11-09). Lien : https://drive.google.com/open?id=1Cw2Sa2qGLVWWBjCv0lBj54OopMoINaCHGXIGI957tcg
Importée le 2026-11-20.

- Gratuit : GPS natif, Google Maps SDK mobile, temps réel via Firebase ou Supabase (0 à 25 € par mois au début).
- Payant (Google, quotas par service depuis mars 2025) : Routes et géocodage, 10 000 appels gratuits par mois puis 5 $ les 1 000 ; carte web 7 $ les 1 000.
- Simulation avec 500 interventions par mois : recalcul toutes les 30 s ≈ 20 000 appels ≈ 50 $ ; toutes les 2 min ≈ 5 000 appels = 0 $. Levier : mettre à jour l'heure d'arrivée toutes les 1 à 2 minutes seulement.
- Dev : 1 500 à 5 000 € chez un freelance (ordre de grandeur). Mapbox : sans intérêt à ce stade.
Le CR du 9/11 a sorti le suivi en temps réel de la bêta. → [[app-beta]]
