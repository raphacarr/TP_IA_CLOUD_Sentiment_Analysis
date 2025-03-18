"""
Point d'entrée principal de l'application
"""
from app.api.app import app
from app.config.prod_config import PROD_API_HOST, PROD_API_PORT, PROD_API_DEBUG
from app.config.dev_config import DEV_API_HOST, DEV_API_PORT, DEV_API_DEBUG

if __name__ == '__main__':
    # Lancement de l'API 
    print(f"Démarrage de l'API d'analyse de sentiments en mode PRODUCTION sur http://{DEV_API_HOST}:{DEV_API_PORT}")
    app.run(host=DEV_API_HOST, port=DEV_API_PORT, debug=DEV_API_DEBUG)
