"""MisPerrisDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', home, name='home'),
    path('galeria/',galeria,name='galeria'),
    path('formulario/',agregarPersona,name="formulario"),
    path('listar_personas/',listarPersona,name="listar_personas"),
    path('eliminar_persona/',eliminarPersona,name="eliminar_persona"),
    path('modificar_personas/',actualizarPersona,name="modificar_personas"),
    path('agregarMascota/',agregarMascota,name="agregarMascota"),
    path('listarMascotas/',listarMascota,name="listarMascotas"),
    path('eliminarMascota/',eliminarMascotas,name="eliminarMascota"),
    path('actualizarMascota/',actualizarMascota,name="actualizarMascota"),
    path('servicios/',servicios,name="servicios"),
    path('menu_perros/',menu_perros,name="menu_perros"),
    path('menu_persona/',menu_persona,name="menu_persona"),
    path('recuperar/',recuperar,name='recuperar'),
    path('logout/',logout,name='logout'),
    path('login/',login,name='login'),
    path('accounts/login/',login,name='login'),
    path('login/registro/',regPersona,name='reg'),
    path('ListarMascotasGaleria',ListarMascotasGaleria,name='ListarMascotasGaleria'),
    
    #borre los import de los 2 path comentado ya que me tiraba error al momento de arrancar el server
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
