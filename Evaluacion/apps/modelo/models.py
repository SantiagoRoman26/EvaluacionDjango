from django.db import models

# Create your models here.
class Estudiante(models.Model):
    estudiante_id=models.AutoField(primary_key=True)
    cedula=models.CharField(max_length=10, unique = True, null = False)
    nombres=models.CharField(max_length=70)
    apellidos=models.CharField(max_length=70)

    def __str__ (self):
        return self.cedula

class Materia(models.Model):
    materia_id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=70 , null=False)
    promedio=models.CharField(max_length=10 , null=False)
    estado=models.CharField(max_length=10 , null=False)
    nota_1=models.CharField(max_length=10)
    nota_2=models.CharField(max_length=10)
    nota_3=models.CharField(max_length=10)
    
