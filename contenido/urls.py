from django.urls import path
from .views import principal,pelicula

urlpatterns = [
    path('',principal,name="principal"),
    path('peliculas/<slug>',pelicula,name="pelicula"),
]