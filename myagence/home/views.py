from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
from django.http import HttpResponseNotFound

personnes = [
        {'id': 1, 'name': 'Jean Dupont', 'age': 30, 'job': 'Développeur'},
        {'id': 2, 'name': 'Marie Curie', 'age': 35, 'job': 'Scientifique'},
        {'id': 3, 'name': 'Paul Martin', 'age': 40, 'job': 'Médecin'}
]

var='3'

@login_required(login_url='/login')
def home(request):
    print(f"Utilisateur connecté : {request.user.is_authenticated}")
    name = None
    email = None
    if request.method == 'GET':
        return render(request, 'home.html',{'list_personne': personnes, 'var': var})
    if request.method == 'POST':
        # Récupérer les données envoyées par le formulaire
        name  = request.POST.get('name')
        email = request.POST.get('email')

        # Passer les données au template pour affichage
        return render(request, 'home.html', {'name': name, 'email': email,'list_personne': personnes, 'var': var})

def page_not_found(request, exception):
    return redirect('/home')

def deconnecter(request):
    logout(request)  # Déconnecter l'utilisateur
    return redirect('/login')  # Rediriger vers la page de connexion après déconnexion

@login_required(login_url='/login')
# Fonction pour afficher la première section
def config(request):
    return render(request, 'config.html')

@login_required(login_url='/login')
# Fonction pour afficher la deuxième section
def robot(request):
    return render(request, 'robot.html')

@login_required(login_url='/login')
# Fonction pour afficher la troisième section
def bras(request):
    return render(request, 'bras.html')