from django.contrib import admin #Importamos las librerías

#Se ha la importación de los modelos que serán vistos en la sección de administración de Django.
from . models import (
    Review,
    Blog,
    )

#Se registra el modelo en la sección de administración.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin): #Clase para referir esta sección.
    list_display = ('id','name','is_active') #Campos que serán visibles en la ventana de administración.
    readonly_fields = ('slug',) #Vemos los datos de todos los campos.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin): #Clase para referir esta sección.
    list_display = ('id','name','is_active') #Campos que serán visibles en la ventana de administración.
    readonly_fields = ('slug',) #Vemos los datos de todos los campos.
    

