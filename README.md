# NetWatch — Plateforme de supervision réseau

## 1. Présentation du projet

NetWatch est une application web développée avec Python et Flask dans le cadre d'un mini-projet pédagogique consacré à la conteneurisation et au déploiement d'applications dans le cloud.

Elle propose une interface permettant de consulter l'état simulé d'équipements réseau et de signaler des incidents.

## 2. Fonctionnalités

- Tableau de bord avec des statistiques sur les équipements.
- Consultation des équipements réseau simulés.
- Page de présentation du projet.
- Formulaire de signalement d'incidents.
- Messages de confirmation après un signalement.
- Interface web en HTML et CSS.

**Remarque :** les équipements affichés sont des données de démonstration. L'application ne réalise pas encore de supervision réseau réelle.

## 3. Technologies utilisées

- Python
- Flask
- HTML5 et CSS3
- Git et GitHub
- Docker
- AWS EC2 pour le déploiement prévu

## 4. Structure du projet

```text
NetWatch/
├── app.py
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── about.html
│   └── report.html
└── static/
    └── css/
        └── style.css
```

## 5. Installation et lancement en local

### Prérequis

- Python installé.
- Git installé.

### Créer un environnement virtuel sous Windows

```powershell
python -m venv .venv
```

### Activer l'environnement virtuel

```powershell
.\.venv\Scripts\Activate.ps1
```

### Installer les dépendances

```powershell
pip install -r requirements.txt
```

### Lancer l'application

```powershell
python app.py
```

Ouvrir ensuite http://127.0.0.1:5000 dans le navigateur.

## 6. Utilisation avec Docker

### Prérequis

Docker Desktop doit être installé et démarré.

### Construire l'image

Depuis le dossier du projet :

```powershell
docker build -t netwatch:v1 .
```

### Lancer un conteneur de test

```powershell
docker run -d --name netwatch-test -p 5001:5000 netwatch:v1
```

Si le nom du conteneur est déjà utilisé, vérifier les conteneurs existants avec :

```powershell
docker ps -a
```

### Accéder à l'application

Ouvrir http://localhost:5001 dans le navigateur.

### Vérifier les conteneurs en cours d'exécution

```powershell
docker ps
```

### Consulter les journaux

```powershell
docker logs netwatch-test
```

### Arrêter le conteneur

```powershell
docker stop netwatch-test
```

### Supprimer le conteneur arrêté

```powershell
docker rm netwatch-test
```

## 7. Limites actuelles

- Les données des équipements sont simulées.
- Les signalements sont conservés temporairement en mémoire.
- Les signalements disparaissent au redémarrage de l'application.
- La connexion à de véritables équipements réseau n'est pas encore implémentée.

## 8. Équipe

Projet réalisé dans le cadre d'un mini-projet pédagogique.

Les membres de l'équipe et leurs contributions seront documentés au fur et à mesure de l'avancement.

## 9. Évolutions prévues

- Publication du code sur GitHub.
- Publication de l'image sur Docker Hub.
- Déploiement sur une instance AWS EC2.
- Accès à l'application depuis Internet.
- Amélioration de la documentation et des tests.

---

**NetWatch — Projet pédagogique de supervision réseau.**
