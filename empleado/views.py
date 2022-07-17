from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def crear(request):
    return render(request, 'empleados/crear.html')

def editar(request):
    return render(request, 'empleados/editar.html')