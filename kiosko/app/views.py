from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.db.models import F

class PostViewSet(viewsets.ModelViewSet):
   """
   API endpoint that allows users to be viewed or edited.
   """
   queryset = Producto.objects.annotate(
      ingreso=Coalesce(Sum("ingresomercaderia__cantidad"), 0),
      egreso=Coalesce(Sum("egresomercaderia__cantidad"), 0),
      stock=F("ingreso")-F("egreso")
   )   
   serializer_class = ProductoSerializer
