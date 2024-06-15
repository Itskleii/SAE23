from django.shortcuts import render
from .forms import ApplicationForm
from django.http import HttpResponseRedirect
from . import models
from .utils.system_check import check_resources
from django.contrib import messages 

# Create your views here.

def index(request):
    return render(request, 'application/index.html')

def affiche(request):
    liste = list(models.Application.objects.all())
    return render(request, 'application/affiche.html', {'liste': liste})


def ajout(request):
    MIN_MEMORY_MB = 2048 
    MIN_CPUS = 2

    if not check_resources(MIN_MEMORY_MB, MIN_CPUS):
        messages.error(request, "Les ressources système ne sont pas suffisantes pour ajouter ce service.")
        return HttpResponseRedirect("/application/")




    if request.method == "POST":
        form = ApplicationForm(request)
        if form.is_valid():
            application = form.save()
            return render(request, "application/affiche.html", {"application": application})

        else:
            return render(request, "application/ajout.html", {"form": form})
    else:
        form = ApplicationForm()
        return render(request, "application/ajout.html", {"form": form})
    

def traitement(request):
    lform = ApplicationForm(request.POST, request.FILES)
    if lform.is_valid():
        application = lform.save()
        return HttpResponseRedirect('/application/')
    else:
        return render(request,"application/ajout.html",{"form": lform})
    


def read(request, id):
    application = models.Application.objects.get(pk=id)
    return render(request,"application/affiche.html",{"application": application})



def affiche(request):
    liste = list(models.Application.objects.all())
    return render(request, 'application/affiche.html', {'liste': liste})

def update(request,id):
    application = models.Application.objects.get(pk=id)
    form = ApplicationForm(application.dico())
    return render(request, "application/ajout.html", {'form':form, 'id':id })
 


def traitementupdate(request, id):
    lform = ApplicationForm(request.POST)
    if lform.is_valid():
        application = lform.save(commit=False) 
        application.id = id
        application.save()
        return HttpResponseRedirect("/application/")
    else:
        return render(request, "application/ajout.html", {"form": lform, "id": id})
    
def delete(request, id):
    application = models.Application.objects.get(pk=id)
    application.delete()
    return HttpResponseRedirect("/application/")
