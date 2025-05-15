from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Modèle représentant un profil utilisateur.
    Attributs:
        user (User): L'utilisateur associé au profil.
        favorite_city (str): Ville préférée de l'utilisateur.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.user.username
