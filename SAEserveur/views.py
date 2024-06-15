from django.shortcuts import render
from .forms import ServeurForm
from django.http import HttpResponseRedirect
from . import models
import reportlab
from reportlab import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from .models import Serveur





# Create your views here.


def index(request):
    return render(request, 'serveur/index.html')

def affiche(request):
    liste = list(models.Serveur.objects.all())
    return render(request, 'serveur/affiche.html', {'liste': liste})

def ajout(request):
    if request.method == "POST":
        form = ServeurForm(request)
        if form.is_valid():
            serveur = form.save()
            return render(request, "serveur/affiche.html", {"serveur": serveur})

        else:
            return render(request, "serveur/ajout.html", {"form": form})
    else:
        form = ServeurForm()
        return render(request, "serveur/ajout.html", {"form": form})
    
def traitement(request):
    lform = ServeurForm(request.POST)
    if lform.is_valid():
        Serveur = lform.save()
        return HttpResponseRedirect('/serveur/affiche/')
    else:
        return render(request,"serveur/ajout.html",{"form": lform})
    


def read(request, id):
    serveur = models.Serveur.objects.get(pk=id)
    return render(request,"serveur/affiche.html",{"serveur": serveur})




def update(request,id):
    serveur = models.Serveur.objects.get(pk=id)
    form = ServeurForm(serveur.dico())
    return render(request, "serveur/ajout.html", {'form':form, 'id':id })
 


def traitementupdate(request, id):
    lform = ServeurForm(request.POST)
    if lform.is_valid():
        serveur = lform.save(commit=False) 
        serveur.id = id
        serveur.save()
        return HttpResponseRedirect("/serveur/")
    else:
        return render(request, "serveur/ajout.html", {"form": lform, "id": id})
    
def delete(request, id):
    serveur = models.Serveur.objects.get(pk=id)
    serveur.delete()
    return HttpResponseRedirect("/serveur/")




def generate_pdf(request, id):
    serveur = get_object_or_404(Serveur, pk=id)
    services = serveur.service_set.all()

    # Créer une réponse HTTP avec un type de contenu PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="fiche_serveur_{serveur.nom}.pdf"'

    # Créer un canvas ReportLab
    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    # Titre
    p.setFont("Helvetica-Bold", 20)
    p.drawString(100, height - 100, f"Fiche du serveur {serveur.nom}")

    # Informations du serveur
    p.setFont("Helvetica", 12)
    p.drawString(100, height - 140, f"Type : {serveur.nom}")
    p.drawString(100, height - 160, f"Nombre de processeurs : {serveur.nb_processeur}")
    p.drawString(100, height - 180, f"Capacité mémoire : {serveur.capacite_memoire} Go")
    p.drawString(100, height - 200, f"Capacité de stockage : {serveur.capacite_stockage} Go")

    # Liste des services
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, height - 240, "Services lancés :")

    p.setFont("Helvetica", 12)
    y = height - 260
    for service in services:
        p.drawString(100, y, f"Nom du service : {service.nom_service}")
        p.drawString(100, y - 20, f"Date de lancement : {service.date_lancement}")
        p.drawString(100, y - 40, f"Espace mémoire utilisé : {service.espace_memoire_utilise} Go")
        p.drawString(100, y - 60, f"Mémoire vive nécessaire : {service.memoire_vive_necessaire} Go")
        y -= 80
        if y < 100:  # Nouvelle page si l'espace n'est plus suffisant
            p.showPage()
            y = height - 100

    # Fermer le PDF
    p.showPage()
    p.save()

    return response