from django.urls import path,include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    path('chat/', views.chat,name='chat'),
    path('contact/', views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('service/',views.service,name='service'),
    path('register/',views.register,name='register'),
    path('search/', views.search_view, name='search'),

]