"""
URL configuration for serveur project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import static
from django.conf.urls.static import static
from . import settings
import SAEserveur

urlpatterns = [
    path('admin/', admin.site.urls),
    path('serveur/', include('SAEserveur.urls')),
    path('tserver/', include('SAEserveur.urls_tserver')),
    path('application/', include('SAEserveur.urls_app')),
    path('service/', include('SAEserveur.urls_service')),
    path('util/', include('SAEserveur.urls_util')),
]


if settings.DEBUG == True:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)