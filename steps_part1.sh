# Create virtualenv and install Django
virtualenv django
source django/bin/activate
pip3 install Django
django-admin --version
## 2.2.3

# REQUIREMENT 1
# Create project and app
django-admin startproject kiosko
cd kiosko
python3 manage.py startapp app
python3 manage.py migrate
# Create admin user
python3 manage.py createsuperuser
## mauri, mauri
python3 manage.py runserver
http://127.0.0.1:8000/admin

# REQUIREMENT 2
# Create model
file <project>/<app>/models.py
'''
from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=    True, default=0)
    nombre = models.CharField(max_length=20)        
    descripcion = models.CharField(max_length=200)  
    precio = models.IntegerField(default=0)         #  must be positive

    def __str__():
        return "Producto "+nombre+": $"+str(precio)+". "+descripcion    
'''
# Activate model
file <project>/<project>/setting.py
copy the name of app in INSTALLED APPS variable,
'app',
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

# REQUIREMENT 3

