from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'helloword.html')

def login(request): 
    print(request.method)
    return render(request, 'users/login.html', {

    })