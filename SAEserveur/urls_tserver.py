from django.urls import path

from . import views_tserver

urlpatterns = [

    path('', views_tserver.index),
    path('ajout/', views_tserver.ajout),
    path('traitement/', views_tserver.traitement),
    path('affiche/', views_tserver.affiche),
    path('affiche/<int:id>/',views_tserver.read),
    path('update/<int:id>/',views_tserver.update),
    path('traitementupdate/<int:id>/', views_tserver.traitementupdate),
    path('delete/<int:id>/', views_tserver.delete),
]