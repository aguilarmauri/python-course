from .models import Producto
from rest_framework import serializers

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        # Fields to Expose for Put from web API
        fields = ['codigo', 'nombre', 'descripcion', 'precio']