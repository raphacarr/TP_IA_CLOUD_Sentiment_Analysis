"""
Tests pour l'API d'analyse de sentiments
"""
import requests
import json
import sys
import os

# Ajouter le répertoire parent au chemin de recherche des modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.config.config import API_PORT

def test_api():
    """Test de l'API d'analyse de sentiments"""
    
    # URL de base de l'API
    base_url = f"http://localhost:{API_PORT}"
    
    # Test de l'endpoint /health
    print("Test de l'endpoint /health...")
    health_response = requests.get(f"{base_url}/health")
    print(f"Statut: {health_response.status_code}")
    print(f"Réponse: {json.dumps(health_response.json(), indent=2, ensure_ascii=False)}")
    print()
    
    # Test de l'endpoint /predict avec un sentiment positif
    print("Test de l'endpoint /predict avec un sentiment positif...")
    positive_text = "J'ai adoré la prestation, c'était vraiment excellent !"
    positive_response = requests.post(
        f"{base_url}/predict",
        json={"text": positive_text},
        headers={"Content-Type": "application/json"}
    )
    print(f"Statut: {positive_response.status_code}")
    print(f"Réponse: {json.dumps(positive_response.json(), indent=2, ensure_ascii=False)}")
    print()
    
    # Test de l'endpoint /predict avec un sentiment négatif
    print("Test de l'endpoint /predict avec un sentiment négatif...")
    negative_text = "Depuis ce matin votre application ne marche pas, je n'arrive pas à déverrouiller ma voiture."
    negative_response = requests.post(
        f"{base_url}/predict",
        json={"text": negative_text},
        headers={"Content-Type": "application/json"}
    )
    print(f"Statut: {negative_response.status_code}")
    print(f"Réponse: {json.dumps(negative_response.json(), indent=2, ensure_ascii=False)}")

if __name__ == "__main__":
    print("Test de l'API d'analyse de sentiments")
    print(f"Assurez-vous que l'API est en cours d'exécution sur http://localhost:{API_PORT}")
    print("Appuyez sur Entrée pour continuer...")
    input()
    
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print(f"Erreur de connexion: Assurez-vous que l'API est en cours d'exécution sur http://localhost:{API_PORT}")
