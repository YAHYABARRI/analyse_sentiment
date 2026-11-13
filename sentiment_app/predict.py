"""Chargement configurable du modèle et prédiction unitaire."""

import os
import sys
from functools import lru_cache
from pathlib import Path
from typing import TypedDict

import joblib

RACINE = Path(__file__).resolve().parents[1]


class Prediction(TypedDict):
    label: str
    score: float


def chemin_modele() -> Path:
    """Retourne SENTIMENT_MODELE, ou le modèle produit dans le dépôt."""
    configure = os.environ.get("SENTIMENT_MODELE")
    return Path(configure) if configure else RACINE / "models" / "sentiment.joblib"


MODELE = chemin_modele()


@lru_cache(maxsize=1)
def charger_modele():
    """Charge le modèle une seule fois par processus."""
    if not MODELE.exists():
        raise FileNotFoundError(
            f"modèle introuvable : {MODELE}. Lancez python src/train.py, "
            "ou indiquez son chemin dans la variable SENTIMENT_MODELE"
        )
    return joblib.load(MODELE)


def predict(texte: str) -> Prediction:
    """Renvoie l'étiquette brute du modèle et sa confiance."""
    if not isinstance(texte, str) or not texte.strip():
        raise ValueError("texte vide")
    pipeline = charger_modele()
    etiquette = str(pipeline.predict([texte])[0])
    score = float(pipeline.predict_proba([texte]).max())
    return {"label": etiquette, "score": round(score, 4)}


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    resultat = predict(" ".join(sys.argv[1:]))
    print(f"{resultat['label']} (confiance {resultat['score']:.0%})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
