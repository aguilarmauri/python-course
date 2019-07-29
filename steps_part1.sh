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
# Create model Producto
file <project>/<app>/models.py
'''
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
'''
# Activate app
file <project>/<project>/setting.py
copy the name of app in INSTALLED APPS variable,
INSTALLED_APPS = [
    ...
    'app',
]
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
# Install modules
pip3 install djangorestframework
pip3 install markdown       # Markdown support for the browsable API.
pip3 install django-filter  # Filtering support
# Activate app
file <project>/<project>/setting.py
copy the name of app in INSTALLED APPS variable,
INSTALLED_APPS = [
    ...
    'rest_framework',
]
# Define dictionary to configure framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.OrderingFilter'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ]
}
# Create serializer to expose fields of model
file <project>/<app>/serializers.py
'''
from .models import Producto
from rest_framework import serializers

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'descripcion', 'precio']
'''
# Create view
file <project>/<app>/views.py
'''
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Producto
class PostViewSet(viewsets.ModelViewSet):
   """
   API endpoint that allows users to be viewed or edited.
   """
   queryset = Producto.objects.all()
   serializer_class = ProductoSerializer

'''
# Create url and register view for the api
'''
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.views import PostViewSet

router = routers.DefaultRouter()
router.register('products', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
'''
# Run the server
python3 manage.py runserver
http://127.0.0.1:8000/api
# 