from django.db import models
from profissional.models import Profissional
from tipo.models import Tipo
from formapagamento.models import Formapagamento

# Create your models here.
class Servico(models.Model):
    servico_profissional = models.ManyToManyField(Profissional)
    servico_tipo = models.ManyToManyField(Tipo)
    servico_formapagamento = models.ManyToManyField(Formapagamento)

    valor_total = models.DecimalField('Valor do serviço', max_digits=8, decimal_places=2, default=0.00)
    tempo_para_conclusao = models.IntegerField('Tempo estimado do serviço, em min', default=0)

    class Meta:
        verbose_name = 'Serviço Prestado'
        verbose_name_plural = 'Serviços Prestados'
        ordering = ['id']

    def __str__(self):
    #    return self.valor_total
         return str(self.servico_tipo)

