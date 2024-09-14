from django import views
from django.contrib import admin
from django.urls import path
from .views import TractorDelete, InstrumentoCreacion, TractorDetalle, CosechadoraLista, TractorLista, CosechadoraDetalle, TractorUpdate, CosechadoraUpdate, CosechadoraDelete, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, HomeView, ComentarioPagina
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
    # path('listaPedales/', PedalLista.as_view(), name='pedales'),
    # path('listaBaterias/', BateriaLista.as_view(), name='baterias'),
    # path('listaTeclados/', TecladoLista.as_view(), name='teclados'),
    # path('listaAmplificadores/', AmplificadorLista.as_view(), name='amplificadores'),
    # path('listaOtros/', OtroLista.as_view(), name='otros'),

    path('tractorDetalle/<int:pk>/', TractorDetalle.as_view(), name='tractor'),
    path('cosechadoraDetalle/<int:pk>/', CosechadoraDetalle.as_view(), name='cosechadora'),
    # path('pedalDetalle/<int:pk>/', PedalDetalle.as_view(), name='pedal'),
    # path('amplificadorDetalle/<int:pk>/', AmplificadorDetalle.as_view(), name='amplificador'),
    # path('tecladoDetalle/<int:pk>/', TecladoDetalle.as_view(), name='teclado'),
    # path('bateriaDetalle/<int:pk>/', BateriaDetalle.as_view(), name='bateria'),
    # path('otroDetalle/<int:pk>/', OtroDetalle.as_view(), name='otro'),

    path('tractorEdicion/<int:pk>/', TractorUpdate.as_view(), name='tractor_editar'),
    path('cosechadoraEdicion/<int:pk>/', CosechadoraUpdate.as_view(), name='cosechadora_editar'),
    # path('pedalEdicion/<int:pk>/', PedalUpdate.as_view(), name='pedal_editar'),
    # path('amplificadorEdicion/<int:pk>/', AmplificadorUpdate.as_view(), name='amplificador_editar'),
    # path('tecladoEdicion/<int:pk>/', TecladoUpdate.as_view(), name='teclado_editar'),
    # path('bateriaEdicion/<int:pk>/', BateriaUpdate.as_view(), name='bateria_editar'),
    # path('otroEdicion/<int:pk>/', OtroUpdate.as_view(), name='otro_editar'),


    path('tractorBorrado/<int:pk>/', TractorDelete.as_view(), name='tractor_eliminar'),
    path('cosechadoraBorrado/<int:pk>/', CosechadoraDelete.as_view(), name='cosechadora_eliminar'),
    # path('pedalBorrado/<int:pk>/', PedalDelete.as_view(), name='pedal_eliminar'),
    # path('amplificadorBorrado/<int:pk>/', AmplificadorDelete.as_view(), name='amplificador_eliminar'),
    # path('tecladoBorrado/<int:pk>/', TecladoDelete.as_view(), name='teclado_eliminar'),
    # path('bateriaBorrado/<int:pk>/', BateriaDelete.as_view(), name='bateria_eliminar'),
    # path('otroBorrado/<int:pk>/', OtroDelete.as_view(), name='otro_eliminar'),

    path('instrumentoCreacion/', InstrumentoCreacion.as_view(), name='nuevo'),

    path('tractorDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('cosechadoraDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    # path('pedalDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    # path('amplificadorDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    # path('bateriaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    # path('tecladoDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    # path('otroDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    path('acercaDeMi/', views.about, name='acerca_de_mi'),
]


# from AppConci import views
# from django.urls import path
# from django.contrib import admin

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
#     path('agregar_tractor/', views.agregar_tractor, name='agregar_tractor'),
#     path('agregar_cosechadora/', views.agregar_cosechadora, name='agregar_cosechadora'),
#     path('search/', views.search, name='search'),
#     path('AcercaDeMi/', views.about, name='acerca_de_mi'),
# ]
