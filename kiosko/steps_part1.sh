# REQUEST 1
django-admin --version          
2.2.3
django-admin startproject kiosko
cd kiosko
python3 manage.py startapp app
python3 manage.py migrate
python3 manage.py createsuperuser
mauri, mauri
python3 manage.py runserver
http://127.0.0.1:8000/admin

# REQUEST 2
# Create model
archivo <project>/<app>/models.py
'''
from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=20)        
    descripcion = models.CharField(max_length=200)  
    precio = models.IntegerField(default=0)         #  must be positive

    def __str__():
        return "Producto "+nombre+": $"+str(precio)+". "+descripcion
'''
# Activate model
copio nombre de la app en archivo <project>/setting.py
'app',
en la variable INSTALLED_APPS
# Add to admin web in admin.py
'''
from .models import Producto
admin.site.register(Producto)
'''
# Crear esquema en base de dato
python manage.py makemigrations app
python3 manage.py migrate
# Run the server
python3 manage.py runserver
http://127.0.0.1:8000/admin
