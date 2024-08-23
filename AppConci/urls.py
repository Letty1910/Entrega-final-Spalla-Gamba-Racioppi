from AppConci import views
from django.urls import path

urlpatterns = [
    path('inicio/', views.inicio),
    path('agregar_cliente/', views.agregar_cliente),
    path('agregar_cosechadoras/', views.agregar_cosechadoras),
    path('agregar_tractores/', views. agregar_tractores),
    path('agregar_ventas/', views.agregar_ventas),
    path('clienteFormulario/', views.clienteFormulario, name='ClienteFormulario'),
    path('cliente_Formulario_2/', views.cliente_Formulario_2, name='cliente_Formulario_2'),
]