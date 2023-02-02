from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate

from .form import RegisterForm

def index(request):
    return render(request, 'index.html',{

    })

def login_view(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos')


    return render(request, 'users/login.html', {
        
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')

def register(request):
    form = RegisterForm()
    return render(request, 'users/register.html', {
        'form': form,
    })