from django.db import models
from servico.models import Servico

#Create your models here.
class Avaliacao(models.Model):
    avaliacao_servico = models.ManyToManyField(Servico)

    nota = models.CharField('Nota', max_length=3)
    comentario = models.TextField('Comentario', max_length=300)
    
    
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering =['id']

    def __str__(self):
        return self.nota