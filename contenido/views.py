from django.shortcuts import render,get_object_or_404
from .models import peliculas
# Create your views here.
def principal(request):
    pelicula=peliculas.objects.get_queryset().order_by('id')
    pocos_requisitos=peliculas.objects.all()[:8]
    medios_requisitos=peliculas.objects.all()[8:16]
    altos_requisitos=peliculas.objects.all()[16:23]
    mas_visitados=peliculas.objects.all()[15:23]
    mas_descargados=peliculas.objects.all()[:8]
    last_film_add=peliculas.objects.get_queryset().order_by('-id')[:8]
    data={
        'peliculas':pelicula,
        'pocos_requisitos':pocos_requisitos,
        'medios_requisitos':medios_requisitos,
        'altos_requisitos':altos_requisitos,
        'mas_visitados':mas_visitados,
        'mas_descargados':mas_descargados,
        'last_film_add':last_film_add,
        
    }
    return render(request,"principal.html",data)

def pelicula(request,slug):
    pelicula=get_object_or_404(peliculas,slug_peliculas=slug)
    data={
        'pelicula':pelicula,
    }
    return render(request,"pelicula.html",data)
