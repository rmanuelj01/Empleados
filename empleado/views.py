from django.shortcuts import render, redirect
from empleado.forms import EmpleadoForm
from .models import Empleado
from .filters import OrderFilter


# Create your views here.

def login(request):
    return render(request, 'login.html')

def inicio(request):
    empleados = Empleado.objects.all()
    myFilter = OrderFilter(request.GET)
    return render(request, 'empleados/index.html', {'empleados': empleados}, {'myFilter': myFilter})

def crear(request):
    formulario = EmpleadoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('inicio')
    return render(request, 'empleados/crear.html', {'formulario': formulario})

def editar(request, id):
    empleado = Empleado.objects.get(id=id)
    formulario = EmpleadoForm(request.POST or None, instance=empleado)
    if formulario.is_valid():
        formulario.save()
        return redirect('inicio')
    return render(request, 'empleados/editar.html', {'formulario': formulario})

def eliminar(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('inicio')