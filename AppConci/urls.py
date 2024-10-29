from django.urls import path
from .views import (
    HomeView, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, 
    CosechadoraLista, TractorLista, OtroLista, CosechadoraDetalle, 
    TractorDetalle, OtroDetalle, CosechadoraUpdate, TractorUpdate, 
    OtroUpdate, CosechadoraDelete, TractorDelete, OtroDelete, 
    MaquinaCreacion, ComentarioPagina
)
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/', views.password_exitoso, name='password_exitoso'),

    path('listaCosechadora/', CosechadoraLista.as_view(), name='lista_cosechadora'),
    path('listaTractor/', TractorLista.as_view(), name='lista_tractor'),
    path('listaOtros/', OtroLista.as_view(), name='lista_otros'),

    path('cosechadoraDetalle/<int:pk>/', CosechadoraDetalle.as_view(), name='cosechadora_detalle'),
    path('tractorDetalle/<int:pk>/', TractorDetalle.as_view(), name='tractor_detalle'),
    path('otroDetalle/<int:pk>/', OtroDetalle.as_view(), name='otro_detalle'),

    path('cosechadoraEdicion/<int:pk>/', CosechadoraUpdate.as_view(), name='cosechadora_editar'),
    path('tractorEdicion/<int:pk>/', TractorUpdate.as_view(), name='tractor_editar'),
    path('otroEdicion/<int:pk>/', OtroUpdate.as_view(), name='otro_editar'),

    path('cosechadoraBorrado/<int:pk>/', CosechadoraDelete.as_view(), name='cosechadora_eliminar'),
    path('tractorBorrado/<int:pk>/', TractorDelete.as_view(), name='tractor_eliminar'),
    path('otroBorrado/<int:pk>/', OtroDelete.as_view(), name='otro_eliminar'),

    path('maquinaCreacion/', MaquinaCreacion.as_view(), name='nuevo'),

    path('cosechadoraDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario_cosechadora'),
    path('tractorDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario_tractor'),
    path('otroDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario_otro'),

    path('acercaDeMi/', views.about, name='acerca_de_mi'),
]
