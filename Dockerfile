# Utiliser une image officielle de Python comme base
FROM python:3.12-slim

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python nécessaires
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application et ses ressources
COPY app.py .
COPY templates/ templates/
COPY static/ static/

# Définir la variable d'environnement du port utilisé par Flask
ENV PORT=5000

# Indiquer que l'application utilise le port 5000
EXPOSE 5000

# Lancer Flask en écoutant sur toutes les interfaces réseau
CMD ["python", "-c", "from app import app; app.run(host='0.0.0.0', port=5000)"]