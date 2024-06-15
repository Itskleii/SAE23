from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models



class ServeurForm(ModelForm):
    class Meta:
        model = models.Serveur
        fields = ('nom', 'type', 'nb_processeur', 'capacite_memoire','capacite_stockage')
        labels = {
            'nom' : _('Nom'),
            'type' : _('Type') ,
            'nb_processeur' : _('nombre de processeur'),
            'capacite_memoire' : _('Capacité de la mémoire'),
            'capacite_stockage': _('Capacité de stockage'),
        }



class ServiceForm(ModelForm):
    class Meta:
        model = models.Service
        fields = ('nom_service', 'date_lancement', 'espace_memoire_utilise', 'memoire_vive_necessaire','serveur')
        labels = {
            'nom_service' : _('Nom du service'),
            'date_lancement' : _('Date du lancement ') ,
            'espace_memoire_utilise' : _('espace memoire utilise'),
            'memoire_vive_necessaire' : _('memoire vive necessaire'),
            'serveur': _('Serveur de lancement'),
        }


class ApplicationForm(ModelForm):
    class Meta:
        model = models.Application
        fields = ('nom_application', 'logo','utilisateur')
        labels = {
            'nom_application' : _('nom de l application '),
            'logo' : _('logo'),
            'utilisateur': _('utilisateur')
        }


# Rechal

class UtilForm(ModelForm):
    class Meta:
        model = models.Util
        fields = {'nom','prenom','email'}
        labels = {
            'nom': _('Nom'),
            'prenom': _('Prenom'),
            'email': _('Email')
        }

    
class TserveurForm(ModelForm):
    class Meta:
        model = models.Tserveur
        fields = {'type','description'}
        labels = {
            'type': _('Type'),
            'description': _('Description')
        }
