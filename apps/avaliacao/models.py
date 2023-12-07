from django.db import models

# Create your models here.

class Avaliacao(models.Model):
    nota = models.CharField('Nota', max_length=3)
    comentario = models.TextField('Comentario', max_length=300)
    usuarioCliente = models.CharField('Telefone', max_length=100)
    
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering =['id']

    def __str__(self):
        return self.nota