from AppConci import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('agregar_tractor/', views.agregar_tractor, name='agregar_tractor'),
    path('agregar_cosechadora/', views.agregar_cosechadora, name='agregar_cosechadora'),
    path('search/', views.search, name='search'),
]

# from AppConci import views
# from django.urls import path

# urlpatterns = [
#     path('inicio/', views.inicio),
#     path('agregar_cliente/', views.agregar_cliente),
#     path('agregar_cosechadoras/', views.agregar_cosechadoras),
#     path('agregar_tractores/', views. agregar_tractores),
#     path('agregar_ventas/', views.agregar_ventas),
#     path('clienteFormulario/', views.clienteFormulario, name='Agregar_cliente'),
#     path('clienteFormulario/', views.clienteFormulario, name='Agregar_cliente'),
#     path('clienteFormulario/', views.clienteFormulario, name='Agregar_cliente'),
#     path('clienteFormulario/', views.clienteFormulario, name='Agregar_cliente'),            
#     path('cliente_Formulario_2/', views.cliente_Formulario_2, name='cliente_Formulario_2'),
# ]