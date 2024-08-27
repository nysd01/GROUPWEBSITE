from django.urls import path,include

from . import views

from django.contrib import admin


jls_extract_var = views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('chat/', views.chat,name='chat'),
    path('contact/', views.contact,name='contact'),
    path('login/',jls_extract_var.login_view,name='login'),
    path('service/',views.service,name='service'),
    path('register/',views.register,name='register'),
    path('search/', views.search_view, name='search'),
    path('cart/',views.cart, name='cart'),


]