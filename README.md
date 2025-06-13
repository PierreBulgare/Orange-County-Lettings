# Orange County Lettings

<img src="https://i.postimg.cc/MHm1vfhD/1689880374259-Orange-County-Lettings-Ad.png" alt="Orange County Lettings" width="600"/>

---

## 🗎 Description

Orange County Lettings est une application web Django de gestion de location.
Ce projet a pour but de mettre à l'échelle l'application en utilisant une architecture modulaire.

Fork à partir de [Python-OC-Lettings-FR](https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR)

Documentation : [Read The Docs](https://orange-county-lettings-docs.readthedocs.io/fr/latest)

## ⚙️ Fonctionnalités

- Affichage d’un catalogue de biens disponibles à la location
- Gestion de profils utilisateurs
- Interface d’administration sécurisée (`/admin`)
- Déploiement via Docker, CI/CD (Github Actions)

---

## 🧑‍💻 Prérequis

- Python 3.6+
- SQLite
- Git, Docker
- Bibliothèques requises dans le fichier `requirements.txt`

---

## 🚀 Installation & lancement (développement)

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/PierreBulgare/Orange-County-Lettings.git
   cd Orange-County-Lettings
   ```
2. **Créer un environnement virtuel**
   
   **Linux/MacOS :**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   **Windows :**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```
4. **Lancer le serveur local**
   ```bash
   python manage.py runserver
   ```
   Accès via http://localhost:8000
5. **Authentification admin**
   - URL : `http://localhost:8000/admin`
   - Login : `admin` / `Abc1234!` (config par défaut)

---

## ✔️ Qualité & tests

- **Linting** : `flake8`
- **Tests unitaires** : `pytest`
- **Couverture de code** : `coverage`

---

## 🔁 Pipeline CI/CD

Pipeline configuré avec GitHub Actions :
- **Linting** : Vérification du code avec `flake8`
- **Tests** : Exécution des tests unitaires avec `pytest`
- **Couverture** : Rapport de couverture avec `coverage`
- **Build** : Création de l'image Docker
- **Déploiement PROD** : Déploiement sur Render

---

## 🗂️ Structure du projet

```
├── lettings/              # Application pour les locations
├── profiles/              # Application pour les profils utilisateurs
├── oc_lettings_site/      # Application principale
├── templates/ + static/   # Front & assets
├── Dockerfile, Procfile   # Pour déploiement
├── requirements.txt       # Dépendances
└── tests.py               # Tests unitaires
```
