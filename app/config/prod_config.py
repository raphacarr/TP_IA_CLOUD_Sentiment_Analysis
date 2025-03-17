"""
Configuration pour l'environnement de production
"""
import os
from app.config.config import BASE_DIR

# Configuration de l'API en production
PROD_API_HOST = '0.0.0.0'
PROD_API_PORT = int(os.environ.get('PORT', 5000))
PROD_API_DEBUG = False

# Chemins des fichiers pour la production
PROD_DATA_DIR = os.path.join(BASE_DIR, 'model', 'data')
PROD_DATASET_PATH = os.path.join(PROD_DATA_DIR, 'dataset.txt')

# Configuration du modèle pour la production
PROD_MODEL_SEPARATOR = '   '
PROD_TEST_SIZE = 0.25
PROD_RANDOM_STATE = 1000
PROD_MAX_DEPTH = 2
PROD_N_ESTIMATORS = 30
