from django.contrib import admin
from .models import categorias,gamespc,gamespsx,gamesps2,gamesps3,peliculas,series,temporadas,ntemporada,capitulos,ncapitulos
# Register your models here.
class PeliculaAdmin(admin.ModelAdmin):
    list_display=['nombre','fecha_estreno','online','disco']
    search_fields=['nombre','nombre_original','descripcion','region','anio','fecha_subida','director','reparto','online']
    list_filter=['genero']
class CategoriaAdmin(admin.ModelAdmin):
    def get_queryset(self,request):
        queryset=super(CategoriaAdmin,self).get_queryset(request)
        queryset=queryset.order_by('nombre')
        return queryset
class GamespcAdmin(admin.ModelAdmin):
    list_display=['nombre','fecha_estreno','disco','enlace_publi']
    search_fields=['nombre','nombre_original','descripcion','anio','fecha_subida','disco']
    list_filter=['genero']
class GamespsxAdmin(admin.ModelAdmin):
    list_display=['nombre','fecha_estreno','disco','enlace_publi']
    search_fields=['nombre','nombre_original','descripcion','anio','fecha_subida','disco']
    list_filter=['genero']
class Gamesps2Admin(admin.ModelAdmin):
    list_display=['nombre','fecha_estreno','disco','enlace_publi']
    search_fields=['nombre','nombre_original','descripcion','anio','fecha_subida','disco']
    list_filter=['genero']
class Gamesps3Admin(admin.ModelAdmin):
    list_display=['nombre','fecha_estreno','disco','enlace_publi']
    search_fields=['nombre','nombre_original','descripcion','anio','fecha_subida','disco']
    list_filter=['genero']
class SeriesAdmin(admin.ModelAdmin):
    list_display=['nombre','nombre_original','fecha_estreno']
    search_fields=['nombre','nombre_original','descripcion','region','anio','fecha_subida','director','reparto','online']
    list_filter=['genero']
class TemporadasAdmin(admin.ModelAdmin):
    list_display=['nombre','ntemporada','serie']
    search_fields=['nombre','nombre_original','descripcion','anio','fecha_subida','ntemporada','online']
    list_filter=['serie']
class CapitulosAdmin(admin.ModelAdmin):
    list_display=['nombre','ncapitulo','temporada']
    search_fields=['nombre','ncapitulo','nombre_original','descripcion','anio','fecha_subida','temporada','temporada','online']
    list_filter=['temporada']
admin.site.register(categorias,CategoriaAdmin)
admin.site.register(gamespc,GamespcAdmin)
admin.site.register(gamespsx,GamespsxAdmin)
admin.site.register(gamesps2,Gamesps3Admin)
admin.site.register(gamesps3,Gamesps3Admin)
admin.site.register(peliculas,PeliculaAdmin)
admin.site.register(series,SeriesAdmin)
admin.site.register(temporadas,TemporadasAdmin)
admin.site.register(ntemporada)
admin.site.register(capitulos,CapitulosAdmin)
admin.site.register(ncapitulos)
admin.site.site_header="Megafly Admin"
admin.site.index_title="Megafly Admin"
admin.site.site_title="Megafly Admin"
    