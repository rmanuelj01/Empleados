from django.shortcuts import render, redirect
from empleado.forms import LibroForm
from .models import Empleado

# Create your views here.

def login(request):
    return render(request, 'login.html')

def inicio(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/index.html', {'empleados': empleados})

def crear(request):
    formulario = LibroForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('inicio')
    return render(request, 'empleados/crear.html', {'formulario': formulario})

def editar(request, id):
    empleado = Empleado.objects.get(id=id)
    formulario = LibroForm(request.POST or None, instance=empleado)
    if formulario.is_valid():
        formulario.save()
        return redirect('inicio')
    return render(request, 'empleados/editar.html', {'formulario': formulario})

    return render(request, 'empleados/editar.html')