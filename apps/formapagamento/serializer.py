from .models import formapagamento
from rest_framework import serializers

class formapagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = formapagamento
        fields = '_all_'