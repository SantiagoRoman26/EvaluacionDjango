
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index,name="estudiantes"),
    path('crearEstudiante', views.crearEstudiante,name="crear"),
]