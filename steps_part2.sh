# REQUIREMENT 1
# Create model Proveedor
file <project>/<app>/models.py
'''
class Proveedor(models.Model):
    nombre = models.CharField(max_length=20)
    cuit = models.IntegerField(max_length=11, unique=True)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=17)

    def __str__(self):
        return "Proveedor "+self.nombre+" cuit "+str(self.cuit)+" direccion "+self.direccion+" tel "+str(self.telefono)
'''
# Register Models: Add to admin web
file <project>/<app>/admin.py
'''
from .models import Producto
admin.site.register(Producto)
'''
# Create schema of db
python3 manage.py makemigrations app
python3 manage.py migrate
# Run the server
python3 manage.py runserver
http://127.0.0.1:8000/admin