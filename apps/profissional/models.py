from django.db import models
from categoria.models import Categoria

# Create your models here.
class Profissional(models.Model):
    profissional_categoria = models.ManyToManyField(Categoria)

    nome_completo = models.CharField('Nome', max_length=300, default='', blank=True)
    idade = models.IntegerField('Idade', default=0)
    cnpj = models.CharField('CNPJ', max_length=50, default='', unique=True)
    telefone = models.CharField('Experiência', max_length=11, default='', blank=True)

    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'
        ordering =['id']

    def __str__(self):
        return self.nome_completo