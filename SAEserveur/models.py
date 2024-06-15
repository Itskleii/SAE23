from django.db import models

# Kleiton

class Serveur(models.Model):
    nom = models.CharField(max_length=100)
    type = models.ForeignKey("Tserveur",on_delete=models.CASCADE)
    nb_processeur = models.IntegerField(blank=False)
    capacite_memoire = models.IntegerField(blank=False)
    capacite_stockage = models.IntegerField(blank=False)
    class Meta:
        managed : False
        db_table = 'SERVEUR'

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine
    
    def dico(self):
        return {"nom" : self.nom, "type": self.type, "nb_processeur":self.nb_processeur, "capacite_memoire": self.capacite_memoire, 'capacite_stockage': self.capacite_stockage}



class Service(models.Model):
    nom_service = models.CharField(max_length=100)
    date_lancement = models.DateField(blank=True)
    espace_memoire_utilise = models.IntegerField(blank=False)
    memoire_vive_necessaire = models.IntegerField(blank=False)
    serveur = models.ForeignKey("Serveur", on_delete=models.CASCADE, default=None)
    class Meta:
        managed : False
        db_table = 'SERVICE'

    def __str__(self):
        chaine = f"{self.nom_service}"
        return chaine
    
    def dico(self):
        return {'nom_service': self.nom_service, 'date_lancement': self.date_lancement, 'espace_memoire_utilise': self.espace_memoire_utilise, 'memoire_vive_necessaire': self.memoire_vive_necessaire, 'serveur': self.serveur}



class Application(models.Model):
    nom_application = models.CharField(max_length=100)
    logo = models.ImageField()
    utilisateur = models.CharField(max_length=25)
    class Meta:
        managed : False
        db_table = 'APPLICATION'

    def __str__(self):
        chaine = f"Le nom de l application est {self.nom_application}, et le(s) utilisateurs {self.utilisateur}"
        return chaine
    
    def dico(self):
        return {'nom_application': self.nom_application, 'utilisateur': self.utilisateur}



#Rechal

class Tserveur(models.Model):
    type = models.CharField(max_length=50)
    description = models.TextField()
    class Meta:
        managed : False
        db_table = 'TSERVEUR'


    def __str__(self):
        chaine = (f"{self.type}")
        return chaine

    def dico(self):
        return {"type": self.type, "description": self.description}

class Util(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    class Meta:
        managed : False
        db_table = 'UTIL'

    def __str__(self):
        chaine = (f"Le prenom de l'utilisateur est : {self.prenom} son nom est : {self.nom} puis son @email : {self.email} ")
        return chaine

    def dico(self):
        return {"nom": self.nom, "prenom": self.prenom, "email": self.email}