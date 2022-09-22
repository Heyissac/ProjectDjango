#Importamos librerías a utilizar en el avance del código.
from audioop import reverse
from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

#Creación de objetos para la tabla de reseñas.
class Review(models.Model):

    class Meta:
        verbose_name_plural = 'Review Profiles' #Nombre plural para el campo en la sección de administración de Django.
        verbose_name = 'Review' #Nombre singular para el campo en la sección de administración de Django.
        ordering = ['-id'] #Ordenamos los datos de manera descendente.
    
    date = models.DateTimeField(blank=True, null=True) #Creamos la variable para guardar la fecha y asignamos su tipo de dato.
    author = models.CharField(max_length=200, blank=True, null=True) #Creamos la variable para guardar el autor y asignamos su tipo de dato.
    name = models.CharField(max_length=200, blank=True, null=True) #Creamos la variable para guardar el título y asignamos su tipo de dato.
    description = models.CharField(max_length=500, blank=True, null=True) #Creamos la variable para guardar la descripción y asignamos su tipo de dato.
    body = RichTextField(blank=True, null=True) #Creamos la variable para guardar el contenido y asignamos su tipo de dato.
    image = models.ImageField(blank=True, null=True, upload_to="review") #Creamos la variable para guardar la imagen y asignamos su tipo de dato.
    slug = models.SlugField(null=True, blank=True) 
    is_active = models.BooleanField(default=True) #Creamos variable para determinar si la reseña está activo.

    #Función que permite guardar los datos en un slug para hacerlos visibles cuando se entre a un URL referido.
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Review, self).save(*args, **kwargs)

    #Función para representar los objetos de clase como una cadena.
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/review/{self.slug}"

#Creación de objetos para la tabla de reseñas.
class Blog(models.Model):

    class Meta:
        verbose_name_plural = 'Blog Profiles' #Nombre plural para el campo en la sección de administración de Django.
        verbose_name = 'Blog' #Nombre singular para el campo en la sección de administración de Django.
        ordering = ["-id"] #Ordenamos los datos por fecha.

    #Creamos las variables y el tipo de dato que albergarán.
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True) #Creamos la variable para guardar el autor y asignamos su tipo de dato.
    name = models.CharField(max_length=200, blank=True, null=True) #Creamos la variable para guardar el título y asignamos su tipo de dato.
    description = models.CharField(max_length=500, blank=True, null=True) #Creamos la variable para guardar la descripción y asignamos su tipo de dato.
    body = RichTextField(blank=True, null=True) #Creamos la variable para guardar el contenido y asignamos su tipo de dato.
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog") #Creamos la variable para guardar la imagen y asignamos su tipo de dato.
    is_active = models.BooleanField(default=True) #Creamos variable para determinar si el blog está activo.

    #Función que permite guardar los datos en un slug para hacerlos visibles cuando se entre a un URL referido.
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    #Función para representar los objetos de clase como una cadena.
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"




