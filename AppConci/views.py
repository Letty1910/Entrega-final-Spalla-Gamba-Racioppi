from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppConci.forms import clienteFormulario, tractoresFormulario, cosechadorasFormulario, SearchForm
from AppConci.models import Cliente, Tractor, Cosechadora

def index(request):
    return render(request, 'index.html')

def agregar_cliente(request):
    if request.method == 'POST':
        form = clienteFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = clienteFormulario()
    return render(request, 'add_cliente.html', {'form': form})

def agregar_tractor(request):
    if request.method == 'POST':
        form = tractoresFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = tractoresFormulario()
    return render(request, 'add_tractor.html', {'form': form})

def agregar_cosechadora(request):
    if request.method == 'POST':
        form = cosechadorasFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cosechadorasFormulario()
    return render(request, 'add_cosechadora.html', {'form': form})

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            clientes = Cliente.objects.filter(nombre_completo__icontains=query)
            tractores = Tractor.objects.filter(familia__icontains=query)
            cosechadoras = Cosechadora.objects.filter(familia__icontains=query)
            return render(request, 'search_results.html', {'clientes': clientes, 'tractores': tractores, 'cosechadoras': cosechadoras})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})

