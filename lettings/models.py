from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle représentant une adresse.
    Attributs:
        number (int): Numéro du lieu.
        street (str): Nom de la rue.
        city (str): Nom de la ville.
        state (str): État ou province.
        zip_code (int): Code postal.
        country_iso_code (str): Code ISO du pays.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        db_table = 'oc_lettings_site_address'
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Modèle représentant une location.
    Attributs:
        title (str): Nom de la location.
        address (Address): Adresse de la location.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        db_table = 'oc_lettings_site_letting'

    def __str__(self):
        return self.title
