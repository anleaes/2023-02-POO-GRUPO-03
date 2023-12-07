from .models import Servico
from rest_framework import serializers

class FormapagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formapagamento
        fields = '_all_'