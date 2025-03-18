"""
Configuration pour l'environnement de développement
"""
import os
from app.config.config import BASE_DIR

# Configuration de l'API en développement
DEV_API_HOST = '0.0.0.0'
DEV_API_PORT = 5000
DEV_API_DEBUG = True

# Chemins des fichiers pour le développement
DEV_DATA_DIR = os.path.join(BASE_DIR, 'model', 'data')
DEV_DATASET_PATH = os.path.join(DEV_DATA_DIR, 'dataset.txt')

# Configuration du modèle pour le développement
DEV_MODEL_SEPARATOR = '   '
DEV_TEST_SIZE = 0.25
DEV_RANDOM_STATE = 1000
DEV_MAX_DEPTH = 2
DEV_N_ESTIMATORS = 30
