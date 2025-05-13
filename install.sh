#!/bin/bash
echo "[*] Installation automatique du SOC Bouclier National..."
docker-compose -f docker-compose.windows.yml up --build -d
echo "[+] Déploiement terminé. Accédez au SOC : https://localhost:8443"
