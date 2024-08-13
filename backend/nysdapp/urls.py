from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('chat/', views.chat,name='chat'),
    path('Login/',views.login,name='Login'),
    path('service/',views.service,name='service'),
    path('Register/',views.register,name='Register')

]