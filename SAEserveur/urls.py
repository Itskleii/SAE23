from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.index),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/', views.affiche),
    path('affiche/<int:id>/',views.read),
    path('update/<int:id>/',views.update),
    path('traitementupdate/<int:id>/', views.traitementupdate),
    path('delete/<int:id>/', views.delete),
    path('<int:id>/pdf/', views.generate_pdf, name='generate_pdf'),





   
   
]