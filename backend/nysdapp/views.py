from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Subscriber
from .forms import SubscriberForm, TestimonialForm
from .models import Product, CartItem, Testimonial
from .forms import AddToCartForm
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .utils import get_gpt_response

def home(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None

    form = SubscriberForm() 
    products = Product.objects.all()   
    cart_item_count = CartItem.objects.filter(session_id=request.session.session_key).count()
    testimonial_form = TestimonialForm()  
    testimonials = Testimonial.objects.all()  

    return render(request, 'main.html', {'username': username, 'form': form, 'products': products, 'cart_item_count': cart_item_count, 'testimonial_form': testimonial_form, 'testimonials': testimonials})


def chat(request):
    bot_message = "Hello! How can I assist you today?"
    user_input = None

    if request.method == 'POST':
        
        user_input = request.POST.get('message')
        if user_input:
            # Check if the query is about catalog or products
            if "catalog" in user_input.lower() or "products" in user_input.lower():
                # Fetch products from the database and generate a custom response
                products = Product.objects.all()
                product_list = "\n".join([f"{product.name} - {product.price}" for product in products])
                prompt = f"A user asked about the catalog. Available products are: {product_list}. Respond to the user."
            else:
                # Regular GPT-4 response
                prompt = f"User: {user_input}"

            # Get GPT-4 response
            bot_message = get_gpt_response(prompt)

    return render(request, 'chat.html', {
        'bot_message': bot_message,
        'user_message': user_input,
    })


def user_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, 'Email and password are required')
            return render(request, 'login.html')

        user = authenticate(request, username=User.objects.filter(email=email).first(), password=password)

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
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        elif pass1 != pass2:
            messages.error(request, "Passwords do not match")
        else:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = firstname
            myuser.last_name = lastname
            myuser.save()
            messages.success(request, 'Your account has been successfully created')
            return redirect('login')
        return render(request, 'register.html')

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

    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            if quantity <= 0:
                messages.error(request, 'Quantity must be a positive integer')
                return redirect('cart_detail')

            cart_item, created = CartItem.objects.get_or_create(product=product, session_id=session_id)
            cart_item.quantity = cart_item.quantity + quantity if not created else quantity
            cart_item.save()

            return redirect('cart_detail')  # Redirect after POST to avoid resubmission
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

@login_required
def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.name = request.user.username
            testimonial.save()
            return redirect('testimonials')
    else:
        form = TestimonialForm()
    return render(request, 'add_testimonial.html', {'form': form})

def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials.html', {'testimonials': testimonials})        

