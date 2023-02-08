from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .forms import RegisterForm

def index(request):
    title = 'Index'
    return render(request, 'index.html',{
        'title': title
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
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username = form.cleaned_data['username'] , password = form.cleaned_data['password1'] )
            login(request, user)
            messages.success(request, f'{ username } registrado con exitó')
            return redirect('index')
        
        else: 
            messages.error(request, 'Usuario o Contraseña incorrectos')
        
    else:
        form= RegisterForm()
        
    context = {'form' : form} 
    return render(request, 'users/register.html', context)