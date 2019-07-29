# REQUIREMENT 1
# Create model Proveedor
file <project>/<app>/models.py
'''
class Proveedor(models.Model):
    nombre = models.CharField(max_length=20)
    cuit = models.IntegerField(unique=True)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return "PROVEEDOR "+self.nombre+" CUIT "+str(self.cuit)+" DIRECCION "+self.direccion+" TELEFONO "+str(self.telefono)
'''
# Register Models: Add to admin web
file <project>/<app>/admin.py
'''
from .models import Proveedor
admin.site.register(Proveedor)
'''
# Update schema of db
python3 manage.py makemigrations app
python3 manage.py migrate
# Run the server
python3 manage.py runserver
http://127.0.0.1:8000/admin



# REQUIREMENT 2
# Create model IngresoMercaderia
file <project>/<app>/models.py
'''
class IngresoMercaderia(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return "INGRESO de "+str(self.cantidad)+" PRODUCTOS "+self.producto.nombre+" en FECHA "+str(self.fecha)+" del PROVEEDOR "+self.proveedor.nombre
'''
# Register Models: Add to admin web
file <project>/<app>/admin.py
'''
from .models import IngresoMercaderia
admin.site.register(IngresoMercaderia)
'''
# Update schema of db
python3 manage.py makemigrations app
python3 manage.py migrate
# Run the server
python3 manage.py runserver
http://127.0.0.1:8000/admin



# REQUIREMENT 3
# Create model EgresoMercaderia
file <project>/<app>/models.py
'''
class EgresoMercaderia(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return "EGRESO de "+str(self.cantidad)+" PRODUCTOS "+self.producto.nombre+" en FECHA "+str(self.fecha)
'''
# Register Models: Add to admin web
file <project>/<app>/admin.py
'''
from .models import EgresoMercaderia
admin.site.register(EgresoMercaderia)
'''
# Update schema of db
python3 manage.py makemigrations app
python3 manage.py migrate
# Run the server
python3 manage.py runserver
http://127.0.0.1:8000/admin

# REQUIREMENT 4
# Modify view to calc stock
file file <project>/<app>/views.py
'''
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.db.models import F

   queryset = Producto.objects.annotate(
      ingreso=Coalesce(Sum("ingresomercaderia__cantidad"), 0),
      egreso=Coalesce(Sum("egresomercaderia__cantidad"), 0),
      stock=F("ingreso")-F("egreso")
   )   
'''
# Update serializer to show stock field
'''
model.stock = serializers.IntegerField(read_only=True)
fields = [
    ...
    'stock'
]
'''
# Run the server
python3 manage.py runserver
http://127.0.0.1:8000/admin
