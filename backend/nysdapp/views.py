from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, 'main.html')

def chat(request):
    if request.method == 'POST':
        return redirect(reverse('home'))
    return render(request, 'chat.html')

def login(request):
    return render(request, 'login.html')

def service(request):
    return render(request, 'service.html')  

def contact(request):
    return render(request, 'contact.html')      

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('/register/')

        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('/register/')    

        elif pass1 != pass2:
            messages.error(request,"Password does not match!")
            return render(request, 'register.html')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()

        messages.success(request, 'your account has been successfully created')
        return redirect('login')
    else:

        return render(request, 'register.html')

def search_view(request):
    if request.method == 'GET':
        search_term = request.GET.get('q')
        if search_term:
            # You can add your search logic here
            # For example, you can use Django's ORM to search a model
            # results = MyModel.objects.filter(name__icontains=search_term)
            results = ['arduino uno, sensors, leds, motors']  # Replace with your search results
            return render(request, 'search_results.html', {'results': results})
    return redirect('home')           
