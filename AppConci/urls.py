from django.urls import path
from .views import (HomeView, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, 
                    CosechadoraLista, TractorLista, OtroLista, CosechadoraDetalle, 
                    TractorDetalle, OtroDetalle, CosechadoraUpdate, TractorUpdate, 
                    OtroUpdate, CosechadoraDelete, TractorDelete, OtroDelete, 
                    MaquinaCreacion, ComentarioPagina)
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

    path('listaCosechadora/', CosechadoraLista.as_view(), name='cosechadora'),
    path('listaTractor/', TractorLista.as_view(), name='tractor'),
    path('listaOtros/', OtroLista.as_view(), name='otros'),

    path('cosechadoraDetalle/<int:pk>/', CosechadoraDetalle.as_view(), name='cosechadora'),
    path('tractorDetalle/<int:pk>/', TractorDetalle.as_view(), name='tractor'),
    path('otroDetalle/<int:pk>/', OtroDetalle.as_view(), name='otro'),

    path('cosechadoraEdicion/<int:pk>/', CosechadoraUpdate.as_view(), name='cosechadora_editar'),
    path('tractorEdicion/<int:pk>/', TractorUpdate.as_view(), name='tractor_editar'),
    path('otroEdicion/<int:pk>/', OtroUpdate.as_view(), name='otro_editar'),

    path('cosechadoraBorrado/<int:pk>/', CosechadoraDelete.as_view(), name='cosechadora_eliminar'),
    path('tractorBorrado/<int:pk>/', TractorDelete.as_view(), name='tractor_eliminar'),
    path('otroBorrado/<int:pk>/', OtroDelete.as_view(), name='otro_eliminar'),

    path('maquinaCreacion/<int:pk>/', MaquinaCreacion.as_view(), name='nuevo'),

    path('cosechadoraDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('tractorDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('otroDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    path('acercaDeMi/', views.about, name='acerca_de_mi'),
    
    ]
