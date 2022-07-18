from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def inicio(request):
    return HttpResponse("<h1>Hola Solmin</h1>")
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'orden/index.html', {'ordenes': ordenes})
def crear_orden(request):
    formularioorden = OrdenForm(request.POST or None, request.FILES or None)
    if formularioorden.is_valid():
        formularioorden.save()
        return redirect('ordenes')
    return render(request, 'orden/crear.html', {'formularioorden': formularioorden})
def editar_orden(request, Nro_orden):
    ordenes = Orden.objects.get(Nro_orden=Nro_orden)
    formularioorden = OrdenForm(request.POST or None, request.FILES or None, instance=ordenes)
    if formularioorden.is_valid() and request.POST:
        formularioorden.save()
        return redirect('ordenes')
    return render(request, 'orden/editar.html', {'formularioorden': formularioorden})
def eliminar_orden(request, Nro_orden):
    ordenes = Orden.objects.get(Nro_orden=Nro_orden)
    ordenes.delete()
    return redirect('ordenes')

def clientes(request):
    return render(request, 'cliente/index.html')

def soldadoras(request):
    return render(request, 'soldadora/index.html')

def encargados(request):
    return render(request, 'encargado/index.html')

def elementos(request):
    return render(request, 'elementos/index.html') 

def planchados(request):
    return render(request, 'planchado/index.html')