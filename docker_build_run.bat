@echo off
echo ===== Construction et déploiement de l'API d'analyse de sentiments avec Docker =====

echo.
echo 1. Construction de l'image Docker...
docker build -t sentiment-analysis-api .

echo.
echo 2. Démarrage du conteneur...
docker run -d -p 5000:5000 -e PORT=5000 -e DEBUG=False --name sentiment-api sentiment-analysis-api

echo.
echo ===== Déploiement terminé =====
echo L'API est accessible à l'adresse : http://localhost:5000
echo.
echo Pour arrêter le conteneur, exécutez : docker stop sentiment-api
echo Pour supprimer le conteneur, exécutez : docker rm sentiment-api
echo.
