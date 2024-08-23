from django.shortcuts import render
from django.http import HttpResponse
from AppConci.models import clienteFormulario


def inicio(request):
    return render(request, 'appconci/index.html')

def agregar_cliente(request):
    return render(request, 'appconci/cliente.html')

def agregar_cosechadoras(request):
    return render(request, 'appconci/cosechadoras.html')

def agregar_tractores(request):
    return render(request, 'appconci/tractores.html')

def agregar_ventas(request):
    return render(request, 'appconci/ventas.html')

def clienteFormulario(request):
    if request.method =='POST':
        cliente = cliente(nombre_completo=request.POST['cliente'], cuit=request.POST['cuit', email=request.POST['email'], localidad=request.POST['localidad'] ])
        cliente.save()
        return render(request, "AppConci/index.html")
    return render(request,'appconci/clienteFormulario.html')

def cliente_Formulario_2(request):
    if request.method == "POST":  
        miFormulario = clienteFormulario(request.POST)  
        print(miFormulario) 

        if miFormulario.is_valid():  
            informacion = miFormulario.cleaned_data  
            cliente = cliente(nombre=informacion["nombre"], camada=informacion["cuit"])  
            cliente.save()  
            return render(request, "AppConci/index.html")  
    else:
        miFormulario = clienteFormulario()  

    return render(request, "AppConci/cliente_Formulario_2.html", {"miFormulario": miFormulario})
