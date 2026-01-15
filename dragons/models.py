from django.db import models

class Dragon(models.Model):
    COULEUR_CHOICES = [
        ('Rouge', 'Rouge'),
        ('Vert', 'Vert'),
        ('Bleu', 'Bleu'),
        ('Noir', 'Noir'),
        ('Blanc', 'Blanc'),
        ('Or', 'Or'),
        ('Argent', 'Argent'),
    ]
    nom = models.CharField(max_length=100)
    couleur = models.CharField(max_length=100, choices=COULEUR_CHOICES)
    categorie = models.CharField(max_length=100)  # Avoid accents in field names usually, but user asked for "catégorie" logic. Stick to english-ish variable names or normalized. User prompt: "catégorie". I'll use "categorie" for the field name.
    taille = models.FloatField(help_text="Taille en mètres")
    age = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='dragons_photos/', blank=True, null=True)

    def __str__(self):
        return self.nom
