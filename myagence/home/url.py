from django.urls import path
from . import views



urlpatterns = [
    path('home'     , views.home       ,   name='home'),
    path('logout'   , views.deconnecter,   name='logout'),  # Ajoutez cette route pour déconnexion
    path('config'   , views.config     ,   name='config'),
    path('robot'    , views.robot      ,   name='robot'),
    path('bras'     , views.bras       ,   name='bras'),
]
