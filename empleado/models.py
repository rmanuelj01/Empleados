from django.db import models

# Create your models here.

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre', null=False)
    cedula = models.CharField(max_length=50, verbose_name='Cédula', null=False)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento', null=False)
    email = models.EmailField(max_length=50, verbose_name='E-mail', null=False)
    telefono = models.CharField(max_length=50, verbose_name='Teléfono', null=False)
    