from django.shortcuts import render, redirect
from apps.modelo.models import Estudiante
from .forms import formularioEstudiante, formularioMateria
# Create your views here.
def index(request):
    listaEstudiantes=Estudiante.objects.all() 
    return render(request, 'estudiantes/index.html',locals())
def crearEstudiante(request):
    formulario_Estudiante=formularioEstudiante(request.POST)
    formulario_Materia=formularioMateria(request.POST)
    if request.method=='POST':
        if formulario_Estudiante.is_valid() :
            estudiante=Estudiante()
            datos_estudiante=formulario_Estudiante.cleaned_data
            estudiante.cedula=datos_estudiante.get('cedula')
            estudiante.nombres=datos_estudiante.get('nombres')
            estudiante.apellidos=datos_estudiante.get('apellidos')
            estudiante.save()
        return redirect(index)
    return render(request, 'estudiantes/crear.html', locals())
def modificarEstudiante(request):
    return render(request, "hola modificarE")
def eliminarEstudiante(request):
    return render(request, "hola eliminarE")
def crearMateria(request):
    return render(request, "hola crearM")
def modificarMateria(request):
    return render(request, "hola modificarM")
def eliminarMateria(request):
    return render(request, "hola eliminarM")
