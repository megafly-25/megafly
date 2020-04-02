from django.shortcuts import render,get_object_or_404
from .models import peliculas
# Create your views here.
def principal(request):
    pelicula=peliculas.objects.get_queryset().order_by('id')
    data={
        'peliculas':pelicula,
    }
    return render(request,"principal.html",data)

def pelicula(request,slug):
    pelicula=get_object_or_404(peliculas,slug_peliculas=slug)
    data={
        'pelicula':pelicula,
    }
    return render(request,"pelicula.html",data)
