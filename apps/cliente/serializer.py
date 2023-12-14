from .models import Cliente
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):    
    class Meta:
#        model = cliente
        model = Cliente        
        fields = '__all__'