# API d'Analyse de Sentiments

Cette API permet d'analyser le sentiment (positif ou négatif) d'un texte en français.

## Structure du Projet

```
├── app/                      # Dossier principal de l'application
│   ├── api/                  # Code de l'API
│   │   ├── app.py            # Application Flask
│   │   ├── routes.py         # Routes de l'API
│   │   └── __init__.py
│   ├── config/               # Configuration
│   │   ├── config.py         # Configuration générale
│   │   ├── dev_config.py     # Configuration de développement
│   │   ├── prod_config.py    # Configuration de production
│   │   └── __init__.py
│   ├── model/                # Modèle d'analyse de sentiments
│   │   ├── data/             # Données
│   │   │   └── dataset.txt   # Dataset d'entraînement
│   │   ├── sentiment_model.py # Classe du modèle
│   │   └── __init__.py
│   ├── scripts/              # Scripts utilitaires
│   │   ├── run_dev.py        # Lancement en mode développement
│   │   └── run_prod.py       # Lancement en mode production
│   ├── static/               # Fichiers statiques (si nécessaire)
│   ├── tests/                # Tests
│   │   ├── test_api.py       # Tests de l'API
│   │   └── __init__.py
│   ├── utils/                # Utilitaires
│   │   ├── text_preprocessing.py # Prétraitement de texte
│   │   └── __init__.py
│   └── __init__.py
├── run.py                    # Point d'entrée principal
├── requirements.txt          # Dépendances
├── Dockerfile                # Configuration Docker
├── docker-compose.yml        # Configuration Docker Compose
├── docker_build_run.bat      # Script pour construire et exécuter avec Docker
├── docker_stop_clean.bat     # Script pour arrêter et nettoyer les conteneurs Docker
└── README.md                 # Documentation
```

## Installation

### Méthode 1 : Installation locale

1. Installer les dépendances :

```bash
pip install -r requirements.txt
```

2. Démarrer l'API :

#### Mode développement

```bash
python app/scripts/run_dev.py
```

#### Mode production

```bash
python run.py
```

L'API sera accessible à l'adresse : http://localhost:5000

### Méthode 2 : Utilisation avec Docker

#### Prérequis
- Docker installé sur votre machine
- Docker Compose installé sur votre machine

#### Option 1 : Utilisation de Docker Compose (recommandé)

1. Construire et démarrer le conteneur :

```bash
docker-compose up -d
```

2. Pour arrêter le conteneur :

```bash
docker-compose down
```

#### Option 2 : Utilisation de Docker sans Docker Compose

1. Construire l'image Docker :

```bash
docker build -t sentiment-analysis-api .
```

2. Exécuter le conteneur :

```bash
docker run -p 5000:5000 -e PORT=5000 -e DEBUG=False sentiment-analysis-api
```

L'API sera accessible à l'adresse : http://localhost:5000

#### Option 3 : Utilisation des scripts batch (Windows)

1. Pour construire et démarrer le conteneur :

```bash
docker_build_run.bat
```

2. Pour arrêter et nettoyer le conteneur :

```bash
docker_stop_clean.bat
```

## Endpoints

### GET /

Page d'accueil avec la documentation des endpoints disponibles.

### POST /predict

Analyse le sentiment d'un texte.

**Requête** :
```json
{
    "text": "Votre texte à analyser ici"
}
```

**Réponse** :
```json
{
    "sentiment": "POSITIVE", // ou "NEGATIVE"
    "text": "Votre texte à analyser ici"
}
```

### GET /health

Vérifie l'état de l'API et affiche la précision du modèle.

**Réponse** :
```json
{
    "status": "ok",
    "model_accuracy": "85.00%"
}
```

## Exemple d'utilisation avec cURL

```bash
curl -X POST http://localhost:5000/predict \
    -H "Content-Type: application/json" \
    -d '{"text": "J'ai adoré la prestation"}'
```

## Exemple d'utilisation avec Python

```python
import requests
import json

url = "http://localhost:5000/predict"
data = {"text": "J'ai adoré la prestation"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)
result = response.json()
print(result)
```

## Utilisation avec Postman

1. Créez une nouvelle requête POST vers http://localhost:5000/predict
2. Dans l'onglet "Body", sélectionnez "raw" et "JSON"
3. Entrez le corps de la requête :
```json
{
    "text": "J'ai adoré la prestation"
}
```
4. Cliquez sur "Send" pour envoyer la requête

## Tests

Pour exécuter les tests de l'API :

```bash
python app/tests/test_api.py
```

## Développement

Pour ajouter de nouvelles fonctionnalités ou améliorer le modèle, vous pouvez :

1. Modifier le modèle dans `app/model/sentiment_model.py`
2. Ajouter de nouvelles routes dans `app/api/routes.py`
3. Ajouter des utilitaires dans `app/utils/`
4. Mettre à jour la configuration dans `app/config/`
