from django.shortcuts import render

from .models import Formapagamento
from rest_framework import viewsets
from .serializer import FormapagamentoSerializer

class FormapagamentoViewSet(viewsets.ModelViewSet):    
    queryset = Formapagamento.objects.all()
    serializer_class = FormapagamentoSerializer