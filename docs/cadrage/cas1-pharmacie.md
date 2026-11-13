# Fiche de cadrage : Ordonnances incomplètes en pharmacie

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)

Détecter avant délivrance les ordonnances incomplètes afin que le pharmacien demande les informations manquantes.

## Utilisateur final (obligatoire)

Le pharmacien ou le préparateur qui contrôle l'ordonnance au comptoir.

## Approche retenue (obligatoire)

Cocher une seule case :

- [x] Règles métier
- [ ] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

Les champs obligatoires sont définis par des règles vérifiables (b), sans besoin de données étiquetées (a). La conséquence d'une erreur (d) peut être médicale, donc la décision finale reste humaine.

## Données nécessaires et leur origine (obligatoire)

Les champs de l'ordonnance numérisée et la liste officielle des mentions obligatoires fournie par la pharmacie.

## Métrique de succès et seuil d'acceptation (obligatoire)

Rappel supérieur à 99 % sur les ordonnances incomplètes, avec moins de 5 % de faux positifs.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Un oubli peut conduire à une délivrance dangereuse ; chaque alerte et chaque absence d'alerte sont validées par le pharmacien.

## Risques éthiques ou de confidentialité (obligatoire)

Les ordonnances contiennent des données de santé sensibles : chiffrement, accès limité et durée de conservation minimale sont requis.

## Approche écartée et pourquoi (facultatif)

