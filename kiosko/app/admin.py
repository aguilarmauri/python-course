from django.contrib import admin

from .models import Producto, Proveedor, IngresoMercaderia, EgresoMercaderia
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(IngresoMercaderia)
admin.site.register(EgresoMercaderia)