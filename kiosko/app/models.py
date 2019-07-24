from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=    True, default=0)
    nombre = models.CharField(max_length=20)        
    descripcion = models.CharField(max_length=200)  
    precio = models.IntegerField(default=0)         #  must be positive

    def __str__():
        return "Producto "+nombre+": $"+str(precio)+". "+descripcion