

from django.urls import path

from . import views_util


urlpatterns = [


    path('', views_util.index),
    path('ajout/', views_util.ajout),
    path('traitement/', views_util.traitement),
    path('affiche/', views_util.affiche),
    path('affiche/<int:id>/',views_util.read),
    path('update/<int:id>/',views_util.update),
    path('traitementupdate/<int:id>/', views_util.traitementupdate),
    path('delete/<int:id>/', views_util.delete),
]