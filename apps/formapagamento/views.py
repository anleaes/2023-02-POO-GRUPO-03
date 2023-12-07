from django.shortcuts import render

from .models import formapagamento
from rest_framework import viewsets
from .serializer import formapagamentoSerializer

class formapagamentoViewSet(viewsets.ModelViewSet):
    queryset = formapagamento.objects.all()
    serializer_class = formapagamentoSerializer