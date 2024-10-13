from django import views
from django.contrib import admin
from django.urls import path
from .views import TractorDelete, MaquinaCreacion, TractorDetalle, CosechadoraLista, TractorLista, CosechadoraDetalle, TractorUpdate, CosechadoraUpdate, CosechadoraDelete, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, HomeView, ComentarioPagina
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='home/logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),
    path('listaTractores/', TractorLista.as_view(), name='tractores'),
    path('listaCosechadoras/', CosechadoraLista.as_view(), name='cosechadoras'),
    path('tractorDetalle/<int:pk>/', TractorDetalle.as_view(), name='tractor'),
    path('cosechadoraDetalle/<int:pk>/', CosechadoraDetalle.as_view(), name='cosechadora'),
    path('tractorEdicion/<int:pk>/', TractorUpdate.as_view(), name='tractor_editar'),
    path('cosechadoraEdicion/<int:pk>/', CosechadoraUpdate.as_view(), name='cosechadora_editar'),
    path('tractorBorrado/<int:pk>/', TractorDelete.as_view(), name='tractor_eliminar'),
    path('cosechadoraBorrado/<int:pk>/', CosechadoraDelete.as_view(), name='cosechadora_eliminar'),
    path('MaquinaCreacion/', MaquinaCreacion.as_view(), name='nuevo'),
    path('tractorDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('cosechadoraDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('AcercaDeMi/', views.about, name='acerca_de_mi'),
]