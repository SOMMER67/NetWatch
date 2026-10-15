# NetWatch — Plateforme de supervision réseau

## 1. Présentation du projet

NetWatch est une application web développée avec Python et Flask dans le cadre d'un mini-projet pédagogique consacré à la conteneurisation et au déploiement d'applications dans le cloud.

Elle permet de consulter un tableau de bord présentant des équipements réseau simulés et de signaler des incidents.

## 2. Liens du projet

* **Application en ligne :** http://13.53.48.105:5001
* **Code source GitHub :** https://github.com/SOMMER67/NetWatch
* **Image Docker Hub :** https://hub.docker.com/r/sommer369/netwatch

## 3. Fonctionnalités

* Tableau de bord avec des statistiques sur les équipements.
* Consultation des équipements réseau simulés.
* Page de présentation du projet.
* Formulaire de signalement d'incidents.
* Messages de confirmation après un signalement.
* Interface web en HTML et CSS.

**Remarque :** les équipements affichés sont des données de démonstration. L'application ne réalise pas encore de supervision réseau réelle.

## 4. Technologies utilisées

* Python 3.12
* Flask
* HTML5 et CSS3
* Git et GitHub
* Docker
* Docker Hub
* AWS EC2

## 5. Structure du projet

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

## 6. Installation et lancement en local

### Prérequis

* Python installé.
* Git installé.
* Docker Desktop installé pour les tests avec Docker.

### Créer un environnement virtuel

```powershell
python -m venv .venv
```

### Activer l'environnement virtuel sous Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### Installer les dépendances

```powershell
pip install -r requirements.txt
```

### Lancer l'application Flask

```powershell
python app.py
```

Ouvrir ensuite http://127.0.0.1:5000 dans le navigateur.

## 7. Utilisation avec Docker

### Construire l'image

Depuis le dossier du projet :

```powershell
docker build -t netwatch:v1 .
```

### Lancer un conteneur de test

```powershell
docker run -d --name netwatch-test -p 5001:5000 netwatch:v1
```

### Accéder à l'application

Ouvrir http://localhost:5001 dans le navigateur.

### Vérifier les conteneurs

```powershell
docker ps
```

### Consulter les journaux

```powershell
docker logs netwatch-test
```

### Arrêter et supprimer le conteneur de test

```powershell
docker stop netwatch-test
docker rm netwatch-test
```

## 8. Publication de l'image Docker

L'image NetWatch v1 est publiée sur Docker Hub.

Pour la télécharger :

```bash
docker pull sommer369/netwatch:v1
```

## 9. Déploiement sur AWS EC2

L'application est déployée sur une instance AWS EC2 sous Ubuntu.

### Télécharger l'image sur le serveur

```bash
sudo docker pull sommer369/netwatch:v1
```

### Lancer le conteneur

```bash
sudo docker run -d --name netwatch-container -p 5001:5000 --restart unless-stopped sommer369/netwatch:v1
```

### Vérifier le conteneur

```bash
sudo docker ps
```

### Accéder à l'application depuis Internet

Ouvrir :

http://13.53.48.105:5001

Le port TCP 5001 doit être autorisé dans les règles entrantes du groupe de sécurité AWS.

## 10. Limites actuelles

* Les données des équipements sont simulées.
* Les signalements sont conservés temporairement en mémoire.
* Les signalements disparaissent au redémarrage de l'application.
* La connexion à de véritables équipements réseau n'est pas encore implémentée.

## 11. Équipe

Projet réalisé dans le cadre d'un mini-projet pédagogique.

Les membres de l'équipe et leurs contributions doivent être renseignés avant la remise finale du projet.

## 12. Améliorations possibles

* Connecter l'application à de véritables équipements réseau.
* Ajouter une base de données pour conserver les signalements.
* Mettre en place une authentification.
* Ajouter des tests automatisés.
* Améliorer la surveillance et la journalisation.

---

**NetWatch — Projet pédagogique de supervision réseau.**
