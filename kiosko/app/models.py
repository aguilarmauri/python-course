from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=True, default=0)
    nombre = models.CharField(max_length=20)        
    descripcion = models.CharField(max_length=200)  
    precio = models.PositiveIntegerField(default=0)         #  must be positive

    def __str__(self):
        return "Producto "+self.nombre+": $"+str(self.precio)+". "+self.descripcion

class Proveedor(models.Model):
    nombre = models.CharField(max_length=20)
    cuit = models.IntegerField(max_length=11, unique=True)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=17)

    def __str__(self):
        return "Proveedor "+self.nombre+" cuit "+str(self.cuit)+" direccion "+self.direccion+" tel "+str(self.telefono)
