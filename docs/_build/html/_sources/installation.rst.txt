Installation
============

Prérequis
---------

- Python 3.8 ou supérieur
- pip
- virtualenv recommandé

Installation locale
-------------------

1. Cloner le dépôt GitHub :
git clone https://github.com/PierreBulgare/Orange-County-Lettings.git
cd Orange-County-Lettings


2. Créer et activer un environnement virtuel :
python -m venv venv
source venv/bin/activate # Sur Linux/Mac
venv\Scripts\activate # Sur Windows


3. Installer les dépendances :
pip install -r requirements.txt


4. Appliquer les migrations et lancer le serveur :
python manage.py migrate
python manage.py runserver
