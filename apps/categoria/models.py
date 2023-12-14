from django.db import models

#Create your models here.
class Categoria(models.Model):
    modo_de_atendimento = models.CharField('Modo de Atendimento', max_length=100, blank=True)
    ramo_de_negocio = models.CharField('Ramo do Negócio', max_length=100, blank=True)
    descricao = models.TextField('Descrição', blank=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering =['id']

    def __str__(self):
        return self.modo_de_atendimento