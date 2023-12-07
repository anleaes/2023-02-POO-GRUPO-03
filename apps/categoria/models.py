from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.CharField('Descrição', max_length=300)
    taxa_padrao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering =['id']

    def __str__(self):
        return self.nome