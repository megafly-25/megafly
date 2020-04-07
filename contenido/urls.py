from django.urls import path
from django.conf.urls import handler404
from .views import principal,pelicula,robots,sitemap,mi_error_404

urlpatterns = [
    path('',principal,name="principal"),
    path('peliculas/<slug>',pelicula,name="pelicula"),
    path('robots.txt',robots),
    path('sitemap.xml',sitemap),
]

handler404=mi_error_404