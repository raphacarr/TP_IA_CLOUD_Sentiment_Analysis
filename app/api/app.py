"""
Application Flask pour l'API d'analyse de sentiments
"""
from flask import Flask
from flask_cors import CORS

from app.api.routes import api_bp
from app.config.config import API_HOST, API_PORT, API_DEBUG

def create_app():
    """
    Crée et configure l'application Flask
    
    Returns:
        Flask: Application Flask configurée
    """
    # Création de l'application Flask
    app = Flask(__name__)
    
    # Activation de CORS pour permettre les requêtes depuis d'autres domaines
    CORS(app)
    
    # Enregistrement des blueprints
    app.register_blueprint(api_bp)
    
    return app

# Création de l'application
app = create_app()

if __name__ == '__main__':
    # Lancement de l'API
    print(f"Démarrage de l'API d'analyse de sentiments sur http://localhost:{API_PORT}")
    app.run(host=API_HOST, port=API_PORT, debug=API_DEBUG)
