from django.db import models
from servico.models import Servico

# Create your models here.

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=20)
    habilidades = models.CharField(max_length=100)
    servicosPrestados = models.ManyToManyField(Servico)

    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'
        ordering =['id']

    def __str__(self):
        return self.nome