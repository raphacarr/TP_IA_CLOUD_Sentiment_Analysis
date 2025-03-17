"""
Routes de l'API d'analyse de sentiments
"""
from flask import Blueprint, request, jsonify
import json

from app.model.sentiment_model import SentimentModel

# Création du blueprint pour les routes de l'API
api_bp = Blueprint('api', __name__)

# Initialisation du modèle d'analyse de sentiments
sentiment_analyzer = SentimentModel()

@api_bp.route('/')
def home():
    """Page d'accueil de l'API"""
    return jsonify({
        "message": "API d'analyse de sentiments",
        "endpoints": {
            "/predict": "POST - Analyser le sentiment d'un texte",
            "/health": "GET - Vérifier l'état de l'API"
        }
    })

@api_bp.route('/predict', methods=['POST'])
def predict():
    """Endpoint pour prédire le sentiment d'un texte"""
    try:
        # Récupérer les données JSON de la requête
        data = request.get_json()
        
        # Vérifier si le texte est présent dans les données
        if 'text' not in data:
            return jsonify({"error": "Le champ 'text' est requis"}), 400
        
        # Récupérer le texte à analyser
        text = data['text']
        
        # Faire la prédiction
        result = sentiment_analyzer.predict(text)
        
        # Convertir le résultat JSON en dictionnaire
        result_dict = json.loads(result)
        
        return jsonify(result_dict)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route('/health', methods=['GET'])
def health():
    """Endpoint pour vérifier l'état de l'API"""
    return jsonify({
        "status": "ok",
        "model_accuracy": f"{sentiment_analyzer.score * 100:.2f}%"
    })
