"""
Script pour lancer l'application en mode développement
"""
import os
import sys

# Ajouter le répertoire parent au chemin de recherche des modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.api.app import app
from app.config.dev_config import DEV_API_HOST, DEV_API_PORT, DEV_API_DEBUG

if __name__ == '__main__':
    # Lancement de l'API en mode développement
    print(f"Démarrage de l'API d'analyse de sentiments en mode DÉVELOPPEMENT sur http://{DEV_API_HOST}:{DEV_API_PORT}")
    app.run(host=DEV_API_HOST, port=DEV_API_PORT, debug=DEV_API_DEBUG)
