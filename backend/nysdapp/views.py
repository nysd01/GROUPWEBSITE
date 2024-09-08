from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Subscriber
from .forms import SubscriberForm
from .models import Product, CartItem
from .forms import AddToCartForm
from django.contrib.auth import authenticate, login as auth_login









def home(request):

    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None

    form = SubscriberForm() 
    products = Product.objects.all()   
    cart_item_count = CartItem.objects.filter(session_id=request.session.session_key).count()

    return render(request, 'main.html', {'username': username, 'form': form, 'products': products,'cart_item_count': cart_item_count })



def chat(request):
    if request.method == 'POST':
        return redirect(reverse('home'))
    return render(request, 'chat.html')


def user_login_view(request):
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
            auth_login(request, user) 
            messages.success(request, 'You have successfully logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'login.html')

    return render(request, 'login.html')


def cart(request):
    session_id = request.session.session_key
    cart_items = CartItem.objects.filter(session_id=session_id)
    total_price = sum(item.subtotal() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def service(request):
    return render(request, 'service.html') 

def about(request):
    return render(request, 'about.html')      

def contact(request):
    return render(request, 'contact.html')      

def payment(request):
    return render(request, 'payment.html')   

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
            products = Product.objects.filter(
                Q(name__icontains=search_term) |
                Q(description__icontains=search_term)
            )
            return render(request, 'search_results.html', {'results': products})
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



def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key

    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            if quantity <= 0:
                messages.error(request, 'Quantity must be a positive integer')
                return redirect('cart_detail')
            cart_item, created = CartItem.objects.get_or_create(product=product, session_id=session_id)
            if created:
                cart_item.quantity = quantity
            else:
                cart_item.quantity += quantity
            cart_item.save()
             # Render the cart page with the updated cart items
            cart_items = CartItem.objects.filter(session_id=session_id)
            total_price = sum(item.subtotal() for item in cart_items)
            return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
            
        else:
            messages.error(request, 'Invalid form data')
            return redirect('cart_detail')
  

def cart_detail(request):
    session_id = request.session.session_key
    cart_items = CartItem.objects.filter(session_id=session_id)
    total_price = sum(item.subtotal() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def reset_cart(request):
    CartItem.objects.filter(session_id=request.session.session_key).delete()
    return redirect('home')

def service_view(request):
    if request.method == 'POST':
        command = request.POST.get('command')
        if command: 
            product = Product.objects.filter(name__icontains=command).first()
            if product:
                message = f'The price of {product.name} is {product.price}'
            else:
                message = 'Product not found'
            return render(request, 'service.html', {'message': message})
        else:
            message = 'Please enter a command'
            return render(request, 'service.html', {'message': message})
    else:
        services = Service.objects.all() 
        return render(request, 'service.html', {'services': services})