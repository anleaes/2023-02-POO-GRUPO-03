from django.db import models

# Create your models here.

class Localizacao(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.endereco