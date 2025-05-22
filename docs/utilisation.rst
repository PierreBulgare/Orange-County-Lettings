Utilisation
===========

Lancement de l'application
--------------------------

Après avoir suivi les étapes d'installation, vous pouvez lancer le serveur de développement Django avec la commande :

.. code-block:: bash

    python manage.py runserver

Ouvrez ensuite votre navigateur et rendez-vous à l'adresse :

`http://127.0.0.1:8000/ <http://127.0.0.1:8000/>`_

Navigation dans l'application
-----------------------------

- **Accueil** : Page d'accueil du site.
- **Profiles** : Permet d'afficher la liste des utilisateurs.
- **Lettings** : Permet d'afficher la liste des locations.

Administration
--------------

L’interface d’administration Django est accessible à l’adresse :

`http://127.0.0.1:8000/admin/ <http://127.0.0.1:8000/admin/>`_

Pour y accéder, créez un superutilisateur si cela n’a pas déjà été fait :

.. code-block:: bash

    python manage.py createsuperuser
