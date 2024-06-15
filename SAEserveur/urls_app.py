

from django.urls import path

from . import views_app


urlpatterns = [


    path('', views_app.index),
    path('ajout/', views_app.ajout),
    path('traitement/', views_app.traitement),
    path('affiche/', views_app.affiche),
    path('affiche/<int:id>/',views_app.read),
    path('update/<int:id>/',views_app.update),
    path('traitementupdate/<int:id>/', views_app.traitementupdate),
    path('delete/<int:id>/', views_app.delete),
]