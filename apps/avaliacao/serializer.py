from .models import Avaliacao
from rest_framework import serializers

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '_all_'
        
