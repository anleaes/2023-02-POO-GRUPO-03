from django.db import models

# Create your models here.
class Servico(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)

    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    tempo_estimado = models.IntegerField('Tempo Estimado (minutos)')
    categoria = models.CharField('Categoria', max_length=50)
    
    class Meta:
        verbose_name = 'Servico Prestado'
        verbose_name_plural = 'Servicos Prestados'
        ordering =['id']

    def __str__(self):
        return self.name