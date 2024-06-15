from django.urls import path

from . import views_service


urlpatterns = [

    path('', views_service.index),
    path('ajout/', views_service.ajout),
    path('traitement/', views_service.traitement),
    path('affiche/', views_service.affiche),
    path('affiche/<int:id>/',views_service.read),
    path('update/<int:id>/',views_service.update),
    path('traitementupdate/<int:id>/', views_service.traitementupdate),
    path('delete/<int:id>/', views_service.delete),
]