from django.shortcuts import render
from .models import Cliente
from rest_framework import viewsets
#from .serializer import clienteSerializer
from .serializer import ClienteSerializer

#class clienteViewSet(viewsets.ModelViewSet):
class ClienteViewSet(viewsets.ModelViewSet):    
    queryset = Cliente.objects.all()
#    serializer_class = clienteSerializer
    serializer_class = ClienteSerializer    