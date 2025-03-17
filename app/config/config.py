"""
Configuration de l'application
"""
import os

# Chemins des fichiers
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'model', 'data')
DATASET_PATH = os.path.join(DATA_DIR, 'dataset.txt')

# Configuration de l'API
API_HOST = '0.0.0.0'
API_PORT = int(os.environ.get('PORT', 5000))
API_DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# Configuration du modèle
MODEL_SEPARATOR = '   '
TEST_SIZE = 0.25
RANDOM_STATE = 1000
MAX_DEPTH = 2
N_ESTIMATORS = 30
