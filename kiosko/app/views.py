from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class PostViewSet(viewsets.ModelViewSet):
   """
   API endpoint that allows users to be viewed or edited.
   """
   queryset = Producto.objects.all()
   serializer_class = ProductoSerializer
