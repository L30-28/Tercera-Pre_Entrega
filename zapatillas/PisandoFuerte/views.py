from django.shortcuts import render

from .models import*
from .forms import*

#from django.views.generic import ListView
#from django.views.generic import CreateView
#from django.views.generic import UpdateView
#from django.views.generic import DeleteView
#from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, "PisandoFuerte/index.html")

def nike(request):
    contexto= {'nike':Nike.objects.all()}
    return render(request, "PisandoFuerte/Nike.html",contexto)

def adidas(request):
    contexto= {'adidas':Adidas.objects.all()}
    return render(request, "PisandoFuerte/Adidas.html",contexto)

def puma(request):
    contexto= {'puma':Puma.objects.all()}
    return render(request, "PisandoFuerte/Puma.html",contexto)

def remeras(request):
    contexto= {'remeras':Remeras.objects.all()}
    return render(request, "PisandoFuerte/Remeras.html",contexto)

#__________________________________Forms
def zapatillaForm(request):
    if request.method == "POST":
        miForm = ZapatillaForm(request.POST)
        if miForm.is_valid():
            zapatilla_modelo=miForm.cleaned_data.get("modelo")
            zapatilla_talle=miForm.cleaned_data.get("talle")
            zapatilla = Adidas(modelo=zapatilla_modelo, talle=zapatilla_talle)
            zapatilla.save()
            
            contexto= {'adidas':Adidas.objects.all()}
            return render(request, "PisandoFuerte/Adidas.html",contexto)
    else:
        miForm= ZapatillaForm()
        
    return render(request, "PisandoFuerte/zapatillaForm.html", {"form":miForm})

def nikeform(request):
    if request.method == "POST":
        miForm = NikeForm(request.POST)
        if miForm.is_valid():
            nike_modelo=miForm.cleaned_data.get("modelo")
            nike_talle=miForm.cleaned_data.get("talle")
            nike = Nike(modelo=nike_modelo, talle=nike_talle)
            nike.save()
            
            contexto= {'nike':Nike.objects.all()}
            return render(request, "PisandoFuerte/Nike.html",contexto)
    else:
        miForm= NikeForm()
        
    return render(request, "PisandoFuerte/nikeForm.html", {"form":miForm})

def pumaform(request):
    if request.method == "POST":
        miForm = PumaForm(request.POST)
        if miForm.is_valid():
            puma_modelo=miForm.cleaned_data.get("modelo")
            puma_talle=miForm.cleaned_data.get("talle")
            puma = Puma(modelo=puma_modelo, talle=puma_talle)
            puma.save()
            
            contexto= {'puma':Puma.objects.all()}
            return render(request, "PisandoFuerte/Puma.html",contexto)
    else:
        miForm= PumaForm()
        
    return render(request, "PisandoFuerte/pumaForm.html", {"form":miForm})

def remerasform(request):
    if request.method == "POST":
        miForm = RemerasForm(request.POST)
        if miForm.is_valid():
            remeras_color=miForm.cleaned_data.get("color")
            remeras_talle=miForm.cleaned_data.get("talle")
            remeras = Remeras(color=remeras_color, talle=remeras_talle)
            remeras.save()
            
            contexto= {'remeras':Remeras.objects.all()}
            return render(request, "PisandoFuerte/Remeras.html",contexto)
    else:
        miForm= RemerasForm()
        
    return render(request, "PisandoFuerte/remerasForm.html", {"form":miForm})

#________________________________Buscar

def buscar(request):
    return render (request, "PisandoFuerte/buscar.html")

def encontrar(request):
    if request.GET["buscar"]:
        patron=request.GET["buscar"]
        zapatillas=Adidas.objects.filter(modelo__icontains=patron)
        contexto = {"adidas":zapatillas}
        return render(request, "PisandoFuerte/Adidas.html",contexto)
    
        
    contexto= {'adidas':Adidas.objects.all()}
    return render(request, "PisandoFuerte/Adidas.html",contexto)

#_________________________________________Nike

#class NikeList(ListView):
    model = Nike
    
#class NikeCreate(CreateView):
    model = Nike
    fields = ["modelo", "talle"]
    success_url = reverse_lazy("nike")
    
#class NikeUpgrade(UpdateView):
    model = Nike
    fields = ["modelo", "talle"]
    success_url = reverse_lazy("nike")
    
#class NikeDelete(DeleteView):
    model = Nike
    success_url = reverse_lazy("nike")
    