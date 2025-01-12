"""myagence URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.views.static import serve
from django.urls import re_path
# Importez la fonction handle_404 depuis l'application 'accueil' (ou celle que vous avez choisie)

handler404 = 'home.views.page_not_found'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(''      , include('login.url')),
    path(''      , include('home.url')),  
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
]
