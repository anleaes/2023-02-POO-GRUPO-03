#from .models import formapagamento
from .models import Formapagamento
from rest_framework import serializers

#class formapagamentoSerializer(serializers.ModelSerializer):
class FormapagamentoSerializer(serializers.ModelSerializer):
    class Meta:
#        model = formapagamento
        model = Formapagamento        
        fields = '__all__'