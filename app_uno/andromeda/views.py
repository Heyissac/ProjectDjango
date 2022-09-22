#Importamos librerías a utilizar en el desarrollo del código.
from multiprocessing import context
from django.shortcuts import render
from django.contrib import messages
from django.views import generic
#Importar los modelos que se utilizarán en algunas vistas.
from .models import (
		Review,
		Blog
	)

from . forms import UploadForm #Importar formulario para subir un blog.
from . forms import CreateUserForm #Importar formulario para crear usuario.

#imports para la creación de funciones login/logout/register
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect

def registerPage(request): #Definimos la función para registrar a los usuarios.
	if request.user.is_authenticated: #Si el usuario está logeado.
		return redirect('andromeda:index') #Lo envía al índice.
	else: #Instrucción else
		form = CreateUserForm() #De no estar logeado, se envía el formulario para registro al usuario.
		if request.method == 'POST': #Instrucción if para validar los datos.
			form = CreateUserForm(request.POST) #Se llama al formulario.
			if form.is_valid(): #Si el formulario es válido
				form.save() #Se guardan los datos
				user = form.cleaned_data.get('username') #Se obtiene el nombre del usuario.
				messages.success(request, 'Account was created for '+user) #Mensaje que indica al usuario, que su cuenta ha sido creada.

				return redirect('andromeda:login') #Se envía al usuario a la página del login.
		

		context = {'form':form} #Permite mostrar la información del formulario.
		return render(request, 'main/register.html', context) #Si el usuario no tiene cuenta, se le redirige a la página de registro.

def loginPage(request): #Definimos la función para permitir que el usuario se logee.
	if request.user.is_authenticated: #Ciclo if/else para validar el logeo del usuario. 
		return redirect('andromeda:index')#Si el usuario está logeado, le envía al índice del sitio web.
	else: #Si no está logeado, debe ingresar sus datos, para tener acceso.
		if request.method == 'POST':
			username = request.POST.get('username') #Campo para validar el usuario.
			password = request.POST.get('password') #Campo para validar la contraseña.

			user = authenticate(request, username=username, password=password) #Verifica si los datos son correctos.

			if user is not None: #Si los datos ingresados son válidos, le permite ingresar.
				login(request, user)
				return redirect('andromeda:index') #Al tener datos correctos, envía al usuario al índice.
			else:
				messages.info(request, 'Username or password is incorrect') #Si los datos son incorrectos, se le indica al usuario que tiene errores.

		context = {} #Muestra y toma el contenido del formulario.
		return render(request, 'main/login.html', context) #Una vez se validen los datos, envía al usuario al login.

def logoutUser(request): #Definimos la función para que el usuario salga de la página.
	logout(request)
	return redirect ('andromeda:login') #Cuando el usuario sale de su cuenta,lo envía a esta dirección.

#Se crea el constructor u objeto para la vista del índice.
class IndexView(generic.TemplateView):
	template_name = "main/index.html" #Agregamos el nombre del archivo HTML al que queremos hacer referencia en la vista.

	#Función para obtener los datos de los archivos que deseamos mostrar.
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		#Instanciamos los objetos que serán visibles en el ídnice.
		review = Review.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		
		#Se agregan las secciones visibles en el índice.
		context["review"] = review
		context["blogs"] = blogs
		return context

#Se crea el constructor u objeto para la vista de las reseñas..
class ReviewView(generic.ListView):
	model = Review #Tabla de donde se obtiene la información para la vista.
	template_name = "main/review.html" #Plantilla HTML a donde iremos cuando ejecutemos esta vista.
	paginate_by = 10

	def get_queryset(self): #Se obtienen los registros guardados.
		return super().get_queryset().filter(is_active=True)

#Se crea el constructur u objeto para la vista de reseñas detalladas.
class ReviewDetailView(generic.DetailView):
	model = Review #Tabla de donde se obtiene la información para la vista.
	template_name = "main/review-detail.html" #Plantilla HTML a donde iremos cuando ejecutemos esta vista.

#Se crea el constructur u objeto para los blogs.
class BlogView(generic.ListView):
	model = Blog #Tabla de donde se obtiene la información para la vista.
	template_name = "main/blog.html" #Plantilla HTML a donde iremos cuando ejecutemos esta vista.
	paginate_by = 10
	
	def get_queryset(self): #Se obtienen los registros guardados.
		return super().get_queryset().filter(is_active=True)

#Se crea el constructur u objeto para ver lo sblogs detallados.
class BlogDetailView(generic.DetailView):
	model = Blog #Tabla de donde se obtiene la información para la vista.
	template_name = "main/blog-detail.html" #Plantilla HTML a donde iremos cuando ejecutemos esta vista.

#Se crea el constructur u objeto para subir blogs.
class UploadBlog(generic.FormView):
	form_class = UploadForm #Tabla de donde se obtiene la información para la vista.
	template_name = "main/upload-blog.html" #Plantilla HTML a donde iremos cuando ejecutemos esta vista.
	success_url = '/' #Colocamos el signo que se coloca al terminar la url.

	def form_valid(self, form): #Creamos la función para validar los datos.
		form.save() #Si el formulario está completo, se guardan los datos el el modelo correspondiente.
		return super().form_valid(form)

#Se crea el constructur u objeto para subir reseñas.
class UploadReview(generic.FormView):
	form_class = UploadForm #Tabla de donde se obtiene la información para la vista.
	template_name = "main/upload-review.html" #Plantilla HTML a donde iremos cuando ejecutemos esta vista.
	success_url = '/' #Colocamos el signo que se coloca al terminar la url.

	def form_valid(self, form): #Creamos la función para validar los datos.
		form.save() #Si el formulario está completo, se guardan los datos el el modelo correspondiente.
		return super().form_valid(form)
