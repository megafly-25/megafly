from django.shortcuts import render

# Create your views here.
def principal_cursos(request):
    return render(request,"principal_cursos.html")
def cursos(request):
    return render(request,"cursos.html")
def cupones(request):
    return render(request,"cupones.html")