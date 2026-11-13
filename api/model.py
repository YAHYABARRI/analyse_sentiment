"""Raccord entre l'API et le modèle entraîné au TP2.

L'API n'entraîne rien et ne connaît pas scikit-learn : elle appelle la fonction
predict() de src/predict.py, qui charge models/sentiment.joblib une seule fois.
"""
import os
from typing import TypedDict

from api.schemas import Label
from sentiment_app.predict import charger_modele
from sentiment_app.predict import predict as _predict

SEUIL_ABSTENTION = float(os.environ.get("SEUIL_ABSTENTION", "0.60"))


class PredictionAPI(TypedDict):
    label: Label
    score: float
    text: str


class SentimentClassifier:
    """Enveloppe du modèle TP2 avec l'interface attendue par l'API."""

    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"

    def __init__(self) -> None:
        charger_modele()  # échoue immédiatement si le joblib manque : on ne démarre pas sans modèle

    def predict(self, text: str) -> PredictionAPI:
        """Renvoie {'label': 'POSITIVE'|'NEGATIVE', 'score': float, 'text': aperçu}."""
        r = _predict(text)  # lève ValueError si le texte est vide
        if r["score"] < SEUIL_ABSTENTION:
            label: Label = "INDETERMINE"
        else:
            correspondance: dict[str, Label] = {"positive": "POSITIVE", "negative": "NEGATIVE"}
            try:
                label = correspondance[r["label"]]
            except KeyError as exc:
                raise ValueError(f"étiquette inconnue: {r['label']}") from exc
        return {"label": label, "score": r["score"], "text": text[:100]}


def load_model() -> SentimentClassifier:
    """Construit le classifier (le cache de chargement est dans src/predict.py)."""
    return SentimentClassifier()
