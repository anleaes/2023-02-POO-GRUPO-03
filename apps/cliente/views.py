from django.shortcuts import render

from .models import cliente
from rest_framework import viewsets
from .serializer import clienteSerializer

class clienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = clienteSerializer