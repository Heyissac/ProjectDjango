from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views #Importamos las vistas.


app_name = "andromeda" #Nombre de la aplicación

#Diseño de las urls a partir de las vistas creadas en views.py.
urlpatterns = [
	path('register/', views.registerPage, name="register"), #Creamos url personalizado para registrar cuentas.
	path('accounts/login/', views.loginPage, name="login"), #Creamos url personalizado para logear cuentas.
	path('logout/', views.logoutUser, name="logout"), #Creamos url personalizado para salir de una cuenta.

	path('', views.IndexView.as_view(), name="index"), #url personalizada para la vista del índice.
	#path('contact/', views.Contact.as_view(), name="contact"),
	path('review/', views.ReviewView.as_view(), name="reviews"), #url personalizada para la vista de las reseñas.
	path('review/<slug:slug>', views.ReviewDetailView.as_view(), name="review"), #url personalizada para la vista de reseñas detalladas.
	path('blog/', views.BlogView.as_view(), name="blogs"), #url personalizada para la vista de blogs.
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"), #url personalizada para la vista de los blogs detallados.
	path('upload-blog/', login_required(views.UploadBlog.as_view()), name = 'uploadblog'), #url personalizada para la vista de la sección para subir blogs, además requiere de un usuario logeado para acceder a la sección.
	path('upload-review/', login_required(views.UploadReview.as_view()), name = 'uploadreview'), #url personalizada para la vista de la sección para subir reseñas.
	]


