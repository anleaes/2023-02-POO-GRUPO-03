from django.db import models

# Create your models here.

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    habilidades = models.JSONField()
    servicosPrestados = models.ManyToManyField(Servico)