from django.shortcuts import render
from .models import curso

# Create your views here.

def home(request):
    cursos = curso.objects.all()
    return render(request, "gestioncursos.html",{"cursos": cursos})
