from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Subscriber
from .forms import SubscriberForm





def home(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None
    return render(request, 'main.html', {'username': username})



def chat(request):
    if request.method == 'POST':
        return redirect(reverse('home'))
    return render(request, 'chat.html')

@login_required
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, 'Email and password are required')
            return render(request, 'login.html')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password')
            return render(request, 'login.html')

        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'login.html')

    return render(request, 'login.html')



def cart(request):
    return render(request, 'cart.html')

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

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed to the newsletter.')
            return redirect('home')  
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = SubscriberForm()
    
    return render(request, 'main.html', {'form': form})