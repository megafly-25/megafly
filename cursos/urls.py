from django.urls import path
from django.conf.urls import handler404
from contenido.views import mi_error_404
from .views import principal_cursos,cursos,cupones
from contenido.sitemaps import PeliculasSitemap

urlpatterns = [
    path('cursos-online',principal_cursos,name='principal_cursos'),
    path('cursos',cursos,name='cursos'),
    path('cupones-online',cupones,name='cupones')
]


handler404=mi_error_404