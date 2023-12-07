from django.db import models

# Create your models here.
class formapagamento(models.models):
    banco = models.CharField(max_length=100)
    tipo_pagamento = models.CharField(max_length=100)
    recibo = models.CharField(max_length=100)