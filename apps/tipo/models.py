from django.db import models

# Create your models here.
class Tipo(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100) 

    duracao_padrao = models.IntegerField('Duração do Serviço (minutos)')
    requisitos = models.TextField('Requisitos do Serviço')
    popularidade = models.IntegerField('Popularidade')
    
    class Meta:
        verbose_name = 'Tipo de Servico'
        verbose_name_plural = 'Tipos de Servicos'
        ordering =['id']

    def __str__(self):
        return self.name