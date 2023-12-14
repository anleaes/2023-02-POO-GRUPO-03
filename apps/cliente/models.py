from django.db import models
from formapagamento.models import Formapagamento

# Create your models here.
class Cliente(models.Model):
    cliente_formapagamento = models.ManyToManyField(Formapagamento)

    nome_completo = models.CharField('Nome', max_length=300, default='')
    idade = models.IntegerField('Idade', default=0)
    cpf = models.CharField('CPF', max_length=50, default='')
    telefone = models.CharField('Telefone', max_length=14, default='')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

    def __str__(self):
        return self.nome_completo
