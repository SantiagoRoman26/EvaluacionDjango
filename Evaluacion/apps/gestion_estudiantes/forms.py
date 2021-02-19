from django import forms
from apps.modelo.models import Estudiante, Materia

class formularioEstudiante(forms.ModelForm):
    class Meta:
        model=Estudiante
        fields=["cedula","nombres","apellidos"]

class formularioMateria(forms.ModelForm):
    class Meta:
        model=Materia
        fields=["nombre","nota_1","nota_2","nota_3"]