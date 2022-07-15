import os
import time
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

def documents(self, filename):
    # verification de l'extension
    real_name, extension = os.path.splitext(filename)
    name = str(int(time.time())) + extension
    return "documents/" + self.num_piece

TYPE_PIECE = (
    ('AUCUN', 'AUCUN'),
    ('ATTESTATION', 'ATTESTATION'),
    ('CNI', 'CNI'),
    ('PASSEPORT', 'PASSEPORT'),
    ('SEJOUR', 'CARTE DE SEJOUR'),
    ('CONSULAIRE', 'CARTE CONSULAIRE'),
)

OPERATEURS = (
    ('MOOV', 'MOOV'),
    ('MTN', 'MTN'),
    ('ORANGE', 'ORANGE'),
)

class User(AbstractUser):
    nom = models.CharField(max_length=255, null=True, verbose_name="Nom et Prénoms")
    email = models.EmailField(unique=True)
    contact1 = models.CharField(max_length=50, unique=True, null=True, verbose_name="Contact")
    contact2 = models.CharField(max_length=50, blank=True, null=True)
    orange_money = models.CharField(max_length=50, blank=True, null=True)
    mtn_money = models.CharField(max_length=50, blank=True, null=True)
    moov_money = models.CharField(max_length=50, blank=True, null=True)
    adresse = models.CharField(max_length=255, verbose_name="ADRESSE", blank=True, null=True)
    image = models.ImageField(null=True, default="avatar.svg")
    type_piece = models.CharField(max_length=50, verbose_name="TYPE DOCUMENT", choices=TYPE_PIECE, default="CNI", null=True, blank=True)
    num_piece = models.CharField(max_length=150, verbose_name="N° PIECE", blank=True, null=True)
    piece = models.FileField(verbose_name="DOCUMENT", upload_to=documents, null=True, blank=True)
    add_le = models.DateTimeField(auto_now_add=True)
    update_le = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'contact1'
    REQUIRED_FIELDS = []

class Evenement(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return ('%s') %(self.nom)

    def save(self, force_insert=False, force_update=False):
        self.nom = self.nom.upper()
        super(Evenement, self).save(force_insert, force_update)



# Create your models here.
