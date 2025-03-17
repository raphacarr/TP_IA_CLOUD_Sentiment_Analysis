"""
Modèle d'analyse de sentiments
"""
import warnings
warnings.simplefilter('ignore')

import pandas
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

from app.config.config import DATASET_PATH, MODEL_SEPARATOR, TEST_SIZE, RANDOM_STATE, MAX_DEPTH, N_ESTIMATORS
from app.utils.text_preprocessing import clean_text_for_sentiment

class SentimentModel:
    """
    Classe pour l'analyse de sentiments
    """
    def __init__(self):
        # Initialisation
        self.dataset = pandas.read_csv(DATASET_PATH, names=['sentence', 'label'], sep=MODEL_SEPARATOR)
        self.vectorizer = None
        self.score = None
        self.model = None
        self.train()
        
    def train(self):
        """
        Entraîne le modèle d'analyse de sentiments
        """
        # Séparation des données et des étiquettes
        sentences = self.dataset['sentence'].values
        y = self.dataset['label'].values

        # Prétraitement des données
        sentences = [clean_text_for_sentiment(sentence) for sentence in sentences]

        # Division des données en ensembles d'entraînement et de test
        sentences_train, sentences_test, y_train, y_test = train_test_split(
            sentences, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
        )

        # Vectorisation des données d'entraînement et de test
        self.vectorizer = CountVectorizer()
        self.vectorizer.fit(sentences_train)
        X_train = self.vectorizer.transform(sentences_train)
        X_test = self.vectorizer.transform(sentences_test)

        # Initialisation et entraînement du modèle
        self.model = XGBClassifier(max_depth=MAX_DEPTH, n_estimators=N_ESTIMATORS)
        self.model.fit(X_train, y_train)

        # Affichage des paramètres du modèle
        print(self.model)
        
        # Prédictions sur les données de test
        y_pred = self.model.predict(X_test)
        predictions = [round(value) for value in y_pred]

        # Évaluation des prédictions
        self.score = accuracy_score(y_test, predictions)
        print(f"Précision: {self.score * 100.0:.2f}%")
    
    def predict(self, text):
        """
        Prédit le sentiment d'un texte
        
        Args:
            text (str): Texte à analyser
            
        Returns:
            str: Résultat de l'analyse au format JSON
        """
        # Prétraitement du texte
        cleaned_text = clean_text_for_sentiment(text)
        
        # Vectorisation et prédiction
        result = self.vectorizer.transform([cleaned_text])
        result = self.model.predict(result)

        # Interprétation du résultat
        if str(result[0]) == "0":
            sentiment = "NEGATIVE"
        elif str(result[0]) == "1":
            sentiment = "POSITIVE"

        # Retour du résultat au format JSON
        return json.dumps({"sentiment": sentiment, "text": text})


# Test du modèle si le fichier est exécuté directement
if __name__ == "__main__":
    model = SentimentModel()
    print(model.predict("Depuis ce matin votre application ne marche pas, je n'arrive pas à déverrouiller ma voiture."))
    print(model.predict("j'ai adore la prestation"))
