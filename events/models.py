from django.db import models
from parametres.models import User, Evenement

class Annonce(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="annonces")
    categorie = models.ForeignKey(Evenement, on_delete=models.CASCADE, related_name='annonce_catégorie')
    titre = models.CharField(max_length=255)
    date = models.DateField()
    carte_annonce = models.FileField(upload_to='carte_annonces/', blank=True, null=True)
    fare_part = models.FileField(upload_to='faire_parts/', blank=True, null=True, verbose_name="Faire Part")
    programme = models.TextField(verbose_name="PROGRAMME", null=True)
    participant = models.ManyToManyField(User, related_name='participants')


    def __str__(self):
        return ('%s') % (self.titre)

    add_le = models.DateTimeField(auto_now_add=True)
    update_le = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "ANNONCES"
        verbose_name = "annonce"
        ordering = ["-add_le", "-update_le"]


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    contenu = models.TextField(null=True, blank=True)
    created_le = models.DateTimeField(auto_now_add=True)
    updated_le = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "MESSAGES"
        verbose_name = "message"
        ordering = ["-created_le", "-updated_le"]

    def __str__(self):
        return ('%s') %(self.contenu[0:50])

