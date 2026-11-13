import os
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]


def test_version_unique():
    from sentiment_app import __version__

    assert __version__ == "0.6.0"


def test_le_modele_se_place_ou_l_on_veut(monkeypatch, tmp_path):
    chemin = tmp_path / "modele.joblib"
    monkeypatch.setenv("SENTIMENT_MODELE", str(chemin))
    from sentiment_app.predict import chemin_modele

    assert chemin_modele() == chemin


def test_l_api_ne_bricole_plus_le_chemin_de_python():
    source = (RACINE / "api" / "model.py").read_text(encoding="utf-8")
    assert "sys.path" not in source
    assert "sentiment_app.predict" in source


def test_commande_affiche_la_version():
    resultat = subprocess.run(
        [sys.executable, "-m", "sentiment_app", "--version"],
        cwd=RACINE,
        capture_output=True,
        text=True,
        check=True,
    )
    assert resultat.stdout.strip() == "sentiment-app 0.6.0"


def test_commande_prediction_json(monkeypatch):
    if not (RACINE / "models" / "sentiment.joblib").exists():
        pytest.skip("modèle absent")
    env = os.environ.copy()
    env["SENTIMENT_MODELE"] = str(RACINE / "models" / "sentiment.joblib")
    resultat = subprocess.run(
        [
            sys.executable,
            "-m",
            "sentiment_app",
            "predict",
            "Livraison rapide, produit conforme, très satisfait",
        ],
        cwd=RACINE,
        env=env,
        capture_output=True,
        text=True,
        check=True,
    )
    assert '"label": "POSITIVE"' in resultat.stdout


def test_dependance_scikit_learn_epinglee():
    texte = (RACINE / "pyproject.toml").read_text(encoding="utf-8")
    assert '"scikit-learn>=1.5,<1.6"' in texte
