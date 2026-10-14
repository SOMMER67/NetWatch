# NetWatch — Plateforme de supervision réseau

## 1. Présentation du projet

NetWatch est une application web développée avec Python et Flask dans le cadre d'un mini-projet pédagogique consacré à la conteneurisation et au déploiement d'applications dans le cloud.

Son objectif est de proposer une interface simple permettant de consulter l'état d'équipements réseau et de signaler des incidents.

## 2. Fonctionnalités

* Tableau de bord présentant des statistiques sur les équipements.
* Consultation de la liste des équipements réseau.
* Page de présentation du projet.
* Formulaire de signalement d'incidents.
* Messages de confirmation après l'envoi d'un signalement.
* Interface web utilisant HTML et CSS.

**Remarque :** les équipements affichés sont des données de démonstration. L'application ne réalise pas encore de supervision réseau réelle.

## 3. Technologies utilisées

* Python
* Flask
* HTML5
* CSS3
* Git et GitHub
* Docker
* AWS EC2 (déploiement prévu dans le cadre du projet)

## 4. Structure du projet

```text
NetWatch/
├── app.py
├── .gitignore
├── README.md
├── requirements.txt
├── Dockerfile
├── templates/
│   ├── index.html
│   ├── about.html
│   └── report.html
└── static/
    └── css/
        └── style.css
```

Certains fichiers, notamment `requirements.txt` et `Dockerfile`, seront ajoutés lors des prochaines étapes.

## 5. Installation et lancement en local

### Prérequis

* Python installé.
* Git installé.

### Cloner le projet

```bash
git clone <URL_DU_DEPOT_GITHUB>
cd NetWatch
```

Remplacez `<URL_DU_DEPOT_GITHUB>` par l'adresse réelle du dépôt GitHub.

### Créer un environnement virtuel

Sous Windows :

```powershell
python -m venv .venv
```

### Activer l'environnement virtuel

```powershell
.\.venv\Scripts\Activate.ps1
```

### Installer les dépendances

Après la création du fichier `requirements.txt` :

```powershell
pip install -r requirements.txt
```

### Lancer l'application

```powershell
python app.py
```

Ouvrez ensuite votre navigateur à l'adresse :

http://127.0.0.1:5000

## 6. Limites actuelles

* Les données des équipements sont simulées.
* Les signalements sont conservés temporairement en mémoire.
* Les signalements disparaissent lorsque l'application redémarre.
* La connexion à de véritables équipements réseau n'est pas encore implémentée.

## 7. Équipe

Projet réalisé dans le cadre d'un mini-projet pédagogique.

Les membres de l'équipe et leurs contributions seront documentés au fur et à mesure de l'avancement.

## 8. Évolutions prévues

* Conteneurisation de l'application avec Docker.
* Publication de l'image sur Docker Hub.
* Déploiement sur une instance AWS EC2.
* Accès à l'application depuis Internet.
* Amélioration de la documentation et des tests.

---

**NetWatch — Projet pédagogique de supervision réseau.**
