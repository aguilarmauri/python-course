from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator

class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=True, default=0)
    nombre = models.CharField(max_length=20)        
    descripcion = models.CharField(max_length=200)  
    precio =  models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal("0"))])

    def __str__(self):
        return "PRODUCTO "+self.nombre+": $"+str(self.precio)+". "+self.descripcion

class Proveedor(models.Model):
    nombre = models.CharField(max_length=20)
    cuit = models.IntegerField(unique=True)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return "PROVEEDOR "+self.nombre+" CUIT "+str(self.cuit)+" DIRECCION "+self.direccion+" TELEFONO "+str(self.telefono)

class IngresoMercaderia(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return "INGRESO de "+str(self.cantidad)+" PRODUCTOS "+self.producto.nombre+" en FECHA "+str(self.fecha)+" del PROVEEDOR "+self.proveedor.nombre

class EgresoMercaderia(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return "EGRESO de "+str(self.cantidad)+" PRODUCTOS "+self.producto.nombre+" en FECHA "+str(self.fecha)