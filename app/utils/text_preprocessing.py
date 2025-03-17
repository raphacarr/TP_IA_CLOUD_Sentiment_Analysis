"""
Fonctions utilitaires pour le prétraitement de texte
"""
import unidecode
import re

def normalize_text(text):
    """
    Normalise un texte en supprimant les accents et les caractères spéciaux
    
    Args:
        text (str): Texte à normaliser
        
    Returns:
        str: Texte normalisé
    """
    # Suppression des accents
    text = unidecode.unidecode(text)
    
    # Conversion en minuscules
    text = text.lower()
    
    # Suppression des caractères spéciaux
    text = re.sub(r'[^\w\s]', '', text)
    
    # Suppression des espaces multiples
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def clean_text_for_sentiment(text):
    """
    Nettoie un texte pour l'analyse de sentiments
    
    Args:
        text (str): Texte à nettoyer
        
    Returns:
        str: Texte nettoyé
    """
    # Normalisation du texte
    text = normalize_text(text)
    
    # Suppression des mots vides (à implémenter si nécessaire)
    
    return text
