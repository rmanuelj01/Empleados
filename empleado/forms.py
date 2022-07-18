from django import forms
from .models import Empleado

class LibroForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'