FROM python:3.12-slim

# Répertoire de travail
WORKDIR /app

# Installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code applicatif, des templates et des fichiers statiques
COPY . .

# Port exposé documenté
EXPOSE 5000

# Variables d'environnement Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV PYTHONUNBUFFERED=1

# Démarrage de l'application sur toutes les interfaces du conteneur
CMD ["python", "app.py"]
