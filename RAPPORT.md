# NETWATCH — Mini-projet de Cloud Computing

**Développement, conteneurisation et déploiement d’une application web sur AWS EC2**

---

| Propriété | Valeur |
| :--- | :--- |
| **Équipe** | 3 membres |
| **Dépôt GitHub** | [github.com/SOMMER67/NetWatch](https://github.com/SOMMER67/NetWatch) |
| **Image Docker Hub** | [hub.docker.com/r/sommer369/netwatch](https://hub.docker.com/r/sommer369/netwatch) |
| **Application publique** | [http://13.53.48.105](http://13.53.48.105) |
| **Date de remise prévue** | 20 octobre 2026 |

*Document de synthèse des livrables techniques et des étapes de déploiement.*

---

## 1. Présentation du projet

NetWatch est une application web réalisée avec Python et Flask. Elle propose une interface comprenant un tableau de bord et une page de formulaire de rapport. Le projet a pour objectif de mettre en pratique le développement d’une application web, le suivi de code avec Git/GitHub, la création d’une image Docker et le déploiement dans le cloud.

**Technologies utilisées :** Python, Flask, HTML/CSS, Git et GitHub, Docker, Docker Hub et Amazon EC2.

> **Limite fonctionnelle à préciser :** ce livrable décrit les fonctionnalités présentes dans l’application. Il ne prétend pas que la supervision automatique en temps réel des équipements réseau ou le stockage persistant des rapports sont implémentés.

---

## 2. Liens de livraison

| Élément | Lien |
| :--- | :--- |
| **Application déployée** | [http://13.53.48.105](http://13.53.48.105) |
| **Code source GitHub** | [https://github.com/SOMMER67/NetWatch](https://github.com/SOMMER67/NetWatch) |
| **Image Docker Hub** | [https://hub.docker.com/r/sommer369/netwatch](https://hub.docker.com/r/sommer369/netwatch) |

---

## 3. Équipe et contributions

| Membre | Contribution identifiée dans le dépôt |
| :--- | :--- |
| **SOMMER67**<br>*(Konaté Idrissa)* | Application initiale, README et documentation, configuration Docker, publication de l’image et déploiement AWS EC2. |
| **varanjfhueijd**<br>*(Touré Ibrahim Hermann Junior)* | Contribution liée à la branche `feature/dashboard-design` : mise à jour du projet et du tableau de bord. |
| **ametech25**<br>*(Ayahoué Mawufilimi Elie)* | Contribution liée à la branche `feature/report-form` : amélioration du formulaire de rapport. |

Les contributions ont été intégrées à la branche principale via les Pull Requests **n° 1** (`dashboard-design`) et **n° 2** (`report-form`).

---

## 4. Dockerfile et construction de l’image

Le `Dockerfile` se trouve à la racine du dépôt. Il utilise une image officielle Python 3.12 légère, définit le répertoire de travail, installe les dépendances depuis `requirements.txt`, copie le code Flask, les templates et les fichiers statiques, puis documente le port 5000 et démarre l’application sur toutes les interfaces du conteneur.

### Commande de construction locale :
```bash
docker build -t netwatch:v1 .
```

### Commande de test local (exemple utilisé) :
```bash
docker run -d --name netwatch-validation -p 5002:5000 netwatch:v1
```

L’image publiée sur Docker Hub est identifiée par `sommer369/netwatch:v1`.

---

## 5. Déploiement sur AWS EC2

L’image a été récupérée depuis Docker Hub sur l’instance EC2. Le conteneur NetWatch a ensuite été recréé avec une publication du port 80 de l’hôte vers le port 5000 du conteneur. La règle HTTP entrante TCP/80 a été ajoutée au groupe de sécurité afin de permettre l’accès web public.

### Récupération de l’image :
```bash
sudo docker pull sommer369/netwatch:v1
```

### Lancement du conteneur :
```bash
sudo docker run -d --name netwatch-container -p 80:5000 --restart unless-stopped sommer369/netwatch:v1
```

### Vérification des conteneurs :
```bash
sudo docker ps
```

**Résultat observé lors de la vérification :** `0.0.0.0:80->5000/tcp` pour NetWatch. Le conteneur `iot-cloud-container` est resté actif sur le port 5000 de l’hôte.

---

## 6. Vérifications réalisées

- [x] L’image Docker a été construite et testée localement.
- [x] L’image `sommer369/netwatch:v1` a été publiée sur Docker Hub puis récupérée sur EC2.
- [x] Le conteneur NetWatch est actif et publié sur le port 80.
- [x] L’application a été ouverte avec succès dans un navigateur à l’adresse [http://13.53.48.105](http://13.53.48.105).
- [x] Le dépôt GitHub contient le code source, le README, le Dockerfile et l’historique des commits.

---

## 7. Points de vigilance pour la démonstration

1. **Vérification pré-évaluation :** vérifier à nouveau que l’URL publique répond, que les pages et le formulaire fonctionnent, que le dépôt GitHub est public et que l’image Docker Hub est accessible.
2. **Adresse IP dynamique :** L’adresse IP publique d’EC2 peut changer si l’instance est arrêtée puis redémarrée.
3. **Protocole HTTP :** Le service doit être testé avec HTTP (`http://`), car aucun certificat HTTPS n’est décrit dans ce déploiement.
4. **Présentation orale :** Pendant l’oral, présenter uniquement les fonctionnalités réellement disponibles et expliquer les commandes principales : `docker build`, `docker push`, `docker pull`, `docker run` et `docker ps`.
