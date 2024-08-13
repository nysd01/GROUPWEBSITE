from django.shortcuts import render, redirect
from django.urls import reverse

def home(request):
    return render(request, 'main.html')

def chat(request):
    if request.method == 'POST':
        return redirect(reverse('home'))
    return render(request, 'chat.html')

def login(request):
    return render(request, 'Login.html')

def service(request):
    return render(request, 'services.html')  

def register(request):
    return render(request, 'Register.html')       
