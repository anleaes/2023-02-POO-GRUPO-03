from django.db import models

class cliente(models.Model):
    nome = models.CharField(max_length=300)
    idade = models.IntegerField()
    cpf_cliente = models.CharField(max_length=50)