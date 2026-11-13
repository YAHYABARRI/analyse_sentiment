"""Commande ``sentiment`` du paquet."""

import argparse
import json
import sys

from sentiment_app import __version__


def construire_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="sentiment")
    parser.add_argument("--version", action="version", version=f"sentiment-app {__version__}")
    sous_commandes = parser.add_subparsers(dest="commande", required=True)
    prediction = sous_commandes.add_parser("predict", help="classifier un avis")
    prediction.add_argument("text", help="avis à classifier")
    service = sous_commandes.add_parser("serve", help="lancer l'API")
    service.add_argument("--host", default="127.0.0.1")
    service.add_argument("--port", default=8000, type=int)
    interface = sous_commandes.add_parser("ui", help="lancer l'interface Streamlit")
    interface.add_argument("--port", default=8501, type=int)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = construire_parser().parse_args(argv)
    try:
        if args.commande == "predict":
            from api.model import SentimentClassifier

            print(json.dumps(SentimentClassifier().predict(args.text), ensure_ascii=False))
            return 0
        if args.commande == "serve":
            import uvicorn

            uvicorn.run("api.main:app", host=args.host, port=args.port)
            return 0
        from streamlit.web import cli as stcli

        from ui import app

        sys.argv = ["streamlit", "run", app.__file__, "--server.port", str(args.port)]
        return stcli.main()
    except (FileNotFoundError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
