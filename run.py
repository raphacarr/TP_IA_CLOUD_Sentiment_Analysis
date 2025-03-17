"""
Point d'entrée principal de l'application
"""
from app.api.app import app
from app.config.prod_config import PROD_API_HOST, PROD_API_PORT, PROD_API_DEBUG

if __name__ == '__main__':
    # Lancement de l'API en mode production
    print(f"Démarrage de l'API d'analyse de sentiments en mode PRODUCTION sur http://{PROD_API_HOST}:{PROD_API_PORT}")
    app.run(host=PROD_API_HOST, port=PROD_API_PORT, debug=PROD_API_DEBUG)
