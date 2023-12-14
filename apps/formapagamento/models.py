from django.db import models

# Create your models here.
class Formapagamento(models.Model):
    banco = models.CharField('Banco', max_length=100, default='')
    meio_escolhido = models.CharField('Meio Escolhido', max_length=100, default='')
    numero_do_recibo = models.CharField('Número do Recibo', max_length=100, default='')

    class Meta:
        verbose_name = 'Forma de Pagamento'
        verbose_name_plural = 'Formas de Pagamentos'
        ordering = ['id']

    def __str__(self):
        #return f'{self.banco} - {self.meio_escolhido}'
        return self.meio_escolhido
