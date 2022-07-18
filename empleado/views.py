from django.shortcuts import render
from empleado.forms import LibroForm
from .models import Empleado

# Create your views here.

def inicio(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/index.html', {'empleados': empleados})

def login(request):
    return render(request, 'login.html')

def crear(request):
    return render(request, 'empleados/crear.html')

def editar(request):
    return render(request, 'empleados/editar.html')