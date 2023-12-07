from django.db import models

class cliente(models.models):
    nome = models.CharField(max_length=300)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=50)