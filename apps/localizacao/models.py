from django.db import models

# Create your models here.
class Localizacao(models.Model):
    cidade = models.CharField('Cidade', max_length=100, blank=True, null=True)
    endereco = models.CharField('Endereço', max_length=100, blank=True, null=True)
    complemento = models.CharField('Complemento', max_length=100, blank=True, null=True)
    cep = models.CharField('Cep', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locais'
        ordering =['id']

    def __str__(self):
        return self.cidade