# Fiche de cadrage : Priorisation des avis négatifs

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)

Classer automatiquement les avis clients afin de présenter en priorité les retours négatifs à l'équipe de support.

## Utilisateur final (obligatoire)

Les agents du support client et leur responsable qualité.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

Des avis historiques étiquetés sont disponibles (a) et une classification locale garde un coût par requête faible (c). Une erreur (d) ne déclenche aucune action automatique : elle modifie seulement l'ordre de lecture.

## Données nécessaires et leur origine (obligatoire)

Les textes d'avis et leurs étiquettes positif ou négatif, exportés de la plateforme de relation client après anonymisation.

## Métrique de succès et seuil d'acceptation (obligatoire)

F1 macro d'au moins 0,85 et rappel de la classe négative d'au moins 0,90 sur un jeu de test séparé.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Un faux négatif retarde le traitement d'un client insatisfait ; tous les avis restent visibles et sont finalement lus par un agent.

## Risques éthiques ou de confidentialité (obligatoire)

Les avis peuvent contenir des noms ou coordonnées : ils doivent être anonymisés, avec suivi des biais de langue et de style.

## Approche écartée et pourquoi (facultatif)

