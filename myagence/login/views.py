from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)
        
        if user is not None:
            # Connexion réussie
            auth_login(request, user)
            print("Connexion réussie")
            # Rediriger vers la page demandée après la connexion
            # next_url = request.GET.get('next', 'home')  # Redirige vers /home/ ou vers la page spécifiée
            return redirect('/home')
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect"
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')