from .models import Producto
from rest_framework import serializers

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        model.stock = serializers.IntegerField(read_only=True)
        # Fields to Expose for Put from web API
        fields = [
            'codigo',
            'nombre',
            'descripcion',
            'precio',
            'stock'
        ]
        