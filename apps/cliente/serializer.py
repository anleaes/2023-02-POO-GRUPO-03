from .models import cliente
from rest_framework import serializers

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = '_all_'