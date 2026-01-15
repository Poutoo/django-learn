from django.db import models

class Dragon(models.Model):
    nom = models.CharField(max_length=100)
    couleur = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100)  # Avoid accents in field names usually, but user asked for "catégorie" logic. Stick to english-ish variable names or normalized. User prompt: "catégorie". I'll use "categorie" for the field name.
    taille = models.FloatField(help_text="Taille en mètres")
    age = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='dragons_photos/', blank=True, null=True)

    def __str__(self):
        return self.nom
