# NetWatch — Application Web de Supervision Réseau

[![Docker Image](https://img.shields.io/badge/docker-sommer369%2Fnetwatch%3Av1-blue?logo=docker)](https://hub.docker.com/r/sommer369/netwatch)
[![Docker Image Mulix](https://img.shields.io/badge/docker-mulix%2Fnetwatch%3Av1-blue?logo=docker)](https://hub.docker.com/r/mulix/netwatch)
[![Python](https://img.shields.io/badge/python-3.12-brightgreen?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/framework-Flask-black?logo=flask)](https://flask.palletsprojects.com/)
[![AWS EC2](https://img.shields.io/badge/cloud-AWS%20EC2-orange?logo=amazon-aws)](http://13.53.48.105)

Mini-projet de Cloud Computing portant sur le développement, la conteneurisation Docker et le déploiement sur Amazon Web Services (AWS EC2).

---

## 📋 Table des matières
1. [Aperçu de l'application](#-aperçu-de-lapplication)
2. [Équipe de développement](#-équipe-de-développement)
3. [Palette graphique](#-palette-graphique)
4. [Lancement local (Python)](#-lancement-local-python)
5. [Conteneurisation Docker](#-conteneurisation-docker)
6. [Déploiement Cloud (AWS EC2)](#-déploiement-cloud-aws-ec2)
7. [Documentation PDF](#-documentation-pdf)

---

## 🚀 Aperçu de l'application

NetWatch est constituée de deux pages principales :
- **Tableau de bord (`/`)** : Métriques réseau (débit, latence, disponibilité), inventaire des équipements surveillés (Switch, Routeur, Passerelle, Serveur), statut opérationnel en direct.
- **Formulaire de rapport d'incident (`/report`)** : Saisie et soumission de rapports techniques d'incidents réseau avec priorisation et suivi immédiat.

---

## 👥 Équipe de développement

| Nom d'utilisateur | Nom complet | Rôle & Contributions |
| :--- | :--- | :--- |
| **SOMMER67** | Konaté Idrissa | Application initiale, README, Docker, AWS EC2 |
| **varanjfhueijd** | Touré Ibrahim Hermann Junior | Branche `feature/dashboard-design` : UI & Tableau de bord |
| **ametech25** | Ayahoué Mawufilimi Elie | Branche `feature/report-form` : Formulaire de rapport |

---

## 🎨 Palette graphique

Le projet intègre une charte tricolore **Bleu, Blanc, Vert** pour une expérience visuelle claire, moderne et axée sur la surveillance réseau. Consultez [PALETTE.md](file:///c:/Users/tourh/Downloads/Netwatch/PALETTE.md) pour les détails.

---

## 💻 Lancement local (Python)

```bash
# Installation des dépendances
pip install -r requirements.txt

# Lancement de l'application
python app.py
```
Accès navigateur : `http://localhost:5000`

---

## 🐳 Conteneurisation Docker

### Construction locale de l'image
```bash
docker build -t netwatch:v1 .
```

### Test local
```bash
docker run -d --name netwatch-validation -p 5002:5000 netwatch:v1
```
Accès : `http://localhost:5002`

---

## ☁️ Déploiement Cloud (AWS EC2)

```bash
# Récupération de l'image officielle Docker Hub
sudo docker pull sommer369/netwatch:v1

# Lancement du conteneur en écoute sur le port public HTTP 80
sudo docker run -d --name netwatch-container -p 80:5000 --restart unless-stopped sommer369/netwatch:v1

# Vérification
sudo docker ps
```

Accès public : [http://13.53.48.105](http://13.53.48.105)

---

## 📄 Documentation complète
Le contenu détaillé du document PDF est disponible dans [RAPPORT.md](file:///c:/Users/tourh/Downloads/Netwatch/RAPPORT.md).
