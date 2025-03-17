@echo off
echo ===== Arrêt et nettoyage des conteneurs Docker =====

echo.
echo 1. Arrêt du conteneur sentiment-api...
docker stop sentiment-api

echo.
echo 2. Suppression du conteneur sentiment-api...
docker rm sentiment-api

echo.
echo ===== Nettoyage terminé =====
