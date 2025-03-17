"""
Script pour lancer l'application en mode production
"""
import os
import sys

# Ajouter le répertoire parent au chemin de recherche des modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.api.app import app
from app.config.prod_config import PROD_API_HOST, PROD_API_PORT, PROD_API_DEBUG

if __name__ == '__main__':
    # Lancement de l'API en mode production
    print(f"Démarrage de l'API d'analyse de sentiments en mode PRODUCTION sur http://{PROD_API_HOST}:{PROD_API_PORT}")
    app.run(host=PROD_API_HOST, port=PROD_API_PORT, debug=PROD_API_DEBUG)
