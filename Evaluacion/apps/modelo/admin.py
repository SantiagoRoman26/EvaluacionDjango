from django.contrib import admin


from apps.modelo.models import Estudiante
from apps.modelo.models import Materia

class AdminEstudiante(admin.ModelAdmin):
    list_display = ('cedula','apellidos','nombres')
    search_fields = ('nombres','apellidos','cedula')

    class Meta:
        model = Estudiante

admin.site.register(Estudiante, AdminEstudiante)


class AdminMateria(admin.ModelAdmin):
    list_display = ('nombre','nota_1','nota_2','nota_3')

    class Meta:
        model = Materia

admin.site.register(Materia, AdminMateria)
