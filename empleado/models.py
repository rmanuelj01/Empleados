from django.db import models

# Create your models here.

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    cedula = models.CharField(max_length=50, verbose_name='Cédula')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=50, verbose_name='Teléfono')
    