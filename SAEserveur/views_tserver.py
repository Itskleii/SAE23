from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from . import models


def index(request):
    liste = list(models.Tserveur.objects.all())
    return render(request, 'tserver/index.html', {'liste': liste})


def affiche(request):
    liste = list(models.Tserveur.objects.all())
    return render(request, 'tserver/affiche.html', {'liste': liste})

def ajout(request):
    if request.method == "POST":
        form = TserveurForm(request)
        if form.is_valid():
            tserver = form.save()
            return render(request, "tserver/affiche.html", {"tserver": tserver})

        else:
            return render(request, "tserver/ajout.html", {"form": form})
    else:
        form = TserveurForm()
        return render(request, "tserver/ajout.html", {"form": form})
    

def traitement(request):
    lform = TserveurForm(request.POST)
    if lform.is_valid():
        lform = lform.save()
        return HttpResponseRedirect('/tserver/')
    else:
        return render(request,"tserver/ajout.html",{"form": lform})
    


def read(request, id):
    tserver = models.Tserveur.objects.get(pk=id)
    return render(request,"tserver/affiche.html",{"tserver": tserver})




def update(request,id):
    tserver = models.Tserveur.objects.get(pk=id)
    form = TserveurForm(tserver.dico())
    return render(request, "tserver/ajout.html", {'form':form, 'id':id })
 


def traitementupdate(request, id):
    lform = TserveurForm(request.POST)
    if lform.is_valid():
        tserver = lform.save(commit=False) 
        tserver.id = id
        tserver.save()
        return HttpResponseRedirect("/tserver/")
    else:
        return render(request, "tserver/ajout.html", {"form": lform, "id": id})
    
def delete(request, id):
    tserver = models.Tserveur.objects.get(pk=id)
    tserver.delete()
    return HttpResponseRedirect("/tserver/")
