# Compte rendu - semaine 6

Le code applicatif est distribué dans une roue contenant `sentiment_app`, `api` et `ui`, sans les tests, les données ni le modèle entraîné. La version unique est `0.6.0`.

Le chemin du modèle est configurable avec `SENTIMENT_MODELE`. Hors du dépôt, la commande échoue avec un message explicite tant que cette variable ne désigne pas un fichier produit par `src/train.py`.

Commandes de contrôle : `python -m build --wheel`, `sentiment --version`, puis `sentiment predict "..."` depuis un autre dossier.
