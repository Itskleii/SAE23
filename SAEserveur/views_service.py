from django.shortcuts import render
from .forms import ServiceForm
from django.http import HttpResponseRedirect
from . import models
from .utils.system_check import check_resources
from django.contrib import messages 


# Create your views here.


def index(request):
    liste = list(models.Service.objects.all())
    return render(request, 'service/index.html', {'liste': liste})


def ajout(request):
    MIN_MEMORY_MB = 2048 
    MIN_CPUS = 2

    if not check_resources(MIN_MEMORY_MB, MIN_CPUS):
        messages.error(request, "Les ressources système ne sont pas suffisantes pour ajouter ce service.")
        return HttpResponseRedirect("/service/")


    if request.method == "POST":
        form = ServiceForm(request)
        if form.is_valid():
            service = form.save()
            return render(request, "service/affiche.html", {"service": service})

        else:
            return render(request, "service/ajout.html", {"form": form})
    else:
        form = ServiceForm()
        return render(request, "service/ajout.html", {"form": form})
    

def traitement(request):
    lform = ServiceForm(request.POST)
    if lform.is_valid():
        service = lform.save()
        return HttpResponseRedirect('/service/')
    else:
        return render(request,"service/ajout.html",{"form": lform})
    


def read(request, id):
    service = models.Service.objects.get(pk=id)
    return render(request,"service/affiche.html",{"service": service})

def affiche(request):
    liste = list(models.Service.objects.all())
    return render(request, 'service/affiche.html', {'liste': liste})


def update(request,id):
    service = models.Service.objects.get(pk=id)
    form = ServiceForm(service.dico())
    return render(request, "service/ajout.html", {'form':form, 'id':id })
 


def traitementupdate(request, id):
    lform = ServiceForm(request.POST)
    if lform.is_valid():
        service = lform.save(commit=False) 
        service.id = id
        service.save()
        return HttpResponseRedirect("/service/")
    else:
        return render(request, "service/ajout.html", {"form": lform, "id": id})
    
def delete(request, id):
    service = models.Service.objects.get(pk=id)
    service.delete()
    return HttpResponseRedirect("/service/")
