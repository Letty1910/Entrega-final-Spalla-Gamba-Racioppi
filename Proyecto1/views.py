from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader
from AppConci.models import Cliente

def saludo(request):
    return HttpResponse("Hola clientes del Grupo Conci")
def otra_vista(request):
    return HttpResponse("<h1>¡Esto es un título!</h1><p>Y este es un párrafo.</p>")
def dia_de_hoy(request):
    hoy = datetime.today()
    return HttpResponse(f"Hoy es {hoy}")
def muestra_nombre(self, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido al Grupo Conci")

# Agregamos al encabezado del archivo el import de Template y de Context


def probando_template(request):

    nom = "Agustin"
    ap = "Spalla"
    listaDeNotas = [10, 1, 5, 3, 9]
    diccionario = {'nombre': nom, 'apellido': ap, "hoy": datetime.now, "Notas":listaDeNotas}

    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario)

    # # Abrimos el archivo html
    # mi_html = open('C:/Users/Agustin Spalla/Documents/Coderhouse/Tercera pre-entrega+Spalla/TerceraPreEntrega/Proyecto1/plantillas/template1.html')

    # # Creamos el template haciendo uso de la clase Template
    # plantilla = Template(mi_html.read())

    # # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    # mi_html.close()

    # # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    # mi_contexto = Context(diccionario)

    # # Terminamos de construír el template renderizándolo con su contexto
    # documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)

def agregar_cliente(request, nom, cuit, email, localidad):
    cliente = Cliente(nombre_completo=nom, cuit=cuit, email=email, localidad=localidad)
    cliente.save()

    return HttpResponse("Se ha agregado un nuevo cliente")

def agregar_cosechadora(request, familia, modelo, serie):
    cosechadoras = cosechadoras(familia=familia, modelo=modelo, serie=serie)
    cosechadoras.save()

    return HttpResponse("Se ha registrado una nueva cosechadora")

def agregar_tractor(request, familia, modelo, serie):
    tractores = tractores(familia=familia, modelo=modelo, serie=serie)
    tractores.save()

    return HttpResponse("Se ha registrado un nuevo tractor")

def agregar_venta(request, cuit, fecha, entregado):
    ventas = ventas(cuit=cuit, fecha_de_venta=fecha, entrega=entregado)
    ventas.save()

    return HttpResponse("Se ha registrado una nueva venta, felicitaciones!!!")