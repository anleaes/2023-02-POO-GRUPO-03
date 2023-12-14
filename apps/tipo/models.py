from django.db import models
from cliente.models import Cliente
from localizacao.models import Localizacao

# Create your models here.
class Tipo(models.Model):
    tipo_cliente = models.ManyToManyField(Cliente)
    tipo_localizacao = models.ManyToManyField(Localizacao)
    
    area_de_atuacao = models.CharField('Área de atuação', max_length=50, default='Serviços Gerais')
    descricao = models.TextField('Descrição do serviço a realizar', max_length=100)

    class Meta:
        verbose_name = 'Tipo de Serviço'
        verbose_name_plural = 'Tipos de Serviço'
        ordering = ['id']

    def __str__(self):
        return self.area_de_atuacao
