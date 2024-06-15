from django.shortcuts import render
from .forms import UtilForm
from django.http import HttpResponseRedirect
from . import models

# Create your views here.


def index(request):
    liste = list(models.Util.objects.all())
    return render(request, 'util/index.html', {'liste': liste})


def ajout(request):
    if request.method == "POST":
        form = UtilForm(request)
        if form.is_valid():
            util = form.save()
            return render(request, "util/affiche.html", {"util": util})

        else:
            return render(request, "util/ajout.html", {"form": form})
    else:
        form = UtilForm()
        return render(request, "util/ajout.html", {"form": form})
    

def traitement(request):
    lform = UtilForm(request.POST)
    if lform.is_valid():
        util = lform.save()
        return HttpResponseRedirect('/util/')
    else:
        return render(request,"util/ajout.html",{"form": util})
    


def read(request, id):
    util = models.Util.objects.get(pk=id)
    return render(request,"util/affiche.html",{"util": util})

def affiche(request):
    liste = list(models.Util.objects.all())
    return render(request, 'util/affiche.html', {'liste': liste})


def update(request,id):
    util = models.Util.objects.get(pk=id)
    form = UtilForm(util.dico())
    return render(request, "util/ajout.html", {'form':form, 'id':id })
 


def traitementupdate(request, id):
    lform = UtilForm(request.POST)
    if lform.is_valid():
        util = lform.save(commit=False) 
        util.id = id
        util.save()
        return HttpResponseRedirect("/util/")
    else:
        return render(request, "util/ajout.html", {"form": lform, "id": id})
    
def delete(request, id):
    util = models.Util.objects.get(pk=id)
    util.delete()
    return HttpResponseRedirect("/util/")
