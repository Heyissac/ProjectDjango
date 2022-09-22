from django import forms #Importamos la librería de formularios Django.
from . models import Blog

from ckeditor.fields import RichTextFormField

#Librerías para crear el formaulario de cuentas de usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
    
#Creamos la clase para albergar la información el formulario.
class UploadForm(forms.ModelForm):

	#Creamos el formulario para el nombre del autor, su campo, y el tipo de dato que llevan dentro.
	author = forms.CharField(max_length=100, required=True,) #Definimos cantidad máxima de caracteres y si el campo es obligatorio.

	#Creamos el formulario para el nombre del anime, su campo, y el tipo de dato que llevan dentro.
	name = forms.CharField(max_length=254, required=True,) #Definimos cantidad máxima de caracteres y si el campo es obligatorio.


	#Creamos el formulario para la descripción del anime, su campo, y el tipo de dato que llevan dentro.		
	description = forms.CharField(max_length=254, required=True,) #Definimos cantidad máxima de caracteres y si el campo es obligatorio.


	#Creamos el formulario para el blog/review del anime, su campo, y el tipo de dato que llevan dentro.
	body = forms.CharField(max_length=100000, required=True,) #Definimos cantidad máxima de caracteres y si el campo es obligatorio.

	image = forms.ImageField()

	#Nueva clase para identificar el destino de los datos.
	class Meta:
		model = Blog #Este formulario almacena los datos en el modelo Blog.
		fields = ('author', 'name', 'description', 'body', 'image') #Campos que se utilzarán del modelo.
	
#Creamos la clase para albergar la información el formulario.
class UploadReview(forms.ModelForm):

	#Creamos el formulario para el nombre del autor, su campo, y el tipo de dato que llevan dentro.
	author = forms.CharField(max_length=100, required=True,) #Definimos cantidad máxima de caracteres y si el campo es obligatorio.

	#Creamos el formulario para el nombre del anime, su campo, y el tipo de dato que llevan dentro.
	name = forms.CharField(max_length=254, required=True,) #Definimos cantidad máxima de caracteres y si el campo es obligatorio.


	#Creamos el formulario para la descripción del anime, su campo, y el tipo de dato que llevan dentro.		
	description = forms.CharField(max_length=254, required=True,) #Definimos cantidad máxima de caracteres y si el campo es obligatorio.


	#Creamos el formulario para el blog/review del anime, su campo, y el tipo de dato que llevan dentro.
	body = forms.CharField(max_length=100000, required=True,) #Definimos cantidad máxima de caracteres y si el campo es obligatorio.

	image = forms.ImageField() #Definimos la variable de imagen y el tipo de dato.

	#Nueva clase para identificar el destino de los datos.
	class Meta:
		model = Blog #Este formulario almacena los datos en el modelo Blog.
		fields = ('author', 'name', 'description', 'body', 'image') #Campos que se utilzarán del modelo.

class CreateUserForm(UserCreationForm): #Definimos el objeto para crear el formulario.
	class Meta:
		model = User #Asignamos el modelo, para guardar los datos(Modelo por defecto de Django).
		fields = ['username', 'email', 'password1', 'password2'] #Definimos los campos que llevará el formulario.